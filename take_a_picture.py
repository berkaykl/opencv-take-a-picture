import cv2 as cv

while True:

    waitingTime = input("Enter waiting time: ")

    if (waitingTime.isdigit()):

        if (int(waitingTime) != 0):
            break
        else:
            print("Please enter a number other than 0!")
    else:
        print("Enter a valid number!")



cap = cv.VideoCapture(0)
counter = 0

while cap.isOpened():
    ret,frame = cap.read()

    cv.imshow("picture", frame)

    key = cv.waitKey(1) & 0XFF

    if (key == ord("c")):
        for i in range(waitingTime,0,-1):
            ret, frame = cap.read()
            cv.putText(frame, str(i), (frame.shape[1]//2 - 50, frame.shape[0]//2), cv.FONT_HERSHEY_SIMPLEX, 3, (255,255,255), 5)
            cv.imshow("picture", frame)
            if (cv.waitKey(1000) & 0XFF == ord("q")):
                break 

        ret,frame = cap.read()
        counter +=1
        cv.imwrite(f"picture{counter}.jpg", frame)
        cv.imshow("picture", frame)



    elif (key == ord("q")):
        break


cap.release()
cv.destroyAllWindows()