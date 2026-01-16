#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import html
import json
import os
import re
from dataclasses import dataclass, asdict
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlencode

import feedparser
import yaml
from dateutil import parser as dtparser

DEFAULT_ARXIV_ENDPOINT = "http://export.arxiv.org/api/query"


# ----------------------------
# Data model
# ----------------------------

@dataclass(frozen=True)
class Paper:
    arxiv_id: str
    title: str
    summary: str
    authors: List[str]
    link: str
    published_utc: datetime
    primary_category: str
    categories: List[str]


# ----------------------------
# IO / utils
# ----------------------------

def load_config(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def ensure_dirs(*paths: str) -> None:
    for p in paths:
        os.makedirs(p, exist_ok=True)


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "")).strip()


def norm(text: str) -> str:
    return normalize_ws(text).lower()


def parse_arxiv_id(link: str) -> str:
    m = re.search(r"arxiv\.org/abs/([^?#]+)", link or "")
    return m.group(1) if m else (link or "")


def entry_date_utc(entry: Any) -> datetime:
    d = None
    if getattr(entry, "published", None):
        d = dtparser.parse(entry.published)
    elif getattr(entry, "updated", None):
        d = dtparser.parse(entry.updated)
    else:
        d = datetime.now(timezone.utc)
    if d.tzinfo is None:
        d = d.replace(tzinfo=timezone.utc)
    return d.astimezone(timezone.utc)


def within_days(dt_utc: datetime, days_back: int) -> bool:
    cutoff = datetime.now(timezone.utc) - timedelta(days=days_back)
    return dt_utc >= cutoff


def compile_terms(terms: List[str]) -> List[re.Pattern]:
    """
    - phrases (contain space or '-') => escaped substring regex, case-insensitive
    - single token => word-boundary regex
    """
    pats: List[re.Pattern] = []
    for t in terms or []:
        t = norm(t)
        if not t:
            continue
        if " " in t or "-" in t:
            pats.append(re.compile(re.escape(t), re.IGNORECASE))
        else:
            pats.append(re.compile(rf"\b{re.escape(t)}\b", re.IGNORECASE))
    return pats


def matches_any(text: str, patterns: List[re.Pattern]) -> bool:
    return any(p.search(text) for p in patterns)


def match_count(text: str, patterns: List[re.Pattern]) -> int:
    return sum(1 for p in patterns if p.search(text))


def stable_topic_slug(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "topic"


def choose_match_text(p: Paper) -> str:
    # με βάση το config σου, θεωρούμε title+abstract πάντα
    return norm(p.title + " " + p.summary)


# ----------------------------
# arXiv fetch
# ----------------------------

def fetch_arxiv(
    endpoint: str,
    search_query: str,
    max_results: int,
    sort_by: str = "submittedDate",
    sort_order: str = "descending",
) -> List[Paper]:
    params = {
        "search_query": search_query,
        "start": 0,
        "max_results": max_results,
        "sortBy": sort_by,
        "sortOrder": sort_order,
    }
    url = endpoint.rstrip("?") + "?" + urlencode(params)
    feed = feedparser.parse(url)

    if getattr(feed, "bozo", 0):
        raise RuntimeError(
            f"Feed parsing failed: {getattr(feed, 'bozo_exception', 'unknown error')}"
        )

    out: List[Paper] = []
    for e in feed.entries:
        title = normalize_ws(html.unescape(getattr(e, "title", "")))
        summary = normalize_ws(html.unescape(getattr(e, "summary", "")))
        link = getattr(e, "link", "")
        authors = [
            a.name for a in getattr(e, "authors", []) or []
            if hasattr(a, "name")
        ]
        published = entry_date_utc(e)

        tags = getattr(e, "tags", []) or []
        categories = [t.get("term", "").strip() for t in tags if t.get("term")]

        primary_category = ""
        if getattr(e, "arxiv_primary_category", None):
            primary_category = (e.arxiv_primary_category.get("term", "") or "").strip()
        if not primary_category and categories:
            primary_category = categories[0]

        out.append(
            Paper(
                arxiv_id=parse_arxiv_id(link),
                title=title,
                summary=summary,
                authors=authors,
                link=link,
                published_utc=published,
                primary_category=primary_category,
                categories=categories,
            )
        )
    return out


def build_allowed_cat_filter(allowed_categories: List[str]) -> Optional[re.Pattern]:
    cats = [c.strip() for c in (allowed_categories or []) if c and str(c).strip()]
    if not cats:
        return None
    # match exact token in categories list later; keep as set instead of regex
    return None


# ----------------------------
# Ranking / filtering
# ----------------------------

def passes_category(p: Paper, allowed: List[str]) -> bool:
    if not allowed:
        return True
    allowed_set = set(allowed)
    # match if primary in allowed OR any tag in allowed
    if p.primary_category in allowed_set:
        return True
    return any(c in allowed_set for c in (p.categories or []))


def score_paper(
    p: Paper,
    global_inc: List[re.Pattern],
    topic_inc: List[re.Pattern],
    boost: List[re.Pattern],
) -> int:
    txt = choose_match_text(p)
    score = 0
    score += 3 * match_count(txt, global_inc)
    score += 4 * match_count(txt, topic_inc)
    score += 2 * match_count(txt, boost)
    return score


def md_paper(p: Paper) -> str:
    date_str = p.published_utc.strftime("%Y-%m-%d")
    authors = ", ".join(p.authors[:10])
    if len(p.authors) > 10:
        authors += ", et al."
    return (
        f"- **{p.title}**  \n"
        f"  {authors}  \n"
        f"  _{date_str}_ · {p.link} · `{p.primary_category or 'n/a'}`  \n"
        f"  <details><summary>Abstract</summary>\n\n"
        f"  {p.summary}\n\n"
        f"  </details>\n"
    )


def write_topic_markdown(
    out_path: str,
    project_title: str,
    topic_name: str,
    updated_str: str,
    papers: List[Paper],
) -> None:
    lines: List[str] = []
    lines.append(f"# {topic_name}\n")
    if project_title:
        lines.append(f"_{project_title}_\n")
    lines.append(f"_Updated: {updated_str}_\n")
    lines.append(f"Total papers shown: **{len(papers)}**\n")
    lines.append("\n---\n")
    for p in papers:
        lines.append(md_paper(p))
        lines.append("\n")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_daily_digest(
    out_path: str,
    project_title: str,
    subtitle: str,
    updated_str: str,
    days_back: int,
    per_topic: List[Tuple[str, str, List[Paper]]],  # (topic_name, slug, papers)
) -> None:
    lines: List[str] = []
    lines.append(f"# Daily arXiv Digest\n")
    if project_title:
        lines.append(f"**{project_title}**  \n")
    if subtitle:
        lines.append(f"{subtitle}\n")
    lines.append(f"\n_Updated: {updated_str}_  \n")
    lines.append(f"_Window: last {days_back} days_\n")
    lines.append("\n---\n")
    lines.append("## Topics\n")
    for name, slug, papers in per_topic:
        lines.append(f"- [{name}](../topics/{slug}.md) — **{len(papers)}** papers\n")
    lines.append("\n---\n")
    for name, _, papers in per_topic:
        lines.append(f"## {name}\n")
        if not papers:
            lines.append("_No matching papers in this window._\n")
            continue
        for p in papers:
            lines.append(md_paper(p))
            lines.append("\n")
        lines.append("\n---\n")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def save_db(db_path: str, items: Dict[str, Any]) -> None:
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def paper_to_json(p: Paper) -> Dict[str, Any]:
    d = asdict(p)
    d["published_utc"] = p.published_utc.isoformat()
    return d


# ----------------------------
# Main
# ----------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--config",
        "-c",
        default=os.environ.get("ARXIV_DAILY_CONFIG", "config.yaml"),
        help="Path to config.yaml (default: config.yaml or env ARXIV_DAILY_CONFIG)",
    )
    args = ap.parse_args()

    cfg = load_config(args.config)

    project = cfg.get("project", {}) or {}
    storage = cfg.get("storage", {}) or {}
    arxiv = cfg.get("arxiv", {}) or {}
    filters = cfg.get("filters", {}) or {}
    topics = cfg.get("topics", []) or []
    output = cfg.get("output", {}) or {}

    project_title = str(project.get("title", "") or "").strip()
    subtitle = str(project.get("subtitle", "") or "").strip()

    data_dir = str(storage.get("data_dir", "data"))
    db_file = str(storage.get("db_file", "papers.json"))
    digests_dir = str(storage.get("digests_dir", "digests"))
    topics_dir = str(storage.get("topics_dir", "topics"))

    # ensure dirs
    ensure_dirs(data_dir, digests_dir, topics_dir)

    db_path = os.path.join(data_dir, db_file)

    endpoint = str(arxiv.get("endpoint", DEFAULT_ARXIV_ENDPOINT))
    days_back = int(arxiv.get("days_back", 3))
    max_results_per_topic = int(arxiv.get("max_results_per_topic", 80))
    fetch_multiplier = int(arxiv.get("fetch_multiplier", 8))
    hard_cap_results = int(arxiv.get("hard_cap_results", 400))
    allowed_categories = arxiv.get("allowed_categories", []) or []

    global_inc_terms = filters.get("include_keywords", []) or []
    global_exc_terms = filters.get("exclude_keywords", []) or []
    dedupe_mode = str(filters.get("dedupe_mode", "topic") or "topic").strip().lower()
    if dedupe_mode not in ("topic", "global"):
        dedupe_mode = "topic"

    max_daily_per_topic = int(output.get("max_daily_per_topic", 12))

    if not isinstance(topics, list) or not topics:
        raise SystemExit("Config error: 'topics' must be a non-empty list.")

    global_inc = compile_terms(global_inc_terms)
    global_exc = compile_terms(global_exc_terms)

    updated_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # DB structure: keep last seen papers per id
    db: Dict[str, Any] = {"updated_utc": updated_str, "papers": {}}
    if os.path.exists(db_path):
        try:
            with open(db_path, "r", encoding="utf-8") as f:
                db = json.load(f) or db
        except Exception:
            pass
        db.setdefault("papers", {})

    global_seen: set[str] = set()  # for global dedupe

    per_topic_results: List[Tuple[str, str, List[Paper]]] = []

    for t in topics:
        name = str(t.get("name", "") or "").strip()
        slug = str(t.get("slug", "") or "").strip() or stable_topic_slug(name)
        query = str(t.get("query", "") or "").strip()
        t_inc_terms = t.get("include_keywords", []) or []
        t_exc_terms = t.get("exclude_keywords", []) or []
        boost_terms = t.get("boost_keywords", []) or []

        if not name or not query:
            # skip malformed topic
            per_topic_results.append((name or "Unnamed topic", slug, []))
            continue

        # fetch size logic
        fetch_n = min(max_results_per_topic * fetch_multiplier, hard_cap_results)

        # fetch
        try:
            pool = fetch_arxiv(endpoint, query, max_results=fetch_n)
        except Exception as e:
            # topic fetch failed, but keep pipeline alive
            per_topic_results.append((name, slug, []))
            continue

        # time window
        pool = [p for p in pool if within_days(p.published_utc, days_back)]

        # category filter
        if allowed_categories:
            pool = [p for p in pool if passes_category(p, allowed_categories)]

        # global exclude
        if global_exc:
            pool = [p for p in pool if not matches_any(choose_match_text(p), global_exc)]

        # global include gate (if provided)
        if global_inc:
            pool = [p for p in pool if matches_any(choose_match_text(p), global_inc)]

        # topic-level include/exclude
        t_inc = compile_terms(t_inc_terms)
        t_exc = compile_terms(t_exc_terms)
        boost = compile_terms(boost_terms)

        if t_exc:
            pool = [p for p in pool if not matches_any(choose_match_text(p), t_exc)]
        if t_inc:
            pool = [p for p in pool if matches_any(choose_match_text(p), t_inc)]

        # dedupe
        if dedupe_mode == "global":
            pool = [p for p in pool if p.arxiv_id not in global_seen]

        # scoring
        scored: List[Tuple[int, int, str, Paper]] = []
        for p in pool:
            s = score_paper(p, global_inc, t_inc, boost)
            ts = int(p.published_utc.timestamp())
            scored.append((s, ts, p.title.lower(), p))

        # sort: score desc, newest desc, title asc
        scored.sort(key=lambda x: (-x[0], -x[1], x[2]))

        selected = [p for _, _, _, p in scored[:max_daily_per_topic]]

        # update dedupe sets
        if dedupe_mode == "global":
            for p in selected:
                global_seen.add(p.arxiv_id)

        # write per-topic page
        topic_md_path = os.path.join(topics_dir, f"{slug}.md")
        write_topic_markdown(topic_md_path, project_title, name, updated_str, selected)

        # update db
        for p in selected:
            db["papers"][p.arxiv_id] = paper_to_json(p)

        per_topic_results.append((name, slug, selected))

    # write daily digest
    digest_name = datetime.now(timezone.utc).strftime("%Y-%m-%d") + ".md"
    digest_path = os.path.join(digests_dir, digest_name)
    write_daily_digest(
        digest_path,
        project_title,
        subtitle,
        updated_str,
        days_back,
        per_topic_results,
    )

    save_db(db_path, db)

    print(f"Done.\n- Digest: {digest_path}\n- Topics: {topics_dir}\n- DB: {db_path}\nConfig: {args.config}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
