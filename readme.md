# LeetCode C++ 算法练习笔记 🚀

本项目用于记录我在 LeetCode 上的算法练习过程。采用 C++ 语言实现，并利用 CMake 构建系统进行本地管理与调试。

## 🛠️ 环境配置

- **语言标准**: C++ 17
- **构建工具**: CMake (3.12+)
- **编译器**: MinGW-w64 (GCC 8.1.0+)
- **编辑器**: VSCode

## 📂 项目结构

本项目采用自动扫描机制，可以直接在根目录或子目录下添加 `.cpp` 文件：

```text
LeetCode_Practice/
├── .gitignore           # 忽略 build、exe 等无用文件
├── CMakeLists.txt       # 核心构建配置文件
├── README.md            # 项目说明文档
├── 001/                 # 按题号分类
│   └── 001_TwoSum.cpp
└── 002/
    └── 002_AddTwoNumbers.cpp