# -*- coding: utf-8 -*-

import cv2
print(cv2.__version__)

cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)
# video_src = 'dataset/video1.avi'

import glob
video_list = glob.glob("second_dataset/*.avi")

count_car = 0


def mark_cars(cars,img):
    for (x,y,w,h) in cars:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


def show_result(img):
    cv2.imshow('video', img)


def congested(count_car):
    if count_car<2:
        return "Low"
    elif count_car<5:
        return "Medium"
    else:
        return "High"


def detect(video_src):

    cap = cv2.VideoCapture(video_src)
    

    while True:
        ret, img = cap.read()
        if (type(img) == type(None)):
            break
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        mark_cars(cars,img)

        count_car = len(cars)
        print congested(count_car)

        show_result(img)
        
        
        if cv2.waitKey(33) == 27:
            break
    cv2.destroyAllWindows()




for my_video_src in video_list:
    
    detect(my_video_src)


