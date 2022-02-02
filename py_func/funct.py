import numpy as np
import cv2 as cv
import scipy.ndimage #for 3D median
from skimage import color #for rgb2lab and rgb2hsv
from skimage.morphology import disk #for disk structured element


def ulcerDetection(image):
    # beta :: stretching parameter
    beta=12

    #StructuringElement : disk Forme - because it's more commonly used for medical images
    kernel = disk(beta)

    # Applying the Top-Hat operation
    topHat_img = cv.morphologyEx(image,cv.MORPH_TOPHAT,kernel)
    bottomHat_img = cv.morphologyEx(image, cv.MORPH_BLACKHAT,kernel)
    topBottom_img=cv.subtract(cv.add(topHat_img,image), bottomHat_img)
    alpha = (3, 3, 3)
    median_topBottom_img= scipy.ndimage.median_filter(topBottom_img, alpha)
    sample=median_topBottom_img
    sample_h= color.rgb2hsv(sample)
    lower_mask = sample_h[:,:,0] > 0.11
    upper_mask = sample_h[:,:,0] < 0.3
    mask = upper_mask*lower_mask

    # get the desired mask and show in original image
    red = sample[:,:,0]*mask
    green = sample[:,:,1]*mask
    blue = sample[:,:,2]*mask
    mask2 = np.dstack((red,green,blue))
    img_ulcer=cv.cvtColor(mask2, cv.COLOR_RGB2GRAY)
    ret, thresh = cv.threshold(mask2,np.mean(median_topBottom_img),255,cv.THRESH_BINARY)

    kernel = disk(3)
    thresh = cv.erode(cv.dilate(thresh,kernel,iterations=2),kernel,iterations=7)

    segmentation=cv.dilate(thresh,kernel,iterations=7)

    return segmentation



def drawContour(segmentation, image):
    seg  = cv.cvtColor(segmentation, cv.COLOR_RGB2GRAY)
    main = image.copy()

    # Dictionary giving RGB colour for label (segment label) - label 1 in red, label 2 in yellow
    RGBforLabel = { 1:(0,0,255), 2:(1,255,255) }

    # Find external contours
    contours,_ = cv.findContours(seg,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

    # Iterate over all contours
    for i,c in enumerate(contours):
        # Find mean colour inside this contour by doing a masked mean
        mask = np.zeros(seg.shape, np.uint8)
        cv.drawContours(mask,[c],-1,255, -1)
        # DEBUG: cv.imwrite(f"mask-{i}.png",mask)
        mean,_,_,_ = cv.mean(seg, mask=mask)
        # DEBUG: print(f"i: {i}, mean: {mean}")

        # Get appropriate colour for this label
        label = 2 if mean > 1.0 else 1
        colour = RGBforLabel.get(label)
        # DEBUG: print(f"Colour: {colour}")

        # Outline contour in that colour on main image, line thickness=1
        cv.drawContours(main,[c],-1,colour,5)

    return cv.cvtColor(main, cv.COLOR_BGR2RGB)