import os
import urllib.request

class urlToImage:

    def __init__(self, url_list, file_path, filename):
        self.url_list = url_list
        self.file_path = file_path
        self.filename = filename

    def createFolder(self):
        try:
            # The directory of the folder will be the path appended by the filename given by the user
            directory = self.file_path + "\\" + self.filename
            
            print("Trying to create the following directory: {directory}".format(directory=directory))
            
            # Create the folder as long as it doesn't already exist in the specified location
            if not os.path.exists(directory):
                os.makedirs(directory)
                
                print("Created the directory.")
                
                # Change the path to include the newly created directory
                self.file_path = directory
                
        except OSError as err:
            print("Error: Cannot create the following directory: {directory}".format(directory=directory))

    def saveImgUrlToFile(self):
        for index, url in enumerate(self.url_list):
            
            # Separate the file extension from the address name
            address, file_extension = os.path.splitext(url)
            # Generate a filename for the image using the specified filename, with index and file extension appended
            img_filename = self.filename + str(index) + file_extension
            
            print("Image Filename: {filename}".format(filename=img_filename))
            
            # Create the path to be used by the urlretrieve method, including the path and filename declared above
            path_to_file = self.file_path + "\\" + img_filename
            # Retrieve the image from the url and save it to the path as declared above
            urllib.request.urlretrieve(url, path_to_file)
            
            print("{img_filename} saved to {directory}".format(img_filename=img_filename, directory=self.file_path))
