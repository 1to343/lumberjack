from ast import Try
from pydoc import tempfilepager
import pyscreenshot as ImageGrab
import cv2
import numpy as np
from matplotlib import pyplot as plt
import autopy
import os, time

screen_size = None
screen_start_point = None
screen_end_point = None

def chg(line):
    ans = ''
    for i in range(len(line)):
        if line[len(line) - 1 - i] == 'l':
            ans = 'r' + ans
        else:
            ans = 'l' + ans
    return ans

# Сперва мы проверяем размер экрана и берём начальную и конечную точку для будущих скриншотов
def check_screen_size():
	#print ("Checking screen size")
	img = ImageGrab.grab()
	# img.save('temp.png')
	global screen_size
	global screen_start_point
	global screen_end_point

	# я так и не смог найти упоминания о коэффициенте в методе grab с параметром bbox, но на моем макбуке коэффициент составляет 2. то есть при создании скриншота с координатами x1=100, y1=100, x2=200, y2=200), размер картинки будет 200х200 (sic!), поэтому делим на 2
	coefficient = 1
	screen_size = (img.size[0] / coefficient, img.size[1] / coefficient) 

	# берем примерно девятую часть экрана примерно посередине.
	screen_start_point = (0, 0)
	screen_end_point = (screen_size[0], screen_size[1])
	#print ("Screen size is" + str(screen_size))

def move_mouse(coord1, coord2):
	autopy.mouse.move(int(screen_start_point[0]) + coord1 , int(screen_start_point[1]) + coord2)


def make_screenshot():
	screenshot = ImageGrab.grab(bbox=(1250, 140, 1600, 650))
	# сохраняем скриншот, чтобы потом скормить его в OpenCV
	screenshot_name = '2.png'
	screenshot.save(screenshot_name)
	return screenshot_name

def snatch():
	autopy.mouse.click()


def find_float(img):
    template1 = cv2.imread('left.png')
    template2 = cv2.imread('right.png')
    template3 = cv2.imread('start.png')
    template4 = cv2.imread('restart.png')
    image = cv2.imread(img)
    cv2.imshow("Image", image)
    cv2.imshow("Template1", template1)
    cv2.imshow("Template2", template2)
    cv2.imshow("Template3", template3)
    cv2.imshow("Template4", template4)
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template1Gray = cv2.cvtColor(template1, cv2.COLOR_BGR2GRAY)
    template2Gray = cv2.cvtColor(template2, cv2.COLOR_BGR2GRAY)
    template3Gray = cv2.cvtColor(template3, cv2.COLOR_BGR2GRAY)
    template4Gray = cv2.cvtColor(template4, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(imageGray, template4Gray,
	cv2.TM_CCOEFF_NORMED)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    (startX, startY) = maxLoc
    endX = startX + template4.shape[1]
    endY = startY + template4.shape[0]
    cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)
    # show the output image
    #cv2.imshow("Output", image)
    #cv2.waitKey(0)


def find_temp(img, temp):
    treshold = 0.8
    image = cv2.imread(img)
    template = cv2.imread(temp)
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(imageGray, templateGray,
	cv2.TM_CCOEFF_NORMED)
    (ycords, xcords) = np.where(result >= treshold)
    dic = {}
    if len(ycords) > 0:
        check_val = ycords[0]
        for i in range(len(ycords)):
            if (ycords[i] - check_val) % 100 == 0:
                dic[ycords[i]] = xcords[i]
    return dic

def rev(line):
    ans = []
    for i in range(len(line)):
        ans.append(line[len(line) - 1 - i])
    return ''.join(ans)

d = {}
d["rrrr"] = "llll"
d["rrrl"] = "lllr"
d["rrlr"] = "llrl"
d["rlrr"] = "lrll"
d["lrrr"] = "rlll"
d["rrll"] = "llrr"
d["rlrl"] = "lrlr"
d["rllr"] = "lrrl"
d["lrrl"] = "rllr"
d["lrlr"] = "rlrl"
d["llrr"] = "rrll"
d["rlll"] = "lrrr"
d["lrll"] = "rlrr"
d["llrl"] = "rrlr"
d["lllr"] = "rrrl"
d["llll"] = "rrrr"
d["rrrrr"] = "lllll"
d["rrrrl"] = "llllr"
d["rrrlr"] = "lllrl"
d["rrlrr"] = "llrll"
d["rlrrr"] = "lrlll"
d["lrrrr"] = "rllll"
d["rrrll"] = "lllrr"
d["rrlrl"] = "llrlr"
d["rrllr"] = "llrrl"
d["rlrrl"] = "lrllr"
d["rlrlr"] = "lrlrl"
d["rllrr"] = "lrrll"
d["lrrrl"] = "rlllr"
d["lrrlr"] = "rllrl"
d["lrlrr"] = "rlrll"
d["llrrr"] = "rrlll"
d["rrlll"] = "llrrr"
d["rlrll"] = "lrlrr"
d["rllrl"] = "lrrlr"
d["rlllr"] = "lrrrl"
d["lrrll"] = "rllrr"
d["lrlrl"] = "rlrlr"
d["lrllr"] = "rlrrl"
d["llrrl"] = "rrllr"
d["llrlr"] = "rrlrl"
d["lllrr"] = "rrrll"
d["rllll"] = "lrrrr"
d["lrlll"] = "rlrrr"
d["llrll"] = "rrlrr"
d["lllrl"] = "rrrlr"
d["llllr"] = "rrrrl"
d["lllll"] = "rrrrr"

check_screen_size()
template1 = cv2.imread('leftbranch.png')
template2 = cv2.imread('rightbranch.png')
template3 = cv2.imread('hat.png')
template4 = cv2.imread('left.png')
template5 = cv2.imread('right.png')
side = 'l'
act = 'l'
c = 1
os.system("xte 'key Left'")
time.sleep(0.03)
os.system("xte 'key Left'")
time.sleep(0.02)
while True:
    img = make_screenshot()
    image = cv2.imread(img) 
    lbrd = find_temp(img, 'leftbranch.png')
    rbrd = find_temp(img, 'rightbranch.png')
    hatd = find_temp(img, 'hat.png')
    a1 = list(lbrd.keys())
    a2 = list(rbrd.keys())
    td = {}
    #print(len(a1), len(a2))
    for i in range(len(a1)):
        #print(a1[i], 'l')
        td[a1[i]] = 'l'
    for i in range(len(a2)):
        #print(a2[i], 'r')
        td[a2[i]] = 'r'
    cs = dict(sorted(td.items()))
    task = list(cs.values())
    #print(td)
    #print(d[rev(''.join(task))])
    for i in d[rev(''.join(task))]:
        if i == 'r':
            os.system("xte 'key Right'")
            time.sleep(0.03)
            os.system("xte 'key Right'")
            time.sleep(0.02)
        else:
            os.system("xte 'key Left'")
            time.sleep(0.03)
            os.system("xte 'key Left'")
            time.sleep(0.02)

    #c -= 1

'''
1286 825 1426 969 left button
1356 897 left click
1453 831 1587 967 right button
1520 899 right click
1486 616 1514 635 hat
1302 451 1416 518 left branch
1461 144 1588 219 right branch
1487 616 1515 635 hat
'''