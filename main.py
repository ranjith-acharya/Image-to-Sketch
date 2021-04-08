import cv2

img_location = 'img/'
filename = 'blackadam.png'

img = cv2.imread(img_location + filename)

# img -> pencil_sketch = gray -> inverted -> blur ->invert_blur -> divide(gray, invert_blur) = pencil_sketch

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert_gray = 255 - gray

blur = cv2.GaussianBlur(invert_gray, (21, 21), 0)
invert_blur = 255 - blur

pencil_sketch = cv2.divide(gray, invert_blur, scale=250.0)

cv2.imwrite('img/sketch/' + filename, pencil_sketch)

cv2.imshow('Original Image: ', img)
cv2.imshow('Pencil Sketch: ', pencil_sketch)
cv2.waitKey(0)