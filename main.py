from PIL import Image
import cv2
import os
import pyautogui
import sys

image = pyautogui.prompt(text='image name : ', title='image')

if not(os.path.exists(image + ".png")):
    pyautogui.alert(f"not exists the file : {image}.png")
    sys.exit()


image_folder = image.split('\\')[-1]

lists = os.listdir()
if not(image_folder in lists):
    os.mkdir(image_folder)



#rbg to gray
im = Image.open(f"{image}.png")
im.convert('LA').save(f"{image_folder}\\grayscale.png")

#to Binarization

this = os.getcwd()
os.chdir(image_folder)
img = cv2.imread(f"grayscale.png", cv2.IMREAD_GRAYSCALE)



ret, dst = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) #dst : Binarization



#border

laplacian = cv2.Laplacian(dst, cv2.CV_8U, ksize=3)
cv2.imwrite(f'laplacian.png', laplacian)







#색 반전

os.chdir(this)
im = Image.open(f'{image_folder}\\laplacian.png')
rgb_im = im.convert('RGB')

width, height = im.size

for x in range(width):
    for y in range(height):
        r,g,b = rgb_im.getpixel((x, y))
        if(r == 255):
            rgb_im.putpixel((x, y), (0, 0, 0, 255))
        else:
            rgb_im.putpixel((x, y), (255, 255, 255, 255))
        

rgb_im.save(f"{image_folder}\\border.png")
