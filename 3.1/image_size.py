import cv2

img = cv2.imread('./yorkie.png', cv2.IMREAD_COLOR)

if len(img.shape) == 3:
    height, width, channels = img.shape[:3]
else:
    height, width = img.shape[:2]
    channels = 1

print(height, width, channels)
