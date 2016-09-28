#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import Image
import numpy as np
import os
from PIL import ImageDraw, ImageFont
import pybrain
from pybrain.structure import SoftmaxLayer
from pybrain.datasets import *
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml.networkreader import NetworkReader
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.shortcuts import *
import errno

def createExample(picName):
    pic = Image.open(picName).convert('RGBA');
    arr = np.array(pic.getdata());
    #print arr;
    #print len(arr);
    return  arr;

def createDataSet(dir):
    files = os.listdir(dir);
    #print len(files);

    """arr = createExample(dir + "test55.png");

    for element in arr :
        if element[0] < 255 and element[1] < 255 and element[2] < 255 and element[3] == 255:
        #if element == (255, 255, 255, 255):
            print "1";
        else:
            print "0";"""

    #inputArr=[]
    #outputArr=[]

    dataset = ClassificationDataSet(1600, 3);


    for item in files:
        clearArr=[]
        arr = createExample(dir+item)
        for element in arr :
            if element[0] < 255 and element[1] < 255 and element[2] < 255 and element[3] == 255:
                clearArr.append(1)
            else:
                clearArr.append(0)
        #inputArr.append(clearArr)
        nameAndExt = os.path.basename(dir + item)
        name, ext = os.path.splitext(nameAndExt)
        clearName = name.split(".")
        itemOut = [0, 0, 0]
        if clearName[0] == "square" or clearName[0] == "squareFilled":
            itemOut[1] = 1
        if clearName[0] == "triangle" or clearName[0] == "triangleFilled" or clearName[0] == "sqrTriangle" or clearName[0] == "sqrTriangleFilled":
            itemOut[2] = 1
        if clearName[0] == "circle" or clearName[0] == "circleFilled":
            itemOut[0] = 1
        #outputArr.append(itemOut);
        dataset.addSample(clearArr,itemOut)
        #print itemOut
        #print clearName[0] + "   " + str(itemOut)
    return dataset
    #print len(inputArr)
    #print  len(outputArr)

    #print dir+item, "lenght -", len(arr);



def main (  ): #{
    MAX_EPOCHS = 5000
    MIN_EPOCHS = 200

    dataSet = createDataSet("pics/")
    net = buildNetwork(1600, 20, 3, hiddenclass=SoftmaxLayer)
    net.sortModules()

    trainer = BackpropTrainer(net, dataSet)

    epochs = 0

    backpropError = 1

    while (backpropError > 0.001) or (epochs < MIN_EPOCHS):
        backpropError = trainer.train()
        if epochs % 100 == 0:
            print '###   ' + str(backpropError) + '   ' + str(epochs)
        epochs += 1
        if epochs > MAX_EPOCHS:
            print('error while traininig %s', backpropError  )
            break
    print epochs

    keyWord = 1

    while 1==1:
        keyWord = raw_input("Enter dir:")
        if str(keyWord) == "close":
            break
        if str(keyWord) == "test":
            arr = makeVectorFromPic("picsForTest/mount.png")
            print net.activate(arr)
            del arr
            arr = makeVectorFromPic("picsForTest/plate.png")
            print net.activate(arr)
            del arr
            arr = makeVectorFromPic("picsForTest/circle.png")
            print net.activate(arr)
            del arr
            arr = makeVectorFromPic("picsForTest/square.45.png")
            print net.activate(arr)
            del arr
            arr = makeVectorFromPic("picsForTest/triangle.210.png")
            print net.activate(arr)
            del arr
            arr = makeVectorFromPic("picsForTest/squareTriangle.png")
            print net.activate(arr)
            del arr
            continue
        else:
            try:
                arr = makeVectorFromPic(str(keyWord))
                print net.activate(arr)
            except IOError as e:
                if e.errno == errno.ENOENT:
                    print e.strerror
                    continue

    #}

def convertPicInWB(dir,factor = 0):

    image = Image.open(dir)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    #print "stat converting  " + dir
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if (S > (((255 + factor) // 2) * 3)):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
    #print "done converting  " + dir
    directory = os.path.dirname(dir)
    nameAndExt = os.path.basename(dir)
    name, ext = os.path.splitext(nameAndExt)
    newDir = directory + "/" + name + "WB"+ str(factor)
    print name + ext
    #print  newDir + ".png"
    image.save(newDir + ".png", "PNG")
    #image.show()
    return  image
    #del image

def makeVectorFromPic(dir):
    image = convertPicInWB(dir)
    clearArr = []
    #arr = createExample(image) #если что, можно попробовать сохранить картинку и потом открывать ее использовав новый путь
    arr = image.getdata()
    #print list(image.getdata())
    #print arr
    for element in arr:
        if len(element) == 4:
            if element[0] < 255 and element[1] < 255 and element[2] < 255 and element[3] == 255:
                clearArr.append(1)
            else:
                clearArr.append(0)
        else:
            if element[0] < 255 and element[1] < 255 and element[2] < 255:
                clearArr.append(1)
            else:
                clearArr.append(0)
    return clearArr

main();
