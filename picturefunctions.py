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
        if not str(params[0]).isdecimal():  # If the params aren't decimal
            return image  # return
        if float(params[0]) < 1:  # If the blur is less than 1
            return image  # return
        image = image.filter(ImageFilter.GaussianBlur(float(params[0])))  # Return blurred image
        plt.subplot(111), plt.imshow(image, cmap='gray')
        plt.title('Result'), plt.xticks([]), plt.yticks([])
        plt.show()

    elif choice == 'N':  # Enhancing Edges
        image = image.filter(ImageFilter.EDGE_ENHANCE)
        plt.subplot(111), plt.imshow(image, cmap='gray')
        plt.title('Result'), plt.xticks([]), plt.yticks([])
        plt.show()

    elif choice == 'F':
        # Using
        # https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html
        # Discrete Fourier Transform and Calculate Shift
        dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        # Magnitude of shift is exponential, apply log and multiply to get values ~ 0-150
        magnitude_spectrum = np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
        # Draw

        # X and Y (columns and rows) then divided by 2 as the rectangle is from the center
        cols, rows = image.size
        hcols, hrows = round(cols / 2), round(rows / 2)
        percy, percx = hrows / 100, hcols / 100
        # Shifts are based on params, if none, default values
        if len(params) == 2:
            xshift = round(int(params[0]) * percx)
            yshift = round(int(params[1]) * percy)
        elif len(params) == 1:
            xshift = round(int(params[0]) * percx)
            yshift = round(int(params[0]) * percy)
        else:
            xshift = round(hcols)
            yshift = round(hrows)
        # 2d array of 0s created, then replace a smaller rectangle with 1s as mask
        mask = np.zeros((rows, cols, 2), np.uint8)
        mask[hrows - yshift:hrows + yshift, hcols - xshift:hcols + xshift] = [1, 1]
        magnitude_spectrum[:] *= (mask[:, :, 0] + 1) / 2
        # Some weird code to filter some magnitude spectrum stuff.
        # Multiply shift with mask for masked shift, and inverse the shift
        fshift = dft_shift * mask
        f_ishift = np.fft.ifftshift(fshift)
        # Inverse discrete fourier transform on image, then format change to get image
        img_back = cv2.idft(f_ishift)
        img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
        # Convert picture back to BMP
        formatted = (img_back * 255 / np.max(img_back)).astype('uint8')
        img_back = Image.fromarray(formatted)

        plt.subplot(221), plt.imshow(image, cmap='gray')
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray')
        plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
        plt.subplot(223), plt.imshow(mask[:, :, 0], cmap='gray')
        plt.title('Mask'), plt.xticks([]), plt.yticks([])
        plt.subplot(224), plt.imshow(img_back, cmap='gray')
        plt.title("Result [" + str(xshift) + " " + str(yshift) + "]"), plt.xticks([]), plt.yticks([])
        plt.show()
        image = img_back

    return image  # If invalid option, return
