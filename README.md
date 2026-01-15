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
## Latest
<!-- LATEST:START -->
**Last update:** 2026-01-15  
**Daily archive:** `digests/2026-01-15.md`  

_Auto-generated. Edit `config.yml` to change topics/keywords._
<!-- LATEST:END -->

<!-- TOPICS:START -->
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

<!-- TOPICS:END -->

### Autonomous Driving & AV

- **SCE-SLAM: Scale-Consistent Monocular SLAM via Scene Coordinate Embeddings**
  - Authors: Yuchen Wu, Jiahe Li, Xiaohan Yu, Lina Yu, Jin Zheng, Xiao Bai
  - Published: 2026-01-14 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.09665v1) | [PDF](https://arxiv.org/pdf/2601.09665v1)
  - Matched: waymo, kitti
- **Terminally constrained flow-based generative models from an optimal control perspective**
  - Authors: Weiguo Gao, Ming Li, Qianxiao Li
  - Published: 2026-01-14 | Category: `cs.LG`
  - Links: [arXiv](https://arxiv.org/abs/2601.09474v1) | [PDF](https://arxiv.org/pdf/2601.09474v1)
  - Matched: trajectory planning
- **MAD: Motion Appearance Decoupling for efficient Driving World Models**
  - Authors: Ahmad Rahimi, Valentin Gerard, Eloi Zablocki, Matthieu Cord, Alexandre Alahi
  - Published: 2026-01-14 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.09452v1) | [PDF](https://arxiv.org/pdf/2601.09452v1)
  - Matched: autonomous driving
- _(See full topic page: [Autonomous Driving & AV](topics/autonomous-driving-av.md))_


### Drones & Aerial Robotics

- **SAM3-DMS: Decoupled Memory Selection for Multi-target Video Segmentation of SAM3**
  - Authors: Ruiqi Shen, Chang Liu, Henghui Ding
  - Published: 2026-01-14 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.09699v1) | [PDF](https://arxiv.org/pdf/2601.09699v1)
  - Matched: imu
- **LARGE: A Locally Adaptive Regularization Approach for Estimating Gaussian Graphical Models**
  - Authors: Ha Nguyen, Sumanta Basu
  - Published: 2026-01-14 | Category: `stat.ME`
  - Links: [arXiv](https://arxiv.org/abs/2601.09686v1) | [PDF](https://arxiv.org/pdf/2601.09686v1)
  - Matched: imu
- **Image2Garment: Simulation-ready Garment Generation from a Single Image**
  - Authors: Selim Emir Can, Jan Ackermann, Kiyohiro Nakayama, Ruofan Liu, Tong Wu, Yang Zheng, Hugo Bertiche, Menglei Chai et al.
  - Published: 2026-01-14 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.09658v1) | [PDF](https://arxiv.org/pdf/2601.09658v1)
  - Matched: imu
- _(See full topic page: [Drones & Aerial Robotics](topics/drones-aerial-robotics.md))_


### SLAM, Localization & Mapping

- **Multimodal Signal Processing For Thermo-Visible-Lidar Fusion In Real-time 3D Semantic Mapping**
  - Authors: Jiajun Sun, Yangyi Ou, Haoyuan Zheng, Chao yang, Yue Ma
  - Published: 2026-01-14 | Category: `cs.RO`
  - Links: [arXiv](https://arxiv.org/abs/2601.09578v1) | [PDF](https://arxiv.org/pdf/2601.09578v1)
  - Matched: slam, mapping
- **Video-MSR: Benchmarking Multi-hop Spatial Reasoning Capabilities of MLLMs**
  - Authors: Rui Zhu, Xin Shen, Shuchen Wu, Chenxi Miao, Xin Yu, Yang Li, Weikang Li, Deguo Xia et al.
  - Published: 2026-01-14 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.09430v1) | [PDF](https://arxiv.org/pdf/2601.09430v1)
  - Matched: localization
- **Ability Transfer and Recovery via Modularized Parameters Localization**
  - Authors: Songyao Jin, Kun Zhou, Wenqi Li, Peng Wang, Biwei Huang
  - Published: 2026-01-14 | Category: `cs.CL`
  - Links: [arXiv](https://arxiv.org/abs/2601.09398v1) | [PDF](https://arxiv.org/pdf/2601.09398v1)
  - Matched: localization
- _(See full topic page: [SLAM, Localization & Mapping](topics/slam-localization-mapping.md))_


### Navigation, Planning & Control

- **SoK: Enhancing Cryptographic Collaborative Learning with Differential Privacy**
  - Authors: Francesco Capano, Jonas Böhler, Benjamin Weggenmann
  - Published: 2026-01-14 | Category: `cs.CR`
  - Links: [arXiv](https://arxiv.org/abs/2601.09460v1) | [PDF](https://arxiv.org/pdf/2601.09460v1)
  - Matched: mpc
- **Feedback-Based Mobile Robot Navigation in 3-D Environments Using Artificial Potential Functions Technical Report**
  - Authors: Ro'i Lang, Elon Rimon
  - Published: 2026-01-14 | Category: `cs.RO`
  - Links: [arXiv](https://arxiv.org/abs/2601.09318v1) | [PDF](https://arxiv.org/pdf/2601.09318v1)
  - Matched: navigation, motion planning
- **Towards Open Environments and Instructions: General Vision-Language Navigation via Fast-Slow Interactive Reasoning**
  - Authors: Yang Li, Aming Wu, Zihao Zhang, Yahong Han
  - Published: 2026-01-14 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.09111v1) | [PDF](https://arxiv.org/pdf/2601.09111v1)
  - Matched: navigation
- _(See full topic page: [Navigation, Planning & Control](topics/navigation-planning-control.md))_


### Manipulation & Grasping

- **Explainable Autoencoder-Based Anomaly Detection in IEC 61850 GOOSE Networks**
  - Authors: Dafne Lozano-Paredes, Luis Bote-Curiel, Juan Ramón Feijóo-Martínez, Ismael Gómez-Talal, José Luis Rojo-Álvarez
  - Published: 2026-01-14 | Category: `cs.CR`
  - Links: [arXiv](https://arxiv.org/abs/2601.09287v1) | [PDF](https://arxiv.org/pdf/2601.09287v1)
  - Matched: manipulation
- **Design Methodology of Hydraulically-driven Soft Robotic Gripper for a Large and Heavy Object**
  - Authors: Ko Yamamoto, Kyosuke Ishibashi, Hiroki Ishikawa, Osamu Azami
  - Published: 2026-01-14 | Category: `cs.RO`
  - Links: [arXiv](https://arxiv.org/abs/2601.09104v1) | [PDF](https://arxiv.org/pdf/2601.09104v1)
  - Matched: grasp, grasping
- _(See full topic page: [Manipulation & Grasping](topics/manipulation-grasping.md))_


### Robot Learning (RL, IL, Foundation Models)

- **Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning**
  - Authors: Chi-Pin Huang, Yunze Man, Zhiding Yu, Min-Hung Chen, Jan Kautz, Yu-Chiang Frank Wang, Fu-En Yang
  - Published: 2026-01-14 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.09708v1) | [PDF](https://arxiv.org/pdf/2601.09708v1)
  - Matched: vision-language-action, vla
- **ShortCoder: Knowledge-Augmented Syntax Optimization for Token-Efficient Code Generation**
  - Authors: Sicong Liu, Yanxian Huang, Mingwei Liu, Jiachi Chen, Ensheng Shi, Yuchi Ma, Hongyu Zhang, Yin Zhang et al.
  - Published: 2026-01-14 | Category: `cs.SE`
  - Links: [arXiv](https://arxiv.org/abs/2601.09703v1) | [PDF](https://arxiv.org/pdf/2601.09703v1)
  - Matched: llm
- **LLMs can Compress LLMs: Adaptive Pruning by Agents**
  - Authors: Sai Varun Kodathala, Rakesh Vunnam
  - Published: 2026-01-14 | Category: `cs.CL`
  - Links: [arXiv](https://arxiv.org/abs/2601.09694v1) | [PDF](https://arxiv.org/pdf/2601.09694v1)
  - Matched: foundation model, llm
- _(See full topic page: [Robot Learning (RL, IL, Foundation Models)](topics/robot-learning-rl-il-foundation-models.md))_


### Multi-Robot & Swarms

- **A Hybrid Machine Learning Framework for Improved Short-Term Peak-Flow Forecasting**
  - Authors: Gabriele Bertoli, Kai Schroeter, Rossella Arcucci, Enrica Caporali
  - Published: 2026-01-14 | Category: `eess.SP`
  - Links: [arXiv](https://arxiv.org/abs/2601.09336v1) | [PDF](https://arxiv.org/pdf/2601.09336v1)
  - Matched: coordination
- **High-Performance Serverless Computing: A Systematic Literature Review on Serverless for HPC, AI, and Big Data**
  - Authors: Valerio Besozzi, Matteo Della Bartola, Patrizio Dazzi, Marco Danelutto
  - Published: 2026-01-14 | Category: `cs.DC`
  - Links: [arXiv](https://arxiv.org/abs/2601.09334v1) | [PDF](https://arxiv.org/pdf/2601.09334v1)
  - Matched: distributed
- **Single-Round Clustered Federated Learning via Data Collaboration Analysis for Non-IID Data**
  - Authors: Sota Sugawara, Yuji Kawamata, Akihiro Toyoda, Tomoru Nakayama, Yukihiko Okada
  - Published: 2026-01-14 | Category: `cs.LG`
  - Links: [arXiv](https://arxiv.org/abs/2601.09304v1) | [PDF](https://arxiv.org/pdf/2601.09304v1)
  - Matched: distributed
- _(See full topic page: [Multi-Robot & Swarms](topics/multi-robot-swarms.md))_


### Safety, Robustness, Uncertainty

- **Value-Aware Numerical Representations for Transformer Language Models**
  - Authors: Andreea Dutulescu, Stefan Ruseti, Mihai Dascalu
  - Published: 2026-01-14 | Category: `cs.CL`
  - Links: [arXiv](https://arxiv.org/abs/2601.09706v1) | [PDF](https://arxiv.org/pdf/2601.09706v1)
  - Matched: robustness
- **Evaluating GAN-LSTM for Smart Meter Anomaly Detection in Power Systems**
  - Authors: Fahimeh Orvati Nia, Shima Salehi, Joshua Peeples
  - Published: 2026-01-14 | Category: `eess.SP`
  - Links: [arXiv](https://arxiv.org/abs/2601.09701v1) | [PDF](https://arxiv.org/pdf/2601.09701v1)
  - Matched: adversarial, anomaly detection
- **The Promptware Kill Chain: How Prompt Injections Gradually Evolved Into a Multi-Step Malware**
  - Authors: Ben Nassi, Bruce Schneier, Oleg Brodt
  - Published: 2026-01-14 | Category: `cs.CR`
  - Links: [arXiv](https://arxiv.org/abs/2601.09625v1) | [PDF](https://arxiv.org/pdf/2601.09625v1)
  - Matched: safety, safe
- _(See full topic page: [Safety, Robustness, Uncertainty](topics/safety-robustness-uncertainty.md))_


### 3D Gaussian Splatting & Neural Rendering (Robotics)

- **Efficient Camera-Controlled Video Generation of Static Scenes via Sparse Diffusion and 3D Rendering**
  - Authors: Jieying Chen, Jeffrey Hu, Joan Lasenby, Ayush Tewari
  - Published: 2026-01-14 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.09697v1) | [PDF](https://arxiv.org/pdf/2601.09697v1)
  - Matched: 3d reconstruction
- **V-DPM: 4D Video Reconstruction with Dynamic Point Maps**
  - Authors: Edgar Sucar, Eldar Insafutdinov, Zihang Lai, Andrea Vedaldi
  - Published: 2026-01-14 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.09499v1) | [PDF](https://arxiv.org/pdf/2601.09499v1)
  - Matched: 3d reconstruction
- **GaussianFluent: Gaussian Simulation for Dynamic Scenes with Mixed Materials**
  - Authors: Bei Huang, Yixin Chen, Ruijie Lu, Gang Zeng, Hongbin Zha, Yuru Pei, Siyuan Huang
  - Published: 2026-01-14 | Category: `cs.CV`
  - Links: [arXiv](https://arxiv.org/abs/2601.09265v1) | [PDF](https://arxiv.org/pdf/2601.09265v1)
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
