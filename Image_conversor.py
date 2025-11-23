import cv2
import pandas as pd


def transformImage(img):
    img = cv2.resize(img, (8, 8))
    img = 255 - img
    img = img * (16 / 255)
    img = cv2.convertScaleAbs(img)

    return img


to_dataframe = []

for i in range(10):
    print(i)
    print()
    for j in range(6):
        print(j)
        print()
        img_general_pathfile = f"Imgs/general - {i} - Copy ({j}).jpg"
        img = cv2.imread(img_general_pathfile, cv2.IMREAD_GRAYSCALE)
        img = transformImage(img)
        print(img)
        flat = img.ravel().tolist()
        flat.append(i)
        print(flat)
        to_dataframe.append(flat)
        print("========================")

df = pd.DataFrame(to_dataframe)
print(df)

df.to_csv("numeros.csv", index = False, header = [i for i in range(65)])
print("Todo en orden")