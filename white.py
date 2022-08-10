
import cv2 as cv
import numpy as np
import math
from time import sleep, time

img = cv.imread('samples/white1.png')
img_norm = cv.imread('samples/normal1.png')

NUM_SAMPLING = 10
THRESHOLD = 255-5

def is_whitePx(pixel):
    ret = True
    for val in pixel:
        if val >= THRESHOLD:
            continue
        else:
            ret = False
            break
    return ret

def is_whitePic(img):
    [row, col, channel] = img.shape
    result = True

    for i in range(NUM_SAMPLING):
        if i*10 >= col or i*10 >= row: 
            break

        ret = is_whitePx(img[i*10, i*10])
        if ret == Fals
            result = ret
            break

    return result

cap = cv.VideoCapture(2)
_, frame = cap.read()
exp_val = cap.get(cv.CAP_PROP_EXPOSURE)
print(exp_val)
auto_exp = cap.get(cv.CAP_PROP_AUTO_EXPOSURE)
print(auto_exp)
#setting auto_exposure value to 1, which corresponds to deactivation of auto exposure control
print('auto exp set: ', cap.set(cv.CAP_PROP_AUTO_EXPOSURE, 1))
#manually set the exposure to the previous value
print('exp setting: ', cap.set(cv.CAP_PROP_EXPOSURE, exp_val))


if not cap.isOpened():
    raise IOError("cannot open webcam")

cnt = 0

while True:
    _, frame = cap.read()
    cv.imshow('hi', frame)

    k = cv.waitKey(1)

    if k%256 == 32:
        _, frame = cap.read()
        cv.imshow('hi', frame)

        trial = 0
        start = time()

        while is_whitePic(frame):
            img_name = f'0810_sample_{cnt}_{trial}.png'
            cv.imwrite(img_name, frame)

            print('too_white. shooting once more')
            trial += 1
            # sleep(1)

            _, frame = cap.read()
            end = time()
            print(end-start, 's took to evaluate and shoot once')
            cv.imshow('hi', frame)
            start = time()


        img_name = f'0810_sample_{cnt}_{trial}.png'
        cv.imwrite(img_name, frame)

        cnt += 1

    elif k%256 == 27:
        break

cap.release()
cv.destroyAllWindows()

