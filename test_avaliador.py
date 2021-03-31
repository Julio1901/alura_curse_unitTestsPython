from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao

class TestAvaliador(TestCase):
    def test_avalia(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 100.0)
        lance_do_gui = Lance(gui, 150.0)
        leilao = Leilao('Leilao de celular')
        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_gui)

# python -m unittest file_test_name
if __name__ == '__main__':
    unittest.main()
