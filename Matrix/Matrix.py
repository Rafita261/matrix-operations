import math
class Matrix :
    def __init__(self) :
        self.M=[[]]
        self.size = 0,0
    def __init__(self, t) :
        self.M = t
        self.size = len(t), len(t[0])
    
    # Matrice Identité d'une matrice carrée
    def id(self) :
        n,m = self.size
        if n!=m :
            raise ValueError("The matrix is not square")
        else :
            t = []
            for i in range(n) :
                h=[]
                for j in range(n) :
                    if i == j :
                        h.append(1)
                    else :
                        h.append(0)
                t.append(h)
            return Matrix(t)
    
    # Casting vers str : faites pour la fonction print()
    def __str__(self) :
        string = []
        x,y = self.size
        M_copy=[]
        for j in range(x) :
            h=[]
            for i in range(y) :
                if self.M[j][i] == int(self.M[j][i]) :
                    h.append(str(int(self.M[j][i])))
                else :
                    h.append(str(round(self.M[j][i],2)))
            M_copy.append(h)
            
        for elem in M_copy :
            string.append('\t'+'('+'\t'.join(elem)+')')
        return '\n'.join(string)+'\n'
        
    # Méthode pour transposer une matrice
    def transpose(self) :
        a,b = self.size
        s=[]
        for x in range(b) :
            h =[]
            for y in range(a) :
                h.append(self.M[y][x])
            s.append(h)
        return Matrix(s)
    def __float__(self) :
        return math.inf
    # Surcharge de l'opération multiplication * pour le produit matriciel / produit avec un nombre
    def __mul__(self,B) :
        if float(B) == math.inf :
            t=[]
            n,m = B.size
            k,p= self.size
            if n!=p :
                raise ValueError("Matrix multiplication is not possible due to incompatible dimensions")
            for i in range(k) :
                h = []
                for j in range(m) :
                    s = 0
                    for l in range(n) :
                        s+=self.M[i][l]*B.M[l][j]
                    h.append(s)
                t.append(h)
            return Matrix(t)
        t=[]
        a = B
        n,m = self.size
        for i in range(n) :
            h = []
            for j in range(m) :
                h.append(a*self.M[i][j])
            t.append(h)
        return Matrix(t)
        
    def __rmul__(self,B) :
        return self * B

    # Surcharge de l'opération ** pour la puissance de matrice 
    def __pow__(self,n) :
        if n==-1 :
            return self.inv()
        if n == 0 : return self.id()
        if n == 1 : return self
        if n != int(n) : 
          raise ValueError("Matrix exponentiation can only be performed with integer powers")
        if n%2 == 0 :
            B = self**(n/2)
            return B*B
        else :
            return self*(self**(n-1)) 
   
    #Surcharge de l'opération + pour additionner deux matrices        
    def __add__(self,B) :
        n,m = self.size
        p,q = B.size
        if n!=p or m!=q :
            raise ValueError("Cannot add two matrices of different dimensions")
        t = self.M
        k = B.M
        s=[]
        for i in range(n) :
            u=[]
            for j in range(m) :
                u.append(t[i][j]+k[i][j])
            s.append(u)
        return Matrix(s)
      
    #Surcharge de l'opération - pour soustraire deux matrices          
    def __sub__(self,B) :
        n,m = self.size
        p,q = B.size
        if n!=p or m!=q :
            raise ValueError("Cannot subtract two matrices of different dimensions")
        t = self.M
        k = B.M
        s=[]
        for i in range(n) :
            u=[]
            for j in range(m) :
                u.append(t[i][j]-k[i][j])
            s.append(u)
        return Matrix(s)
    
    # Méthode pour trouver le cofacteur d'une matrice en position (i,j) (Commençant par 0)
    def cof(self,i,j) :
        n,m = self.size
        t=self.M
        h=[]
        for k in range(n) :
            T=[]
            if k==i :
                continue
            for l in range(m) :
                if l==j : continue
                T.append(t[k][l])
            h.append(T)
        return Matrix(h)
    
    # Méthode pour calculer le déterminant d'une matrice carrée 
    def det(self) :
        s=0
        n,m = self.size
        if n!=m :
            raise ValueError("Determinants can only be calculated for square matrices!")
        t=self.M
        if n==2 :
            s+=t[0][0]*t[1][1]-(t[1][0]*t[0][1])
            return s
        for i in range(n) :
            s+=((-1)**i)*t[0][i]*(self.cof(0,i)).det()
        return s
     
    # Méthode pour trouver la comatrice d'une matrice
    def com(self) :
        t=[]
        n,m = self.size
        for i in range(n) :
            h=[]
            for j in range(m) :
                s=((-1)**i)*((-1)**j)*(self.cof(i,j)).det()
                h.append(s)
            t.append(h)
        return Matrix(t)
        
    # Méthode pour trouver l' inverse d'une matrice '
    def inv(self) :
        n,m = self.size
        d = self.det()
        if n==2 :
            t=self.M
            a,b= t[0]
            c,e=t[1]
            return Matrix([[e/d,-b/d],[-c/d,a/d]])
        t = self.com().transpose().M
        if n!=m :
            raise ValueError("Non-square matrices do not have an inverse")
        if d == 0 :
            raise ValueError("The matrix is not invertible because its determinant is 0")
        for i in range(n) :
            for j in range (m) :
                t[i][j] /=d
        return Matrix(t)