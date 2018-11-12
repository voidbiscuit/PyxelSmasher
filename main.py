# Imports
import numpy as np

from PIL import Image
import picturefunctions as pf
from matplotlib import pyplot as plt

plt.close()
# File Open
original = 'pictures/PandaOriginal.bmp'
noise = 'pictures/PandaNoise.bmp'
print("Opening ", noise, "...")
original = Image.open(original)
noise = Image.open(noise)

# Fill Data
transformations = [noise]

# Transform
while True:
    image = transformations[-1]
    # Menu
    print(str.format(
        "\n\n\n\n\n\n\n\n\n\n"
        "\n error = {0}"
        "\n"
        "\n  - - - - Menu"
        "\n"
        "\nG | Gaussian Blur"
        "\nN | Remove Noise"
        "\nF | Fourier Transform"
        "\nB | Back"
        "\nS | Run Script"
        "\nNumerical Value to Open Picture Specified [{1}]"
        "\n"
        "\n"
        "\n",
        str(np.sqrt(np.mean(np.square(
            np.array(original) - np.array(image)
        )))),
        len(transformations)
    ))
    choice = input("\nCommand : ").upper()
    if len(choice) < 1:
        print("\nInvalid")
    # If numerical open picture
    elif choice.isdecimal():
        choice = int(choice)
        if 0 < choice <= len(transformations):
            plt.subplot(111), plt.imshow(transformations[choice - 1], cmap='gray')
            plt.title("Image [" + str(choice) + "]"), plt.xticks([]), plt.yticks([])
            plt.show()
        elif 0 == choice:
            plt.subplot(111), plt.imshow(original, cmap='gray')
            plt.title("Image [Original]"), plt.xticks([]), plt.yticks([])
            plt.show()
    # Else, get first char of input converted to upper, and use as case in switch.
    else:
        params = str(choice).replace("\s+", " ").split(" ")
        choice = params[0]
        if len(params) > 0:
            params = params[1:]

        if choice == 'C':
            transformations = [transformations[0]]
            image= transformations[0]
        elif choice == 'B':
            if 1 < len(transformations):
                transformations.pop()
        elif choice == 'S':
            params = params[0]
            print(str(params))
            script_file = 'scripts/' + params + ".sc"
            print(script_file)
            try:
                file = open(script_file, 'r')
                script = file.readlines()
                file.close()
                for line in script:
                    line = line.upper()
                    params = line.replace('\n', '').replace("\s", " ").split(' ')
                    if len(line.strip("\n")) > 0:
                        choice = params[0]
                        if choice == 'B':
                            if 1 < len(transformations):
                                transformations.pop()
                        elif len(params) > 0:
                            params = params[1:]
                        print(str(choice) + " " + str(params))
                        image = pf.modify(
                            image=image,
                            choice=choice[0],
                            params=params
                        )
                        transformations.append(image)
            except FileNotFoundError:
                print("File not found")
        else:
            image = pf.modify(image=image, choice=choice, params=params)
            transformations.append(image)
    plt.subplot(111), plt.imshow(image, cmap='gray')
    plt.title("Image [" + str(len(transformations)) + "]"), plt.xticks([]), plt.yticks([])
    plt.show()
