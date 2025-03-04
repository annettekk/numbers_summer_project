import unittest
import os
from src.my_code import sum_num  # Import the function from your script

class TestSumNum(unittest.TestCase):

    def setUp(self):
        """Create a temporary input file with test numbers."""
        self.test_filename = "test_numbers.txt"
        with open(self.test_filename, "w") as f:
            f.write("10.5\n20\n30.75\n5\n")  # Example numbers

    def tearDown(self):
        """Remove the temporary test file after each test."""
        os.remove(self.test_filename)

    def test_sum_num(self):
        """Test that sum_num correctly sums numbers in the file."""
        expected_sum = 66.25  # 10.5 + 20 + 30.75 + 5
        result = sum_num(self.test_filename)  # Call the function
        self.assertAlmostEqual(result, expected_sum, places=2)  # Allow small precision errors

if __name__ == "__main__":
    unittest.main()
