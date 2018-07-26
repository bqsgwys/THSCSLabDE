import numpy as np

import cv2

img = cv2.pyrDown(cv2.imread("EEPika.png", cv2.IMREAD_UNCHANGED))

ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY) , 127, 255, cv2.THRESH_BINARY)
#ret=127
#print("thresh",thresh)
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("image", img)
#print("contours",contours)
#c为轮廓点坐标
for c in contours:
  # find bounding box coordinates:最小的矩形，把找到的形状包起来
  x,y,w,h = cv2.boundingRect(c)#x，y是矩阵左点的坐标，w，h是矩阵的宽和高
  print(w,h)
  cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

  # find minimum area:带有旋转角
  rect = cv2.minAreaRect(c)
  # calculate coordinates of the minimum area rectangle
  box = cv2.boxPoints(rect)
  # normalize coordinates to integers
  box = np.intc(box)
  print("box",box)
  # draw contours
  cv2.drawContours(img, [box], 0, (0,0, 255), 3)

  # calculate center and radius of minimum enclosing circle
  (x,y),radius = cv2.minEnclosingCircle(c)
  #print((x,y))
  #print(radius)
  # cast to integers
  center = (int(x),int(y))#圆心
  radius = int(radius)#半径
  # draw the circle
  img = cv2.circle(img,center,radius,(0,255,0),2)

cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("b", img)

cv2.waitKey()
cv2.destroyAllWindows()
