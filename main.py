# Imports
from PIL import Image, ImageShow
import picturefunctions as pf
from matplotlib import pyplot as plt

# File Open
filename = 'pictures/PandaNoise.bmp'
print("Opening ", filename, "...")
original = Image.open(filename)

# Fill Data
transformations = [original]

# Transform
while True:
    image = transformations[-1]
    # Menu
    print(str.format(
        "\n\n\n\n\n\n\n\n\n\n"
        "\n  - - - - Menu"
        "\n"
        "\nG | Gaussian Blur"
        "\nN | Remove Noise"
        "\nF | Fourier Transform"
        "\nB | Back"
        "\nS | Run Script"
        "\nNumerical Value to Open Picture Specified [{0}]"
        "\n",
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
            # ImageShow.show(transformations[choice - 1])
    # Else, get first char of input converted to upper, and use as case in switch.
    else:
        choice = choice[0]
        if choice == 'V':
            pf.modify()
        elif choice == 'G':
            blur_factor = int(input("\nGaussian Blur by how much? : "))
            transformations.append(pf.modify(image=image, choice='G', params=blur_factor))
        elif choice == 'N':
            transformations.append(pf.modify(image=image, choice='N'))
        elif choice == 'B':
            if 1 < len(transformations):
                transformations.pop()
        elif choice == 'F':
            transformations.append(pf.modify(image=image, choice='F'))

        elif choice == 'S':
            script_file = 'scripts/' + input("\nEnter filename <filename>.sc : ") + ".sc"
            try:
                file = open(script_file, 'r')
                script = file.readlines()
                file.close()
                for line in script:
                    instruction = line.replace('\n', '').split(' ')
                    if len(instruction) > 0:
                        # print(instruction)
                        image = pf.modify(
                            image=image,
                            choice=instruction[0],
                            params=0 if len(instruction) < 2 else instruction[1:]
                        )
                    transformations.append(image)
            except FileNotFoundError:
                print("File not found")
