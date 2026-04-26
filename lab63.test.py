import unittest
import os

# імпортуй свій файл (заміни назву!)
import lab63 as solution


class TestGameServer(unittest.TestCase):

    def write_input(self, content):
        with open("gamsrv.in.txt", "w") as f:
            f.write(content)

    def read_output(self):
        with open("gamsrv.out.txt", "r") as f:
            return f.read().strip()

    def test_small_graph(self):
        input_data = """5 6
1 3
1 2 4
2 3 1
2 4 7
3 4 2
4 5 3
1 5 10
"""
        self.write_input(input_data)

        solution.solve()

        output = self.read_output()
        self.assertEqual(output, "4")


    def test_single_client(self):
        input_data = """3 2
2
1 2 5
2 3 3
"""
        self.write_input(input_data)

        solution.solve()

        output = self.read_output()
        self.assertEqual(output, "3")


    def test_all_clients_except_one(self):
        input_data = """4 3
1 2 3
1 4 2
2 4 2
3 4 1
"""
        self.write_input(input_data)

        solution.solve()

        output = self.read_output()
        self.assertTrue(output.isdigit())


    def tearDown(self):
        # очищення файлів після тесту
        if os.path.exists("gamsrv.in.txt"):
            os.remove("gamsrv.in.txt")
        if os.path.exists("gamsrv.out.txt"):
            os.remove("gamsrv.out.txt")


if __name__ == "__main__":
    unittest.main()