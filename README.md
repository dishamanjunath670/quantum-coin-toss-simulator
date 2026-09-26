 🪙 Quantum Coin Toss Simulator

A beginner-friendly software project that demonstrates basic quantum computing concepts using Python and Qiskit.

📌 About the Project

The Quantum Coin Toss Simulator uses a qubit to simulate a coin toss.

A Hadamard gate is applied to the qubit to create a superposition. The qubit is then measured to produce either `0` or `1`.

* `0` → Heads
* `1` → Tails

The simulator allows the user to choose the number of tosses and displays the Heads/Tails results, percentages, quantum circuit, and graph.

 ⚛️ Quantum Concept

The project demonstrates:

* Qubit
* Superposition
* Hadamard gate
* Quantum measurement
* Probability

The Hadamard gate creates approximately equal probabilities for measuring `0` and `1`.

 ✨ Features

* 🪙 Quantum coin toss simulation
* 🔢 User-defined number of tosses
* ⚛️ Quantum circuit visualization
* 📊 Heads/Tails statistics
* 📈 Graphical results
* 🖥️ Interactive GUI
* 🔄 Reset functionality

 🛠️ Technologies Used

* Python
* Qiskit
* Qiskit Aer
* Tkinter
* Matplotlib

 📊 Example Result

One experiment with 1000 tosses produced:

| Result | Count | Percentage |
| ------ | ----: | ---------: |
| Heads  |   492 |      49.2% |
| Tails  |   508 |      50.8% |
| Total  |  1000 |       100% |

The exact results can vary between runs because measurement outcomes are probabilistic.

🚀 How to Run

 1. Install the required packages

```bash
pip install qiskit qiskit-aer matplotlib
```

2. Run the basic simulator

```bash
python coin_toss.py
```

 3. Run the GUI version

```bash
python quantum_coin_gui.py
```

 📂 Project Files

| File                  | Description                       |
| --------------------- | --------------------------------- |
| `coin_toss.py`        | Basic quantum coin toss simulator |
| `quantum_coin_gui.py` | Interactive GUI version           |
| `README.md`           | Project documentation             |

 🎯 Project Objective

The main objective is to provide a simple and interactive way to understand fundamental quantum computing concepts through a familiar coin-toss example.

🔮 Future Scope

* Execute the experiment on real quantum hardware
* Add multi-qubit experiments
* Add more quantum gates
* Export experimental results to CSV
* Add additional statistical analysis

👩‍💻 Author

Disha M

This project was developed as a beginner quantum computing project using Python and Qiskit.
