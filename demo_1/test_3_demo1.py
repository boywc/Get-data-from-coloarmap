from Get_Data_from_Coloarmap import *

if __name__ == "__main__":
    data = np.load("./demo_1/data.npy")

    box_leftdown_real = [-180, -70] # x,y
    box_rightup_real = [180, 70]    # x,y


    #  find_data(data,
    # Lon,    经度
    # Lat,    纬度
    # box_leftdown_real,   数据左下角真实值
    # box_rightup_real,    数据右上角真实值
    # range_box = 2,       选取数据范围，像素上下左右 box框大小
    # draw_box=10,         绘制数据点，点大小
    # filter=0,            过滤无效值阈值，小于这个数的不参与计算
    # show=False           数据box展示

    draw_board = np.zeros_like(data, dtype=np.uint8)
    name = ["Apollo11", "Apollo16", "Apollo17", "CE5", "CE6"]
    input_Lon = np.array([23.47297,    15.51,      30.7717,     -51.916,  -153.998])
    input_Lat = np.array([0.67408,     -8.97,      20.1908,      43.058,   -41.625])
    for index, name_now in enumerate(name):
        out, draw = find_data(data, input_Lon[index], input_Lat[index], box_leftdown_real, box_rightup_real, range_box=5,filter=0, show=True)
        draw_board[draw[0]:draw[1], draw[2]:draw[3]] = 255

        print(name_now, "   ", out)

    cv2.imwrite("./demo_1/draw.jpg", draw_board)
