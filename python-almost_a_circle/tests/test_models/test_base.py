import unittest

from models.base import Base


class BaseTestCase(unittest.TestCase):
    def test_id_generation(self):
        # Creamos dos instancias de la clase Base sin proporcionar un ID
        obj1 = Base()
        obj2 = Base()

        # Comprobamos que los IDs generados son únicos
        self.assertNotEqual(obj1.id, obj2.id)

    def test_id_assignment(self):
        # Creamos una instancia de la clase Base proporcionando un ID
        obj = Base(id=10)
        
    # Comprobamos que el ID asignado es el esperado
        self.assertEqual(obj.id, 10)

if __name__ == '__main__':
    unittest.main()    