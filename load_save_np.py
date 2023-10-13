import numpy as np

# np save
a = np.array([10,10,10,10,10])
b = np.array(['b','r','r','b','r'])
file_s = 'bilder'
np.savez(file_s, a = a, b = b)

# np load
with np.load(file_s+'.npz') as data:

    a = data['a']
    b = data['b']
    print(a)
    print(b)