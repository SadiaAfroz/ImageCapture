import cv2
import time

# for webcam it's 0
#if to read videos using file path
cam = cv2.VideoCapture(0)

cv2.namedWindow("Capture image")

image_counter=0
start_time=time.time()

while True:
    #get the image frame
    #ret: successfuly read or not 
    ret, frame= cam.read()

    if not ret:
        print("failed to take the frame")
        break

    #showing the webcam to user
    # cv2.imshow("test", frame)

    #keyboard binding function: passing 0 wait for infinite time for pressing any key
    k=cv2.waitKey(1)

    # print(k)
    if k%256 == 27 :
        #escape key has been pressed
        print("Escape hit, closing the app")
        break

    # check if 5 seconds passed
    if time.time() - start_time >=5:
        img_name="opencv_frame_{}.png".format(image_counter)
        cv2.imwrite(img_name,frame)
        print("Screenshot taken")
        start_time=time.time()
        image_counter+=1


#release capture pointer
cam.release()

cv2.destroyAllWindows()