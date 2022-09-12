import unittest
import numpy as np

from quantestpy import TestCircuit


class TestTestCircuitCRYGate(unittest.TestCase):
    """
    How to execute this test:
    $ pwd
    {Your directory where you git-cloned quantestpy}/quantestpy
    $ python -m unittest test.test_test_circuit_cry_gate
    ........
    ----------------------------------------------------------------------
    Ran 7 tests in 0.006s

    OK
    $
    """

    def test_cry_regular_qubit_order(self,):
        circ = TestCircuit(2)
        lambda_ = np.pi/8
        actual_gate = circ._create_all_qubit_gate_from_cry_gate(
            control_qubit=[0], target_qubit=[1], control_value=[1],
            parameter=[lambda_]
        )

        expected_gate = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, np.cos(lambda_/2), -np.sin(lambda_/2)],
            [0, 0, np.sin(lambda_/2), np.cos(lambda_/2)]])

        self.assertIsNone(
            np.testing.assert_allclose(actual_gate, expected_gate,
                                       atol=1e-07))

    def test_cry_qiskit_qubit_order(self,):
        circ = TestCircuit(2)
        lambda_ = np.pi/8
        circ._from_right_to_left_for_qubit_ids = True
        actual_gate = circ._create_all_qubit_gate_from_cry_gate(
            control_qubit=[0], target_qubit=[1], control_value=[1],
            parameter=[lambda_]
        )

        expected_gate = np.array([
            [1, 0, 0, 0],
            [0, np.cos(lambda_/2), 0, -np.sin(lambda_/2)],
            [0, 0, 1, 0],
            [0, np.sin(lambda_/2), 0, np.cos(lambda_/2)]])

        self.assertIsNone(
            np.testing.assert_allclose(actual_gate, expected_gate,
                                       atol=1e-07))

    def test_cry_flip_control_target(self,):
        circ = TestCircuit(2)
        lambda_ = np.pi/8
        actual_gate = circ._create_all_qubit_gate_from_cry_gate(
            control_qubit=[1], target_qubit=[0], control_value=[1],
            parameter=[lambda_]
        )

        expected_gate = np.array([
            [1, 0, 0, 0],
            [0, np.cos(lambda_/2), 0, -np.sin(lambda_/2)],
            [0, 0, 1, 0],
            [0, np.sin(lambda_/2), 0, np.cos(lambda_/2)]])

        self.assertIsNone(
            np.testing.assert_allclose(actual_gate, expected_gate,
                                       atol=1e-07))

    def test_cry_three_qubits_qiskit_qubit_order(self,):
        circ = TestCircuit(3)
        lambda_ = np.pi/8
        circ._from_right_to_left_for_qubit_ids = True
        actual_gate = circ._create_all_qubit_gate_from_cry_gate(
            control_qubit=[0], target_qubit=[2], control_value=[1],
            parameter=[lambda_]
        )

        # this is qiskit's output
        expected_gate = np.array(
            [[1. + 0.j,  0. + 0.j,  0. + 0.j,
              0. + 0.j,  0. + 0.j,  0. + 0.j,
              0. + 0.j,  0. + 0.j],
             [0. + 0.j,  0.98078528+0.j,  0. + 0.j,
                0. + 0.j,  0. + 0.j, -0.19509032+0.j,
                0. + 0.j,  0. + 0.j],
                [0. + 0.j,  0. + 0.j,  1. + 0.j,
                 0. + 0.j,  0. + 0.j,  0. + 0.j,
                 0. + 0.j,  0. + 0.j],
                [0. + 0.j,  0. + 0.j,  0. + 0.j,
                 0.98078528+0.j,  0. + 0.j,  0. + 0.j,
                 0. + 0.j, -0.19509032+0.j],
                [0. + 0.j,  0. + 0.j,  0. + 0.j,
                 0. + 0.j,  1. + 0.j,  0. + 0.j,
                 0. + 0.j,  0. + 0.j],
                [0. + 0.j,  0.19509032+0.j,  0. + 0.j,
                 0. + 0.j,  0. + 0.j,  0.98078528+0.j,
                 0. + 0.j,  0. + 0.j],
                [0. + 0.j,  0. + 0.j,  0. + 0.j,
                 0. + 0.j,  0. + 0.j,  0. + 0.j,
                 1. + 0.j,  0. + 0.j],
                [0. + 0.j,  0. + 0.j,  0. + 0.j,
                 0.19509032+0.j,  0. + 0.j,  0. + 0.j,
                 0. + 0.j,  0.98078528+0.j]])

        self.assertIsNone(
            np.testing.assert_allclose(actual_gate, expected_gate,
                                       atol=1e-07))

    def test_cry_control_value_is_zero(self,):
        circ = TestCircuit(2)
        lambda_ = np.pi/8
        actual_gate = circ._create_all_qubit_gate_from_cry_gate(
            control_qubit=[0], target_qubit=[1], control_value=[0],
            parameter=[lambda_]
        )

        expected_gate = np.array([
            [np.cos(lambda_/2), -np.sin(lambda_/2), 0, 0],
            [np.sin(lambda_/2), np.cos(lambda_/2), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])

        self.assertIsNone(
            np.testing.assert_allclose(actual_gate, expected_gate,
                                       atol=1e-07))

    def test_cry_multiple_controls(self,):
        circ = TestCircuit(3)
        lambda_ = np.pi/8
        actual_gate = circ._create_all_qubit_gate_from_cry_gate(
            control_qubit=[0, 1], target_qubit=[2], control_value=[1, 1],
            parameter=[lambda_]
        )

        expected_gate = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 1, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 1, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 1, 0, 0],
                                  [0, 0, 0, 0, 0, 0,
                                   np.cos(lambda_/2), -np.sin(lambda_/2)],
                                  [0, 0, 0, 0, 0, 0,
                                   np.sin(lambda_/2), np.cos(lambda_/2)]])

        self.assertIsNone(
            np.testing.assert_allclose(actual_gate, expected_gate,
                                       atol=1e-07))

    def test_cry_multiple_targets(self,):
        lambda_ = np.pi/8

        circ = TestCircuit(3)
        gate_0 = circ._create_all_qubit_gate_from_cry_gate(
            control_qubit=[0], target_qubit=[1, 2], control_value=[1],
            parameter=[lambda_]
        )

        circ = TestCircuit(3)
        gate_1_0 = circ._create_all_qubit_gate_from_cry_gate(
            control_qubit=[0], target_qubit=[1], control_value=[1],
            parameter=[lambda_]
        )
        gate_1_1 = circ._create_all_qubit_gate_from_cry_gate(
            control_qubit=[0], target_qubit=[2], control_value=[1],
            parameter=[lambda_]
        )

        self.assertIsNone(
            np.testing.assert_allclose(gate_0, np.matmul(gate_1_0, gate_1_1),
                                       atol=1e-07))