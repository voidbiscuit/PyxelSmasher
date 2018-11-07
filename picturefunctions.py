from PIL import Image, ImageFilter


def modify(image=Image.NONE, choice=' ', params=[]):
    params = params if isinstance(params, list) else [params]
    if image == Image.NONE or choice == ' ': return image
    
    # Gaussian Blur
    
    if choice == 'G':
        if len(params) < 1: return image
        if not str(params[0]).isdigit(): return image
        # print("Performing Gaussian " + str(params[0]))
        return image.filter(ImageFilter.GaussianBlur(int(params[0])))
    
    
    # Image Enhance
    
    if choice == 'N':
        # print("Enhancing Edges")
        return image.filter(ImageFilter.EDGE_ENHANCE)
    
    
    # Fourier Transform
    
    
    
    
    
    # Return image anyway, in case none of the characters were recognised
    return image
