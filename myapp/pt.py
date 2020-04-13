# from . import data
import dlib
import cv2 as cv
import math
import numpy as np
import os
from imutils import face_utils
from imutils.face_utils import FaceAligner

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('/home/supun/Desktop/django-test/testapp/myapp/shape_predictor_68_face_landmarks.dat')

framecount = 0
nullframes = 0
deyemouth = 0.0
mid_angle = 0
dplus, temp = 0, 0
x,y,w,h = 0,0,0,0
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
temp5 = 0
temp6 = 0
temp7 = 0
temp8 = 0
temp9 = 0
temp10 = 0
temp11 = 0
temp12 = 0
temp13 = 0
temp14 = 0
temp15 = 0
temp16 = 0


import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = "",
    database = "nbdatabase"
)

mycursor = mydb.cursor()

# def checkUsr(val):
#     mycursor.execute("SELECT id,fname FROM `myapp_student` WHERE funq='" + str(val) + "';")
#     myresult = mycursor.fetchone()

#     usrdata = []
#     if myresult:
#         for x in myresult:
#             usrdata.append(x)
#         return usrdata
#     else:
#         return False


# def getNotices(acayr, dpt):
#     mycursor.execute("SELECT * FROM `myapp_notice` WHERE (acayear = '"+ str(acayr) +"' OR acayear = '0') AND (dpt = '"+ str(dpt) +"' OR dpt = 'all');")
#     myresult = mycursor.fetchall()

#     collection = []
#     if myresult:
#         for x in myresult:
#             collection.append(x)
#         return collection
#     else:
#         return False


def getUserImages():
    mycursor.execute("SELECT `imgname`,`uindex` FROM `myapp_uimage`")
    myresult = mycursor.fetchall()

    collection = []
    usr = ''
    if myresult:
        for x in myresult:
            collection.append(x[0])
            usr = x[1]
        return collection, usr
    else:
        return False


def truncateSnap():
    # query = "TRUNCATE `nbdatabase`.`myapp_uimage`;"
    mycursor.execute("TRUNCATE `nbdatabase`.`myapp_uimage`;")
    mydb.commit()


def resize(image, width=None, height=None, inter=cv.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions

        try:
            r = height / float(h)
        except:
            r = 1
        
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions

        try:
            r = width / float(w)
        except:
            r = 1

        
        dim = (width, int(h * r))

    # resize the image
    resized = cv.resize(image, dim, interpolation=inter)


    # return the resized image
    return resized


def coords(shape, dtype="int"):
    	# initialize the list of (x, y)-coordinates
	coords = np.zeros((68, 2), dtype=dtype)
 
	# loop over the 68 facial landmarks and convert them
	# to a 2-tuple of (x, y)-coordinates
	for i in range(0, 68):
		coords[i] = (shape.part(i).x, shape.part(i).y)
 
	# return the list of (x, y)-coordinates
	return coords


def distances(p1, p2):
    dist =  math.sqrt( ((p1['x']-p2['x'])**2)+((p1['y']-p2['y'])**2) )

    return round(dist, 3)


def getRatio(l1, l2 = 5.0, d = 0):
    return round(l1/l2, d)


def findArea(a, b, c):
    s = (a + b + c) / 2

    return (s*(s-a)*(s-b)*(s-c)) ** 0.5


def getAngle(p1,p2,p3,p4):
    x = ((p3['y'] - p1['y'])*(p1['x'] - p2['x'])*(p3['x'] - p4['x']) + p1['x']*(p1['y'] - p2['y'])*(p3['x'] - p4['x']) - p3['x'] * (p3['y'] - p4['y']) * (p1['x'] - p2['x'])) / ((p1['y'] - p2['y']) * (p3['x'] - p4['x']) - (p3['y'] - p4['y']) * (p1['x'] - p2['x']))
    y = p1['y'] * (p1['x'] - p2['x']) + (p1['y'] - p2['y']) * (x - p1['x'])

    pcenter = {'x' : x, 'y' : y}
    pmid = {'x': x, 'y': p1['y']}

    c = distances(pcenter, pmid)
    b = distances(p1, pmid)

    return (b /c)


def alignFace(frame):

    img = cv.imread("/home/supun/Desktop/django-test/testapp/media/" + str(frame), 0)
    
    fa = FaceAligner(predictor, desiredFaceWidth=256)

    # load the input image, resize it, and convert it to grayscale
    gray = resize(img, width=800)

    # show the original input image and detect faces in the grayscale
    # image
    rects = detector(gray, 2)

    # loop over the face detections
    for rect in rects:
        # extract the ROI of the *original* face, then align the face
        # using facial landmarks
        # (x, y, w, h) = rect_to_bb(rect)
        # faceOrig = resize(frame[y:y + h, x:x + w], width=256)
        faceAligned = fa.align(img, gray, rect)

        # import uuid
        # f = str(uuid.uuid4())
        # cv.imwrite("foo/" + f + ".png", faceAligned)

        # display the output images
        # cv.imshow("Aligned", faceAligned)
        # cv.waitKey(0)
        cv.imwrite("roi"+str(frame)+".jpg", faceAligned)

    try:
        os.remove("/home/supun/Desktop/django-test/testapp/media/" + str(frame))
    except:
        pass


def recognition_face(snapframe):
    global deyemouth
    global mid_angle
    global dplus
    global temp1
    global temp2
    global temp3
    global temp4
    global temp5
    global temp6
    global temp7
    global temp8
    global temp9
    global temp10
    global temp11
    global temp12
    global temp13
    global temp14
    global temp15
    global temp16

    alignFace(snapframe)

    img = cv.imread("roi"+str(snapframe)+".jpg", 1)
    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    

    
    # if snapframe is 10:
    #     img = resize(img, width=600)
    #     face_rect = detector(img, 1)
    
    # img = resize(img, width=600)
    face_rect = detector(img, 1)
    
        
    for (i, rect) in enumerate(face_rect):
        shape = predictor(img, rect)
        shape = coords(shape)
        
	    # cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # (x, y, w, h) = face_utils.rect_to_bb(rect)
	    # cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        count = 0



        p = {'x': 0, 'y': 0}

        
        for (x, y) in shape:
            cv.circle(img, (x,y), 1, (0,0,255), -1)
            count += 1

            p[count] = {'x': x, 'y': y}


        # chin

        # l1 = math.sqrt( ((p[1]['x']-p[17]['x'])**2)+((p[1]['y']-p[17]['y'])**2) )
        l1 = distances(p[1], p[17])
        l2 = distances(p[2], p[16])
        l3 = distances(p[3], p[15])
        l4 = distances(p[4], p[14])
        # l5 = distances(p[5], p[13])
        l6 = distances(p[6], p[12])


        # eye

        l7 = distances(p[37], p[46])
        l77 = distances(p[40], p[43])

        # eye to mouth corner
        l8 = distances(p[37], p[49])
        l9 = distances(p[46], p[55])

        # vertical distance
        l10 = distances(p[28], p[9])

        # mouth distance
        l11 = distances(p[49], p[55])


        # /
        l12 = distances(p[49], p[6])

        # \
        l13 = distances(p[55], p[12])

        # A
        l14 = distances(p[28], p[32])
        l15 = distances(p[28], p[36])


        # ><
        l16 = distances(p[55], p[37])
        l17 = distances(p[49], p[46])

        # _
        l18 = distances(p[18], p[27])
        l19 = distances(p[18], p[23])
        l20 = distances(p[27], p[22])


        l5 = distances(p[32], p[36])


        a1 = getAngle(p[37],p[36],p[46],p[32])

        # l21 = (((l18/l19) + (l18/l20))/2)/l10
        # l21 = getRatio(((l18/l19) + (l18/l20))/2,l10)
        l21 = (((l18/l19) + (l18/l20))/2) / l10

        # l22 = getRatio(l2,(((l18/l19) + (l18/l20))/2))
        l22 = l2 / (((l18/l19) + (l18/l20))/2)

        # l23 = getRatio(l2,l7)
        l23 = l2 / l7

        l24 = l7 / l77

        l25 = l23 / l24

        l26 = l2 / ((l12 + l13) / 2)

        l27 = l10 / l7

        l28 = l10 / l11

        l29 = l10 / ((l8 + l9) / 2.0)

        l30 = l5 / l77

        # l22 = l2 / (((l18/l19) + (l18/l20))/2)

        # l23 = l2 / l7

        # l24 = l7 / l77

        # l25 = l23 / l24

        # l26 = l2 / ((l12 + l13) / 2)

        # print(l21)


        
        # d1chin = math.sqrt( ((pchin['p1x']-pmid['p1x'])**2)+((pchin['p1y']-pmid['p1y'])**2) )
        # cv.line(img, (pchin['p1x'],pchin['p1y']), (pmid['p1x'],pmid['p1y']), (0,255,0), 2)
        
        # deyemouth += (crossX / crossY)
        deyemouth += l1
        mid_angle += a1

        # - | -
        dplus += l21

        # temp1 += a1
        # temp2 += l21
        # temp3 += l22
        # temp4 += l25
        # temp5 += l26
        # temp6 += l27

        a1 = findArea(distances(p[37], p[34]), distances(p[34], p[49]), distances(p[49], p[37]))
        a2 = findArea(distances(p[37], p[34]), distances(p[34], p[40]), distances(p[37], p[40]))
        a3 = findArea(distances(p[40], p[43]), distances(p[34], p[40]), distances(p[34], p[43]))
        a4 = findArea(distances(p[43], p[34]), distances(p[43], p[46]), distances(p[34], p[46]))
        a5 = findArea(distances(p[34], p[46]), distances(p[46], p[55]), distances(p[55], p[34]))
        a6 = findArea(distances(p[49], p[34]), distances(p[34], p[55]), distances(p[55], p[49]))



        # area set 2
        a11 = findArea(distances(p[3], p[28]), distances(p[28], p[34]), distances(p[34], p[3]))
        a21 = findArea(distances(p[28], p[15]), distances(p[15], p[34]), distances(p[34], p[28]))
        a31 = findArea(distances(p[3], p[34]), distances(p[34], p[6]), distances(p[6], p[3]))
        a41 = findArea(distances(p[34], p[15]), distances(p[15], p[12]), distances(p[12], p[34]))
        a51 = findArea(distances(p[6], p[28]), distances(p[28], p[34]), distances(p[34], p[6]))
        a61 = findArea(distances(p[34], p[28]), distances(p[28], p[12]), distances(p[12], p[34]))
        a71 = findArea(distances(p[6], p[34]), distances(p[34], p[9]), distances(p[9], p[6]))
        a81 = findArea(distances(p[9], p[34]), distances(p[34], p[12]), distances(p[12], p[9]))


        dist1 =  math.sqrt((p[37]['x']-p[34]['x'])**2)
        dist2 =  math.sqrt((p[34]['y']-p[37]['y'])**2)

        dist3 =  math.sqrt((p[34]['x']-p[46]['x'])**2)
        dist4 =  math.sqrt((p[34]['y']-p[46]['y'])**2)

        ag1 = math.atan2(dist1, dist2)
        ag2 = math.atan2(dist3, dist4)


        fdist1 =  math.sqrt((p[9]['x']-p[2]['x'])**2)
        fdist2 =  math.sqrt((p[9]['y']-p[2]['y'])**2)

        fdist3 =  math.sqrt((p[16]['x']-p[9]['x'])**2)
        fdist4 =  math.sqrt((p[16]['y']-p[9]['y'])**2)

        fdist5 =  math.sqrt((p[9]['x']-p[37]['x'])**2)
        fdist6 =  math.sqrt((p[9]['y']-p[37]['y'])**2)

        fdist7 =  math.sqrt((p[46]['x']-p[9]['x'])**2)
        fdist8 =  math.sqrt((p[9]['y']-p[46]['y'])**2)

        
        fdist9 =  math.sqrt((p[28]['x']-p[6]['x'])**2)
        fdist10 =  math.sqrt((p[6]['y']-p[28]['y'])**2)

        fdist11 =  math.sqrt((p[12]['x']-p[28]['x'])**2)
        fdist12 =  math.sqrt((p[12]['y']-p[28]['y'])**2)

        fag1 = math.atan2(fdist1, fdist2)
        fag2 = math.atan2(fdist3, fdist4)

        fag3 = math.atan2(fdist5, fdist6)
        fag4 = math.atan2(fdist7, fdist8)

        nag1 = math.atan2(fdist9, fdist10)
        nag2 = math.atan2(fdist11, fdist12)


        ag = ag1 + ag2

        fagA = fag1 + fag2
        fagB = fag3 + fag4

        fag = fagA / fagB

        nag = (nag1 + nag2) / fagB



        # r1 = a1 /a2
        # r2 = a1 /a3
        # r3 = a1 /a4
        # r4 = a1 /a5
        r5 = a1 /a6
        # r6 = a2 /a3
        # r7 = a2 /a4
        # r8 = a2 /a5
        r9 = a2 /a6
        # r10 = a3 /a4
        # r11 = a3 /a5
        r12 = a3 /a6
        # r13 = a4 /a5
        r14 = a4 /a6
        # r15 = a5 /a6


        # angle ratio set 2 ##################
        
        r002 = a11 / a31
        r011 = a21 / a61
        r015 = a31 / a51
        r017 = a31 / a71
        r022 = a41 / a81
        r027 = a61 / a81

        temp1 += l28
        temp2 += l29
        temp3 += l30

        temp4 += nag

        temp5 += r5

        temp6 += r002
        temp7 += r011 #============
        temp8 += r015 #============

        temp9 += r9

        temp10 += r017 #============
        temp11 += r022

        temp12 += r12

        temp13 += r027

        temp14 += r14

        temp15 += fag

        temp16 += ag



        try:
            os.remove("roi"+str(snapframe)+".jpg")
        except:
            pass

        # return getRatio(temp1), getRatio(temp2), getRatio(temp3), getRatio(temp4), getRatio(temp5), getRatio(temp6), getRatio(temp7),getRatio(temp8),getRatio(temp9),getRatio(temp10),getRatio(temp11),getRatio(temp12),getRatio(temp13),getRatio(temp14),getRatio(temp15),getRatio(temp16,5,1)

        # original
        # return getRatio(temp5), getRatio(temp9), getRatio(temp12), getRatio(temp14), getRatio(temp1), getRatio(temp2), getRatio(temp3,5,1), getRatio(temp16,5,1), getRatio(temp6,5,1), getRatio(temp15,5,1), getRatio(temp4,5,1), getRatio(temp11,5,1), getRatio(temp13,5,1)
        
        return getRatio(temp5), getRatio(temp9), getRatio(temp12), getRatio(temp14), getRatio(temp1), getRatio(temp2), getRatio(temp3,5,1), getRatio(temp16,5,1), getRatio(temp4,5,1), getRatio(temp11,5,1), getRatio(temp13,5,1)
        # return getRatio(temp3,5,1)



# gotdata, usr = data.getUserImages()



def test():

    ccount = 0
    output1 = ''
    gotdata = []
    usr = ''

    if getUserImages():
        gotdata, usr = getUserImages()
    
    for x in gotdata:

        ccount += 1

        if ccount is not 5:
            recognition_face(str(x))
        else:
            t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11 = recognition_face(str(x))
            output1 = '' + str(t1) + str(t2) + str(t3) + str(t4) + str(t5) + str(t6) + str(t7) + str(t8) + str(t9) + str(t10) + str(t11)
            truncateSnap()
            return output1


# print(gotdata)