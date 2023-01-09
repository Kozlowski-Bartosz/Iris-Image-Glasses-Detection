import cv2
import numpy as np

def reduce_noise(input_image):
    return cv2.GaussianBlur(input_image, (5,5), 0)

def mask_reflections(input_image, kernel_size=5, threshold=180):
    grayscale = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((kernel_size,kernel_size),np.uint8)    
    th, mask = cv2.threshold(grayscale, threshold, 255, cv2.THRESH_BINARY)
    #th, mask = cv2.threshold(grayscale, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)   #Reflections smaller than the kernel size are removed
    result = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    return result

def apply_mask(input_image, mask):
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    img = input_image.copy()
    #m = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img[mask == 255] = (0,0,255)
    
    return img

def count_reflections(im):
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    
def process_image(im, thresh):
    denoised_im = im.copy()
    denoised_im = reduce_noise(denoised_im)
    mask = mask_reflections(denoised_im, threshold=thresh)
    masked = apply_mask(im, mask)
    count_reflections(mask)
    hori = np.concatenate((im, mask, masked), axis=1)
    cv2.imshow("Image", hori)