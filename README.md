# Quantum Security Toolkit

An intermediate-level programming project implementing **Quantum Key Distribution (QKD)** using the foundational **BB84 protocol**. This toolkit demonstrates how quantum mechanics can be leveraged to secure communication channels and automatically detect eavesdroppers.

## 🛠️ Technology Stack
* **Python 3.11**
* **Qiskit**
* **NumPy**
* **Matplotlib**
* **VS Code**

---

## 📁 Project Structure & Modules

* **`bb84.py` (BB84 Protocol Implementation):** Simulates the core protocol where sender (Alice) generates random bits and encodes them using random quantum bases (`+` or `x`), while receiver (Bob) independently selects measurement bases to establish a shared secret key
* **`attack.py` (Attack Simulation):** Models an eavesdropper (Eve) who intercepts and measures the qubits in transit. Because observing a quantum state alters its value, this simulation introduces measurable disturbance into the transmission.
* **`detect.py` (Eavesdropping Detection):** Calculates the error rate by comparing subsets of keys between Alice and Bob to determine if channel integrity has been compromised.

---

## 🚀 Getting Started & Installation

### 1. Clone the Repository
Clone this repository to your local machine using Git or download it via GitHub.

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
```bash
python -m venv venv
```

### 3. Activate
venv\Scripts\activate [WINDOWS]
source venv/bin/activate [macOS/ Linux]

### 4. Install Required Libraries
pip install qiskit numpy matplotlib

### 5. Running the Scripts

Run the BB84 Key Generation:
python bb84.py

Run the Eavesdropper Attack Simulation:
python attack.py

Run Eavesdropping Detection:
python detect.py
