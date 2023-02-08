#RUN PYTHON FILE IN VIRTUAL ENVIRONMENT
#run file in the command prompt. Make sure to give an image path using ‘-i’ argument.
#If the image is in another directory, then you need to give full path of the image
#code - (py colour_detection.py -i sample.jpg)

import numpy as np
import pandas as pd

#OpenCV-Python is a library of Python bindings designed to solve computer vision 
#problems. cv2. imread() method loads an image from the specified file
import cv2

#We are using argparse library to create an argument parser. We can directly give an image 
#path from the command prompt
import argparse

#Creating argument parser to take image path from command line
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
img = cv2.imread(img_path)

#declaring global variables (are used later on)
clicked = False
r = g = b = xpos = ypos = 0

#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


#We have the r,g and b values. Now, we need another function which will return 
# us the color name from RGB values.
#To get the color name, we calculate a distance(d) which tells us how close we are to 
# color and choose the one having minimum distance.
#Our distance is calculated by this formula:
#d = abs(Red – ithRedColor) + (Green – ithGreenColor) + (Blue – ithBlueColor)
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


#It will calculate the rgb values of the pixel which we double click. The function 
#parameters have the event name, (x,y) coordinates of the mouse position, etc.
#In the function, we check if the event is double-clicked then we calculate and 
# set the r,g,b values along with x,y positions of the mouse.
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# we created a window in which the input image will display. Then, we set a 
# callback function which will be called when a mouse event happens.      
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)



#Whenever a double click event occurs, it will update the color name and RGB values on the window.
#Using the cv2.imshow() function, we draw the image on the window.
#When the user double clicks the window, we draw a rectangle and get the color name to draw 
#text on the window using cv2.rectangle and cv2.putText() functions.
while(1):

    cv2.imshow("image",img)
    if (clicked):
   
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #Hit 'esc' key for breaking the loop  
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()

#SUMMARY -
#Color Detection OpenCV Python is the process of detecting the name of any color.Well, for humans 
#this is an extremely easy task but for computers, it is not straightforward. Human eyes and
#brains work together to translate light into color.