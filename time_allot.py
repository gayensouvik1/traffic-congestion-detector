
import cv2
import time
print(cv2.__version__)

cascade_src = 'cascade/cascade.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)


import glob
video_list = glob.glob("second_dataset/*.avi")

count_car = 0
res = 0


def mark_cars(cars,img):
    for (x,y,w,h) in cars:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


def show_result(num,img):
    cv2.imshow('video'+str(num), img)
    # global res
    # res = res+1
    # src = "result/"+str(res)+".jpg"
    # import scipy.misc
    # scipy.misc.imsave(src, img)

    # img.save("result/"+str(res)+".jpg")



def congested(count_car):
    if count_car<5:
        return "Low"
    elif count_car<10:
        return "Medium"
    else:
        return "High"

check_null = 0

def detection(num,cap):
    ret, img1 = cap.read()
    global check_null
    if (type(img1) == type(None)):
        check_null = 1
        return
    img = img1[0:450,130:450]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    mark_cars(cars,img)
    
    count_car = len(cars)
    cv2.putText(img,str(count_car)+"->"+congested(count_car), (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2)
    show_result(num,img)
    return count_car



from random import randint


def detect():

    global check_null
    cnt = 0
    video_src1 = "second_dataset/"+str(randint(1,253))+".avi"
    video_src2 = "second_dataset/"+str(randint(1,253))+".avi"
    video_src3 = "second_dataset/"+str(randint(1,253))+".avi"
    video_src4 = "second_dataset/"+str(randint(1,253))+".avi"

    cap1 = cv2.VideoCapture(video_src1)
    cap2 = cv2.VideoCapture(video_src2)
    cap3 = cv2.VideoCapture(video_src3)
    cap4 = cv2.VideoCapture(video_src4)
    

    while True:


        if check_null == 1:
            print "hello"
            check_null = 0
            break
        
        cnt1 = detection(1,cap1)
        
        if check_null == 1:
            check_null = 0
            break
        cnt2 = detection(2,cap2)
        if check_null == 1:
            check_null = 0
            break
        cnt3 = detection(3,cap3)
        if check_null == 1:
            check_null = 0
            break
        cnt4 = detection(4,cap4)
        
        if cv2.waitKey(33) == 27:
            break
        cnt= cnt+1
        print cnt


import random
random.shuffle(video_list)

while True:
    detect()


