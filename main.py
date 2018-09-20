import urlToImage

def main():
    url_list = [YOUR_LIST_OF_URLS_GO_HERE]
    file_path = r'YOUR\DESIRED\FILE\PATH'
    filename = input("Filename: ")
                
    url_to_img_converter = urlToImage(url_list, file_path, filename)

    url_to_img_converter.createFolder()
    url_to_img_converter.saveImgUrlToFile()

if __name__ == "__main__":
    main()
