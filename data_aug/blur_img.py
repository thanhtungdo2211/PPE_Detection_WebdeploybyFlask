import os
import cv2

def blur_image(image_folder):
    """Apply blur effect to images in a folder."""
    # Get list of image files in the folder
    image_files = os.listdir(image_folder)
    
    for image_file in image_files:
        # Full path to the image file
        image_path = os.path.join(image_folder, image_file)
        
        # Read the image using OpenCV
        image = cv2.imread(image_path)
        
        # Apply blur effect to the image
        blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
        
        # Save the blurred image with the same filename
        blurred_image_path = os.path.join(image_folder, "blurred_" + image_file)
        cv2.imwrite(blurred_image_path, blurred_image)

# Call the function to apply blur effect to images in a folder
blur_image('path/to/image/folder')
