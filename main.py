# Imports
from PIL import Image, ImageShow
import picturefunctions as pf

# File Open
filename = 'pictures/PandaNoise.bmp'
print("Opening ", filename, "...")
original = Image.open(filename)

# Fill Data
transformations = [original]

# Transform
while (True):
    image = transformations[-1]
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
    if len(choice) < 1:
        print("\nInvalid")
    # If numerical open picture
    elif choice.isdecimal():
        choice = int(choice)
        if 0 < choice <= len(transformations):
            ImageShow.show(transformations[choice - 1])
    # Else, get first char of input converted to upper, and use as case in switch.
    else:
        choice = choice[0]

        if choice == 'G':
            blurby = int(input("\nGaussian Blur by how much? : "))
            transformations.append(pf.modify(image=image, choice='G', params=blurby))
        elif choice == 'N':
            transformations.append(pf.modify(image=image, choice='N'))
        elif choice == 'B':
            if 1 < len(transformations):
                transformations.pop()

        elif choice == 'S':
            scriptfile = 'scripts/' + input("\nEnter filename <filename>.sc : ") + ".sc"
            try:
                file = open(scriptfile, 'r')
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
