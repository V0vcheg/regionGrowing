import sys
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def calcHist(img: cv.Mat, chan: int, size: int):
    img_height = img.shape[0]
    img_width = img.shape[1]

    histogram = np.zeros((size,1)) 
    for y in range(0, img_height):
        for x in range(0, img_width):
            histogram[img[y, x]][0] +=1
         
    return histogram

def norm(hist: cv.Mat, dst: cv.Mat, a:int, b: int):
    min = float(hist.min())
    max = float(hist.max())

    hist_height = hist.shape[0]
    hist_width = hist.shape[1]

    for x in  range(0, hist_height):
        for y in range(0, hist_width):
            c = hist[x,y]
            dst[x,y] = (b-a) * ((c - min) / (max - min) + a)


def cumsum(a):
    a = iter(a)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)
    return np.array(b)

def eql(hist: cv.Mat, dst: cv.Mat):
    c = cumsum(hist)
    norm(c, dst, 0, 256)



def main():
    img = cv.imread("image1.jpg")
    if img is None:
        exit(0)

    bgr = cv.split(img)
    b_hist = calcHist(bgr[0], 0, 256)
    g_hist = calcHist(bgr[1], 0, 256)
    r_hist = calcHist(bgr[2], 0, 256)
    #print(b_hist)
    norm(b_hist, b_hist, 0, 256)
    norm(g_hist, g_hist, 0, 256)
    norm(r_hist, r_hist, 0, 256)

    b_hist_eql = b_hist.copy()
    g_hist_eql = g_hist.copy()
    r_hist_eql = r_hist.copy()
    eql(b_hist, b_hist_eql)
    eql(g_hist, g_hist_eql)
    eql(r_hist, r_hist_eql)

    

    histImage = np.zeros((255, 255, 3), dtype=np.uint8)
    histImage_eql = np.zeros((255, 255, 3), dtype=np.uint8)
    bin_w = int(round( 255/255 ))
    for i in range(1, 255):
        cv.line(histImage_eql, ( bin_w*(i-1), 255 - int(b_hist_eql[i-1]) ),
                ( bin_w*(i), 255 - int(b_hist_eql[i]) ),
                ( 255, 0, 0), thickness=2)
        cv.line(histImage_eql, ( bin_w*(i-1), 255 - int(g_hist_eql[i-1]) ),
                ( bin_w*(i), 255 - int(g_hist_eql[i]) ),
                ( 0, 255, 0), thickness=2)
        cv.line(histImage_eql, ( bin_w*(i-1), 255 - int(r_hist_eql[i-1]) ),
                ( bin_w*(i), 255 - int(r_hist_eql[i]) ),
                ( 0, 0, 255), thickness=2)

    for i in range(1, 255):
        cv.line(histImage, ( bin_w*(i-1), 255 - int(b_hist[i-1]) ),
                ( bin_w*(i), 255 - int(b_hist[i]) ),
                ( 255, 0, 0), thickness=2)
        cv.line(histImage, ( bin_w*(i-1), 255 - int(g_hist[i-1]) ),
                ( bin_w*(i), 255 - int(g_hist[i]) ),
                ( 0, 255, 0), thickness=2)
        cv.line(histImage, ( bin_w*(i-1), 255 - int(r_hist[i-1]) ),
                ( bin_w*(i), 255 - int(r_hist[i]) ),
                ( 0, 0, 255), thickness=2)

                
    cv.imshow('Norm hist', histImage)
    cv.imshow('Equ hist', histImage_eql)

    cv.waitKey()

if __name__ == "__main__":
    main()