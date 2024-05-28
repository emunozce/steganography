"""
    This module contains functions for processing images.
    It can be used to check if an image contains hidden data
    and remove it if necessary.

    Uses the technique of least significant bit (LSB) steganography.
"""

from pathlib import Path
from PIL import Image
import numpy as np


def has_hidden_data(image_path: Path) -> bool:
    """
    The function `has_hidden_data` checks if an image contains hidden data by analyzing the least
    significant bit of each color channel.

    :param image_path: The `image_path` parameter is a string that represents
    the file path to an image
    file that you want to check for hidden data. This function `has_hidden_data` uses
    the least
    significant bit (LSB) method to determine if there is hidden data in the image.
    It calculates the number of :return:
    The function `has_hidden_data` returns a boolean value - `True` if the image has hidden
    data (LSB changes exceed the threshold), and `False` otherwise.
    """
    image = Image.open(image_path)
    pixels = np.array(image)

    # Check the LSB of each color channel
    lsb_changes = (pixels & 1).sum()
    total_bits = pixels.size * 8  # 8 bits per color channel

    threshold = total_bits * 0.01  # 1% change threshold
    if lsb_changes > threshold:
        return True
    return False


def clean_image(image_path: Path, output_path: Path) -> None:
    """
    The function `clean_image` takes an image file, removes the least significant bit of
    each color channel, and saves the modified image to a specified output path.

    :param image_path: The `image_path` parameter is the file path to the image
    that you want to clean.
    This function reads the image from this path and performs the cleaning operation on
    it :type image_path: Path
    :param output_path: The `output_path` parameter in the `clean_image` function
    is the file path where the cleaned image will be saved after processing.
    It specifies the location and filename of the cleaned image file that will be
    generated by the function:type output_path: Path
    """
    image = Image.open(image_path)
    pixels = np.array(image)

    # Zero out the LSB of each color channel
    clean_pixels = pixels & ~1

    clean_img = Image.fromarray(clean_pixels)
    clean_img.save(output_path)
