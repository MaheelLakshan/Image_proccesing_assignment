# ---------------------------------------------------------
#   Name : LAKSHAN R.A.M.
#   Reg No: EG/2019/362
#   Take Home Assignment 1
#   Question 1
# ---------------------------------------------------------


# import required libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# The function to reduce the intensity levels of the original image
def adjust_intensity_levels(img_path, levels):
    # Open the image
    img = Image.open(img_path)
    # convert image to grayscale
    img = img.convert('L')

    # Create a figure to hold the subplots
    fig = plt.figure(figsize=(15, 10))

    for i, level in enumerate(levels):
        img_array = np.array(img)

        # Reduce the intensity levels
        reduction_factor = 256 // level
        reduced_img_array = (img_array // reduction_factor) * reduction_factor

        # Convert the array back to an image
        reduced_img = Image.fromarray(reduced_img_array.astype('uint8'))

        # Create a new subplot for this image
        fig.add_subplot(2, len(levels)//2, i+1)
        plt.axis('off')
        plt.title(f'Intensity Levels: {level}')
        plt.imshow(reduced_img, cmap='gray')

        # Save the image
        reduced_img.save(f'images/output/question_1/reduced_intensity_level_{level}.jpg')

    # Display all the subplots
    plt.tight_layout()
    plt.show()
    return


# Define the image path and the intensity levels to reduce to
image_path = 'images/input/question_1/happy smiling dog.jpg'
Varies_Level_intensities = [256, 128, 64, 32, 16, 8, 4, 2]


# Calling the function to reduce the intensity levels
adjust_intensity_levels(image_path, Varies_Level_intensities)