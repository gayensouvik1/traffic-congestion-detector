# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV 
import cv2
 
# capture frames from a video
cap = cv2.VideoCapture('dataset/video1.avi')
 
# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')

def rotate(image,angle):
    (h, w) = image.shape[:2]
    center = (w / 2, h)
     
    # rotate the image by 180 degrees
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated




def count_cars(image,ind):
    # convert to gray scale of each frames
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
     
    # To draw a rectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.namedWindow("Channels"+str(ind))
    cv2.imshow('Channels'+str(ind), image)
    return len(cars)





 
# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
    north_up = rotate(frames,12)
    north_down = north_up[20:330, 0:150]
    north_up = north_up[20:300, 150:300]
    south_up =frames[300:550,0:300]
     
    cnt1 = count_cars(north_down,1)
    cnt2 = count_cars(north_up,2)
    cnt3 = count_cars(south_up,3)
    
    print (cnt1,cnt2,cnt3)
     
    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()
