import rasterio
from PIL import Image
import io


def load_image():
    """
    load .tiff image from folder images
    :return:DatasetReader object
    """
    image = rasterio.open("images/S2L2A_2022-06-09.tiff")
    return image


def process_atributtes():
    """
    collect the data from  DatasetReader atributtes
    :return: dictionary
    """
    image = load_image()
    print(image)
    image_info = {'image_size': {
        "width": image.width,
        "height": image.height

    }, "bands": image.count, "CRS": str(image.crs),
        "bounding_box": {
            "left": image.bounds[0],
            "bottom": image.bounds[1],
            "right": image.bounds[2],
            "top": image.bounds[3]
        }
    }
    return image_info


def process_thumbnail():
    """
    Transforms th DatasetReader object into png byte image
    :return: bytes
    """
    image = load_image()
    im = Image.fromarray(image.read(1))
    im_resize = im.resize((500, 500))
    buf = io.BytesIO()
    im_resize.save(buf, format='PNG')
    byte_img = buf.getvalue()

    return byte_img
