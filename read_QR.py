import cv2
from pyzbar.pyzbar import decode

def read():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cv2.startWindowThread()
    cap.set(3,640) # 3 - width
    cap.set(4,480) # 4 - height
    while cap.isOpened():
        success , frame = cap.read()
        cv2.imshow('Reading QR code', frame)
        cv2.waitKey(1)
        for code in decode(frame):
            code = code.data.decode('Utf-8')
            print(code + '\n')
            cap.release()
            cv2.destroyAllWindows()
            break