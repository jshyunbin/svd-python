import numpy as np
from PIL import Image
import math

# load image to numpy array in grayscale
image = Image.open('image.jpg').convert('L')
A = np.array(image, 'float64')

(n, m) = A.shape

U, s, VT = np.linalg.svd(A) # TODO: replace numpy function

tlen = min(n, m)
Sigma = np.zeros(A.shape)

for i in range(tlen):
    Sigma[i][i] = s[i]

B = U.dot(Sigma.dot(VT))
Image.fromarray(np.uint8(B), 'L').save('100%.jpg', 'JPEG')
t_1 = int(tlen/100)
B = U[:, :t_1].dot(Sigma[:t_1, :t_1].dot(VT[:t_1]))
Image.fromarray(np.uint8(B), 'L').save('1%.jpg', 'JPEG')
t_10 = int(tlen/10)
B = U[:, :t_10].dot(Sigma[:t_10, :t_10].dot(VT[:t_10]))
Image.fromarray(np.uint8(B), 'L').save('10%.jpg', 'JPEG')
half = int(tlen/2)
B = U[:, :half].dot(Sigma[:half, :half].dot(VT[:half]))
Image.fromarray(np.uint8(B), 'L').save('50%.jpg', 'JPEG')
t_80 = int(tlen*4/5)
B = U[:, :t_80].dot(Sigma[:t_80, :t_80].dot(VT[:t_80]))
Image.fromarray(np.uint8(B), 'L').save('80%.jpg', 'JPEG')