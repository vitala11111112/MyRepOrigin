import unittest
import MyRep
class TestMyrep(unittest.TestCase):
    def setUp(self):
        self.obj = MyRep.MyRep()
    def test_sravnenie(self):
        self.assertEqual(self.obj.sravnenie([3,2,1]),[1,2,3])
        self.assertEqual(self.obj.sravnenie([]),[])
        self.assertEqual(self.obj.sravnenie([3,2,1,6,54,111,1000]),[1, 2, 3, 6, 54, 111, 1000])
unittest.main()