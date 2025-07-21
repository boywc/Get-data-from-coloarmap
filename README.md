# Get-data-from-coloarmap

## 项目简介

**Get-data-from-coloarmap** 是一个基于 Python 的科研图片数值提取工具，专为论文、报告等热力图（colormap）和色标条（colorbar）图片还原出数值矩阵。适用于数据复用、学术复现、科学可视化等场景。

---

## 适用场景

- 学术论文、报告仅以图片形式发布的数据还原
- 热力图（colormap）、色标条（colorbar）自动批量提取
- 空间数据（如经纬度）与色值映射自动标定

---

## 功能特点

- **图像数值还原**：输入图片和色标条，快速输出原始数据矩阵。
- **高性能支持**：CPU、GPU、分块计算全覆盖。
- **数据可视化**：一键展示数据分布、单点查询。
- **灵活参数配置**：所有坐标、范围参数在代码中清晰自定义。

---

## 依赖环境

```bash
pip install numpy opencv-python matplotlib cupy
````

> GPU 计算需 CUDA 环境，普通 CPU 环境无需特殊硬件。

---

## 目录结构

```
Get-data-from-coloarmap/
│
├── Get_Data_from_Coloarmap.py      # 主功能脚本
├── README.md
│
├── demo_1/
│   ├── colorbar.png                # 色标条图片
│   ├── data.npy                    # 提取后保存的数据
│   ├── draw.jpg                    # 单点查询分布结果（test_3 生成）
│   ├── jgre20757-fig-0007-m.jpg    # 热力图原图
│   ├── test_1_demo1.py             # 数据提取脚本
│   ├── test_2_demo1.py             # 数据可视化脚本
│   └── test_3_demo1.py             # 单点数据查询脚本
│
├── demo_2/
│   ├── colorbar.jpg                # 色标条图片
│   ├── data.jpg                    # 热力图图片
│   ├── data.npy                    # 提取后保存的数据
│   ├── draw.jpg                    # 单点分布
│   ├── test_1_demo2.py
│   ├── test_2_demo2.py
│   └── test_3_demo2.py
│
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

## 参数说明

所有参数（坐标、范围、色值）均可在各 demo 脚本内直接修改，无需单独配置文件。

* `box_leftdown`, `box_leftdown_real`：热力图左下角像素及对应实际坐标
* `box_rightup`, `box_rightup_real`：热力图右上角像素及对应实际坐标
* `box_leftdown_cb`, `box_left_real_cb`：色标条左端像素和实际值
* `box_rightup_cb`, `box_right_real_cb`：色标条右端像素和实际值
* `block`：分块处理参数（适用于大图或内存有限）

---

## 案例参考

### 案例1

* 论文原图：[Global Regolith Thermophysical Properties of the Moon From the Diviner Lunar Radiometer Experiment](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2017JE005387)
* 热力图图片：`demo_1/jgre20757-fig-0007-m.jpg`
* 色标条图片：`demo_1/colorbar.png`
* 参数详见 demo 脚本

### 案例2

* 热力图图片：`demo_2/data.jpg`
* 色标条图片：`demo_2/colorbar.jpg`
* 其它参数详见 demo 脚本

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

本项目基于 MIT License 开源。请自由使用、修改和分发。

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
