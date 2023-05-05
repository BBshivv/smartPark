import cv2
import pickle
img = cv2.imread('carParkImg.png')
width,height=107,48
#try:
    #with open("carparkpos","rb") as f:
        #poslist=pickle.load(f)
#except:
poslist=[] #saving boxes

def mouseClick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        poslist.append((x, y))

    #with open("carparkpos","wb") as f:
        #pickle.dump(poslist,f) #creating a pickle object everytime click is made


while True:
    img = cv2.imread('carParkImg.png')
    for pos in poslist:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    #cv2.rectangle(img,(50,192),(157,240),(255,0,255),2)
    cv2.imshow('image',img)
    cv2.setMouseCallback("image", mouseClick)

    cv2.waitKey(1)