import urlencode
import unittest

class TestCombinations(unittest.TestCase):
    
    def setUp(self):
        self.decoded = "http://abcdef.com/whatever/something?a=ahem&b=1234&c=ok-thats-it#params{'from':'here'}"
        self.encoded = "http%3A%2F%2Fabcdef.com%2Fwhatever%2Fsomething%3Fa%3Dahem%26b%3D1234%26c%3Dok-thats-it%23params%7B%27from%27%3A%27here%27%7D"

    def test_encode(self):
        self.assertEqual(self.encoded, urlencode.encode(self.decoded))

    def test_decode(self):
        self.assertEqual(self.decoded, urlencode.decode(self.encoded))

if __name__ == '__main__':
    unittest.main()