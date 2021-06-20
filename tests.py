import unittest
from convert import Convert

class TestSuite(unittest.TestCase):

    def test_input_exists(self):
        with self.assertRaises(ValueError):
            self.assertTrue(Convert().toRoman())
    
    def test_input_is_not_none(self):
        with self.assertRaises(ValueError):
            self.assertTrue(Convert().toRoman(number=None))
    
    def test_input_is_integer(self):
        with self.assertRaises(ValueError):
            self.assertTrue(Convert().toRoman(number='input'))
    
    def test_input_is_not_zero(self):
        with self.assertRaises(ValueError):
            self.assertTrue(Convert().toRoman(number=0))
    def test_input_is_not_less_than_zero(self):
        with self.assertRaises(ValueError):
            self.assertTrue(Convert().toRoman(number=-10))

    def test_input_is_not_out_of_range(self):
        with self.assertRaises(ValueError):
            self.assertTrue(Convert().toRoman(number=4000))

    def test_2_equals_II(self):
        self.assertEqual(Convert().toRoman(number=2), 'II')

    def test_7_equals_VII(self):
        self.assertEqual(Convert().toRoman(number=7), 'VII')

    def test_9_equals_IX(self):
        self.assertEqual(Convert().toRoman(number=9), 'IX')
    
    def test_25_equals_XXV(self):
        self.assertEqual(Convert().toRoman(number=25), 'XXV')
    
    def test_75_equals_LXXV(self):
        self.assertEqual(Convert().toRoman(number=75), 'LXXV')

    def test_250_equals_CCL(self):
        self.assertEqual(Convert().toRoman(number=250), 'CCL')

    def test_500_equals_D(self):
        self.assertEqual(Convert().toRoman(number=500), 'D')
    
    def test_750_equals_DCCL(self):
        self.assertEqual(Convert().toRoman(number=750), 'DCCL')

    def test_1001_equals_MI(self):
        self.assertEqual(Convert().toRoman(number=1001), 'MI')
    
    def test_1250_equals_MCCL(self):
        self.assertEqual(Convert().toRoman(number=1250), 'MCCL')

    def test_2421_equals_MMCDXXI(self):
        self.assertEqual(Convert().toRoman(number=2421), 'MMCDXXI')
    
    def test_3999_equals_MMMCMXCIX(self):
        self.assertEqual(Convert().toRoman(number=3999), 'MMMCMXCIX')

    def test_II_equals_2(self):
        self.assertEqual(Convert().toArabic(number='II'), 2)
    
    def test_IV_equals_4(self):
        self.assertEqual(Convert().toArabic(number='IV'), 4)
    
    def test_VII_equals_7(self):
        self.assertEqual(Convert().toArabic(number='VII'), 7)
    
    def test_IX_equals_9(self):
        self.assertEqual(Convert().toArabic(number='IX'), 9)
    
    def test_XXV_equals_25(self):
        self.assertEqual(Convert().toArabic(number='XXV'), 25)
    
    def test_LXXV_equals_75(self):
        self.assertEqual(Convert().toArabic(number='LXXV'), 75)

    def test_CCL_equals_250(self):
        self.assertEqual(Convert().toArabic(number='CCL'), 250)

    def test_D_equals_500(self):
        self.assertEqual(Convert().toArabic(number='D'), 500)

    def test_DCCL_equals_750(self):
        self.assertEqual(Convert().toArabic(number='DCCL'), 750)

    def test_MI_equals_1001(self):
        self.assertEqual(Convert().toArabic(number='MI'), 1001)
    
    def test_MCCL_equals_1250(self):
        self.assertEqual(Convert().toArabic(number='MCCL'), 1250)
    
    def test_MMCDXXI_equals_2421(self):
        self.assertEqual(Convert().toArabic(number='MMCDXXI'), 2421)
    
    def test_MMMCMXCIX_equals_3999(self):
        self.assertEqual(Convert().toArabic(number='MMMCMXCIX'), 3999)
