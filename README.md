# Get-data-from-coloarmap

## 项目简介

**Get-data-from-coloarmap** 是一个基于Python的图像数据提取工具，专门用于从科学论文或报告中的热力图（colormap）与颜色条（colorbar）中精准提取数值数据。项目旨在帮助用户快速有效地获得难以直接访问的原始数据，提升数据分析效率。

---

## 功能特点

* **图像数据提取**：从colormap和colorbar图片中精准地提取数据。
* **多种计算方式支持**：

  * CPU/GPU计算切换
  * 数据分块/非分块计算
* **数据可视化**：

  * 直观展示提取结果
  * 可选单点数据查询与可视化

---

## 依赖环境

```bash
pip install numpy opencv-python matplotlib cupy
```

**注：** GPU计算需要支持CUDA的显卡和相应驱动。

---

## 文件结构

```
Get-data-from-coloarmap
│
├── Get_Data_from_Coloarmap.py       # 核心功能实现
├── demo_1
│   ├── test_1_demo1.py              # Demo 1数据提取脚本
│   ├── test_2_demo1.py              # Demo 1数据展示脚本
│   ├── test_3_demo1.py              # Demo 1单点数据提取脚本
│   └── data.npy                     # 提取后的数据文件
│
└── demo_2
    ├── test_1_demo2.py              # Demo 2数据提取脚本
    ├── test_2_demo2.py              # Demo 2数据展示脚本
    ├── test_3_demo2.py              # Demo 2单点数据提取脚本
    └── data.npy                     # 提取后的数据文件
```

---

## 使用方法

### 1. 提取数据

运行`test_1_demoX.py`进行数据提取，支持多种计算模式。

```bash
python test_1_demo1.py
```

### 2. 显示数据

运行`test_2_demoX.py`可视化已提取的数据。

```bash
python test_2_demo1.py
```

### 3. 单点数据查询

运行`test_3_demoX.py`可进行特定经纬度数据提取。

```bash
python test_3_demo1.py
```

---

## 示例说明

* **Demo 1** 来源于论文：[Global Regolith Thermophysical Properties of the Moon From the Diviner Lunar Radiometer Experiment](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2017JE005387)
* **Demo 2** 可用于类似图像的数据提取与分析。

---

## 贡献

欢迎提交Issue或Pull Request共同完善项目。

---

## 许可证

本项目基于MIT许可协议。

---

## 许可协议

本项目基于 MIT License 开源。 请自由使用、修改和分发。

## 代码维护与联系

**主要维护人员：**

* GitHub: [Henry-Baiheng](https://github.com/Henry-Baiheng)
* 邮箱: [1243244190@qq.com](mailto:1243244190@qq.com)

**作者与项目仓库：**

* GitHub: [boywc](https://github.com/boywc)
* 邮箱: [liurenruis@gmail.com](mailto:liurenruis@gmail.com)
* 项目主页: [Get-data-from-coloarmap](https://github.com/boywc/Get-data-from-coloarmap.git)
* Git 克隆地址: `https://github.com/boywc/Get-data-from-coloarmap.git`

欢迎 Star、Fork 与使用本项目！如有问题或建议，欢迎通过 GitHub Issue 或邮件联系作者或维护者。
