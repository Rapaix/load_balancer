from load_balancer import read_file, load_balancer
from unittest import TestCase


class TestLoadBalancer(TestCase):

    def setUp(self):
        self.array_arquivo = read_file('input_teste.txt')
        self.resultado_final = load_balancer(
            self.array_arquivo[2:], self.array_arquivo[0], self.array_arquivo[1],)

    def test_deve_retornar_uma_string_quando_o_valor_de_ttask_esta_fora_dos_limites(self):
        array_arquivo = read_file('input_teste_ttask.txt')
        mensagem_esperada = 'O valor 11 de ttask está fora dos limites'

        self.assertEqual(mensagem_esperada, array_arquivo)

    def test_deve_retornar_uma_array_não_vazio_quando_o_txt_esta_correto(self):

        valor_esperado = [4, 2, 1, 3, 0, 1, 0, 1]

        self.assertEqual(valor_esperado, self.array_arquivo)

    def test_deve_retornar_uma_string_quando_o_valor_de_umax_esta_fora_dos_limites(self):
        array_arquivo = read_file('input_teste_umax.txt')
        mensagem_esperada = 'O valor 0 de umax está fora dos limites'

        self.assertEqual(mensagem_esperada, array_arquivo)

    def test_deve_retornar_o_resultadofianal_do_load_balancer_quando_passado_txt_correto(self):
        valor_esperado = ['1,', '2,2,', '2,2,', '2,2,1,',
                          '1,2,1,', '2,', '2,', '1,', '1,', '0', '15']
        self.assertEqual(valor_esperado, self.resultado_final)
