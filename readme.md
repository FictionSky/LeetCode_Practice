# LeetCode C++ Practice

这个仓库用于按题号整理 LeetCode C++ 练习，并通过 CMake 做本地编译与运行。

## 环境

- 语言标准：`C++17`
- 构建工具：`CMake 3.12+`
- 编译器：`MinGW-w64 / GCC`
- 编辑器：`VSCode`

## 目录结构

所有题目统一放在 `problems/` 下，避免根目录随着题量增加变得混乱。

```text
LeetCode_Practice/
├── .gitignore
├── CMakeLists.txt
├── readme.md
├── problems/
│   ├── 001/
│   │   ├── 001.md
│   │   └── 001_TwoSum.cpp
│   ├── 002/
│   │   ├── 002.md
│   │   └── 002_AddTwoNumbers.cpp
│   └── ...
└── docs/
```

## 模板规则

每道题通常包含两个文件：

- 一个 `md` 文件，记录中文题目说明、提示和复杂度目标
- 一个 `cpp` 文件，作为本地练习模板

练习模板遵循下面的规则：

- 保留 `Solution` 签名，或题目要求的设计类名称
- 保留本地 `main`
- 注释使用中文，明确告诉你应该在哪里写代码
- 运行输出使用中文，方便你直接看本地测试结果
- 不直接提供最终可提交答案

## 构建

先配置：

```bash
cmake -S . -B build
```

构建单题：

```bash
cmake --build build --target 001_TwoSum
```

运行：

```bash
build/bin/001_TwoSum.exe
```
