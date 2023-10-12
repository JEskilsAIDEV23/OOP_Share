import numpy as np
import math

xy = np.array(['20','35'], dtype = str)
k = 5
model_class = np.array([[40,20,'Red'],[50,50, 'Blue'],[60,90, 'Blue'],[10,25, 'Red'],[70,70, 'Blue'],[60,10, 'Red'],[25,80, 'Blue']], dtype=str)

def knn_alt(xy, model_class, k):

    model_values = {}
    pred_list = []
    class_list = []

    for i in range(len(model_class)):
        model_values[str(i)+' '+ model_class[i][-1]] = [model_class[i][0:-1]]

    for key in model_values.keys():
        
        mxy = model_values[key][0]
        #print(mxy)
        dist_1 = 0

        for i in range(len(mxy)):
            dist_1 += (int(xy[i]) - int(mxy[i]))**2
        dist = math.sqrt(dist_1)
        model_values[key] = dist
        pred_list.append(dist)

    pred_list.sort()
    #print(pred_list)
    xp = pred_list[0:k]

    for i in range(len(xp)):
        for key in model_values.keys():
            if xp[i] == model_values[key]:
                key = key.split()[1]
                class_list.append(key)

    print(f'n Red = {class_list.count("Red")}')
    print(f'n Blue = {class_list.count("Blue")}')

knn_alt(xy, model_class, k)