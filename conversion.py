#images: jpg, jpeg, tif, tiff, png
#global varibles
images = ["jpg", "jpeg", "tif", "tiff", "png"]

def retrieve_compatable_conversions(file_type):
    if file_type in images:
        return images