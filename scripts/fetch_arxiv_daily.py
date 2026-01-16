#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import html
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Tuple
from urllib.parse import urlencode

import feedparser
import yaml
from dateutil import parser as dtparser

ARXIV_API_BASE = "http://export.arxiv.org/api/query"


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
# Basic utils
# ----------------------------

def load_config(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def ensure_dirs() -> None:
    os.makedirs("docs/topics", exist_ok=True)


def slugify(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "topic"


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


def normalize_match_in(value: Any) -> str:
    """
    Accept:
      - "title", "abstract", "title+abstract"
      - ["title","abstract"] (any order)
    Return one of: "title", "abstract", "title+abstract"
    """
    if value is None:
        return "title+abstract"

    if isinstance(value, str):
        s = value.strip().lower()
        if s in ("title", "ti"):
            return "title"
        if s in ("abstract", "summary", "abs"):
            return "abstract"
        if s in ("title+abstract", "title+abs", "ti+abs", "both", "all"):
            return "title+abstract"
        return "title+abstract"

    if isinstance(value, (list, tuple, set)):
        items = {str(x).strip().lower() for x in value if str(x).strip()}
        has_title = any(x in ("title", "ti") for x in items)
        has_abs = any(x in ("abstract", "summary", "abs") for x in items)
        if has_title and has_abs:
            return "title+abstract"
        if has_title:
            return "title"
        if has_abs:
            return "abstract"
        return "title+abstract"

    return "title+abstract"


# ----------------------------
# arXiv fetch (pool by categories)
# ----------------------------

def build_category_query(categories: List[str]) -> str:
    cats = [str(c).strip() for c in (categories or []) if str(c).strip()]
    if not cats:
        cats = ["cs.RO", "cs.CV"]
    return "(" + " OR ".join([f"cat:{c}" for c in cats]) + ")"


def fetch_arxiv_pool(search_query: str, max_results: int) -> List[Paper]:
    params = {
        "search_query": search_query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = ARXIV_API_BASE + "?" + urlencode(params)
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


# ----------------------------
# Markdown output
# ----------------------------

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


def write_topic_page(topic_name: str, slug: str, papers: List[Paper], updated_str: str) -> None:
    path = f"docs/topics/{slug}.md"
    lines: List[str] = []
    lines.append(f"# {topic_name}\n")
    lines.append(f"_Updated: {updated_str}_\n")
    lines.append(f"Total papers shown: **{len(papers)}**\n")
    lines.append("\n---\n")
    for p in papers:
        lines.append(md_paper(p))
        lines.append("\n")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_index(updated_str: str, topics_meta: List[Dict[str, Any]], days_back: int) -> None:
    path = "docs/index.md"
    lines: List[str] = []
    lines.append("# arXiv Daily – Robotics\n")
    lines.append(f"_Updated: {updated_str}_\n")
    lines.append(f"_Window: last {days_back} days_\n")
    lines.append("\n## Topics\n")
    for t in topics_meta:
        lines.append(f"- [{t['name']}](topics/{t['slug']}.md) — **{t['count']}** papers\n")
    lines.append("\n---\n")
    lines.append("Generated automatically from arXiv.\n")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


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
    ensure_dirs()

    days_back = int(cfg.get("days_back", 2))
    max_per_topic = int(cfg.get("max_results_per_topic", 20))

    fetch_multiplier = int(cfg.get("fetch_multiplier", 10))
    hard_cap_results = int(cfg.get("hard_cap_results", 300))

    match_in = normalize_match_in(cfg.get("match_in", "title+abstract"))

    must_have_any = cfg.get("must_have_any", []) or []
    exclude_any = cfg.get("exclude_any", []) or []
    categories = cfg.get("categories", []) or []
    topics_map: Dict[str, List[str]] = cfg.get("topics", {}) or {}

    if not isinstance(topics_map, dict) or not topics_map:
        raise SystemExit("Config error: 'topics' must be a mapping of {Topic Name: [keywords...]}")

    # Decide fetch size for the pool
    fetch_n = min(max_per_topic * fetch_multiplier, hard_cap_results)

    # Build pool query and fetch
    pool_query = build_category_query(categories)
    pool = fetch_arxiv_pool(pool_query, max_results=fetch_n)

    # 1) Time window
    pool = [p for p in pool if within_days(p.published_utc, days_back)]

    # 2) Choose matching text field(s)
    def paper_text(p: Paper) -> str:
        if match_in == "title":
            return norm(p.title)
        if match_in == "abstract":
            return norm(p.summary)
        return norm(p.title + " " + p.summary)

    # 3) Global exclude (if any)
    if exclude_any:
        exc_pats = compile_terms(exclude_any)
        pool = [p for p in pool if not matches_any(paper_text(p), exc_pats)]

    # 4) Global gate must_have_any
    if must_have_any:
        gate_pats = compile_terms(must_have_any)
        pool = [p for p in pool if matches_any(paper_text(p), gate_pats)]

    # 5) Topic assignment + ranking
    updated_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    topics_meta: List[Dict[str, Any]] = []

    for topic_name, keywords in topics_map.items():
        slug = slugify(topic_name)
        kw_pats = compile_terms(keywords or [])

        scored: List[Tuple[int, Paper]] = []
        seen_ids = set()

        for p in pool:
            if p.arxiv_id in seen_ids:
                continue
            txt = paper_text(p)
            c = match_count(txt, kw_pats)
            if c <= 0:
                continue
            seen_ids.add(p.arxiv_id)
            scored.append((c, p))

        # Sort: more keyword hits first, then newest, then stable tie-breakers
        scored.sort(
            key=lambda cp: (
                -cp[0],
                -int(cp[1].published_utc.timestamp()),
                cp[1].title.lower(),
                cp[1].arxiv_id,
            )
        )

        papers = [p for _, p in scored[:max_per_topic]]
        write_topic_page(topic_name, slug, papers, updated_str)
        topics_meta.append({"name": topic_name, "slug": slug, "count": len(papers)})

    # Index
    write_index(updated_str, topics_meta, days_back)
    print(f"Done. Pages generated under docs/ (config: {args.config})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
