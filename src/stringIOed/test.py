from io import StringIO
import unittest


def process_input(input_data):
    return input_data.upper()


class TestProcessInput(unittest.TestCase):
    def test_process_input(self):
        input_data = "hello"
        expected_output = "HELLO"

        # 使用 StringIO 模拟输入
        input_stream = StringIO(input_data)
        result = process_input(input_stream.read())

        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()