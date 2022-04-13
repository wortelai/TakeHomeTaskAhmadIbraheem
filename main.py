import Convolution
import numpy as np

img = np.array([[[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3],[4,5,6],[7,8,9]]])
filter = np.array([[1,2],[3,4]])

conv_result = Convolution.Conv(img, filter)
print(f' The result of convolving image \n {img} \n\n with filter \n {filter}\n\n is: \n {conv_result}')