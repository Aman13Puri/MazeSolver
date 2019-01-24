import cv2
import numpy as np

maze = cv2.imread('maze.png')
maze = cv2.cvtColor(maze, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(maze, 200, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('maze',binary)
#the size of each block of the maze (path and the wall currently)
pixX = 0
pixY = 0
prevLim = 0
lim = 0
block = 1
height = np.size(binary, 0)
width = np.size(binary, 1)
while(pixY<height and pixX<width):
               pixY= 0
               prevLim = lim
               while(binary[pixY,pixX] == binary[pixX,pixY]):
                              pixY = pixY+1
                              
               lim =pixY
               pixX = pixX+1
               if(prevLim != 0 and prevLim == lim):
                              block = block +1
               elif(prevLim != 0 and prevLim != lim):
                              break
print("BlockSize")
print(block)
#Conversion of the maze Image to a matrix where the a wall block will represent a 0 element and path block will represent a 1 element
pixX = 0
pixY = 0
col = 0
row = 0
imgArr = []
while(pixY<height):
               col=0
               pixX=0
               while(pixX<width):
                              i=int(block/2)+pixY
                              j=int(block/2)+pixX
                              px = binary[i,j]
                              imgArr.append(px)
                              pixX=pixX+block
                              col=col+1
               pixY=pixY+block
               row=row+1
blockHeight = int(height/block)
blockWidth = int(width/block)
print("blockHeight")
print(blockHeight)
print("blockWidth")                              
print(blockWidth)

imgMat = [[0 for i in range(blockHeight)] for j in range(blockWidth)]
for i in range(blockHeight):
               for j in range(blockWidth):
                              if(imgArr[i*blockHeight+j] == 255):
                                             imgMat[i][j] = 1
                              else:
                                             imgMat[i][j] = 0
print(imgMat)


                              






















               
