import numpy as np
import cv2

src1 = cv2.imread('./aloeL.png', cv2.IMREAD_COLOR)
src2 = cv2.imread('./aloeR.png', cv2.IMREAD_COLOR)

alpha = 0.5
beta = 0.5
gamma = 0.0

dst = cv2.addWeighted(src1, alpha, src2, beta, gamma)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()