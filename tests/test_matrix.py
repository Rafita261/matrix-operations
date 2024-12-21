import unittest
from Matrix import Matrix  

class TestMatrixOperations(unittest.TestCase):

    def test_matrix_diagonalization(self):
        # Matrice de départ
        A = Matrix([[1, 1], [4, 1]])
        # Matrice de passage
        P = Matrix([[1, -1], [2, 2]])
        # Transformation T
        T = (P**-1) * A * P
        expected_T = [[3.0, 0.0], [0.0, -1.0]]  # Exemple de résultat attendu
        self.assertEqual(T.M, expected_T)

    def test_fibonacci(self):
        # Suite de Fibonacci en O(log n)
        def F(n):
            M = Matrix([[1, 1], [1, 0]])
            A0 = Matrix([[1], [1]])
            Mn = M**n
            s = Mn * A0
            return s.M[1][0]
        
        # Test du Fibonacci de n = 100
        self.assertEqual(F(9), 55)
        self.assertEqual(F(100), 573147844013817084101)

if __name__ == '__main__':
    unittest.main()
