# Robotics ArXiv Daily (Autonomous Vehicles • Drones • 3D Gaussian Splatting • More)

A lightweight daily ArXiv digest for robotics-related papers, including:
- Autonomous driving (perception / prediction / planning / BEV / mapping)
- Drones / aerial robotics (navigation, control, SLAM, perception)
- SLAM / Localization / Mapping
- Navigation / Planning / Control
- Manipulation
- Robot Learning (RL/IL/foundation models)
- Multi-robot / swarms
- Safety / robustness / uncertainty
- 3D Gaussian Splatting / Neural Rendering for robotics

This repo updates automatically via GitHub Actions.

---

## How it works (simple)
- Every day, the workflow runs `scripts/fetch_arxiv_daily.py`
- It queries arXiv by category, filters by topic keywords, and produces:
  - `digests/YYYY-MM-DD.md` (daily archive)
  - `topics/<topic>.md` (one file per topic)
  - an updated “Today” block below

---

<!-- BEGIN TODAY -->
<!-- END TODAY -->

---

## Configuration
Edit `config.yml` to change:
- categories
- topic names + keywords
- how many days back to consider
- max papers per topic

---

## Local run (optional)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python scripts/fetch_arxiv_daily.py
