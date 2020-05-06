import cv2
import numpy as np
import glob
from tkinter import Tk as tk
from tkinter import filedialog as file
'''
root = tk() #1 3 6 7 8 12 14
root.floder = file.askdirectory()
floder = str(root.floder)
'''
seq=[]
seq.append("/media/lab/INTEL_SSD/610821239/dataset/2DMOT2015/test/00/img1")
seq.append("/media/lab/INTEL_SSD/610821239/dataset/2DMOT2015/test/01/img1")
seq.append("/media/lab/INTEL_SSD/610821239/dataset/2DMOT2015/test/02/img1")
seq.append("/media/lab/INTEL_SSD/610821239/dataset/2DMOT2015/test/03/img1")
seq.append("/media/lab/INTEL_SSD/610821239/dataset/2DMOT2015/test/04/img1")
seq.append("/media/lab/INTEL_SSD/610821239/dataset/2DMOT2015/test/05/img1")
seq.append("/media/lab/INTEL_SSD/610821239/dataset/2DMOT2015/test/06/img1")
seq.append("/media/lab/INTEL_SSD/610821239/dataset/2DMOT2015/test/07/img1")
seq.append("/media/lab/INTEL_SSD/610821239/dataset/2DMOT2015/test/08/img1")
seq.append("/media/lab/INTEL_SSD/610821239/dataset/2DMOT2015/test/09/img1")
seq.append("/media/lab/INTEL_SSD/610821239/dataset/2DMOT2015/test/10/img1")



img_array = []
for i in range(len(seq)):
    for filename in sorted(glob.glob(seq[i] +"/*.jpg")):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
        print(filename)



        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        out = cv2.VideoWriter(str(i)+".mp4",fourcc,15, size)
        
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    img_array.clear()