import cv2
import numpy as np

# 将左上右下表示的框转换为中心点坐标和宽高表示的框
def xyxy_to_xywh(xyxy):
    center_x = (xyxy[0] + xyxy[2]) / 2
    center_y = (xyxy[1] + xyxy[3]) / 2
    w = xyxy[2] - xyxy[0]
    h = xyxy[3] - xyxy[1]
    return (center_x, center_y, w, h)


# 在图像上绘制一个框
def plot_one_box(xyxy, img, color=(0, 200, 0), target=False):
    xy1 = (int(xyxy[0]), int(xyxy[1]))
    xy2 = (int(xyxy[2]), int(xyxy[3]))
    if target:
        color = (0, 0, 255)
    cv2.rectangle(img, xy1, xy2, color, 1, cv2.LINE_AA)  # filled


# 计算IOU（交并比）
def cal_iou(box1, box2):
    """

    :param box1: xyxy 左上右下
    :param box2: xyxy
    :return:
    """
    x1min, y1min, x1max, y1max = box1[0], box1[1], box1[2], box1[3]
    x2min, y2min, x2max, y2max = box2[0], box2[1], box2[2], box2[3]
    # 计算两个框的面积
    s1 = (y1max - y1min + 1.) * (x1max - x1min + 1.)
    s2 = (y2max - y2min + 1.) * (x2max - x2min + 1.)

    # 计算相交部分的坐标
    xmin = max(x1min, x2min)
    ymin = max(y1min, y2min)
    xmax = min(x1max, x2max)
    ymax = min(y1max, y2max)

    inter_h = max(ymax - ymin + 1, 0)
    inter_w = max(xmax - xmin + 1, 0)

    intersection = inter_h * inter_w
    union = s1 + s2 - intersection

    # 计算iou
    iou = intersection / union
    return iou


# 将中心点坐标和宽高表示的框转换为左上右下表示的框
def xywh_to_xyxy(xywh):
    x1 = xywh[0] - xywh[2] // 2
    y1 = xywh[1] - xywh[3] // 2
    x2 = xywh[0] + xywh[2] // 2
    y2 = xywh[1] + xywh[3] // 2

    return [x1, y1, x2, y2]


# 计算框1和框2的IOU
if __name__ == "__main__":
    box1 = [100, 100, 200, 200]
    box2 = [100, 100, 200, 300]
    iou = cal_iou(box1, box2)
    print(iou)
    # 修改框1的值
    box1.pop(0)
    box1.append(555)
    print(box1)
    print(np.eye(6) * 0.1)
