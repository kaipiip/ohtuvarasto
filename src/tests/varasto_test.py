import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.varasto = Varasto(0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_negatiivisen_saldon(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_konstruktori_luo_tyhjan_varaston_ja_neg_saldon(self):
        self.varasto = Varasto(0, -10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_pienemman_saldon_kuin_tilavuus(self):
        self.varasto = Varasto(10, 5)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_konstruktori_luo_suuremman_saldon_kuin_tilavuus(self):
        self.varasto = Varasto(5, 10)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_neg_saldoa(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_liikaa_saldoa(self):
        self.varasto.lisaa_varastoon(1000)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaa_varastosta_neg_arvon(self):
        saatu_maara = self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaa_varastosta_yli_saldon(self):
        self.varasto = Varasto(10, 10)
        saatava_maara = self.varasto.saldo
        saatu_maara = self.varasto.ota_varastosta(15)
        self.assertAlmostEqual(saatu_maara, saatava_maara)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_str_(self):
        self.assertEqual(str(self.varasto), 
                               "saldo = 0, vielä tilaa 10")
