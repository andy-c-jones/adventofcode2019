from src.day5.intcode_executor import *
import unittest

class TestIntcodeExecutor(unittest.TestCase):

    def test_part1(self):
        cpu = IntCode(read_input(), input_fn=lambda: 1)
        cpu.run()

    def test_part2(self):
        cpu = TestableIntCode(read_input(), inputs=[5])
        cpu.run()
        self.assertEqual(cpu.outputs[0], 9436229)
