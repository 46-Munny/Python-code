import cv2

im = cv2.imread(r'E:\\Education\\4-2 all\\4-2 all\\ML Lab\\ML tuto\\OPENCV\\img.jpg')  
cv2.imshow('Original Image',im)  
cv2.imshow('Blurred Image', cv2.blur(im, (3,3)))  
cv2.waitKey(0)  
cv2.destroyAllWindows()  
