# --- Programmierblatt 05 Aufgabe 2 ---
import numpy as np
# %%
class Vandermonde_model:
    #Interpolation with Newton
    def fit(self, x, y):
        if np.shape(x)[0] != np.shape(y)[0]:
            raise ValueError('x and y must have same dimension')
        n = np.shape(x)[0]
        if n<2: raise ValueError('at least two points must be given to plot graph')
        a = np.zeros(n)  
        
        a[0]=y[0]
        a[1]= (y[1]-y[0])/(x[1]-x[0])
        
        for j in range(2,n):
            Xj_k = x[j]-x[j-1]
            a[j] = -a[j-1]/Xj_k
            for k in range(2,j):
               Xj_k *= x[j]-x[j-k]
               a[j] -= a[j-k]/Xj_k
            a[j] += y[j]/Xj_k 
        
        self.x = x
        self.y = y
        self.p = a   
        
    def __call__(self, x):
        return np.polyval(self.p,x)
    
    def add_points(self, x, y):
        #Add aditional points from x & y without destroying existing p
        n = np.shape(self.p)
        if np.shape(x)[0] != np.shape(y)[0]:
            raise ValueError('x and y must have same dimension')
        m = np.shape(x)[0]
        if n<2: raise ValueError('at least two points must be given to plot graph')
        
        a = np.zeros(m) 
        x = np.concatenate(self.x, x)
        y = np.concatenate(self.y, y)
        
        for j in range(n,n+m):
            Xj_k = x[j]-x[j-1]
            a[j-n] = -a[j-1]/Xj_k
            for k in range(2,j):
               Xj_k *= x[j]-x[j-k]
               if k > j:
                  a[j-n] -= self.p[n+j-k]/Xj_k #if ak value is in p
               else:
                   a[j-n] -= a[j-k]/Xj_k
            a[j-n] += y[j]/Xj_k 
        
        self.x = x
        self.y = y
        self.p = a 