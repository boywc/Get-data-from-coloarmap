# Get-data-from-coloarmap

## 项目简介

**Get-data-from-coloarmap** 是一个基于 Python 的科研图片数值提取工具，专为论文、报告等热力图（colormap）和色标条（colorbar）图片还原出数值矩阵。适用于数据复用、学术复现、科学可视化等场景。

---

## 适用场景

- 学术论文、报告仅以图片形式发布的数据还原
- 热力图（colormap）、色标条（colorbar）自动批量提取
- 空间数据（如经纬度）与色值映射自动标定
- 标定点物理量插值与关系展示（如地表H值-热惯量曲线）

---

## 功能特点

- **图像数值还原**：输入图片和色标条，快速输出原始数据矩阵。
- **高性能支持**：CPU、GPU、分块计算全覆盖，支持大尺寸图片。
- **数据可视化**：一键展示数据分布、单点查询、物理量插值可视化。
- **灵活参数配置**：所有坐标、范围参数在代码中清晰自定义。

---

## 依赖环境

```bash
pip install numpy opencv-python matplotlib cupy scipy
````

> GPU 计算需 CUDA 环境，普通 CPU 环境无需特殊硬件。

---

## 目录结构

```
Get-data-from-coloarmap/
│
├── Get_Data_from_Coloarmap.py      # 主功能脚本，所有API均在此文件
├── README.md
│
├── demo_1/                         # 演示样例1（含图片、脚本、结果）
│   ├── colorbar.png
│   ├── data.npy
│   ├── draw.jpg
│   ├── jgre20757-fig-0007-m.jpg
│   ├── test_1_demo1.py
│   ├── test_2_demo1.py
│   ├── test_3_demo1.py
│   ├── trans.py                    # H值-热惯量插值与展示（样条拟合、定点推断）
│
├── demo_2/                         # 演示样例2（含图片、脚本、结果）
│   ├── colorbar.jpg
│   ├── data.jpg
│   ├── data.npy （建议通过网盘下载，见案例2说明）
│   ├── draw.jpg
│   ├── test_1_demo2.py
│   ├── test_2_demo2.py
│   └── test_3_demo2.py
```

---

## 操作流程

### 1. 数据提取

以 demo\_1、demo\_2 为例，运行如下命令：

```bash
python demo_1/test_1_demo1.py
# 或
python demo_2/test_1_demo2.py
```

* 支持四种提取方式（见脚本）：

  * 数据不切块 CPU 计算
  * 数据切块 CPU 计算
  * 数据不切块 GPU 计算
  * 数据切块 GPU 计算

**注意事项：**
请根据实际需求，**选取你想保存的那组数据**（如 demo\_1 中的 `get_data_1`，demo\_2 中的 `get_data_4`）。
需在脚本中加一句：

```python
get_data = get_data_4  # 或你选择的其他变量
np.save("./demo_2/data.npy", get_data)
```

否则会出现变量未定义错误。

所有参数说明（像素坐标、实际地理范围、色标条参数、分块大小等）均在脚本顶部注释，需根据你的图片实际情况调整。

---

### 2. 数据可视化

```bash
python demo_1/test_2_demo1.py
# 或
python demo_2/test_2_demo2.py
```

* 显示提取后数据与色标关系，便于直观验证和科学绘图。

---

### 3. 单点数值查询

```bash
python demo_1/test_3_demo1.py
# 或
python demo_2/test_3_demo2.py
```

* 支持以经纬度/空间坐标批量查询像元数值，支持区域统计、数据点标记（draw\.jpg）。

> 脚本内已示例多个点位自动查询与绘图，可自定义点位与统计范围。

---

### 4. 物理量插值与可视化

如需基于论文中的标定点，对地表 H 值与热惯量（Thermal Inertia）之间关系进行插值、推断或科学展示，可直接运行：

```bash
python demo_1/trans.py
```

* 输出：自动计算出指定着陆点 H 值对应的热惯量，并绘制 H-热惯量关系曲线与所有标记点。
* 结果可用于论文复现、地表物性分析等二次科研场景。

---

## 参数说明

所有参数（坐标、范围、色值）均可在各 demo 脚本内直接修改，无需单独配置文件。

* `box_leftdown`, `box_leftdown_real`：热力图左下角像素及对应实际坐标
* `box_rightup`, `box_rightup_real`：热力图右上角像素及对应实际坐标
* `box_leftdown_cb`, `box_left_real_cb`：色标条左端像素和实际值
* `box_rightup_cb`, `box_right_real_cb`：色标条右端像素和实际值
* `block`：分块处理参数（适用于大图或内存有限）

---

## API 参考

下列所有函数均在 `Get_Data_from_Coloarmap.py` 文件中：

| 函数名                             | 主要参数                                                                                                        | 说明                                  |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **get\_colormap**               | (dataname, box\_leftdown, box\_rightup, box\_leftdown\_real, box\_rightup\_real, show=False)                | 裁剪主图图片指定区域，返回像素色值阵列（RGB），支持坐标标定和可视化 |
| **get\_colorbar**               | (barname, box\_leftdown\_cb, box\_rightup\_cb, box\_left\_real\_cb, box\_right\_real\_cb, show=False)       | 读取色标条图片并提取色带，返回色标色值列表，支持显示          |
| **data\_matching**              | (box\_data, box\_cb, box\_left\_real\_cb, box\_right\_real\_cb)                                             | 主图阵列与色标进行匹配（CPU），输出主图数值阵列           |
| **data\_matching\_cupy**        | (box\_data, box\_cb, box\_left\_real\_cb, box\_right\_real\_cb)                                             | 同上，采用GPU（cupy）加速                    |
| **data\_matching\_block**       | (box\_data, box\_cb, box\_left\_real\_cb, box\_right\_real\_cb, block)                                      | 分块处理主图（CPU），适合大尺寸图像                 |
| **data\_matching\_block\_cupy** | (box\_data, box\_cb, box\_left\_real\_cb, box\_right\_real\_cb, block)                                      | 分块处理主图（GPU），适合大尺寸图像                 |
| **display\_get\_data**          | (cb, data, cb\_min, cb\_max, data\_x\_min, data\_x\_max, data\_y\_min, data\_y\_max)                        | 用主图实际坐标范围和色标，展示最终数值阵列与色带对应关系        |
| **find\_data**                  | (data, Lon, Lat, box\_leftdown\_real, box\_rightup\_real, range\_box=2, draw\_box=10, filter=0, show=False) | 查询主图上指定经纬度/坐标位置数值，支持小区域均值、显示和掩码绘制   |

---

## 案例参考

### 案例1

* 论文原图：[Global Regolith Thermophysical Properties of the Moon From the Diviner Lunar Radiometer Experiment](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2017JE005387)
* 热力图图片：`demo_1/jgre20757-fig-0007-m.jpg`
* 色标条图片：`demo_1/colorbar.png`
* H值-热惯量插值脚本：`demo_1/trans.py`（插值与可视化，支持定点推断与曲线展示）
* 参数详见 demo 脚本

### 案例2

* 论文原图：[A new global map of lunar surface chemical abundances from Chang’E-3 X-ray spectrometer](https://www.sciencedirect.com/science/article/pii/S0019103518300563)
* 热力图图片：`demo_2/data.jpg`
* 色标条图片：`demo_2/colorbar.jpg`
* **数据矩阵（data.npy）未包含在仓库内，如需体验完整流程，请从以下链接下载并放入 `demo_2/data.npy`：**
  [百度网盘下载地址（提取码: fc5f）](https://pan.baidu.com/s/1VR9TwGPiHDNkcVeeY0mpvg?pwd=fc5f)
* 参数详见 demo 脚本

> 其它热力图及色标条仅需更换图片，并同步更新坐标参数，即可复用。

---

## 常见问题

* **色标条需要横向、无刻度且左低右高吗？**

  * 是。建议预处理色标条，去除刻度、保持横向。
* **分块参数 block 的作用？**

  * 适合处理超大图片，防止内存溢出，加速处理。

---

## 贡献

欢迎通过 Issue 或 Pull Request 提交改进建议或新功能。若需适配特殊图像或增加新功能，欢迎联系作者交流。

---

## 许可协议

本项目基于 [MIT License](LICENSE) 开源。
请自由使用、修改和分发。

---

## 代码维护与联系

**主要维护人员：**

* GitHub: [Henry-Baiheng](https://github.com/Henry-Baiheng)
* 邮箱: [1243244190@qq.com](mailto:1243244190@qq.com)

**作者与项目仓库：**

* GitHub: [boywc](https://github.com/boywc)
* 邮箱: [liurenruis@gmail.com](mailto:liurenruis@gmail.com)
* 项目主页: [https://github.com/boywc/Get-data-from-coloarmap.git](https://github.com/boywc/Get-data-from-coloarmap.git)
* Git 克隆地址: `https://github.com/boywc/Get-data-from-coloarmap.git`

欢迎 Star、Fork 与使用本项目！如有问题或建议，欢迎通过 GitHub Issue 或邮件联系作者或维护者。

---
