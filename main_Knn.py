import numpy as np
import math
from PIL import Image
from cls_Knn import *

paths = ['/Users/jeskils/knn/cats', '/Users/jeskils/knn/dogs']
cluster_n = ['cat','dog']
b = 50
h = 50

def make_model(paths, cluster_n, b, h):

    pf = Files2model()
    pf.set_path2f(paths)
    pf.set_cluster_names(cluster_n)
    model_id_list, model_file_list = pf.model_file()
    model_sng_list = scale_n_grey_fnp(model_file_list, b , h)
    bilder = make_model_file(model_sng_list, model_id_list)

    return bilder, model_sng_list, model_id_list, model_file_list
#d = Calculate_Knn('/Users/jeskils/knn/Dice/3/3.png','/Users/jeskils/knn/Model_Img_(100x100).npz',100,100,3)


def use_model(test_file, model2use, b, h, k):

    res_mod = Calculate_Knn(test_file,model2use,b,h,k)

    return res_mod

#make_model(paths, cluster_n, b, h)

model2use = '/Users/jeskils/knn/Model_Img_(50x50).npz'
b = 50
h = 50
k = 5
test_file = '/Users/jeskils/knn/test/cat.946.jpg'

res_mod = use_model(test_file, model2use, b, h, k)
