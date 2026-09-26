
import tkinter as tk
from tkinter import messagebox
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

simulator = AerSimulator()


def toss_coin():
    try:
        tosses = int(entry.get())

        if tosses <= 0:
            messagebox.showerror("Error", "Enter a number greater than 0.")
            return

        heads = 0
        tails = 0

        # Circuit shown to the user
        display_circuit = QuantumCircuit(1, 1)
        display_circuit.h(0)
        display_circuit.measure(0, 0)

        # Perform quantum tosses
        for i in range(tosses):

            coin = QuantumCircuit(1, 1)
            coin.h(0)
            coin.measure(0, 0)

            result = simulator.run(coin, shots=1).result()
            outcome = list(result.get_counts().keys())[0]

            if outcome == "0":
                heads += 1
            else:
                tails += 1

        # Calculate percentages
        heads_percentage = (heads / tosses) * 100
        tails_percentage = (tails / tosses) * 100

        # Display results
        result_label.config(
            text=f"Total Tosses: {tosses}\n"
                 f"Heads: {heads} ({heads_percentage:.1f}%)\n"
                 f"Tails: {tails} ({tails_percentage:.1f}%)"
        )

        # Experiment summary
        summary_label.config(
            text=f"Experiment Summary:\n"
                 f"Heads occurred {heads_percentage:.1f}% of the time.\n"
                 f"Tails occurred {tails_percentage:.1f}% of the time.\n"
                 f"The expected probability is approximately 50% for each."
        )

        # Display circuit
        circuit_text.config(
            text=display_circuit.draw(output="text")
        )

        # Graph
        labels = ["Heads", "Tails"]
        values = [heads, tails]

        plt.figure(figsize=(6, 4))
        plt.bar(labels, values)

        # 50% reference line
        plt.axhline(
            tosses / 2,
            linestyle="--",
            label="Expected 50%"
        )

        plt.title("Quantum Coin Toss Results")
        plt.xlabel("Result")
        plt.ylabel("Number of Tosses")
        plt.legend()
        plt.show()

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid number."
        )


def reset():
    entry.delete(0, tk.END)

    result_label.config(
        text="Results will appear here"
    )

    summary_label.config(
        text=""
    )

    circuit_text.config(
        text="Circuit will appear here"
    )


# Main window
window = tk.Tk()
window.title("Quantum Coin Toss Simulator")
window.geometry("650x700")

# Title
title = tk.Label(
    window,
    text="Quantum Coin Toss Simulator",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

# Instruction
instruction = tk.Label(
    window,
    text="Enter the number of quantum tosses:"
)
instruction.pack()

# Input
entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=15,
    justify="center"
)
entry.pack(pady=10)

# Toss button
toss_button = tk.Button(
    window,
    text="TOSS COIN",
    font=("Arial", 14, "bold"),
    command=toss_coin
)
toss_button.pack(pady=8)

# Reset button
reset_button = tk.Button(
    window,
    text="RESET",
    font=("Arial", 11),
    command=reset
)
reset_button.pack(pady=5)

# Results
result_label = tk.Label(
    window,
    text="Results will appear here",
    font=("Arial", 14)
)
result_label.pack(pady=15)

# Summary
summary_label = tk.Label(
    window,
    text="",
    font=("Arial", 11),
    justify="center"
)
summary_label.pack(pady=10)

# Circuit heading
circuit_heading = tk.Label(
    window,
    text="Quantum Circuit",
    font=("Arial", 15, "bold")
)
circuit_heading.pack(pady=5)

# Circuit display
circuit_text = tk.Label(
    window,
    text="Circuit will appear here",
    font=("Courier New", 11),
    justify="left"
)
circuit_text.pack(pady=10)

window.mainloop()