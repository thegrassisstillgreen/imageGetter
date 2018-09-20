import os
import urllib.request

class urlToImage:

    def __init__(self, url_list, file_path, filename):
        self.url_list = url_list
        self.file_path = file_path
        self.filename = filename

    def createFolder(self):
        try:
            directory = self.file_path + "\\" + self.filename
            print("Trying to create the following directory: {directory}".format(directory=directory))
            if not os.path.exists(directory):
                os.makedirs(directory)
                print("Created the directory.")
                self.file_path = directory
                
        except OSError as err:
            print("Error: Cannot create the following directory: {directory}".format(directory=directory))

    def saveImgUrlToFile(self):
        for index, url in enumerate(self.url_list):
            address, file_extension = os.path.splitext(url)
            img_filename = self.filename + str(index) + file_extension
            print("Image Filename: {filename}".format(filename=img_filename))
            path_to_file = self.file_path + "\\" + img_filename
            urllib.request.urlretrieve(url, path_to_file)
            print("{img_filename} saved to {directory}".format(img_filename=img_filename, directory=self.file_path))
