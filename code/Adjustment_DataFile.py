import os
import cv2
import numpy as np
from PIL import Image
from shutil import copy
import os
import os.path as osp
import time

def tiff_png(path, path1):
    im = Image.open(path+path1)
    im.save(path+".png")
    os.remove(path+path1)

def load_img_labelme_json(count, imglist):
    ImageFile_dir = '../images_mj'
    if not os.path.exists(ImageFile_dir):
        print('-'*100+'\n'+'Create new folder')
        os.mkdir(ImageFile_dir)
    dir1_con = "../images_mj/mahjong_setting_con" 
    dir1_res = "../images_mj/mahjong_setting_res" 
    dir1_con_res = "../images_mj/mahjong_setting_con_res"
    txt_file = "../images_mj/Txt_File"

    if not os.path.exists(txt_file):
        print('-'*100+'Create new folder')
        os.mkdir(txt_file)

    dir1_con_txt = "../images_mj/Txt_File/con_txt" 
    dir1_res_txt = "../images_mj/Txt_File/res_txt" 
    dir1_con_res_txt = "../images_mj/Txt_File/con_res_txt"

    if not os.path.exists(dir1_con):
        print('-'*100+'\n'+'Create new folder')
        os.mkdir(dir1_con)
    if not os.path.exists(dir1_res):
        print('-'*100+'\n'+'Create new folder')
        os.mkdir(dir1_res)
    if not os.path.exists(dir1_con_res):
        print('-'*100+'\n'+'Create new folder')
        os.mkdir(dir1_con_res)
    if not os.path.exists(dir1_con_txt):
        print('-'*100+'\n'+'Create new folder')
        os.mkdir(dir1_con_txt)
    if not os.path.exists(dir1_res_txt):
        print('-'*100+'\n'+'Create new folder')
        os.mkdir(dir1_res_txt)
    if not os.path.exists(dir1_con_res_txt):
        print('-'*100+'\n'+'Create new folder')
        os.mkdir(dir1_con_res_txt)

    for i in range(count):
        img_path = dataset_root_path
        filestr = imglist[i].split(".")[0]
        # print(f'filestr {filestr}')
        file_filter = imglist[i].split(".")
        if file_filter[1] == 'jpg':
            img_path_json = img_path + filestr + ".jpg"
            img = cv2.imread(img_path_json)
            # print(img)
            
            if img is not None:
                start = time.process_time()
                # contrast = 200
                # brightness = 0
                # output = img * (contrast/127 + 1) - contrast + brightness
                # output = np.clip(output, 0, 255)
                # output = np.uint8(output)
                
                
                filename = filestr + "v1" + ".jpg"
                filename2 = filestr + "v2" + ".jpg"
                filename3 = filestr + "v3" + ".jpg"
                path_1 = "../images_mj/mahjong_setting_res/" + filename
                path_2 = "../images_mj/mahjong_setting_con/" + filename2
                path_3 = "../images_mj/mahjong_setting_con_res/" + filename3
                if not os.path.exists(path_1) or not os.path.exists(path_2) or not os.path.exists(path_3):
                    # path_2 = img_path+".jpg"
                    # cv2.imwrite(path_1, output)
                    res1 = np.uint8(np.clip((cv2.add(1*img,30)), 0, 255))
                    con1 = np.uint8(np.clip((cv2.add(1.5*res1,0)), 0, 255))
                    res_con = np.uint8(np.clip((cv2.add(1.5*img,30)), 0, 255))
                    cv2.imwrite(path_1, con1)
                    cv2.imwrite(path_2, res1)
                    cv2.imwrite(path_3, res_con)
                    end = time.process_time()
                    print('Time['+ str(i) +']' + ': '  + "執行時間：%f 秒" % (end - start)+", Adjustment Finish")
                else:
                    print(f'file exits')
            else:
                pass
            
        elif file_filter[1] == 'txt' and file_filter[0] != 'classes':
            start = time.process_time()
            filename = filestr + "v1" + ".txt"
            filename2 = filestr + "v2" + ".txt"
            filename3 = filestr + "v3" + ".txt"
            path_1 = "../images_mj/Txt_File/res_txt/" + filename
            path_2 = "../images_mj/Txt_File/con_txt/" + filename2
            path_3 = "../images_mj/Txt_File/con_res_txt/" + filename3
            if not os.path.exists(path_1) or not os.path.exists(path_2) or not os.path.exists(path_3):
                copy(dataset_root_path+filestr+".txt", path_1)
                copy(dataset_root_path+filestr+".txt", path_2)
                copy(dataset_root_path+filestr+".txt", path_3)
            else:
                    print(f'file exits')
            end = time.process_time()
            print('Time['+ str(i) +']' + ': '  + "執行時間：%f 秒" % (end - start)+", /Copy Finish\ ")
        else:
            pass

        
        
        # print(cnt)

        #增加亮度
        # res1 = np.uint8(np.clip((cv2.add(1*img,30)), 0, 255))
        # res2 = np.uint8(np.clip((cv2.add(1*img2,30)), 0, 255))


        #增加對比度
        # con1 = np.uint8(np.clip((cv2.add(1.5*img,0)), 0, 255))
        # con2 = np.uint8(np.clip((cv2.add(1.5*img2,0)), 0, 255))

        #輸出圖片
        # cv2.imwrite(f'{img}/labelme_json/test/{filestr}_res1.png',res1)
        # cv2.imwrite(f'{img}/labelme_json/test/{filestr}_res2.png',res2)
        # cv2.imwrite(f'{img}/labelme_json/test/{filestr}_con1.png',con1)
        # cv2.imwrite(f'{img}/labelme_json/test/{filestr}_con2.png',con2)





# def load_img_pic(count, imglist):
#     for i in range(count):
        
#         img = dataset_root_path
#         # print(imglist[i].split("."))
#         if "tif" in imglist[i]:
#             filestr = imglist[i].split(".")[0]
#             img_path_pic = img + "pic/" + filestr + ".tif"
#             img2 = cv2.imread(img_path_pic, 3)
#             if img2 is not None:
#                 path_2 = img+"pic/test/"+filestr+"_res1_con1.png"
#                 #增加亮度
#                 res1 = np.uint8(np.clip((cv2.add(1*img2,30)), 0, 255))
#                 #增加對比度
#                 con1 = np.uint8(np.clip((cv2.add(1.5*res1,0)), 0, 255))
#                 cv2.imwrite(path_2, con1)
#             else:
#                 pass
#         else:

#             filestr = imglist[i].split(".")[0]
#             img_path_pic = img + "pic/" + filestr + ".png"
#             img2 = cv2.imread(img_path_pic)
            
#             if img2 is not None:
#                 # contrast = 200
#                 # brightness = 0
#                 # output = img2 * (contrast/127 + 1) - contrast + brightness
#                 # output = np.clip(output, 0, 255)
#                 # output = np.uint8(output)
#                 path_2 = img+"pic/test/"+filestr+"_res1_con1.png"
#                 filename = filestr+".png"
#                 # cv2.imwrite(path_2,output)
#                 #增加亮度
#                 res1 = np.uint8(np.clip((cv2.add(1*img2,30)), 0, 255))

#                 #增加對比度
#                 con1 = np.uint8(np.clip((cv2.add(1.5*res1,0)), 0, 255))
#             cv2.imwrite(path_2, con1)
        
# 基础设置
dataset_root_path = "../data_labeled/"
img_floder = dataset_root_path
# mask_floder = dataset_root_path + "cv2_mask"
# yaml_floder = dataset_root_path
try:
    imglist = os.listdir(img_floder)
except FileNotFoundError:
    dataset_root_path = "data_labeled"
    img_floder = dataset_root_path
    imglist = os.listdir(img_floder)
    print(imglist)
# print(f'imglist : {imglist}')
count = len(imglist)

# print(imglist)
# print(count)

#lunch the program

Tot_start = time.process_time()
load_img_labelme_json(count, imglist)
# load_img_pic(count, imglist)
Tot_end = time.process_time()
print('Total Program Processing Time' + ' -> '  + "執行時間：%f 秒" % (Tot_end - Tot_start)+", Done")

