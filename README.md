# 🧠 QHack 2022 — PennyLane101 Coding Challenges

This repository contains my complete solutions to the **PennyLane101 Coding Challenges** from **QHack 2022**, developed using the PennyLane quantum machine learning framework.

Each section corresponds to one challenge and demonstrates a core concept in quantum computing, including quantum circuits, measurements, device backends, gradients, and noise modeling.

---

## 📚 Challenge Overview

| Question | Topic | Key Concepts |
|--------|------|--------------|
| Q1 | Single-qubit circuits | Gate ordering, expectation values |
| Q2 | Device backends | Pure vs mixed quantum states |
| Q3 | Quantum communication | Superdense coding |
| Q4 | Differentiation | Finite-difference gradients |
| Q5 | Noise & error detection | Bit-flip channels, density matrices |

---

## 📂 Repository Structure

QHack2022-PennyLane101-Solutions/
│
├── README.md
├── requirements.txt
│
├── question1_single_qubit/
│ └── solution.py
│
├── question2_devices/
│ └── solution.py
│
├── question3_superdense_coding/
│ └── solution.py
│
├── question4_gradients/
│ └── solution.py
│
└── question5_error_detection/
└── solution.py


Each folder contains a **self-contained solution** for the corresponding challenge.

---

## 🧩 Question 1 — Single-Qubit Circuit Equivalence

🔹 **Goal:**  
Compare two quantum circuits that differ only by gate ordering and qubit indexing.

🔹 **Key Insight:**  
Even when gates are applied in different orders or on different wires, expectation values can coincide due to symmetry.

🔹 **What’s demonstrated:**
- Parameterized quantum circuits
- Expectation values
- Gate commutation effects

---

## 🧪 Question 2 — Knowing Your Devices

🔹 **Goal:**  
Compare identical circuits executed on:
- `default.qubit` (pure-state simulator)
- `default.mixed` (density matrix simulator)

🔹 **Method:**  
- Construct the same circuit on both devices
- Convert the pure state into a density matrix
- Compute the matrix one-norm difference

🔹 **What’s demonstrated:**
- Device backends
- State vectors vs density matrices
- Quantum state comparison

---

## 📡 Question 3 — Superdense Coding with Partial Entanglement

🔹 **Goal:**  
Implement a superdense coding protocol using a **non-maximally entangled state**.

🔹 **Highlights:**
- Controlled entanglement via parameter `α`
- Alice encodes two classical bits using Pauli gates
- Bob decodes via Bell measurement

🔹 **What’s demonstrated:**
- Quantum communication protocols
- Conditional gate logic
- Measurement probabilities

---

## 📐 Question 4 — Finite-Difference Gradients

🔹 **Goal:**  
Compute gradients of a variational quantum circuit **without using autodiff**.

🔹 **Method:**  
Central finite-difference approximation:

\[
\frac{\partial f}{\partial \theta_i}
\approx \frac{f(\theta_i + \delta/2) - f(\theta_i - \delta/2)}{\delta}
\]

🔹 **What’s demonstrated:**
- Variational circuits
- Manual gradient computation
- Parameter-shift alternatives

---

## ⚠️ Question 5 — Bit-Flip Error Detection

🔹 **Goal:**  
Identify which qubit experienced a bit-flip error using measurement statistics.

🔹 **Approach:**
- Prepare a three-qubit density matrix
- Introduce a probabilistic bit-flip channel
- Decode error location from output probabilities

🔹 **What’s demonstrated:**
- Noise modeling
- Mixed quantum states
- Error diagnosis logic

---

## ▶️ How to Run

### 1️⃣ Install dependencies
```bash
pip install pennylane numpy


#🧠 Skills Demonstrated

-Quantum circuit construction
-PennyLane QNodes
-Measurement theory
-Device backends
-Noise channels
-Gradient computation
-Quantum communication protocols
