# Matrix Operations Module

## Description

`Matrix_operations` is a Python module designed to handle and perform various matrix operations. It includes functionalities such as addition, subtraction, multiplication, transposition, determinant calculation, and more.

## Features

- **Matrix Creation**: Initialize a matrix with a list of lists.
```python
from Matrix import Matrix
A = Matrix([[1, 2, 1], [0, 1, 1], [1, 0, 1]])
```

- **Display**: Print formatted elements of a matrix.
```python
print(A)
```

- **Identity Matrix**: Generate an identity matrix for a square matrix.
```python
I = A.id()
print(I)  # Displays the 3×3 identity matrix, matching the size of A
```

- **Addition and Subtraction**: Perform operations on matrices of the same dimensions.
```python
B = Matrix([[2, 1, 0], [0, 1, 1], [1, 0, 0]])
print(A + B)
print(A - B)
```

- **Multiplication**: Perform compatible matrix multiplication.
```python
print(A * B)
print(3 * A) 
```

- **Transpose**: Returns the transpose of a matrix.
```python
T = A.transpose()
print(T)
```

- **Power**: Calculate powers of a matrix, including the inverse.
```python
n = 3
M = A**n
print(M)
Inv = A**-1  # Inverse of A
print(Inv)
```

- **Determinant**: Calculate the determinant of square matrices.
```python
d = A.det()
print(d)
```

- **Cofactor Matrix**: Compute the cofactor matrix.
```python
C = A.com()
print(C)
```

- **Inverse**: Calculate the inverse of a matrix if possible.
```python
I1 = A.inv()
print(I1)
I2 = A**-1
print(I2)
```

## Installation

Clone the project and install it locally using `pip`:
```bash
git clone https://github.com/Rafita261/matrix-operations.git
cd matrix-operations
pip install .
```

For development mode:
```bash
pip install -e .
```

## Tests

To run tests (in the `tests/` directory):
```bash
pytest tests/
```

## Contributions

Contributions are welcome. Please submit a pull request or report an issue on GitHub.

## License

This project is licensed under the MIT License.

---

## Author

Fitahiana Christalin RATSIMBAZAFY (Rafita261/Chriskely)
