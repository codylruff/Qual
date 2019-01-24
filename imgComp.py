from PIL import Image

def compressImage(path, reduce_by):

    image = Image.open(path)
    size = image.size

    size(0) = size(0) * reduce_by
    size(1) = size(1) * reduce_by

    image = image.resize(size,Image.ANTIALIAS)
    image.save(path,optimize=True, quality=95)
