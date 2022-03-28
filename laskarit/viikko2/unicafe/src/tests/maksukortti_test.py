import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_rahan_otto_onnistuu(self):
        self.maksukortti.lataa_rahaa(10)
        returnvalue = self.maksukortti.ota_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 10)
        self.assertEqual(returnvalue, True)

    def test_rahan_otto_epaonnistuu(self):
        self.maksukortti.lataa_rahaa(5)
        returnvalue = self.maksukortti.ota_rahaa(20)
        self.assertEqual(self.maksukortti.saldo, 15)
        self.assertEqual(returnvalue, False)

    def test_lataa_negatiivista_rahaa(self):
        self.maksukortti.lataa_rahaa(-1)
        self.assertEqual(self.maksukortti.saldo, 9)
        
    def test_print_maksukortti(self):
        self.assertEqual(str(self.maksukortti), f"saldo: {round(self.maksukortti.saldo / 100, 2)}")