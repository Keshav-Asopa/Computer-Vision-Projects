import cv2

def img2sketch(photo, k_size):
    #Read Image
    img=cv2.imread(photo)
    
    # Convert to Grey Image
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img=cv2.bitwise_not(grey_img)
    #invert_img=255-grey_img

    # Blur image
    blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

    # Invert Blurred Image
    invblur_img=cv2.bitwise_not(blur_img)
    #invblur_img=255-blur_img

    # Sketch Image
    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

    #Edge 
    edges = cv2.Canny(grey_img, 30, 100)

    # Save Sketch 
    cv2.imwrite('sketch.png', sketch_img)
    cv2.imwrite('edge.png', edges)

    # Display sketch
    #cv2.imshow('sketch image',sketch_img)
    #cv2.waitKey(0)
    #v2.destroyAllWindows()
    
#Function call
img2sketch(photo='test.jpg', k_size=7)