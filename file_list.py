import os
import numpy as np
from PIL import Image


rep_cat = 'C:\\tmp\\repo\\data\\test\\cats'
file_list_cat = os.listdir(rep_cat)
rep_dog= 'C:\\tmp\\repo\\data\\test\\dogs'
file_list_dog = os.listdir(rep_dog)

bilder_lista = []

for i in file_list_cat:
    bilder_lista.append('C:\\tmp\\repo\\data\\test\\cats\\'+i)

for i in file_list_dog:
    bilder_lista.append('C:\\tmp\\repo\\data\\test\\dogs\\'+i)

min_b = 100
max_b = 100
min_h = 100
max_h = 100 


for i in range(len(bilder_lista)):

    img = Image.open(bilder_lista[i])
    if img.size[0] > max_b:
        max_b = img.size[0]
    if img.size[0] < min_b:
        min_b = img.size[0]
    if img.size[1] > max_h:
        max_h = img.size[1]
    if img.size[1] < min_h:
        min_h = img.size[1]

print(min_b, max_b, min_h, max_h)









