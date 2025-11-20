# instalar opencv-python

import cv2

img_array = cv2.imread("Datasets/miNumero.png", cv2.IMREAD_GRAYSCALE)
#print(img_array)
nueva_img = cv2.resize(img_array, (8,8))

print(nueva_img)
