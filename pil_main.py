from PIL import Image
import numpy as np
import math

img = Image.open("1.png")
print(type(img))

#img.show()

#print(img.size)

img_2 = img.convert('L')

#img_2.show()

#for i in range(90):
 #   for j in range(90):
   #     d = img_2.getpixel(xy=(i,j))
     #   print(d)


#ny_bild = Image.new(mode='RGBA', size=(35,35), color = 'pink')

img = Image.new(mode='RGBA', size=(100,100), color = (200,200,200,255))

#pixels = img.load()

#for i in range(70):
    #for j in range(70):
        #pixels[i,j] = (100+i,170-j,170-i)

r = 10
x1 = 21
y1 = 21
x2 = math.pi*r
y2 = math.pi*r
#r = math.sqrt((x2-x1)**2+(y2-x1)**2)


cords = np.zeros([400,2])

n = 0
for i in range(-200,200):
    for j in range(-200,200):
        if math.sqrt((i-x1)**2+(j-y1)**2) / r >= 0.99 and math.sqrt((i-x1)**2+(j-y1)**2) / r <= 1.01:
            print(i,j)
            cords[n,0] = i-x1
            cords[n,1] = j-y1
            n +=1
print(n)

#print(cords)

pixels = img.load()


for i in range(n):
#print(cords[i][0])

    pixels[cords[i][0],cords[i][1]] = (0,0,0)

img.show()

r = 25 

for i in range(51):
    for j in range(51):
        if round(math.sqrt((i-25)**2+(j-25)**2),0) == r:
            pixels[i,j] = (100,100,100)

img.show()