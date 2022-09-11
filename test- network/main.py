import numpy as np
arr = np.array([['-','-','-'],['-','-','-'],['-','-','-']])
arr[1,2] = 'x'
print(arr)

if arr[1,2] == 'x':
    print('hi')