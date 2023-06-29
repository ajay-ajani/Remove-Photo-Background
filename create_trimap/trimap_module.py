import cv2, os, sys
import numpy as np

def trimap(image, name, size, number, erosion=False):
    """
    This function creates a trimap based on simple dilation algorithm

    Args:
        arg1: binary image
        arg2: name in string
        arg3: unknown region pixel
        arg4: number in string (for naming purpose)
        arg5: erosion value in pixel (default is False)

    Returns:
        trimap

    Raises:
        non-binary image, complete foreground erosion
    """

    pixels    = 2*size + 1;                        ## Double and plus 1 to have an odd-sized kernel            
    kernel    = np.ones((pixels,pixels),np.uint8)  ## How many pixel of extension do I get

    if erosion is not False:
        erosion = int(erosion)                                    
        erosion_kernel = np.ones((3,3), np.uint8)                     ## Design an odd-sized erosion kernel
        image = cv2.erode(image, erosion_kernel, iterations=erosion)  ## How many erosion do you expect
        image = np.where(image > 0, 255, image)                       ## Any gray-clored pixel becomes white (smoothing)
        # Error-handler to prevent entire foreground annihilation
        if cv2.countNonZero(image) == 0:
            print("ERROR: foreground has been entirely eroded");
            sys.exit();

    dilation  = cv2.dilate(image, kernel, iterations = 1)

    dilation  = np.where(dilation == 255, 127, dilation) 	## WHITE to GRAY
    remake    = np.where(dilation != 127, 0, dilation)		## Smoothing
    remake    = np.where(image > 127, 200, dilation)		## mark the tumor inside GRAY

    remake    = np.where(remake < 127, 0, remake)		## Embelishment
    remake    = np.where(remake > 200, 0, remake)		## Embelishment
    remake    = np.where(remake == 200, 255, remake)		## GRAY to WHITE

    path = "./images/results/"                                  ## Change the directory
    new_name = '{}px_'.format(size) + name + '_{}.png'.format(number);
    cv2.imwrite(os.path.join(path , new_name) , remake)


if __name__ == '__main__':
    name  = "trimap.png"; 
    image = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    size = 10;         
    number = name[-5];
    title = "test_image"

    trimap(image, title, size, number, erosion=10);
    print("Here")

