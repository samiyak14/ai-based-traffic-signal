# 🚦 AI-Based Traffic Signal Optimization

An AI-based traffic signal optimization project that explores the use of **Reinforcement Learning (RL)** to improve traffic signal control under simulated traffic conditions.

The project compares a traditional **fixed-time traffic signal strategy** with an RL-based approach trained using **Proximal Policy Optimization (PPO)** in the **SUMO (Simulation of Urban MObility)** environment.

---

## 📌 Overview

Traffic congestion can be influenced by inefficient traffic signal timing, particularly when traffic conditions vary throughout the day.

This project explores whether an intelligent traffic signal controller can learn to adapt its behaviour based on traffic conditions rather than relying entirely on predefined signal timings.

The project includes:

- A fixed-time traffic signal baseline
- A reinforcement learning-based traffic signal controller
- Traffic simulation using SUMO
- PPO-based agent training
- Traffic performance analysis
- Visualizations and simulation outputs for comparison

---

## 🎯 Objectives

The main objectives of this project are to:

- Simulate a traffic signal environment using SUMO.
- Establish a baseline using fixed-time signal control.
- Develop a reinforcement learning environment for traffic signal optimization.
- Train an RL agent using the PPO algorithm.
- Analyse traffic behaviour under different signal control strategies.
- Compare the performance of fixed-time and RL-based approaches.

---

## 🧠 Approach

### 1. Traffic Simulation

The project uses **SUMO** to simulate a traffic network and generate traffic scenarios.

The simulation provides the environment in which different traffic signal control strategies can be evaluated.

### 2. Fixed-Time Control

A traditional fixed-time traffic signal strategy is used as a baseline.

Signal phases operate according to predefined timings without adapting to changing traffic conditions.

### 3. Reinforcement Learning

The traffic signal controller is formulated as a reinforcement learning problem.

The RL agent interacts with the simulated traffic environment and learns to select signal actions based on the observed traffic state.

### 4. PPO Training

The **Proximal Policy Optimization (PPO)** algorithm is used to train the reinforcement learning agent.

The trained model is then evaluated within the traffic simulation environment.

### 5. Performance Analysis

Simulation outputs are collected and analysed to compare the behaviour of the fixed-time and reinforcement-learning approaches.

The repository includes generated plots, maps, trained models, and traffic simulation outputs.

---

## 🛠️ Technologies Used

- **Python**
- **Reinforcement Learning**
- **PPO (Proximal Policy Optimization)**
- **Stable-Baselines3**
- **SUMO (Simulation of Urban MObility)**
- **TraCI**
- **Matplotlib**
- **NumPy**
- **Traffic Simulation**

---

## 📂 Project Structure

```text
ai-based-traffic-signal/
│
├── maps/                  # Traffic network and map-related files
├── maps_images/           # Generated map visualizations
├── models/                # Trained reinforcement learning models
├── plots/                 # Generated analysis plots
├── trafficlight_2/        # Traffic signal simulation files
│
├── configuration.sumocfg  # SUMO simulation configuration
├── train.py               # RL training script
├── requirements.txt       # Python dependencies
│
├── tripinfo.xml           # Simulation trip information
├── tripinfo_fixed.xml     # Results from fixed-time control
└── tripinfo_rl.xml        # Results from RL-based control
```

---

## 📊 Results & Analysis

The project evaluates traffic signal control using simulation-based results from both approaches.

The generated outputs are used to analyse differences in traffic behaviour and evaluate whether an adaptive reinforcement learning controller can provide improvements over conventional fixed-time control.

Visualizations and simulation outputs are included in the repository under the `plots/`, `maps/`, and `maps_images/` directories.

---

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed:

- Python 3.x
- SUMO
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/samiyak14/ai-based-traffic-signal.git
cd ai-based-traffic-signal
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Make sure SUMO and its required environment variables are correctly configured.

### Running the Project

The training process can be started using:

```bash
python train.py
```

The SUMO configuration is provided in:

```text
configuration.sumocfg
```

---

## 🔬 Future Improvements

Potential areas for further development include:

- Testing the controller under a wider range of traffic conditions.
- Experimenting with additional reinforcement learning algorithms.
- Improving the reward function and state representation.
- Evaluating performance across larger and more complex traffic networks.
- Incorporating real-world traffic data.
- Comparing additional traffic efficiency metrics.

---

## 📚 Key Learning Outcomes

This project provided practical experience with:

- Reinforcement learning
- Traffic simulation
- PPO-based model training
- Simulation-based experimentation
- Performance evaluation
- Data visualization
- Comparing AI-based and traditional control strategies

---

## 👩‍💻 Author

**Samiya Budye**

Computer Science Engineering — Artificial Intelligence & Machine Learning

[GitHub](https://github.com/samiyak14)
