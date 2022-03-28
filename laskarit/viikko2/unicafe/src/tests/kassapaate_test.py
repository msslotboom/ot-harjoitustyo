import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(0)

    def test_oikea_maara_rahaa_ja_myyty(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_oikea_maara_edullisia_aterioita(self):    
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_oikea_maara_kalliita_aterioita(self):    
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_osto_onnistuu_tarpeeksi_rahaa_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(vaihtoraha, 1000-240)

    def test_osto_onnistuu_tarpeeksi_rahaa_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(vaihtoraha, 1000-400)

    def test_osto_edullinen_onnistuu_ostojen_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_osto_onnistuu_ostojen_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_maksu_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kallis_maksu_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    #####Tests that use Maksukortti
    def test_maksu_kortilla_veloittaa_ja_palauttaa_edullinen(self):
        self.maksukortti.lataa_rahaa(1000)
        returnvalue = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000-240)
        self.assertEqual(returnvalue,True)

    def test_maksu_kortilla_veloittaa_ja_palauttaa_maukas(self):
        self.maksukortti.lataa_rahaa(1000)
        returnvalue = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000-400)
        self.assertEqual(returnvalue,True)



    #Maksut kortilla maara kasvaa
    def test_maksu_kortilla_tarpeeksi_rahaa_edullinen_kasvaa(self):
        self.maksukortti.lataa_rahaa(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maksu_kortilla_tarpeeksi_rahaa_edullinen_kasvaa(self):
        self.maksukortti.lataa_rahaa(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)


    #Maksu epaonnistuu
    def test_maksu_kortilla_ei_veloittaa_jos_ei_tarpeeksi_rahaa_edullinen(self):
        self.maksukortti.lataa_rahaa(10)
        returnvalue = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 10)
        self.assertEqual(returnvalue,False)

    def test_maksu_kortilla_ei_veloittaa_jos_ei_tarpeeksi_rahaa_maukas(self):
        self.maksukortti.lataa_rahaa(10)
        returnvalue = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 10)
        self.assertEqual(returnvalue,False)



    #Maksut kortilla veloitus ok
    def test_maksu_kortilla_tarpeeksi_rahaa_edullinen_veloitus_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksu_kortilla_tarpeeksi_rahaa_maukas_veloitus_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)



    #Saldon nosto toimii
    def test_saldon_nosto_kassasta_veloittaa_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+10)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_saldon_nosto_kassasta_veloittaa_oikein_jos_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 0)

