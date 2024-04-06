import cv2 as cv
import numpy as np
img = cv.imread('C:/Users/User 2/Desktop/park.jpg')
cv.imshow('Park', img)
cv.waitKey(0)

b,g,r = cv.split(img)
cv.imshow('b', b)
cv.waitKey(0)
cv.imshow('g', g)
cv.waitKey(0)
cv.imshow('r', r)
cv.waitKey(0)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)
cv.waitKey(0)

blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b,blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.waitKey(0)
cv.imshow('green', green)
cv.waitKey(0)
cv.imshow('red', red)
cv.waitKey(0)