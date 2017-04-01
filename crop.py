import cv2
image = cv2.imread("lenna.jpg")
# crop_img = img[100:2400, 100:2300] # Crop from x, y, w, h -> 100, 200, 300, 400
# # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
# cv2.imshow("cropped", crop_img)
# cv2.waitKey(0)


# grab the dimensions of the image and calculate the center
# of the image
(h, w) = image.shape[:2]
center = (w / 2, h)
 
# rotate the image by 180 degrees
M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("rotated", rotated)
cv2.waitKey(0)