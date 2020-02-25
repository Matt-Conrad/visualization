import numpy as np
from PyQt5.QtGui import QPixmap, QImage

def np_arr_to_pixmap(image):
    # Scale the pixel intensity to uint8
    if image.dtype == 'bool':
        rescaled_image = (image.astype(np.uint8) * 255)
    elif image.dtype == 'float64':
        rescaled_image = (image * 255).astype(np.uint8)
    rescaled_image = np.ascontiguousarray(rescaled_image)
    # Create the QPixmap object
    height, width = rescaled_image.shape
    bytes_per_line = width
    q_image = QImage(rescaled_image, width, height, bytes_per_line, QImage.Format_Grayscale8)
    pixmap = QPixmap.fromImage(q_image)

    return pixmap

