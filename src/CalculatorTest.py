import unittest
from Calculator import Calculator
from CSVReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data_add = CsvReader("./src/addition.csv").data
        for row in test_data_add:
            result = int(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtract_method_calculator(self):
        test_data_sub = CsvReader("./src/subtraction.csv").data
        for row in test_data_sub:
            result = int(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculator(self):
        test_data_mul = CsvReader("./src/multiplication.csv").data
        for row in test_data_mul:
            result = int(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide_method_calculator(self):
        test_data_div = CsvReader("./src/division.csv").data
        for row in test_data_div:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_method_calculator(self):
        test_data_sqr = CsvReader("./src/square.csv").data
        for row in test_data_sqr:
            result = int(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_squareRoot_method_calculator(self):
        test_data_sqrt = CsvReader("./src/sqroot.csv").data
        for row in test_data_sqrt:
            result = float(row['Result'])
            self.assertEqual(self.calculator.squareroot(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()
