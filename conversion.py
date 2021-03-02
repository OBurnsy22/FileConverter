#images: jpg, jpeg, tif, tiff, png
#global varibles
images = ["jpg", "jpeg", "tif", "tiff", "png"]

def retrieve_compatable_conversions_select(file_type):
    if file_type in images:
        return images

def open_dropped_file(self, event):
    #compatable_converstion = retrieve_compatable_conversions_select(event.data)
    breakpoint()