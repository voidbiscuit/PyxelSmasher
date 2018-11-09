from PIL import Image, ImageFilter
import numpy as np
import cv2
from matplotlib import pyplot as plt


def modify(image=Image.NONE, choice=' ', params=0):
    params = params if isinstance(params, list) else [params]  # Convert params into list if only 1
    if image == Image.NONE or choice == ' ':  # If no image or no operation
        return image  # return nothing

    elif choice == 'G':  # Gaussian Blur
        if len(params) < 1:  # If there's no params
            return image  # return
        if not str(params[0]).isdigit():  # If the params aren't decimal
            return image  # return
        if int(params[0]) < 1:  # If the blur is less than 1
            return image  # return
        return image.filter(ImageFilter.GaussianBlur(int(params[0])))  # Return blurred image

    elif choice == 'N':  # Enhancing Edges
        return image.filter(ImageFilter.EDGE_ENHANCE)

    elif choice == 'F':  # Fourier Transform
        dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
        plt.subplot(121), plt.imshow(image, cmap='gray')
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
        plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
        plt.show()

        cols, rows = image.size
        crow, ccol = round(rows / 2), round(cols / 2)

        # create a mask first, center square is 1, remaining all zeros
        mask = np.zeros((rows, cols, 2), np.uint8)
        mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1

        # apply mask and inverse DFT
        fshift = dft_shift * mask
        f_ishift = np.fft.ifftshift(fshift)
        img_back = cv2.idft(f_ishift)
        img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

        plt.subplot(121), plt.imshow(image, cmap='gray')
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img_back, cmap='gray')
        plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
        plt.show()
        image = img_back

    return image  # If invalid option, return
