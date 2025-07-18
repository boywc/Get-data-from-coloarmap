import cv2
import numpy as np
import cupy as cp
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.colors import BoundaryNorm

# 数据匹配         map       colorbar    color最小值      color最大值
def data_matching_cupy(box_data, box_cb, box_left_real_cb, box_right_real_cb):
    box_data = cp.asarray(box_data)
    box_cb = cp.asarray(box_cb)
    box_data_4d = cp.expand_dims(box_data, axis=-2)
    box_cb_4d = cp.reshape(box_cb, (1, 1, len(box_cb), 3))
    loss = box_data_4d - box_cb_4d
    loss = cp.sqrt(cp.sum(loss**2, axis=3))
    loss = cp.argmin(loss, axis=2)
    data = box_left_real_cb + loss * (box_right_real_cb-box_left_real_cb) / len(box_cb)
    data = cp.asnumpy(data)
    return data

# 数据匹配         map       colorbar    color最小值      color最大值
def data_matching(box_data, box_cb, box_left_real_cb, box_right_real_cb):
    box_data_4d = np.expand_dims(box_data, axis=-2)
    box_cb_4d = np.reshape(box_cb, (1, 1, len(box_cb), 3))
    loss = box_data_4d - box_cb_4d
    loss = np.sqrt(np.sum(loss**2, axis=3))
    loss = np.argmin(loss, axis=2)
    data = box_left_real_cb + loss * (box_right_real_cb-box_left_real_cb) / len(box_cb)
    return data

# 获取colorbar      路径        左下            右上           左侧最小值           右侧最大值
def get_colorbar(barname, box_leftdown_cb, box_rightup_cb, box_left_real_cb, box_right_real_cb, show=False):
    coloarbar_img = cv2.imread(barname)
    coloarbar_img = cv2.cvtColor(coloarbar_img, cv2.COLOR_BGR2RGB)
    box_cb = coloarbar_img[box_rightup_cb[1]:box_leftdown_cb[1], box_leftdown_cb[0]:box_rightup_cb[0], :]
    box_cb = box_cb.astype(np.float32)
    box_cb = np.mean(box_cb, axis=0)
    if show:
        print(box_cb.shape)
        box_cb_show = np.array([box_cb/255])
        plt.imshow(box_cb_show, extent = [box_left_real_cb, box_right_real_cb, 0, 1], aspect='auto')
        plt.show()
    return box_cb

# 获取colormap      路径        左下            右上           左下值           右上值
def get_colormap(dataname, box_leftdown, box_rightup, box_leftdown_real, box_rightup_real, show=False):
    data_img = cv2.imread(dataname)
    data_img = cv2.cvtColor(data_img, cv2.COLOR_BGR2RGB)
    box_data = data_img[box_rightup[1]:box_leftdown[1], box_leftdown[0]:box_rightup[0], :]
    box_data = box_data.astype(np.float32)
    if show:
        plt.imshow(box_data/255, extent = [box_leftdown_real[0], box_rightup_real[0], box_leftdown_real[1], box_rightup_real[1]])
        plt.show()
    return box_data

def cut_data(data_mat, block=20):
    split_arr_2d = np.array_split(data_mat, block, axis=1)
    return split_arr_2d

def data_matching_block_cupy(box_data, box_cb, box_left_real_cb, box_right_real_cb, block):
    list_block_data = cut_data(box_data, block=block)
    ii = 1
    data_list = []
    for i in list_block_data:
        data_red_block = data_matching_cupy(i, box_cb, box_left_real_cb, box_right_real_cb)
        data_list.append(data_red_block)
        print("\rFinish %d / %d "%(ii, block), end="")
        ii += 1
    zuhe = np.hstack(data_list)
    print("\n")
    print("Finish Matching")
    return zuhe

def data_matching_block(box_data, box_cb, box_left_real_cb, box_right_real_cb, block):
    list_block_data = cut_data(box_data, block=block)
    ii = 1
    data_list = []
    for i in list_block_data:
        data_red_block = data_matching(i, box_cb, box_left_real_cb, box_right_real_cb)
        data_list.append(data_red_block)
        print("\rFinish %d / %d "%(ii, block), end="")
        ii += 1
    zuhe = np.hstack(data_list)
    print("\n")
    print("Finish Matching")
    return zuhe

def display_get_data(cb, data, cb_min, cb_max, data_x_min, data_x_max, data_y_min, data_y_max):
    # 制作coloarbar
    custom_cmap = ListedColormap(cb/255)
    bounds = np.linspace(cb_min, cb_max, len(cb)+1)
    norm = BoundaryNorm(bounds, custom_cmap.N)

    fig, ax = plt.subplots()
    im = ax.imshow(data, cmap=custom_cmap, extent = [data_x_min, data_x_max, data_y_min, data_y_max])

    cbar = plt.colorbar(im)

    plt.show()

def find_data(data, Lon, Lat, box_leftdown_real, box_rightup_real, range_box = 2, draw_box=10, filter=0, show=False):
    h, w = data.shape

    h_re = (box_rightup_real[1] - box_leftdown_real[1]) / h
    w_re = (box_rightup_real[0] - box_leftdown_real[0]) / w

    Lon = box_rightup_real[0] + Lon
    w_inp = int(Lon / w_re)
    Lat = box_rightup_real[1] - Lat
    h_inp = int(Lat / h_re)

    box_data = data[h_inp-range_box:h_inp+range_box, w_inp-range_box:w_inp+range_box]
    range_box = draw_box
    if show:
        plt.imshow(box_data)
        plt.show()
    mask = box_data > filter
    return np.mean(box_data[mask]), [h_inp-range_box, h_inp+range_box, w_inp-range_box, w_inp+range_box]
