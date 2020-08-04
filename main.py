import numpy as np
from PIL import Image
import math

# load image to numpy array in grayscale
image = Image.open('image.jpg').convert('L')
A = np.array(image, 'float_')

AAT = A.dot(np.transpose(A))
ATA = np.transpose(A).dot(A)

def is_upper(A):
    (n, m) = A.shape
    for i in range(n):
        for j in range(i-1):
            if A[i][j]:
                return False
    return True

def norm(v):
    return math.sqrt(sum([x**2 for x in v]))

def QRDecmp(A):
    (n, m) = A.shape
    if n != m: 
        raise TypeError
    R = A
    Q = np.array([[0.0] * n for _ in range(n)])

    for k in range(n-1):
        

def RFA(A):
    while not is_upper(A):
        
