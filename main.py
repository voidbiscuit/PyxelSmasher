# Imports
from PIL import Image, ImageFilter, ImageShow

# File Open
filename = 'pictures/PandaNoise.bmp'
print("Opening ", filename, "...")
original = Image.open(filename)

# Fill Data
transformations = []
transformations.append(original)

# Transform
while (True):
    # Menu
    print(str.format(
        "\n\n\n\n\n\n\n\n\n\n"
        "\n  - - - - Menu"
        "\n"
        "\nG | Gaussian Blur"
        "\nN | Remove Noise"
        "\nB | Back"
        "\nS | Run Script"
        "\nNumerical Value to Open Picture Specified [{0}]"
        "\n",
        len(transformations)
    ))
    choice = input("\nCommand : ").upper()

    # If numerical open picture
    if choice.isdecimal():
        choice = int(choice)
        if 0 < choice <= len(transformations):
            ImageShow.show(transformations[choice - 1])
        # Else, get first char of input converted to upper, and use as case in switch.
    else:
        choice = choice[0]
        if choice == 'G':
            blurby = int(input("\nGaussian Blur by how much? : "))
            transformations.append(transformations[-1].filter(ImageFilter.GaussianBlur(blurby)))
        elif choice == 'N':
            transformations.append(transformations[-1].filter(ImageFilter.EDGE_ENHANCE))
        elif choice == 'B':
            if 1 < len(transformations):
                transformations.pop()
        elif choice == 'S':
            scriptfile = 'scripts/', input("\nEnter File Name : ")
