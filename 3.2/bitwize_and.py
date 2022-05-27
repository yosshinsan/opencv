import numpy as np
import cv2

src1 = cv2.imread('./yorkie.png', cv2.IMREAD_COLOR)

print("shape")
print(src1.shape)
print("shape2")
print(src1.shape[:3])

height, width, channels = src1.shape[:3]
src2 = np.zeros((height, width, channels), np.uint8)
cv2.rectangle(src2, (150, 135), (290, 315), (255, 255, 255), thickness=-1)

dst = cv2.bitwise_and(src1, src2)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()