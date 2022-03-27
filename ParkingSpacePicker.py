import pickle
import cv2
 
width, height = 107, 48
 
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []
 
 
def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
 
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)
 
 


def parkingspacepicker():
    while True:
        img = cv2.imread('carParkImg.png')
        # print("jay "+str(img))
        for pos in posList:
            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
 
        # cv2.imshow("Image", img)
        frame = cv2.imencode('.jpg', img)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        cv2.setMouseCallback("Image", mouseClick)
        # cv2.waitKey(1)

