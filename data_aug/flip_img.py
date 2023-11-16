import cv2
import os

def flip_image_and_annotation(image_folder, annotation_folder):
    """Flip images and their corresponding annotations horizontally."""
    # Get list of image files in the folder
    image_files = os.listdir(image_folder)
    
    for image_file in image_files:
        # Full path to the image file
        image_path = os.path.join(image_folder, image_file)
        
        # Read the image using OpenCV
        image = cv2.imread(image_path)
        
        # Flip the image horizontally
        flipped_image = cv2.flip(image, 1)
        
        # Save the flipped image with the same filename
        flipped_image_path = os.path.join(image_folder, "flipped_" + image_file)
        cv2.imwrite(flipped_image_path, flipped_image)
        
        # Full path to the annotation file of the image
        annotation_file = image_file.split('.')[0] + '.txt'
        annotation_path = os.path.join(annotation_folder, annotation_file)
        
        if os.path.exists(annotation_path):
            # Read annotation data from the file
            with open(annotation_path, 'r') as f:
                annotations = f.readlines()
            
            # Flip the bounding box coordinates in the annotation
            flipped_annotations = []
            for annotation in annotations:
                parts = annotation.split()
                flipped_x = 1.0 - float(parts[1])  # Flip x-coordinate
                flipped_annotation = ' '.join([parts[0], str(flipped_x)] + parts[2:])
                flipped_annotations.append(flipped_annotation)
            
            # Save the updated annotation data
            flipped_annotation_path = os.path.join(annotation_folder, "flipped_" + annotation_file)
            with open(flipped_annotation_path, 'w') as f:
                f.write('\n'.join(flipped_annotations))
        else:
            print(f"No annotation file found for image {image_file}.")

# Call the function to flip images and update annotations in a folder
flip_image_and_annotation('path/to/image/folder', 'path/to/annotation/folder')
