#!/usr/bin/env python3
"""
Robotics ArXiv Daily
- Queries arXiv API by category.
- Filters into topic buckets via keyword matching (title + abstract).
- Writes:
  1) digests/YYYY-MM-DD.md  (daily archive)
  2) topics/<topic>.md      (one file per topic)
  3) README.md "Today" block with links + previews

Run:
  python scripts/fetch_arxiv_daily.py
"""

from __future__ import annotations

import dataclasses
import datetime as dt
import json
import os
import re
from typing import Dict, List, Tuple

import feedparser
import requests
import yaml
from dateutil import parser as dateparser

ARXIV_API = "https://export.arxiv.org/api/query"
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG_PATH = os.path.join(REPO_ROOT, "config.yml")
DB_PATH = os.path.join(REPO_ROOT, "state_db.json")
DIGEST_DIR = os.path.join(REPO_ROOT, "digests")
TOPICS_DIR = os.path.join(REPO_ROOT, "topics")
README_PATH = os.path.join(REPO_ROOT, "README.md")


@dataclasses.dataclass
class Paper:
    arxiv_id: str
    title: str
    authors: List[str]
    published: dt.datetime
    updated: dt.datetime
    summary: str
    link_abs: str
    link_pdf: str
    primary_category: str


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_db() -> dict:
    if not os.path.exists(DB_PATH):
        return {"seen_ids": []}
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_db(db: dict) -> None:
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "topic"


def arxiv_query(category: str, max_results: int = 250) -> List[Paper]:
    params = {
        "search_query": f"cat:{category}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    resp = requests.get(ARXIV_API, params=params, timeout=60)
    resp.raise_for_status()
    feed = feedparser.parse(resp.text)

    papers: List[Paper] = []
    for e in feed.entries:
        link_abs = e.id.replace("http://", "https://")
        arxiv_id = link_abs.rsplit("/", 1)[-1]

        title = " ".join(e.title.split())
        authors = [a.name for a in getattr(e, "authors", [])] if hasattr(e, "authors") else []
        published = dateparser.parse(e.published)
        updated = dateparser.parse(e.updated)

        pdf = ""
        for l in e.links:
            if getattr(l, "type", "") == "application/pdf":
                pdf = l.href.replace("http://", "https://")
                break
        if not pdf:
            pdf = link_abs.replace("/abs/", "/pdf/") + ".pdf"

        primary = ""
        if hasattr(e, "arxiv_primary_category"):
            primary = e.arxiv_primary_category.get("term", "")
        elif hasattr(e, "tags") and e.tags:
            primary = e.tags[0].get("term", "")

        summary = " ".join(getattr(e, "summary", "").split())

        papers.append(
            Paper(
                arxiv_id=arxiv_id,
                title=title,
                authors=authors,
                published=published,
                updated=updated,
                summary=summary,
                link_abs=link_abs,
                link_pdf=pdf,
                primary_category=primary,
            )
        )
    return papers


def is_recent(p: Paper, days_back: int) -> bool:
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days_back)
    pub = p.published
    if pub.tzinfo is None:
        pub = pub.replace(tzinfo=dt.timezone.utc)
    return pub >= cutoff


def match_keywords(p: Paper, keywords: List[str]) -> List[str]:
    hay = normalize(p.title + " " + p.summary)
    matched = []
    for kw in keywords:
        nkw = normalize(kw)
        if nkw and nkw in hay:
            matched.append(kw)
    return matched


def format_paper_md(p: Paper, matched: List[str]) -> str:
    authors = ", ".join(p.authors[:8]) + (" et al." if len(p.authors) > 8 else "")
    pub = p.published.date().isoformat()
    tags = ", ".join(matched[:8]) if matched else ""
    cat = p.primary_category or "unknown"
    return (
        f"- **{p.title}**\n"
        f"  - Authors: {authors}\n"
        f"  - Published: {pub} | Category: `{cat}`\n"
        f"  - Links: [arXiv]({p.link_abs}) | [PDF]({p.link_pdf})\n"
        f"  - Matched: {tags}\n"
    )


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_daily_digest(today: str, sections: Dict[str, List[str]]) -> str:
    ensure_dir(DIGEST_DIR)
    path = os.path.join(DIGEST_DIR, f"{today}.md")

    lines = [f"# Daily Digest — {today}", ""]
    lines.append("Auto-generated from arXiv using topic keyword filters.")
    lines.append("> Edit `config.yml` to adjust topics/keywords and limits.\n")

    for topic, items in sections.items():
        lines.append(f"## {topic}\n")
        if not items:
            lines.append("_No matches today._\n")
        else:
            lines.extend([x.strip() for x in items])
            lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).strip() + "\n")
    return path


def write_topics(today: str, sections: Dict[str, List[str]]) -> Dict[str, str]:
    """
    One file per topic:
      topics/<slug>.md
    Returns: topic -> relative path
    """
    ensure_dir(TOPICS_DIR)
    topic_paths: Dict[str, str] = {}

    for topic, items in sections.items():
        slug = slugify(topic)
        path = os.path.join(TOPICS_DIR, f"{slug}.md")
        rel = os.path.relpath(path, REPO_ROOT)
        topic_paths[topic] = rel

        lines = [f"# {topic}", ""]
        lines.append(f"**Last update:** {today}")
        lines.append("")
        lines.append("> Auto-generated. Edit `config.yml` to change keywords/topics.")
        lines.append("")

        if not items:
            lines.append("_No matches today._")
        else:
            lines.append("## Latest\n")
            lines.extend([x.strip() for x in items])

        lines.append("\n---\n")
        lines.append("Back to main page: [README](../README.md)")

        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines).strip() + "\n")

    return topic_paths


def update_readme(today: str, digest_rel_path: str, sections: Dict[str, List[str]], topic_paths: Dict[str, str]) -> None:
    begin = "<!-- BEGIN TODAY -->"
    end = "<!-- END TODAY -->"

    lines: List[str] = []
    lines.append("## ✅ Today\n")
    lines.append(f"**Last update:** {today}  ")
    lines.append(f"**Daily archive:** `{digest_rel_path}`  ")
    lines.append("")
    lines.append("_Auto-generated. Edit `config.yml` to change topics/keywords._\n")

    lines.append("### Browse by topic (links)\n")
    for topic in sections.keys():
        rel = topic_paths.get(topic)
        if rel:
            lines.append(f"- **[{topic}]({rel})**")
    lines.append("")

    # previews
    for topic, items in sections.items():
        lines.append(f"### {topic}\n")
        if not items:
            lines.append("_No matches today._\n")
        else:
            preview = items[: min(3, len(items))]
            lines.extend([x.strip() for x in preview])
            rel = topic_paths.get(topic)
            if rel:
                lines.append(f"- _(See full topic page: [{topic}]({rel}))_\n")
        lines.append("")

    today_block = "\n".join(lines).strip()

    if not os.path.exists(README_PATH):
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(f"# Robotics ArXiv Daily\n\n{begin}\n{today_block}\n{end}\n")
        return

    with open(README_PATH, "r", encoding="utf-8") as f:
        original = f.read()

    if begin not in original or end not in original:
        original = original.rstrip() + f"\n\n{begin}\n{today_block}\n{end}\n"
    else:
        pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
        original = pattern.sub(f"{begin}\n{today_block}\n{end}", original)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(original)


def main() -> None:
    cfg = load_config()
    days_back = int(cfg.get("days_back", 2))
    per_topic_cap = int(cfg.get("max_results_per_topic", 20))
    categories = list(cfg.get("categories", []))
    topics: Dict[str, List[str]] = cfg.get("topics", {})

    db = load_db()
    seen = set(db.get("seen_ids", []))

    recent: List[Paper] = []
    for cat in categories:
        try:
            papers = arxiv_query(cat, max_results=250)
            for p in papers:
                if is_recent(p, days_back=days_back):
                    recent.append(p)
        except Exception as e:
            print(f"[WARN] Failed category {cat}: {e}")

    # Deduplicate across categories by base id (drop version suffix)
    uniq: Dict[str, Paper] = {}
    for p in recent:
        base_id = re.sub(r"v\d+$", "", p.arxiv_id)
        if base_id not in uniq or p.updated > uniq[base_id].updated:
            uniq[base_id] = p

    sections: Dict[str, List[str]] = {t: [] for t in topics.keys()}
    assignments: Dict[str, Tuple[str, List[str]]] = {}

    # Assign each paper to best matching topic (most matched keywords)
    for base_id, p in uniq.items():
        if base_id in seen:
            continue

        best_topic = None
        best_matched: List[str] = []
        for topic, kws in topics.items():
            matched = match_keywords(p, kws)
            if len(matched) > len(best_matched):
                best_matched = matched
                best_topic = topic

        if best_topic and best_matched:
            assignments[base_id] = (best_topic, best_matched)

    # Sort by published date desc
    sorted_ids = sorted(
        assignments.keys(),
        key=lambda bid: (uniq[bid].published if uniq[bid].published.tzinfo else uniq[bid].published.replace(tzinfo=dt.timezone.utc)),
        reverse=True,
    )

    per_topic_counts = {t: 0 for t in topics.keys()}
    for base_id in sorted_ids:
        topic, matched = assignments[base_id]
        if per_topic_counts[topic] >= per_topic_cap:
            continue
        p = uniq[base_id]
        sections[topic].append(format_paper_md(p, matched))
        per_topic_counts[topic] += 1
        seen.add(base_id)

    db["seen_ids"] = sorted(list(seen))[-50000:]
    save_db(db)

    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    digest_path = write_daily_digest(today, sections)
    digest_rel = os.path.relpath(digest_path, REPO_ROOT)

    topic_paths = write_topics(today, sections)
    update_readme(today, digest_rel, sections, topic_paths)

    print(f"Updated: {digest_rel}")
    print(f"Topics written: {len(topic_paths)}")


if __name__ == "__main__":
    main()
