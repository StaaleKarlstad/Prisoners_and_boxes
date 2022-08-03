import unittest
import main_simulation
from box import Box
from prisoner import Prisoner
import random

class Test_prisoners_and_boxes(unittest.TestCase):

    def test_generate_prisoners(self):
        test_list=['prisoner1', 'prisoner2', 3, True]
        main_simulation.generate_prisoners(test_list)
        
        self.assertAlmostEqual(len(test_list), 100)
        self.assertAlmostEqual(test_list[0].number, 1)
        self.assertAlmostEqual(test_list[len(test_list)-1].number, len(test_list))

    def test_generate_boxes(self):
        test_list=['box1', 'box2', 3, True]
        main_simulation.generate_boxes_with_notes(test_list, main_simulation.generate_notes())
        
        self.assertEqual(len(test_list), 100)
        self.assertEqual(test_list[0].box_number, 1)
        self.assertEqual(test_list[len(test_list)-1].box_number, len(test_list))

        for box in test_list:
            self.assertIsInstance(box.note_number, int)
    
    def test_prisoner_note_check(self):
        prisoner1=Prisoner(1,1)
        prisoner1.check_note(1)
        self.assertEqual(prisoner1.free, True)
        prisoner2=Prisoner(2,2)
        prisoner2.check_note(3)
        self.assertEqual(prisoner2.free, False)

    
    def test_check_for_correct_note(self):
        box_list=[]
        prisoner_list=[]
        notes_fail_list=[2,4,1,6,3,8,5,10,7,12,9,14,11,16,13,18,15,20,17,22,19,24,21,26,23,28,25,30
                ,27,32,29,34,31,36,33,38,35,40,37,42,39,44,41,46,43,48,45,50,47,52,49,54,51,56
                ,53,58,55,60,57,62,59,64,61,66,63,68,65,70,67,72,69,74,71,76,73,78,75,80,77,82
                ,79,84,81,86,83,88,85,90,87,92,89,94,91,96,93,98,95,100,97,99]
        
        main_simulation.generate_boxes_with_notes(box_list, notes_fail_list)
        main_simulation.generate_prisoners(prisoner_list)

        for prisoner in prisoner_list:
            main_simulation.check_for_correct_note(box_list, prisoner)
            self.assertEqual(prisoner.free, False)
        
        #==========================================================================================
        
        notes_success_list=[x for x in range(1, 101)]

        main_simulation.generate_boxes_with_notes(box_list, notes_success_list)
        main_simulation.generate_prisoners(prisoner_list)

        for prisoner in prisoner_list:
            main_simulation.check_for_correct_note(box_list, prisoner)
            self.assertEqual(prisoner.free, True)

if __name__ == '__main__':
    unittest.main()
