import numpy as np
import cv2

img = cv2.imread('./yorkie.png', cv2.IMREAD_COLOR)

x = 200
y = 100
channel = 0

bgr_val = img[y, x]
#print(type(bgr_val))
print(f'bgr_val({x}, {y}) = {bgr_val}')

b_val = img[y, x, channel]
print(f'b_val({x}, {y}) = {b_val}')
