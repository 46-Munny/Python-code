import cv2  
img = cv2.imread(r'E:\\Education\\4-2 all\\4-2 all\\ML Lab\\ML tuto\\OPENCV\\img.jpg')  
edges = cv2.Canny(img, 100, 200)  
  
cv2.imshow("Edge Detected Image", edges)  
cv2.imshow("Original Image", img)  
cv2.waitKey(0)  # waits until a key is pressed  
cv2.destroyAllWindows()  # destroys the window showing image
