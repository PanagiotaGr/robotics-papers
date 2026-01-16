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
## ✅ Today

**Last update:** 2026-01-16  
**Daily archive:** `digests/2026-01-16.md`  

_Auto-generated. Edit `config.yml` to change topics/keywords._

## Latest arXiv Digest

Updated: **2026-01-16**  
Window: last **2** days

| Topic | Papers | Link |
|------|--------|------|
| Autonomous Driving & AV | 18 | view |
| SLAM, Localization & Mapping | 12 | view |
| Drones & Aerial Robotics | 9 | view |
| 3D Gaussian Splatting & Neural Rendering (Robotics) | 4 | view |

### Browse by topic (links)

- **[Autonomous Driving & AV](topics/autonomous-driving-av.md)**
- **[Drones & Aerial Robotics](topics/drones-aerial-robotics.md)**
- **[SLAM, Localization & Mapping](topics/slam-localization-mapping.md)**
- **[Navigation, Planning & Control](topics/navigation-planning-control.md)**
- **[Manipulation & Grasping](topics/manipulation-grasping.md)**
- **[Robot Learning (RL, IL, Foundation Models)](topics/robot-learning-rl-il-foundation-models.md)**
- **[Multi-Robot & Swarms](topics/multi-robot-swarms.md)**
- **[Safety, Robustness, Uncertainty](topics/safety-robustness-uncertainty.md)**
- **[3D Gaussian Splatting & Neural Rendering (Robotics)](topics/3d-gaussian-splatting-neural-rendering-robotics.md)**

### Autonomous Driving & AV

- **DeepUrban: Interaction-Aware Trajectory Prediction and Planning for Automated Driving by Aerial Imagery**
  - Authors: Constantin Selzer, Fabian B. Flohr
  - Published: 2026-01-15 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.10554v1) | [PDF](https://arxiv.org/pdf/2601.10554v1)
  - Matched: autonomous driving, nuscenes
- **BikeActions: An Open Platform and Benchmark for Cyclist-Centric VRU Action Recognition**
  - Authors: Max A. Buettner, Kanak Mazumder, Luca Koecher, Mario Finkbeiner, Sebastian Niebler, Fabian B. Flohr
  - Published: 2026-01-15 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.10521v1) | [PDF](https://arxiv.org/pdf/2601.10521v1)
  - Matched: autonomous driving
- **SatMap: Revisiting Satellite Maps as Prior for Online HD Map Construction**
  - Authors: Kanak Mazumder, Fabian B. Flohr
  - Published: 2026-01-15 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.10512v1) | [PDF](https://arxiv.org/pdf/2601.10512v1)
  - Matched: autonomous driving, bev, hd map, nuscenes
- _(See full topic page: [Autonomous Driving & AV](topics/autonomous-driving-av.md))_


### Drones & Aerial Robotics

- **DInf-Grid: A Neural Differential Equation Solver with Differentiable Feature Grids**
  - Authors: Navami Kairanda, Shanthika Naik, Marc Habermann, Avinash Sharma, Christian Theobalt, Vladislav Golyanik
  - Published: 2026-01-15 | Category: `cs.LG`
  - Links: [arXiv](https://arxiv.org/abs/2601.10715v1) | [PDF](https://arxiv.org/pdf/2601.10715v1)
  - Matched: imu
- **Communication-Efficient and Privacy-Adaptable Mechanism -- a Federated Learning Scheme with Convergence Analysis**
  - Authors: Chun Hei Michael Shiu, Chih Wei Ling
  - Published: 2026-01-15 | Category: `cs.LG`
  - Links: [arXiv](https://arxiv.org/abs/2601.10701v1) | [PDF](https://arxiv.org/pdf/2601.10701v1)
  - Matched: imu
- **Data-driven stochastic reduced-order modeling of parametrized dynamical systems**
  - Authors: Andrew F. Ilersich, Kevin Course, Prasanth B. Nair
  - Published: 2026-01-15 | Category: `cs.LG`
  - Links: [arXiv](https://arxiv.org/abs/2601.10690v1) | [PDF](https://arxiv.org/pdf/2601.10690v1)
  - Matched: imu
- _(See full topic page: [Drones & Aerial Robotics](topics/drones-aerial-robotics.md))_


### SLAM, Localization & Mapping

- **CoGen: Creation of Reusable UI Components in Figma via Textual Commands**
  - Authors: Ishani Kanapathipillai, Obhasha Priyankara
  - Published: 2026-01-15 | Category: `cs.HC`
  - Links: [arXiv](https://arxiv.org/abs/2601.10536v1) | [PDF](https://arxiv.org/pdf/2601.10536v1)
  - Matched: mapping
- **SVII-3D: Advancing Roadside Infrastructure Inventory with Decimeter-level 3D Localization and Comprehension from Sparse Street Imagery**
  - Authors: Chong Liu, Luxuan Fu, Yang Jia, Zhen Dong, Bisheng Yang
  - Published: 2026-01-15 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.10535v1) | [PDF](https://arxiv.org/pdf/2601.10535v1)
  - Matched: localization, mapping
- **H-EFT-VA: An Effective-Field-Theory Variational Ansatz with Provable Barren Plateau Avoidance**
  - Authors: Eyad I. B Hamid
  - Published: 2026-01-15 | Category: `quant-ph`
  - Links: [arXiv](https://arxiv.org/abs/2601.10479v1) | [PDF](https://arxiv.org/pdf/2601.10479v1)
  - Matched: localization
- _(See full topic page: [SLAM, Localization & Mapping](topics/slam-localization-mapping.md))_


### Navigation, Planning & Control

- **Lunar-G2R: Geometry-to-Reflectance Learning for High-Fidelity Lunar BRDF Estimation**
  - Authors: Clementine Grethen, Nicolas Menga, Roland Brochard, Geraldine Morin, Simone Gasparini, Jeremy Lebreton, Manuel Sanchez Gestido
  - Published: 2026-01-15 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.10449v1) | [PDF](https://arxiv.org/pdf/2601.10449v1)
  - Matched: navigation
- **MATRIX AS PLAN: Structured Logical Reasoning with Feedback-Driven Replanning**
  - Authors: Ke Chen, Jiandian Zeng, Zihao Peng, Guo Li, Guangxue Zhang, Tian Wang
  - Published: 2026-01-15 | Category: `cs.AI`
  - Links: [arXiv](https://arxiv.org/abs/2601.10101v1) | [PDF](https://arxiv.org/pdf/2601.10101v1)
  - Matched: replanning
- **The PROPER Approach to Proactivity: Benchmarking and Advancing Knowledge Gap Navigation**
  - Authors: Kirandeep Kaur, Vinayak Gupta, Aditya Gupta, Chirag Shah
  - Published: 2026-01-14 | Category: `cs.LG`
  - Links: [arXiv](https://arxiv.org/abs/2601.09926v1) | [PDF](https://arxiv.org/pdf/2601.09926v1)
  - Matched: navigation
- _(See full topic page: [Navigation, Planning & Control](topics/navigation-planning-control.md))_


### Manipulation & Grasping

- **C-GRASP: Clinically-Grounded Reasoning for Affective Signal Processing**
  - Authors: Cheng Lin Cheng, Ting Chuan Lin, Chai Kai Chang
  - Published: 2026-01-15 | Category: `cs.AI`
  - Links: [arXiv](https://arxiv.org/abs/2601.10342v1) | [PDF](https://arxiv.org/pdf/2601.10342v1)
  - Matched: grasp
- **The impact of tactile sensor configurations on grasp learning efficiency -- a comparative evaluation in simulation**
  - Authors: Eszter Birtalan, Miklós Koller
  - Published: 2026-01-15 | Category: `cs.RO`
  - Links: [arXiv](https://arxiv.org/abs/2601.10268v1) | [PDF](https://arxiv.org/pdf/2601.10268v1)
  - Matched: grasp, tactile
- **History Is Not Enough: An Adaptive Dataflow System for Financial Time-Series Synthesis**
  - Authors: Haochong Xia, Yao Long Teng, Regan Tan, Molei Qin, Xinrun Wang, Bo An
  - Published: 2026-01-15 | Category: `cs.AI`
  - Links: [arXiv](https://arxiv.org/abs/2601.10143v1) | [PDF](https://arxiv.org/pdf/2601.10143v1)
  - Matched: manipulation
- _(See full topic page: [Manipulation & Grasping](topics/manipulation-grasping.md))_


### Robot Learning (RL, IL, Foundation Models)

- **MatchTIR: Fine-Grained Supervision for Tool-Integrated Reasoning via Bipartite Matching**
  - Authors: Changle Qu, Sunhao Dai, Hengyi Cai, Jun Xu, Shuaiqiang Wang, Dawei Yin
  - Published: 2026-01-15 | Category: `cs.CL`
  - Links: [arXiv](https://arxiv.org/abs/2601.10712v1) | [PDF](https://arxiv.org/pdf/2601.10712v1)
  - Matched: reinforcement learning, llm
- **From One-to-One to Many-to-Many: Dynamic Cross-Layer Injection for Deep Vision-Language Fusion**
  - Authors: Cheng Chen, Yuyu Guo, Pengpeng Zeng, Jingkuan Song, Peng Di, Hang Yu, Lianli Gao
  - Published: 2026-01-15 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.10710v1) | [PDF](https://arxiv.org/pdf/2601.10710v1)
  - Matched: llm
- **LIBERTy: A Causal Framework for Benchmarking Concept-Based Explanations of LLMs with Structural Counterfactuals**
  - Authors: Gilat Toker, Nitay Calderon, Ohad Amosy, Roi Reichart
  - Published: 2026-01-15 | Category: `cs.CL`
  - Links: [arXiv](https://arxiv.org/abs/2601.10700v1) | [PDF](https://arxiv.org/pdf/2601.10700v1)
  - Matched: llm
- _(See full topic page: [Robot Learning (RL, IL, Foundation Models)](topics/robot-learning-rl-il-foundation-models.md))_


### Multi-Robot & Swarms

- **Distributed Perceptron under Bounded Staleness, Partial Participation, and Noisy Communication**
  - Authors: Keval Jain, Anant Raj, Saurav Prakash, Girish Varma
  - Published: 2026-01-15 | Category: `cs.LG`
  - Links: [arXiv](https://arxiv.org/abs/2601.10705v1) | [PDF](https://arxiv.org/pdf/2601.10705v1)
  - Matched: distributed
- **Coarsening Causal DAG Models**
  - Authors: Francisco Madaleno, Pratik Misra, Alex Markham
  - Published: 2026-01-15 | Category: `stat.ML`
  - Links: [arXiv](https://arxiv.org/abs/2601.10531v1) | [PDF](https://arxiv.org/pdf/2601.10531v1)
  - Matched: distributed
- **Codebook Design for Limited Feedback in Near-Field XL-MIMO Systems**
  - Authors: Liujia Yao, Changsheng You, Zixuan Huang, Chao Zhou, Zhaohui Yang, Xiaoyang Li
  - Published: 2026-01-15 | Category: `cs.IT`
  - Links: [arXiv](https://arxiv.org/abs/2601.10391v1) | [PDF](https://arxiv.org/pdf/2601.10391v1)
  - Matched: distributed
- _(See full topic page: [Multi-Robot & Swarms](topics/multi-robot-swarms.md))_


### Safety, Robustness, Uncertainty

- **See Less, Drive Better: Generalizable End-to-End Autonomous Driving via Foundation Models Stochastic Patch Selection**
  - Authors: Amir Mallak, Erfan Aasi, Shiva Sreeram, Tsun-Hsuan Wang, Daniela Rus, Alaa Maalouf
  - Published: 2026-01-15 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.10707v1) | [PDF](https://arxiv.org/pdf/2601.10707v1)
  - Matched: out-of-distribution, robustness
- **ProbFM: Probabilistic Time Series Foundation Model with Uncertainty Decomposition**
  - Authors: Arundeep Chinta, Lucas Vinh Tran, Jay Katukuri
  - Published: 2026-01-15 | Category: `cs.LG`
  - Links: [arXiv](https://arxiv.org/abs/2601.10591v1) | [PDF](https://arxiv.org/pdf/2601.10591v1)
  - Matched: uncertainty, calibration
- **Adversarial Evasion Attacks on Computer Vision using SHAP Values**
  - Authors: Frank Mollard, Marcus Becker, Florian Roehrbein
  - Published: 2026-01-15 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.10587v1) | [PDF](https://arxiv.org/pdf/2601.10587v1)
  - Matched: adversarial
- _(See full topic page: [Safety, Robustness, Uncertainty](topics/safety-robustness-uncertainty.md))_


### 3D Gaussian Splatting & Neural Rendering (Robotics)

- **WildRayZer: Self-supervised Large View Synthesis in Dynamic Environments**
  - Authors: Xuweiyi Chen, Wentao Zhou, Zezhou Cheng
  - Published: 2026-01-15 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.10716v1) | [PDF](https://arxiv.org/pdf/2601.10716v1)
  - Matched: novel view synthesis
- **RSATalker: Realistic Socially-Aware Talking Head Generation for Multi-Turn Conversation**
  - Authors: Peng Chen, Xiaobao Wei, Yi Yang, Naiming Yao, Hui Chen, Feng Tian
  - Published: 2026-01-15 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.10606v1) | [PDF](https://arxiv.org/pdf/2601.10606v1)
  - Matched: gaussian splatting, 3d gaussian splatting, 3dgs
- **Thinking Like Van Gogh: Structure-Aware Style Transfer via Flow-Guided 3D Gaussian Splatting**
  - Authors: Zhendong Wang, Lebin Zhou, Jingchuan Xiao, Rongduo Han, Nam Ling, Cihan Ruan
  - Published: 2026-01-15 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.10075v1) | [PDF](https://arxiv.org/pdf/2601.10075v1)
  - Matched: gaussian splatting, 3d gaussian splatting, 3dgs
- _(See full topic page: [3D Gaussian Splatting & Neural Rendering (Robotics)](topics/3d-gaussian-splatting-neural-rendering-robotics.md))_
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
