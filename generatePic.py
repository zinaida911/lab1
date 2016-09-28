#!/usr/bin/env python

import Image
from PIL import ImageDraw, ImageFont
import os

def generatePic():
    square = Image.new("RGB", (40, 40), (255, 255, 255))
    draw = ImageDraw.Draw(square)
    draw.rectangle((10, 10, 30, 30), fill=(255, 255, 255), outline=(0, 0, 0))  # square
    square.save("generatedPics/square.png", "PNG")

    circle = Image.new("RGB", (40, 40), (255, 255, 255))
    draw = ImageDraw.Draw(circle)
    draw.ellipse((5, 5, 35, 35), outline="black", fill="white")  # circle
    circle.save("generatedPics/circle.png", "PNG")

    sqrTriangle1 = Image.new("RGB", (40, 40), (255, 255, 255))
    draw = ImageDraw.Draw(sqrTriangle1)
    draw.polygon((5, 5, 35, 35, 5, 35), outline=(0, 0, 0), fill=(255, 255, 255))  # triangle
    sqrTriangle1.save("generatedPics/sqrTriangle.png", "PNG")

    triangle = Image.new("RGB", (40, 40), (255, 255, 255))
    draw = ImageDraw.Draw(triangle)
    draw.polygon((30, 30, 10, 30, 20, 10), outline=(0, 0, 0), fill=(255, 255, 255))  # triangle
    triangle.save("generatedPics/triangle.png", "PNG")

    squareF = Image.new("RGB", (40, 40), (255, 255, 255))
    draw = ImageDraw.Draw(squareF)
    draw.rectangle((10, 10, 30, 30), fill="black", outline=(0, 0, 0))  # square
    squareF.save("generatedPics/squareFilled.png", "PNG")

    circleF = Image.new("RGB", (40, 40), (255, 255, 255))
    draw = ImageDraw.Draw(circleF)
    draw.ellipse((5, 5, 35, 35), outline="black", fill="black")  # circle
    circleF.save("generatedPics/circleFilled.png", "PNG")

    sqrTriangle1F = Image.new("RGB", (40, 40), (255, 255, 255))
    draw = ImageDraw.Draw(sqrTriangle1F)
    draw.polygon((5, 5, 35, 35, 5, 35), outline=(0, 0, 0), fill="black")  # triangle
    sqrTriangle1F.save("generatedPics/sqrTriangleFilled.png", "PNG")

    triangleF = Image.new("RGB", (40, 40), (255, 255, 255))
    draw = ImageDraw.Draw(triangleF)
    draw.polygon((30, 30, 10, 30, 20, 10), outline=(0, 0, 0), fill="black")  # triangle
    triangleF.save("generatedPics/triangleFilled.png", "PNG")

    square = Image.new("RGB", (40, 40), (255, 255, 255))
    draw = ImageDraw.Draw(square)
    draw.rectangle((10, 10, 30, 30), fill=(255, 255, 255), outline=(0, 0, 0))  # square
    draw.polygon((30, 30, 10, 30, 20, 10), outline=(0, 0, 0), fill="black")  # triangle
    square.save("generatedPics/squareTriangle.png", "PNG")

    print "111";

def rotarePic(picDir, picName, angle):
    src_im = Image.open(picDir)
    size = 40, 40

    dst_im = Image.new("RGBA", (40, 40), "white")
    im = src_im.convert('RGBA')
    rot = im.rotate(angle, Image.BILINEAR).resize(size)  # NEAREST BILINEAR BICUBIC
    dst_im.paste(rot, (0, 0), rot)
    newDirPic = os.path.dirname(picDir) + "/" + picName + "." + str(angle) + ".png"
    dst_im.save(newDirPic, "PNG")


def main():  #{

    generatePic();
    #rotarePic("generatedPics/triangle7.png");
    dir="generatedPics/"
    files = os.listdir(dir);
    for item in files: #{
        nameAndExt = os.path.basename(dir + item)
        name, ext = os.path.splitext(nameAndExt)
        #print name
        if name == "square" or name == "squareFilled" :
            for angle in range(30,61,15):
                rotarePic(dir+item,name,angle)
        if name == "triangle" or name == "triangleFilled" :
            for angle in range(15,359,15):
                rotarePic(dir+item,name,angle)
        if name == "sqrTriangle" or name == "sqrTriangleFilled" :
            for angle in range(90,359,90):
                rotarePic(dir+item,name,angle)
    #}

#}

main();