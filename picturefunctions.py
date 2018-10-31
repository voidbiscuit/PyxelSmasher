from PIL import Image, ImageFilter


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

    return image  # If invalid option, return
