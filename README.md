# Matrix Operations Module

## Description

`Matrix_operations` est un module Python conçu pour manipuler et effectuer diverses opérations sur des matrices. Il inclut des fonctionnalités telles que l'addition, la soustraction, la multiplication, la transposition, le calcul du déterminant, et plus encore.

## Fonctionnalités

- **Création de matrices** : Initialisez une matrice avec une liste de listes.
```python 
from Matrix import Matrix
A = Matrix([[1,2,1],[0,1,1],[1,0,1]])
```
- **Affichage** : Affichez les éléments formatés d'une matrice.
```python
print(A)
```
- **Matrice identité** : Génère une matrice identité pour une matrice carrée.
```python
I = A.id()
print(I) #Affiche la matrice identité 3×3 : taille de A
```
- **Addition et soustraction** : Opérations entre matrices de mêmes dimensions.
```python
B = Matrix([2,1,0],[0,1,1],[1,0,0])
print(A+B)
print(A-B)
```
- **Multiplication** : Multiplication matricielle compatible.
```python
print(A*B) 
```
- **Transposition** : Retourne la transposée d'une matrice.
```python
T = A.transpose()
print(T)
```
- **Puissance** : Calcul de puissances d'une matrice, y compris l'inverse.
```python
n = 3
M = A**3 
print(M)
Inv = A**-1 #inverse de A
print(Inv)
```
- **Déterminant** : Calcul du déterminant des matrices carrées.
```python
d = A.det()
print(d)
```
- **Comatrice** : Calcul de la comatrice.
```python
C = A.com()
print(C)
```
- **Inverse** : Calcule l'inverse d'une matrice si possible.
```python
I1 = A.inv()
print(I1)
I2 = A**-1
print(I2)
```

## Installation

Clonez le projet et installez-le localement avec `pip`:
```bash
git clone https://github.com/Rafita261/matrix-operations.git
cd matrix-operations
pip install .
```

Pour un mode développement :
```bash
pip install -e .
```

##Tests

Pour exécuter les tests (si vous avez des tests unitaires dans tests/) :
```bash
pytest tests/
```
##Contributions

Les contributions sont les bienvenues. Veuillez soumettre une pull request ou signaler un problème sur GitHub.

##Licence

Ce projet est sous licence MIT.


---

##Auteur

Fitahiana Christalin RATSIMBAZAFY (Rafita261/Chriskely)
