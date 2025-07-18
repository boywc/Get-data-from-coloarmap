from Get_Data_from_Coloarmap import *

if __name__ == "__main__":
    # 读取colormap
    box_leftdown = [476, 5117]        # x,y
    box_leftdown_real = [-180, -60] # x,y
    box_rightup = [14868, 325]       # x,y
    box_rightup_real = [180, 60]    # x,y

    box_data = get_colormap("./demo_2/data.jpg", box_leftdown, box_rightup, box_leftdown_real, box_rightup_real, True)

    # 读取coloarbar
    box_leftdown_cb = [533, 217]        # x,y
    box_left_real_cb = 0.0
    box_rightup_cb = [5025, 78]       # x,y
    box_right_real_cb = 0.8
    box_cb = get_colorbar("./demo_2/colorbar.jpg", box_leftdown_cb, box_rightup_cb, box_left_real_cb, box_right_real_cb, True)

    block = 10000
    # 四个解决方案案例
    # 数据不切块CPU计算
    # print("run1")
    # get_data_1 = data_matching(box_data, box_cb, box_left_real_cb, box_right_real_cb)
    # # 数据切块CPU计算
    # print("run2")
    # get_data_2 = data_matching_block(box_data, box_cb, box_left_real_cb, box_right_real_cb, block)
    # # 数据不切块GPU计算
    # print("run3")
    # get_data_3 = data_matching_cupy(box_data, box_cb, box_left_real_cb, box_right_real_cb)
    # 数据切块GPU计算
    print("run4")
    get_data_4 = data_matching_block_cupy(box_data, box_cb, box_left_real_cb, box_right_real_cb, block)
    print(get_data_1.shape, get_data_2.shape, get_data_3.shape, get_data_4.shape)
    # 保存match数据
    print("开始保存")
    np.save("./demo_2/data.npy", get_data)
    print("保存成功")
