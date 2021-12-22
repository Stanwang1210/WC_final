from deepface import DeepFace
import os
from os.path import join
import cv2
import sys
from sys import exit
import glob
img1 = sys.argv[1]
Auth_dir = glob.glob("./Auth/*.jpg")
# img2 = join(Auth_dir, "*/.jpg")
# print(Auth_dir)
# exit(0)
success = False
for img2 in Auth_dir:
    print("Verifying ...", end="\r")
    if success:
        exit(0)
    if os.path.exists(img1) :

        if (cv2.imread(img1) is not None) :
        # print("Both exists")

            result = DeepFace.verify(img1_path = img1, img2_path = img2, enforce_detection=False)
            # print(result)
            if result["verified"]:
                print("Successfully Access !")
                success = True
            # else:
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