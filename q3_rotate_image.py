# ---------------------------------------------------------
#   Name : LAKSHAN R.A.M.
#   Reg No: EG/2019/362
#   Take Home Assignment 1
#   Question 3
# ---------------------------------------------------------

# import required libraries
from PIL import Image


# Create a function to rotate an image 
def rotate_image(img_path, angles):
    # Open the image
    img = Image.open(img_path)

    # Iterate over the angles
    for angle in angles:
        # Rotate the image by the given angle
        rotated_img = img.rotate(angle, resample=Image.BICUBIC, expand=True)

        # Display the image
        rotated_img.show()

        # Save the image
        rotated_img.save(f'images/output/question_3/rotated_image_{angle}.jpg')
    return


# Define the image path and angles to rotate by
image_path = 'images/input/question_3/happy smiling dog.jpg'
rotate_angles = [45, 90]
# Calling the function
rotate_image(image_path, rotate_angles)