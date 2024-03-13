import cv2
import numpy as np

def spatial_average(image_path, kernel_size):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    averaged_img = cv2.blur(img, (kernel_size, kernel_size))

    cv2.imshow(f"Spatial Average {kernel_size}x{kernel_size}", averaged_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

spatial_average("input_image.jpg", 3)
spatial_average("input_image.jpg", 10)
spatial_average("input_image.jpg", 20)
