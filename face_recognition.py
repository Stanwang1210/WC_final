# from deepface import DeepFace
import os
from os.path import join
import cv2
import sys
from sys import exit
import glob
from API import verify
img1 = sys.argv[1]
img2 = glob.glob("./Auth/*.jpg")
pair_num = len(img2)
# img2 = join(Auth_dir, "*/.jpg")
# print(Auth_dir)
# exit(0)
success = False
# for img2 in Auth_dir:
    # print("Verifying ...", end="\r")
    # if success:
        # exit(0)
if os.path.exists(img1) :

    if (cv2.imread(img1) is not None) :
    # print("Both exists")

        result = verify(img1, img2)
        if 'error' in result.keys():
            if result['error']  == "Face could not be detected. Please confirm that the picture is a face photo or consider to set enforce_detection param to False.":
                    print("Can not detect face. Pls take the photo again !")
                    exit(0)
        elif 'pair_1' in result.keys():
            for i in range(1, pair_num +1):
                if result[f'pair_{i}']["verified"]:
                    print("Successfully Access !")
                    success = True
                    exit(0)
        #     print("Access Failed !")
    else:
        if cv2.imread(img1) is  None:
            print(f"File {img1} is Null !", end="\r") 
        # if cv2.imread(img2) is  None:
        #     print(f"File {img2} is Null !")
else:
    if os.path.exists(img1) :
        print(f"File {img1} not exists !", end="\r")
        
        # if os.path.exists(img2):
        #     print(f"File {img2} not exists !")
print("Access Denied !!!")
