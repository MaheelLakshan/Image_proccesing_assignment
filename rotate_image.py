import cv2
import numpy as np

def rotate_image(image_path, angle):
    img = cv2.imread(image_path)

    rows, cols, _ = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated_img = cv2.warpAffine(img, M, (cols, rows))

    cv2.imshow(f"Rotated {angle} degrees", rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

rotate_image("input_image.jpg", 45)
rotate_image("input_image.jpg", 90)
