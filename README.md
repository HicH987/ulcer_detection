# Ulcer detection
## Description
ulcer detection in endoscopy videos using color segmentation with HSV
using python's librarys:
-   **numpy**
-   **openCV**
-   **matplotlib**: to disply figures in nooebook
-   **scipy.ndimage**: for 3D median
-   **skimage.color**: for rgb2hsv
-   **skimage.morphology**: for disk structured element

## Features
### Ulcer image
![md_1](https://user-images.githubusercontent.com/62667537/152111578-fc7bc70f-0179-4572-89c1-2ca7bf37c956.png)

<h3>Top-Hat filtre</h3>
<p>The top-hat filter is used to enhance bright objects of interest in a dark background</p>
![md_2](https://user-images.githubusercontent.com/62667537/152111793-ea7797df-f91b-4400-8bad-87d8fd2710f1.png)

<h3>Bottom(black)-Hat filtre</h3>
<p>Bottom-Hat filter is used to do the opposite of top-hat, enhance dark objects of interest in a bright background</p>

![md_3](https://user-images.githubusercontent.com/62667537/152111858-53217e7c-8567-4b65-84c1-cfeb35d1ba46.png)


<h3>Combine top-bottom with image</h3>
<p>
    It is possible to add the bright areas to the image and subtract the dark areas from it. <br>As a result, there will be an enhancement in the contrast between bright and dark areas: <br>
    <strong>  I(contrast enhanced) = I + topHat(I) - bottomHat(I) </strong> 
</p>

![md_4](https://user-images.githubusercontent.com/62667537/152111862-5d54d5fa-0281-4dad-9b35-be7a667ac808.png)

<h3>Applicated Median filter</h3>
<p>
    3D median filter is applied to remove the salt and pepper noise, and improve the image from extra noise
</p>

![md_5](https://user-images.githubusercontent.com/62667537/152111865-568d797d-0511-4b24-8115-3098c0095af5.png)

<h3>Applicated HSV filter</h3>
<p>
    In the RGB representation the hue and the luminosity are expressed as a linear combination of the R,G,B channels, whereas they correspond to single channels of the HSV image (the Hue and the Value channels). A simple segmentation of the image can then be effectively performed by a mere thresholding of the HSV channels.
</p>

![md_6](https://user-images.githubusercontent.com/62667537/152111868-6295bc61-06a0-41cd-9b78-af1d0c550383.png)

<h3>Set a threshold on the Hue channel</h3>
<p>notice that we first defined a lower and upper mask for the intended object. The value of the mask is derived from the color bar value at the side of the Hue Graph. Notice that the <strong>ulcer</strong> has a hue that is really different from the background.</p>

![md_7](https://user-images.githubusercontent.com/62667537/152111870-1d6be6dc-5cf8-454e-91cb-51450d5b831e.png)

<h3>Segment RGB to Gray</h3>
<p>Convert the segment to grayscale to apply morphological filters to it</p>

![md_8](https://user-images.githubusercontent.com/62667537/152111872-b16345f1-1b2d-4f84-add4-51e21fbd9cc2.png)

<h3>Apply Morphological filters</h3>
<p>enhance segment with morphologic filters</p>

![md_9](https://user-images.githubusercontent.com/62667537/152111873-f0aa1066-904a-4369-baef-2bbbd1a09830.png)

<h3>Overlay segmented image on top of main image</h3>
<p>Display the contour of the detected segment (ulcer) by superimposing the original image with segment after morphological enhancement</p>

![md_10](https://user-images.githubusercontent.com/62667537/152111875-4140b37d-9145-4378-b587-49d865893b40.png)


## Deployment
-   all videos are in [ulcer_detection/tree/main/dataset/videos]
-   each video has the name "Endpscopy_<number of the video>.mp4"
-   <number of the video> ∈ [0,4]

To launch the detection on a video, open your favorite Terminal and run this commands:
```sh
python detection_on_video.py <number of the video>
```

