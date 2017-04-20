
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


def show_result(img):
    cv2.imshow('video', img)
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


def detect(video_src):

    cap = cv2.VideoCapture(video_src)
    

    while True:
        ret, img1 = cap.read()
        if (type(img1) == type(None)):
            break
        img = img1[0:450,130:450]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        mark_cars(cars,img)
        
        count_car = len(cars)
        cv2.putText(img,str(count_car)+"->"+congested(count_car), (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2)
        show_result(img)
        
        
        if cv2.waitKey(33) == 27:
            break
    cv2.destroyAllWindows()




for my_video_src in video_list:
    
    detect(my_video_src)
    time.sleep(5)


