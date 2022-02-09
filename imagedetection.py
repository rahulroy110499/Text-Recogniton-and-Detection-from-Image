import cv2
import pytesseract
#opening the image
pytesseract.pytesseract.tesseract_cmd= 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('3.jpg')

img = cv2.cvtColor(img ,cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))

# #detecting characters
# hImg, wImg,_ = img.shape #size of our image
# boxes = pytesseract.image_to_boxes(img)#store all things in list
# for b in boxes.splitlines():
#     # print(b)
#     b=b.split(' ') #splliting them
#     print(b)
#     x,y,w,h= int(b[1]),int(b[2]),int(b[3]),int(b[4]) #turning into interger as they are strings
#     #now we can use these values to create rectangles
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
#     #label these characters around there box
#     cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)


#detecting words
hImg, wImg,_ = img.shape #size of our image
boxes = pytesseract.image_to_data(img)#store all things in list
print(boxes)
for x,b in enumerate(boxes.splitlines()):#everytime it loops it will put the value of the count in x
    
    if x!=0:
        b=b.split() #splliting them
        print(b)
        if len(b)==12: #if length of the bis more than 11 or just 12 then we will do the next operations    
            #the bounding boxes are at 6th 7th 8th and 9th position
            x,y,w,h= int(b[6]),int(b[7]),int(b[8]),int(b[9]) #turning into interger as they are strings
            #now we can use these values to create rectangles
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
            #label these characters around there box
            # b(11) is the text
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)




cv2.imshow('Result',img)
cv2.waitKey(0)
#creating  a box around it 

