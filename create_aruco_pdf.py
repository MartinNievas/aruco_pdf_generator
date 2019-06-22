from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
import numpy as np
import cv2
import cv2.aruco as aruco
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Aruco tags in pdf pages')
    parser.add_argument('--num', type=int, required=None, default=2,
                        help='Integer for the amount of tags to generate. Default [2]')
    parser.add_argument('--size', type=int, required=None, default=14,
                        help='Tag size in cm. Default [14]')

    args = parser.parse_args()
    tag_num = args.num
    tag_size = args.size

    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)

    for i in range(0,tag_num):
        # last parameter is total image size
        img = aruco.drawMarker(aruco_dict, i, 700)
        cv2.imwrite("generated_tags/test_marker"+str(i)+".jpg", img)
    
    c = canvas.Canvas('generated_tags/tags.pdf')
    for i in range(0,tag_num,2):
        c.drawImage("generated_tags/test_marker"+str(i)+".jpg", 1*cm, (i%2)*tag_size*cm+1*cm,\
                    tag_size*cm, tag_size*cm)
        c.drawImage("generated_tags/test_marker"+str(i+1)+".jpg", 1*cm, (i%2+1)*tag_size*cm+1.5*cm,\
                    tag_size*cm, tag_size*cm)
        c.showPage()
    c.save()
