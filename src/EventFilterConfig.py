#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import logging


CAMERANAME = "cameraName"
CAMERASN = "cameraSn"
CAMERACODE = "cameraCode"
CAMERAIP = "cameraIp"
fieldnames = [CAMERANAME, CAMERACODE, CAMERASN, CAMERAIP]
# 非机房相机
def get_stranger_camera():
    strange_cameras = []
    try:
        with open("./camerasn.csv", newline="",encoding="utf-8") as csvfile:
            camera_info = csv.DictReader(csvfile, fieldnames= fieldnames)
            for c in camera_info:
                camera_sn = c[CAMERASN]
                if camera_sn == CAMERASN:
                    continue
                strange_cameras.append(camera_sn)
        logging.info("get stranger camera succeed")
    except Exception as e:
        logging.error(f"get stranger camera error {str(e)}")
    return strange_cameras


StrangerCameras = get_stranger_camera()

print(f"stranger cameras: {StrangerCameras}")


# with open('../vendor/Ivs3800/camerasn.csv', 'w', newline='') as csvfile:
#     fieldnames = ['cameraName', 'cameraCode', 'cameraSn', "cameraIp"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'cameraSn': '03860032935110120000', 'cameraName': '11#RF东侧电梯厅出入口1', 'cameraIp': "84.11.17.4", 'cameraCode':"03860032935110120000#039a38a858a9404492fefd76c68884c0"})
