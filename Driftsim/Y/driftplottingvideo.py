import argparse
import math
import scipy
import numpy as np
from scipy import special, optimize
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import cv2

img1 = cv2.imread('/home/aske/test/ThreeDdiffusion/Y/Images/parralleldiffusion1.png')

fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')

height, width, layers = img1.shape

video = cv2.VideoWriter('ZdistParDiffusionPhiminus9Dx5.avi',fourcc,10,(width,height))

for i in range(100):
    img = cv2.imread('/home/aske/test/ThreeDdiffusion/Y/Images/pardiffusionphi9Zdist' + str(i) + '.png')
    
    video.write(img)
    #cv2.imshow('Video', img)
    
cv2.destroyAllWindows()
video.release()

    