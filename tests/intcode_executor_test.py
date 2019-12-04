from day2.intcode_executor import execute
from day2.intcode_executor import restore_from_before_fire_and_execute
from day2.intcode_executor import set_noun_and_verb_and_execute
from day2.intcode_executor import day_two_solution
import unittest

class TestIntcodeExecutor(unittest.TestCase):

# the fuel needed to launch the craft is the sum of the fuel needed
# to launch the modules
    def test_simple_addition_program(self):
        self.assertEqual(execute([1, 5, 5, 3, 99, 0]), [1, 5, 5, 0, 99, 0])
        self.assertEqual(execute([1, 5, 6, 3, 99, 1, 0]), [1, 5, 6, 1, 99, 1, 0])
        self.assertEqual(execute([1, 5, 6, 3, 99, 0, 1]), [1, 5, 6, 1, 99, 0, 1])
        self.assertEqual(execute([1, 5, 6, 3, 99, 1, 4]), [1, 5, 6, 5, 99, 1, 4])
        self.assertEqual(execute([1, 5, 6, 3, 99, 21, 54]), [1, 5, 6, 75, 99, 21, 54])

    def test_simple_addition_program_using_third_parameter_to_overwrite_other_positions(self):
        self.assertEqual(execute([1, 0, 0, 0, 99]), [2, 0, 0, 0, 99])
        self.assertEqual(execute([1, 3, 2, 1, 99]), [1, 3, 2, 1, 99])

    def test_simple_multiplication_program(self):
        self.assertEqual(execute([2, 0, 0, 3, 99]), [2, 0, 0, 4, 99])
        self.assertEqual(execute([2, 1, 0, 3, 99]), [2, 1, 0, 2, 99])
        self.assertEqual(execute([2, 1, 1, 3, 99]), [2, 1, 1, 1, 99])
        self.assertEqual(execute([2, 2, 4, 3, 99]), [2, 2, 4, 396, 99])
        self.assertEqual(execute([2, 3, 3, 3, 99]), [2, 3, 3, 9, 99])
    
    def test_day2_examples(self):
        self.assertEqual(execute([1,0,0,0,99]), [2,0,0,0,99])
        self.assertEqual(execute([2,3,0,3,99]), [2,3,0,6,99])
        self.assertEqual(execute([2,4,4,5,99,0]), [2,4,4,5,99,9801])
        self.assertEqual(execute([1,1,1,4,99,5,6,0,99]), [30,1,1,4,2,5,6,0,99])
        self.assertEqual(execute([1,9,10,3,2,3,11,0,99,30,40,50]), [3500,9,10,70, 2,3,11,0, 99, 30,40,50])
        
    def test_restore_replaces_postion1_with_12_and_position2_with_2(self):
        self.assertEqual(restore_from_before_fire_and_execute([1, 0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 0, 0]),[2, 12, 2, 0, 99, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(restore_from_before_fire_and_execute([1, 0, 0, 5, 99, 1, 2, 3, 4, 0, 0, 0, 0]),[1, 12, 2, 5, 99, 2, 2, 3, 4, 0, 0, 0, 0])

    # def test_day2_input(self):
    #     print(restore_from_before_fire_and_execute([1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,9,19,23,1,23,5,27,2,27,10,31,1,6,31,35,1,6,35,39,2,9,39,43,1,6,43,47,1,47,5,51,1,51,13,55,1,55,13,59,1,59,5,63,2,63,6,67,1,5,67,71,1,71,13,75,1,10,75,79,2,79,6,83,2,9,83,87,1,5,87,91,1,91,5,95,2,9,95,99,1,6,99,103,1,9,103,107,2,9,107,111,1,111,6,115,2,9,115,119,1,119,6,123,1,123,9,127,2,127,13,131,1,131,9,135,1,10,135,139,2,139,10,143,1,143,5,147,2,147,6,151,1,151,5,155,1,2,155,159,1,6,159,0,99,2,0,14,0]))

    def test_set_noun_and_verb_and_execute_sets_postion1_with_noun_and_postion2_with_verb(self):
        self.assertEqual(set_noun_and_verb_and_execute([1, 0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 0, 0], 12, 2),[2, 12, 2, 0, 99, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(set_noun_and_verb_and_execute([1, 0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 0, 0], 3, 4), [99, 3, 4, 0, 99, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_inputs_that_result_in_19690720(self):
        self.assertEqual(day_two_solution([1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,9,19,23,1,23,5,27,2,27,10,31,1,6,31,35,1,6,35,39,2,9,39,43,1,6,43,47,1,47,5,51,1,51,13,55,1,55,13,59,1,59,5,63,2,63,6,67,1,5,67,71,1,71,13,75,1,10,75,79,2,79,6,83,2,9,83,87,1,5,87,91,1,91,5,95,2,9,95,99,1,6,99,103,1,9,103,107,2,9,107,111,1,111,6,115,2,9,115,119,1,119,6,123,1,123,9,127,2,127,13,131,1,131,9,135,1,10,135,139,2,139,10,143,1,143,5,147,2,147,6,151,1,151,5,155,1,2,155,159,1,6,159,0,99,2,0,14,0]), [40, 19])
        
    def test_final(self):
        self.assertEqual(100 * 40 + 19, 4019)
