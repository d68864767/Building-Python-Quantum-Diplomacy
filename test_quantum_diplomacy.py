# test_quantum_diplomacy.py

# Importing required libraries
import unittest
from unittest.mock import patch, Mock
from quantum_diplomacy import QuantumDiplomacy

class TestQuantumDiplomacy(unittest.TestCase):
    def setUp(self):
        self.quantum_diplomacy = QuantumDiplomacy()

    @patch('quantum_diplomacy.requests.get')
    def test_get_diplomacy_data(self, mock_get):
        # Mocking the response from the API
        mock_response = Mock()
        expected_result = {"data": "test_data"}
        mock_response.json.return_value = expected_result
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Asserting the expected result
        self.assertEqual(self.quantum_diplomacy.get_diplomacy_data(), expected_result)

    @patch('quantum_diplomacy.QuantumDiplomacy.get_diplomacy_data')
    def test_run(self, mock_get_diplomacy_data):
        # Mocking the response from the get_diplomacy_data method
        mock_get_diplomacy_data.return_value = {"data": "test_data"}

        # Asserting the expected result
        self.assertIsInstance(self.quantum_diplomacy.run(), dict)

if __name__ == '__main__':
    unittest.main()
