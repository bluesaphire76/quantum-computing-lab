"""Tests for the Qiskit Bell-state implementation."""

import pytest

from quantum_computing_lab.circuits.bell_state import (
    create_bell_circuit,
    simulate_bell_state,
)


def test_bell_circuit_structure() -> None:
    """The Bell circuit must use two qubits and two classical bits."""
    circuit = create_bell_circuit()

    assert circuit.num_qubits == 2
    assert circuit.num_clbits == 2


def test_bell_state_measurements() -> None:
    """A Bell-state simulation must produce only correlated states."""
    counts = simulate_bell_state(shots=1024)

    assert counts
    assert set(counts).issubset({"00", "11"})
    assert sum(counts.values()) == 1024


def test_invalid_shots() -> None:
    """Invalid shot counts must be rejected."""
    with pytest.raises(ValueError, match="greater than zero"):
        simulate_bell_state(shots=0)
