import pydicom
import os
import function.settings as settings
from function.Show_Img import *
from function.Find_Ind import *
from function.Draw_Ellipse_Circle import *
from function.BFS_Connect import *
from function.BFSCanny_To_Contour import *
from function.Histogram import *
from function.Calculate_Defect_Area import *

from function.Find_Defect import *

from function.Cal_Arc_Length import *
from function.Total_Defect_Img import *
from function.Set_DefaultVal import *
from function.Set_Triangle import *
from function.SetWidth_Img import *
from function.Merge_Contour import *
from function.TypeCD_Find_Defect import *
from function.Detect_ByContour import *


def apply(file, save_path, input_mode, type_of_parts="A", width_of_column=0.65, area_of_column=11.4, num_of_section=8, JPG=True):
    Set_DefaultVal(file, type_of_parts, width_of_column, area_of_column, num_of_section)

    print(type_of_parts)
    ds = pydicom.dcmread(file)
    img_orginal = ds.pixel_array
    img256 = (img_orginal/256).astype('uint8')
    s1, s2 = img_orginal.shape
    if s1 > s2:
        img_orginal = cv2.rotate(img_orginal, cv2.ROTATE_90_COUNTERCLOCKWISE)
        img256 = cv2.rotate(img256, cv2.ROTATE_90_COUNTERCLOCKWISE)
        s1, s2 = img_orginal.shape
    settings.img_height = s1

    final_imgrgba = Set_ImgRGBA(img256)
    # n_channels = 4
    # img_height, img_width = img256.shape
    # final_imgrgba = np.zeros((img_height, img_width, n_channels), dtype=np.uint8)

    #Find Part
    print('Find part')
    ind = Find_Ind(img256)

    #Declare Part
    # w = 400
    if settings.type_of_parts == "A": ##partA寬度0.65 英吋 = 16.509999999999998 亳米 = 330.19個pixel
        w = 300
    elif settings.type_of_parts == "B": ##partB寬度0.604 英吋 = 15.341599999999998 亳米 = 306.83個pixel
        w = 300
    elif settings.type_of_parts == "C": ##partC寬度0.448 英吋 = 11.379199999999999 亳米 = 227.58個pixel
        w = 200
    elif settings.type_of_parts == "D": ##partD寬度0.448 英吋 = 11.379199999999999 亳米 = 227.58個pixel
        w = 200
    imgpart1, imgpart2, imgpart3 = img256[:,ind[0]-w:ind[0]+w], img256[:,ind[1]-w:ind[1]+w], img256[:,ind[2]-w:ind[2]+w]
    imgpart_list = [imgpart1, imgpart2, imgpart3]

    imgpart1_, imgpart2_, imgpart3_ = img_orginal[:,ind[0]-w:ind[0]+w], img_orginal[:,ind[1]-w:ind[1]+w], img_orginal[:,ind[2]-w:ind[2]+w]
    imgpart65536_list = [imgpart1_, imgpart2_, imgpart3_]

    imgrgb = cv2.merge((255-img256,255-img256,255-img256))
    # result_filename = file+'_rgb.jpg'
    # cv2.imwrite(result_filename, imgrgb)
    offset_list = [(ind[0]-200, ind[0]+300), (ind[1]-550, ind[1]-100), (ind[2]+120, ind[2]+600)]

    part_side = [ind[0]+50, ind[1]-550, ind[2]+120]
    name = ["left", "mid", "right"]
    
    Set_Triangle(img256, ind)
    # return
    for i in range(3):
        #i = i + 1
        settings.path = file+"_"+name[i]
        settings.whole_column = False
        # try:
        imgpart_ellipse, ellipse_list = Draw_Ellipse_Circle(imgpart_list[i], part_side[i], imgpart65536_list[i])
        Show_Img(imgpart_ellipse, 0)
        s1, s2 = imgpart_ellipse.shape

        if Check_Detectable(imgpart_list[i]) == False:
            settings.ret_arclen.append(settings.arclen_list)
            settings.ret_area.append(0)
            settings.ret_errormessage.append("NonDetectable")

        imgpart, imgpart65536, ellipse_list, imgrgbpart = SetWidth_Img(img256, img_orginal, ellipse_list, ind[i]-w, imgpart_list[i])
        imgpart_ellipse, ellipse_list = Draw_Ellipse_Circle(imgpart, part_side[i], imgpart65536)

        print('Canny')
        if settings.type_of_parts == "A" or settings.type_of_parts == "B":
            canny_output = Find_Defect(imgpart, ellipse_list, imgpart65536)
        else:
            canny_output = TypeD_Test(imgpart, ellipse_list, imgpart65536)

        kernel = np.ones((3,3), np.uint8)
        dilation = cv2.dilate(canny_output, kernel, iterations = 1)
        erosion = cv2.erode(dilation, kernel, iterations = 1) 

        print('BFS contour connection')
        imgpart_bfs_canny = BFS_Connect(erosion, imgpart_ellipse)
        Show_Img(imgpart_bfs_canny, 0)

        # plt.figure(figsize=(30, 30))
        # plt.imshow(canny_output, cmap=plt.cm.gray, vmin=0, vmax=255)
        # plt.show()

        s1, s2 = imgpart_bfs_canny.shape
        for j in range(s1):
            for k in range(s2):
                if j <= 40 or j >= s1 - 40:
                    imgpart_bfs_canny[j][k] = 0

        print('Draw connected contour')

        imgpart_contour, full_contour, contours= BFSCanny_To_Contour(imgpart_bfs_canny, imgrgbpart, ellipse_list)

        contour_interval_list, dis_of_defect_list = Detect_ByContour(contours, ellipse_list, imgrgbpart, imgpart, imgpart65536)

        img_contour, img_full, img_mask, img_mask_leftright = Merge_Contour(imgpart_contour, full_contour, ellipse_list, imgpart, imgrgbpart)

        imgpart_Arclength, imgpart_Arclength_contour, imgrgb_reason = Cal_Arc_Length(imgpart, ellipse_list, imgpart65536, img_contour, imgrgbpart, contour_interval_list, dis_of_defect_list)

        area = Calculate_Defect_Area(contours, ellipse_list, imgrgbpart, imgpart65536, img_mask, imgpart)

        imgpart_Arclength, imgpart_Arclength_contour = Circle_Notation(imgpart_Arclength, imgpart_Arclength_contour, ellipse_list)
        s1, s2, s3 = imgpart_Arclength_contour.shape
        cv2.line(imgpart_Arclength_contour, (0, int(settings.triangle_y1)), (s2-1, int(settings.triangle_y1)), (255, 255, 255), 2)
        cv2.line(imgpart_Arclength_contour, (0, int(settings.triangle_y2)), (s2-1, int(settings.triangle_y2)), (255, 255, 255), 2)
        # plt.figure(figsize=(10, 10))
        # plt.imshow(imgpart_Arclength_contour)
        # plt.show()
        # plt.figure(figsize=(10, 10))
        # plt.imshow(imgrgb_reason)
        # plt.show()
        
        if settings.type_of_parts == "A" or settings.type_of_parts == "B":
            t_size, thickness = 2.5, 5
        else:
            t_size, thickness = 1.5, 3
        text = str(area)+'('+str(np.round(area*100/(settings.area_of_column/settings.num_of_section), decimals=1))+"%)"
        font = cv2.FONT_HERSHEY_SIMPLEX
        textsize = cv2.getTextSize(text, font, t_size, thickness)[0]
        textX = int((imgpart_Arclength_contour.shape[1] - textsize[0])/2)
        cv2.putText(imgpart_Arclength_contour, text, (int(textX), int(80)), cv2.FONT_HERSHEY_SIMPLEX, t_size, (0, 255, 255), thickness, cv2.LINE_AA)
        
        # plt.figure(figsize=(10, 10))
        # plt.imshow(imgpart_Arclength_contour)
        # plt.show()

        _file = (file.split("\\")[-1] if input_mode == "path" else file.split("/")[-1])
        if (JPG):
            # result_filename = file+"_"+name[i]+'_Arc.jpg'
            # cv2.imwrite(result_filename, imgpart_Arclength)
            result_filename = save_path + "/" + _file+"_"+name[i]+'_ArcContour.jpg'
            cv2.imwrite(result_filename, imgpart_Arclength_contour)
            # result_filename = file+"_"+name[i]+'ContourFull.jpg'
            # cv2.imwrite(result_filename, img_full)

            result_filename = save_path + "/" + _file+"_"+name[i]+'_Reason.jpg'
            cv2.imwrite(result_filename, imgrgb_reason)

        offset_list[i] = settings.offset
        final_imgrgba = Total_Defect_Img(offset_list[i], imgpart_Arclength_contour, text, final_imgrgba)
        
        s1, s2 = img256.shape
        cv2.rectangle(final_imgrgba, (0, 0), (s2-1, s1-1), (0,0,255,255), 3)
        # plt.figure(figsize=(10, 10))
        # plt.imshow(final_imgrgba)
        # plt.show()
        result_filename = save_path + "/" + _file+'_transparent.png'
        cv2.imwrite(result_filename, final_imgrgba)

        settings.ret_arclen.append(settings.arclen_list)
        settings.ret_area.append(area)
        settings.ret_errormessage.append("")
        print("================================")
        # except:
        #     print("Error in " + file + " " + name[i])
        #     settings.error.append(file)

    print(settings.ret_arclen)
    print(settings.ret_area)
    print(settings.ret_errormessage)
    # plt.figure(figsize=(10, 10))
    # plt.imshow(img256, cmap=plt.cm.binary, vmin=0, vmax=255)
    # plt.show()

    # ret_arclen = settings.ret_arclen
    # ret_area = settings.ret_area
    # max_len = 0
    # for i in range(3):
    #     for j in range(len(ret_arclen[i])):
    #         for k in range(len(ret_arclen[i][j])):
    #             if ret_arclen[i][j][k] > max_len:
    #                 max_len = ret_arclen[i][j][k]
    # area1, area2, area3 = ret_area[0], ret_area[1], ret_area[2]
    # print(max_len, area1, area2, area3)
    return settings.ret_arclen, settings.ret_area, settings.ret_errormessage
