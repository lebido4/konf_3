import unittest
from app import parse_value, process_dict, parse_toml_to_config

class TestConfigTool(unittest.TestCase):
    
    def test_numbers(self):
        """Тест обработки чисел"""
        self.assertEqual(parse_value(42), "42")
        self.assertEqual(parse_value(3.14), "3.14")

    def test_strings(self):
        """Тест обработки строк"""
        self.assertEqual(parse_value("hello"), "[[hello]]")
        self.assertEqual(parse_value("world"), "[[world]]")




if __name__ == "__main__":
    unittest.main()
