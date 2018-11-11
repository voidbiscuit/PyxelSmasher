from PIL import Image, ImageFilter
import numpy as np
import cv2
from matplotlib import pyplot as plt


def modify(image, choice=' ', params=0):
    params = params if isinstance(params, list) else str(params).split()  # Convert params into list if only 1
    if choice == ' ':
        return image

    elif choice == 'G':  # Gaussian Blur
        if len(params) < 1:  # If there's no params
            return image  # return
        if not str(params[0]).isdigit():  # If the params aren't decimal
            return image  # return
        if int(params[0]) < 1:  # If the blur is less than 1
            return image  # return
        image = image.filter(ImageFilter.GaussianBlur(int(params[0])))  # Return blurred image
        plt.subplot(111), plt.imshow(image, cmap='gray')
        plt.title('Result'), plt.xticks([]), plt.yticks([])

    elif choice == 'N':  # Enhancing Edges
        image = image.filter(ImageFilter.EDGE_ENHANCE)
        plt.subplot(111), plt.imshow(image, cmap='gray')
        plt.title('Result'), plt.xticks([]), plt.yticks([])

    elif choice == 'F':
        # Using
        # https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
        dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)

        magnitude_spectrum = 10 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
        plt.subplot(221), plt.imshow(image, cmap='gray')
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray')
        plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

        cols, rows = image.size
        hcols, hrows = round(cols / 2), round(rows / 2)
        xshift = int(params[0]) if len(params) > 0 else 120
        yshift = int(params[1]) if len(params) > 1 else 70

        # create a mask first, center square is 1, remaining all zeros
        mask = np.zeros((rows, cols, 2), np.uint8)
        mask[hrows - yshift:hrows + yshift, hcols - xshift:hcols + xshift] = 1

        # for j in range(0, cols):
        #    for i in range(0, rows):
        #        mask[i, j] = mask[i, j] if 50 < magnitude_spectrum[i, j] < 160 else 0
        # apply mask and inverse DFT
        fshift = dft_shift * mask
        f_ishift = np.fft.ifftshift(fshift)
        img_back = cv2.idft(f_ishift)
        img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

        plt.subplot(223), plt.imshow(mask[:, :, 0], cmap='gray')
        plt.title('Mask'), plt.xticks([]), plt.yticks([])
        plt.subplot(224), plt.imshow(img_back, cmap='gray')
        plt.title('Result'), plt.xticks([]), plt.yticks([])

        formatted = (img_back * 255 / np.max(img_back)).astype('uint8')
        image = Image.fromarray(formatted)
    plt.show()
    return image  # If invalid option, return
