import cv2

img = cv2.imread('./yorkie.png', cv2.IMREAD_GRAYSCALE)

print(f'shape = {img.shape}')
print(f'shape = {img.dtype}')