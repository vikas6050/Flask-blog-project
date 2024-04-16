#users/picture_handler.py

import os
from PIL import Image
# Import necessary modules from flask
from flask import url_for, current_app 

# Function to add a profile picture
def add_profile_pic(pic_upload,username):
    # Get the filename of the uploaded picture
    filename = pic_upload.filename
    # Get the extension type of the file
    ext_type = filename.split('.')[-1]
    # Create a new filename for storage using the username and original extension
    storage_filename = str(username) + '.' + ext_type
    
    # Define the filepath where the picture will be stored
    # It's in a folder named 'profile_pics' within the 'static' folder of the application
    filepath = os.path.join(current_app.root_path,'static/profile_pics',storage_filename)
    
    # Define the output size for the picture
    output_size = (200,200)
    
    # Open the picture and resize it
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    # Save the resized picture to the defined filepath
    pic.save(filepath)
    
    # Return the filename of the stored picture
    return storage_filename