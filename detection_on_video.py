# importing the necessary libraries
import numpy as np
import cv2 as cv
import sys
from py_func.funct import ulcerDetection, drawContour

videoPath="dataset/videos/Endoscopy_"+str(sys.argv[1])+".mp4"
cap = cv.VideoCapture(videoPath)
 
# Loop until the end of the video
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, image = cap.read()
    image =cv.cvtColor(image, cv.COLOR_BGR2RGB)
    image = cv.resize(image, (250, 222), fx = 0, fy = 0,
                         interpolation = cv.INTER_CUBIC)
    
    main=drawContour(ulcerDetection(image), image)
   
    # Display the resulting frame
    cv.imshow('Video', main)
    # define q as the exit button
    
    if cv.waitKey(30) & 0xFF == ord('q'):
        break
 
# release the video capture object
cap.release()
# Closes all the windows currently opened.
cv.destroyAllWindows()
