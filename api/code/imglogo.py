# import cv2
# import base64
# # from ultralytics import YOLO
# import torch
# from yolov7.models.experimental import attempt_load

# from utils.general import non_max_suppression

# def getImgPred(ing_data):
#     model = attempt_load('api/code/best.pt')
#     img_file = 'temp.jpg'
#     with open(img_file,'wb') as f:
#         f.write(base64.b64decode(img_data))
#     img = cv2.imread('temp.jpg')
#     result=model.predict(source=img,save=True)
#     print(result)
    