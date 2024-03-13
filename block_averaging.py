import cv2
import numpy as np

def block_average(image_path, block_size):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape

    for i in range(0, h, block_size):
        for j in range(0, w, block_size):
            block = img[i:i+block_size, j:j+block_size]
            avg_value = np.mean(block)
            img[i:i+block_size, j:j+block_size] = avg_value

    cv2.imshow(f"Block Averaging {block_size}x{block_size}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

block_average("input_image.jpg", 3)
block_average("input_image.jpg", 5)
block_average("input_image.jpg", 7)
