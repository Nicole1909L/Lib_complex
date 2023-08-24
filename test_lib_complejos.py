import lib_complejos as lcp
import unittest

class TestcplxOperations (unittest.TestCase):

    def test_sumacplx(self):
        suma = lcp.sumacplx(c1=(5,1.8),c2=(3,-5.6))
        self.assertAlmostEqual(suma[0], 8)
        self.assertAlmostEqual(suma[1], -3.8)

        suma = lcp.sumacplx(c1=(3,9),c2=(-2,6))
        self.assertAlmostEqual(suma[0], 1)
        self.assertAlmostEqual(suma[1], 15)

    def test_multicplx(self):
        multip = lcp.multicplx(c1=(5,1.8),c2=(3,-5.6))
        self.assertAlmostEqual(multip[0], 25.08)
        self.assertAlmostEqual(multip[1], -22.6)

        multip = lcp.multicplx(c1=(3,9),c2=(-2,6))
        self.assertAlmostEqual(multip[0], -60)
        self.assertAlmostEqual(multip[1], 0)
    
    def test_restcplx(self):
        resta = lcp.restcplx(c1=(5,1.8),c2=(3,-5.6))
        self.assertAlmostEqual(resta[0], 2)
        self.assertAlmostEqual(resta[1], 7.4)

        resta = lcp.restcplx(c1=(3,9),c2=(-2,6))
        self.assertAlmostEqual(resta[0], 5)
        self.assertAlmostEqual(resta[1], 3)

    def test_divicplx(self):
        divis = lcp.divicplx(c1=(5,1.8),c2=(3,-5.6))
        self.assertAlmostEqual(divis[0], 0.12, places= 1)
        self.assertAlmostEqual(divis[1], 0.82, places= 1)

        divis = lcp.divicplx(c1=(3,9),c2=(-2,6))
        self.assertAlmostEqual(divis[0], 1.2)
        self.assertAlmostEqual(divis[1], -0.9)

    def test_moducplx(self):
        modulo = lcp.moducplx(4,5)
        self.assertAlmostEqual(modulo, 6.40, places= 1)

        modulo = lcp.moducplx(2,8)
        self.assertAlmostEqual(modulo, 8.24, places= 1)
    
    def test_conjucplx(self):
        conjugado = lcp.conjucplx(4,5)
        self.assertAlmostEqual(conjugado[0], 4)
        self.assertAlmostEqual(conjugado[1], -5)

        conjugado = lcp.conjucplx(2,-8)
        self.assertAlmostEqual(conjugado[0], 2)
        self.assertAlmostEqual(conjugado[1], 8)

    def test_fasecplx(self):
        fase = lcp.fasecplx(4,5)
        self.assertAlmostEqual(fase, 0.89, places= 1)

        fase = lcp.fasecplx(2,8)
        self.assertAlmostEqual(fase, 1.32, places= 1)

    def test_geomcplx(self):
        geomet = lcp.geomcplx(4,5)
        self.assertAlmostEqual(geomet[0], 4.0, places= 1)
        self.assertAlmostEqual(geomet[1], 4.99, places= 1)

        geomet = lcp.geomcplx(2,8)
        self.assertAlmostEqual(geomet[0], 1.99, places= 1)
        self.assertAlmostEqual(geomet[1], 8.0,places=1)


if __name__ == '__main__':
    unittest.main()