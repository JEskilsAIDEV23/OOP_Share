import numpy as np
import math

def knn(x, y, k =3):

    model_xy = np.array([[40,20],[50,50],[60,90],[10,25],[70,70,],[60,10],[25,80]])
    model_class = np.array(['Red','Blue','Blue','Red','Blue','Red','Blue'], dtype=str)
    n_model = len(model_xy)
    x_probable = np.empty([7,1], dtype = float)
    model_pred = {}
    class_pred = []

    for i in range(n_model):
        dist = math.sqrt((x-model_xy[i,0])**2+(y-model_xy[i,1])**2)
        model_pred[str(i)+' '+str(model_class[i])] = dist
        x_probable[i] = dist

    xp = x_probable.tolist()
    xp.sort()

    for i in range(len(xp[:k])):
        if xp[i][0] in model_pred.values():
            for j in model_pred.keys():
                if xp[i][0] == model_pred[j]:
                    j = j.split(' ')
                    class_pred.append(j[1])


    pred_count_Red = class_pred.count('Red')
    pred_count_Blue = class_pred.count('Blue')

    if pred_count_Red > pred_count_Blue:
        print(f'Sample with x = {x} and y = {y} most likely belongs to class Red')
        print(f'With k = {k}, number of Red clusters in model closest were {pred_count_Red}')

    if pred_count_Blue > pred_count_Red:
        print(f'Sample with x = {x} and y = {y} most likely belongs to class Blue')
        print(f'With k = {k}, number of Blue clusters in model closest were {pred_count_Blue}')    

    return model_pred


model_pred = knn(x = 20, y = 35, k = 5)

for i in model_pred.keys():
    print(i, model_pred[i])
