import cv2
import numpy as np

choice=input("want to remove image background or want to circle it? press 1 or 2: ")
if choice==1:
    # Load image
    image = cv2.imread('cross.png')
    print("image background removed successfuly")

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a mask
    ret, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # Apply morphological transformations to remove small noise
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel, iterations = 2)

    # Apply distance transform to create a distance map
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.1*dist_transform.max(),255,0)

    # Apply dilation to fill holes in the mask
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(opening,sure_fg)
    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers+1
    markers[unknown==255] = 0

    # Apply watershed algorithm to segment the image
    markers = cv2.watershed(image,markers)
    image[markers == -1] = [255,0,0]

    # Save output image
    cv2.imwrite('output.jpg', image)
    print("image background removed successfulyy")
else:
    # Load image
    img = cv2.imread('cross.png')

    # Get image dimensions
    height, width, channels = img.shape

    # Create a black image with a white circle in the center
    circle_img = np.zeros((height, width), dtype=np.uint8)
    cv2.circle(circle_img, (width // 2, height // 2), min(width // 2, height // 2), (255, 255, 255), -1)

    # Apply mask to the original image
    masked_img = cv2.bitwise_and(img, img, mask=circle_img)

    cv2.imwrite('output.jpg', masked_img)

    # Display the masked image
    cv2.imshow('Masked Image', masked_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("converted into circle")
