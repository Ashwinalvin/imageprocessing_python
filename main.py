import cv2
import numpy
img1 = cv2.imread('sports 1.jpg',-1)
img2 = cv2.imread('ashwinrr.jfif',-1)
def show():
    cv2.imshow('img1',img1)
    cv2.waitKey(70000)
    cv2.destroyAllWindows()

def resized_img(width,height):
    resized=cv2.resize(img1,(width,height))
    cv2.imshow('resized',resized)
    cv2.waitKey(70000)
    cv2.destroyAllWindows()

def blur_img(b,a):
    blurred=cv2.GaussianBlur(img1,(b,a),0)
    cv2.imshow('blurred',blurred)
    cv2.waitKey(70000)
    cv2.destroyAllWindows()

def gray():
    gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    cv2.waitKey(70000)
    cv2.destroyAllWindows()

bord = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT)
cv2.imshow('img',bord)
cv2.waitKey(700000)
cv2.destroyAllWindows()









