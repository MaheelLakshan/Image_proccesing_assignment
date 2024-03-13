import cv2
import numpy as np

def reduce_intensity_levels(image_path, levels):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    levels = 2 ** int(levels)

    normalized_img = (img // levels) * levels
    cv2.imshow("Reduced Intensity Levels", normalized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

reduce_intensity_levels("input_image.jpg", 4) 
