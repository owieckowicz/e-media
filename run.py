import cv2
import numpy as np

filename = "square.png"
img = cv2.imread(filename)

window = "Window"
# Create a named window
cv2.namedWindow(window)

# Move window to sertain place
cv2.moveWindow(window, 600, 200)

# Percent of original size
scale_percent = 1000
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# Show image
cv2.imshow(window, resized)
print(img)

# for line in open(filename, "rb"):
#     if 'END' in line:
# break
#     if 'LINES' in line:
#         # remove trailing newline
#         line = line.rstrip('\n')
#         # extract integer value
#         print int(line.split('=')[1])  # 2240

#pixel checking
pix = img[0][0]
print("pixel:")
print(pix)
#dimensions of picture
shape = img.shape
print("shape:(x,y,color format table size):")
print(shape)
#size
size = img.size
print("size:")
print(size)
print()
cv2.waitKey()
cv2.destroyAllWindows()

#print raw data
file = open('square.png', encoding='ANSI')
f1 = file.readlines()
for line in f1:
    print(line.rstrip())
file.close()