import sqlite3

try:
    conn = sqlite3.connect('number_plate_db1')
    cursor = conn.cursor()
    print("Opened database successfully")
except Exception as e:
    print("Error during connection: ", str(e))


# LOAD THU VIEN VA MODUL CAN THIET
import cv2
import pytesseract
#DOC CAMERA - TACH HINH ANH NHAN DIEN
#webcam = cv2.VideoCapture('http://192.168.1.9:4747/video')
webcam = cv2.VideoCapture(0)

while(True):
    check, frame = webcam.read()
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1)
    if key == ord('0'):
        cv2.imwrite(filename='saved_img.jpg', img=frame)
        webcam.release()
        img_new = cv2.imread('saved_img.jpg')
        cv2.waitKey(1650)
        cv2.destroyAllWindows()
        img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
        break
img_new = cv2.imshow("Anh Goc", img_new)
gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
contours,h = cv2.findContours(thresh,1,2)
largest_rectangle = [0,0]
for cnt in contours:
    lenght = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, lenght, True)
    if len(approx)==4: 
        area = cv2.contourArea(cnt)
        if area > largest_rectangle[0]:
            largest_rectangle = [cv2.contourArea(cnt), cnt, approx]
x,y,w,h = cv2.boundingRect(largest_rectangle[1])
image=img_[y:y+h, x:x+w]
cv2.drawContours(img_,[largest_rectangle[1]],0,(0,255,0),8)
cropped = img_[y:y+h, x:x+w]
cv2.imshow('Dinh Vi Bien So', img_)
cv2.drawContours(img_,[largest_rectangle[1]],0,(255,255,255),18)
#DOC HINH ANH CHUYEN THANH FILE TEXT
#pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/User/AppData/Local/Tesseract-OCR/tesseract.exe'

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imshow('Ket Qua', thresh)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening
data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
print("Bien so xe la:")

sqlite_insert_query = """INSERT INTO number_plate
                        (number) 
                        VALUES 
                        (?)""",(data)

count = cursor.execute("INSERT INTO number_plate (number) VALUES (?)",(data,))
conn.commit()
print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
cursor.close()

print(data)
cv2.waitKey()
