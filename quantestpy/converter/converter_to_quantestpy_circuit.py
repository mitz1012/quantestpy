from quantestpy import QuantestPyCircuit
from quantestpy.converter.sdk.qasm import _cvt_openqasm_to_quantestpy_circuit
from quantestpy.converter.sdk.qiskit import (
    _cvt_qiskit_to_quantestpy_circuit, _is_instance_of_qiskit_quantumcircuit)
from quantestpy.exceptions import QuantestPyError


def cvt_input_circuit_to_quantestpy_circuit(circuit) -> QuantestPyCircuit:

    # QuantestPyCircuit
    if isinstance(circuit, QuantestPyCircuit):
        quantestpy_circuit = circuit

    # qasm
    elif isinstance(circuit, str):
        quantestpy_circuit = _cvt_openqasm_to_quantestpy_circuit(circuit)

    # qiskit.QuantumCircuit()
    elif _is_instance_of_qiskit_quantumcircuit(circuit):
        quantestpy_circuit = _cvt_qiskit_to_quantestpy_circuit(circuit)

    else:
        raise QuantestPyError(
            "Input circuit must be one of the following: "
            "qasm, qiskit.QuantumCircuit and QuantestPyCircuit."
        )

    return quantestpy_circuit
