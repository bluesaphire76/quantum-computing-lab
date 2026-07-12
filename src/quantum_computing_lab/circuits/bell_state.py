"""Bell-state circuit implemented with Qiskit."""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def create_bell_circuit() -> QuantumCircuit:
    """Create and measure a two-qubit Bell-state circuit."""
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    return circuit


def simulate_bell_state(shots: int = 1024) -> dict[str, int]:
    """Simulate a Bell-state circuit and return measurement counts."""
    if shots <= 0:
        raise ValueError("shots must be greater than zero")

    simulator = AerSimulator()
    circuit = create_bell_circuit()
    result = simulator.run(circuit, shots=shots).result()

    return dict(result.get_counts(circuit))


if __name__ == "__main__":
    counts = simulate_bell_state()
    print(f"Bell-state measurement counts: {counts}")
