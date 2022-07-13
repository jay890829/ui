import pydicom
import numpy as np
import cv2
import glob
import argparse
import matplotlib
from function.apply import *
import function.settings as settings # set verbose 
import re

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

def enter(input_mode, file_or_path, type_, width, area, section, save_path, JPG):
    settings.init(0)
    if input_mode=='file':
        ret_arclen, ret_area, ret_errormessage = apply(file_or_path, save_path, input_mode, type_, width, area, section, JPG)
        print(settings.error)
    elif input_mode == 'path':
        index = 0
        total_max_len = 0
        ring_defect_area = []
        with open(save_path + "/結論.txt", "w") as fin:
            for filename in natural_sort(glob.glob(file_or_path + "/*.dcm")):
                print('---------- Start procssing ',filename,' ----------')

                ret_arclen, ret_area, ret_errormessage = apply(filename, save_path, input_mode, type_, width, area, section, JPG)
                fin.write("File: " + filename.split("\\")[-1] + "\n")

                max_len = 0
                for i in range(3):
                    for j in range(len(ret_arclen[i])):
                        for k in range(len(ret_arclen[i][j])):
                            if ret_arclen[i][j][k] > max_len:
                                max_len = ret_arclen[i][j][k]

                fin.write("最大瑕疵長度: " + str(max_len))
                if (max_len <= 0.08):
                    fin.write(" 合格\n")
                else:
                    fin.write(" 不合格\n")

                if (max_len > total_max_len):
                    total_max_len = max_len

                area1, area2, area3 = ret_area[0], ret_area[1], ret_area[2]

                try:
                    ring_defect_area[0 + 3 * int(index/section)] += (area1 if ret_errormessage[0]=='' else 0)
                except:
                    ring_defect_area.append((area1 if ret_errormessage[0]=='' else 0))

                try:
                    ring_defect_area[1 + 3 * int(index/section)] += (area2 if ret_errormessage[1]=='' else 0)
                except:
                    ring_defect_area.append((area2 if ret_errormessage[1]=='' else 0))

                try:
                    ring_defect_area[2 + 3 * int(index/section)] += (area3 if ret_errormessage[2]=='' else 0)
                except:
                    ring_defect_area.append((area3 if ret_errormessage[2]=='' else 0))

                if (int(index/section) == 0):
                    fin.write("瑕疵面積: " + "第一環: " + (str(area1) if ret_errormessage[0]=='' else "undetectable") + " 第二環: " + (str(area2) if ret_errormessage[1]=='' else "undetectable") + " 第三環: " + (str(area3) if ret_errormessage[2]=='' else "undetectable") + "\n")
                else:
                    fin.write("瑕疵面積: " + "第四環: " + (str(area1) if ret_errormessage[0]=='' else "undetectable") + " 第五環: " + (str(area2) if ret_errormessage[1]=='' else "undetectable") + " 第六環: " + (str(area3) if ret_errormessage[2]=='' else "undetectable") + "\n")
                fin.write("--------------------------------------\n")
                index += 1
                print('---------- File ',filename,' is processed ----------')
            print(ring_defect_area)
            fin.write("總結\n")
            fin.write("整體最大瑕疵長度: " + str(total_max_len) + (" 合格" if total_max_len <= 0.08 else " 不合格") + "\n")
            flag = True
            for x in ring_defect_area:
                if (x/area > 0.2):
                    flag = False
                    break
            fin.write("整體瑕疵面積加總: " + ("合格\n" if flag else "不合格\n"))
            fin.write("第一環: " + str(ring_defect_area[0]) + "(" + '{:.1%}'.format(ring_defect_area[0]/area) + ")\n")
            fin.write("第二環: " + str(ring_defect_area[1]) + "(" + '{:.1%}'.format(ring_defect_area[1]/area) + ")\n")
            fin.write("第三環: " + str(ring_defect_area[2]) + "(" + '{:.1%}'.format(ring_defect_area[2]/area) + ")\n")
            fin.write("第四環: " + str(ring_defect_area[3]) + "(" + '{:.1%}'.format(ring_defect_area[3]/area) + ")\n")
            fin.write("第五環: " + str(ring_defect_area[4]) + "(" + '{:.1%}'.format(ring_defect_area[4]/area) + ")\n")
            fin.write("第六環: " + str(ring_defect_area[5]) + "(" + '{:.1%}'.format(ring_defect_area[5]/area) + ")\n")
        print(settings.error)
    


	



