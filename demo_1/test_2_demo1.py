from Get_Data_from_Coloarmap import *

if __name__ == "__main__":

    # 读取coloarbar
    box_leftdown_cb = [20, 40]        # x,y
    box_left_real_cb = 0.02
    box_rightup_cb = [780, 30]       # x,y
    box_right_real_cb = 0.09
    box_cb = get_colorbar("./demo_1/colorbar.png", box_leftdown_cb, box_rightup_cb, box_left_real_cb, box_right_real_cb, True)

    # 读取保存数据
    data = np.load("./demo_1/data.npy")

    box_leftdown_real = [-180, -70] # x,y
    box_rightup_real = [180, 70]    # x,y

    # 显示保存数据
    display_get_data(box_cb, data, box_left_real_cb, box_right_real_cb, box_leftdown_real[0], box_rightup_real[0], box_leftdown_real[1], box_rightup_real[1])
