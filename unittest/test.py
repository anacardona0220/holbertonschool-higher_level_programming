import unittest
# importo la funcion que vamos a testear sum_n_numbers
from prueba_suma import sum_numbers


# unittest tranaja con una clase, es decir hay que definirla, testSum, cogemos el
class testSum(unittest.TestCase):
    # modulo unittest que heredamos todo lo de la clase TestCase
    def test_sum_numbers_default_args(self):  # crear prueba por prueba
        # assert_equal me permite hacer una comparacion de iguales
        self.assertEqual(sum_numbers(), 5050)
        

    def test_sum_numbers_default_args1(self):  # crear prueba por prueba
        # assert_equal me permite hacer una comparacion de igu self.assertEqual(sum_numbers(), 5050)
        self.assertEqual(sum_numbers(0), 5050)
    
    def test_sum_numbers_various_inputs(self):
        self.assertEqual(sum_numbers(range(1, 11)), 55)
        self.assertEqual(sum_numbers((1,2,3,)), 6)
        self.assertEqual(sum_numbers([1,2,3]), 6)
        self.assertEqual(sum_numbers([]), 0)
        
        

if __name__ == '__main__':  # este es el standar para ejecutar unittest,es como se llama a la ejecucion de unittest
    unittest.main()
