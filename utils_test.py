import unittest
from Utils import Utils

class utils_tests(unittest.TestCase):

#Test case for reversed

    def test_reversed_1(self):
        message1 = "Reversed function test failed"
        
        #test reversed with integer input
        self.assertEqual(Utils.reversed(123),321, message1)
        
        #test reversed with float input
        self.assertEqual(Utils.reversed(1.23),321, message1)
        
        #test reversed with string input
        self.assertEqual(Utils.reversed("test"),321, message1)
       
#Test case for formatter       
       
    def test_formatter_2(self):
        message2 = "Formatter function test failed"
        
        #test formatter with integer input
        self.assertEqual(Utils.formatter(9),('0b1001','0o11'), message2)
        
        #test formatter with float input
        self.assertEqual(Utils.formatter(9.9),('0b1001','0o11'), message2)
        
        #test formatter with string input
        self.assertEqual(Utils.formatter("test"),('0b1001','0o11'), message2)

if __name__ == '__main__':
	unittest.main()