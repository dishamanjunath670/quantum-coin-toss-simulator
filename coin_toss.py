from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

simulator = AerSimulator()

# Ask the user how many times to toss
tosses = int(input("How many quantum coin tosses? "))

heads = 0
tails = 0

for i in range(tosses):

    coin = QuantumCircuit(1, 1)

    # Create superposition
    coin.h(0)

    # Measure the qubit
    coin.measure(0, 0)

    if i == 0:
    	print("\nQuantum Circuit:")
    	print(coin.draw())

    # Run the simulator
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
print("\nQuantum Coin Toss Results")
print("--------------------------")
print("Total tosses:", tosses)
print("Heads:", heads, f"({heads_percentage:.1f}%)")
print("Tails:", tails, f"({tails_percentage:.1f}%)")

# Create graph
labels = ["Heads", "Tails"]
values = [heads, tails]

plt.bar(labels, values)
plt.title("Quantum Coin Toss Results")
plt.xlabel("Result")
plt.ylabel("Number of Tosses")

plt.show()