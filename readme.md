# LeetCode C++ Practice

这个仓库用于按题号整理 LeetCode C++ 练习，并通过 CMake 做本地编译、运行和调试。

## 环境

- 语言标准：`C++17`
- 构建工具：`CMake 3.12+`
- 编译器：`MinGW-w64 / GCC`
- 编辑器：`VSCode`

## 目录结构

所有题目统一放在 `problems/` 下，避免根目录随着题量增加变得混乱。

```text
LeetCode_Practice/
|- CMakeLists.txt
|- readme.md
|- lc.cmd
|- ld.cmd
|- problems/
|  |- 001/
|  |  |- 001.md
|  |  `- 001_TwoSum.cpp
|  |- 002/
|  |  |- 002.md
|  |  `- 002_AddTwoNumbers.cpp
|  `- ...
`- scripts/
```

## 模板规则

每道题通常包含两个文件：

- 一个 `md` 文件，记录题目说明、示例、约束、提示和解题思路
- 一个 `cpp` 文件，作为本地练习模板

练习模板遵循这些规则：

- 保留 `Solution` 签名，或题目要求的设计类名称
- 保留本地 `main`
- 注释使用中文，明确告诉你应该在哪里补代码
- 运行输出使用中文，方便直接看本地测试结果
- 不直接提供最终可提交答案

## 快速运行单题

写好某题代码后，在项目根目录直接运行：

```powershell
.\lc 1
.\lc 14
.\lc 146
```

也可以输入完整三位题号：

```powershell
.\lc 001
.\lc 014
```

`lc.cmd` 会调用 `scripts/lc_runner.ps1`，自动根据题号找到 `problems/<题号>/` 下唯一的 `.cpp` 文件，执行 `cmake --build build --target <目标名>`，然后运行 `build/bin/<目标名>.exe`。如果 `build/` 还没有配置，它会先自动执行 `cmake -S . -B build`。

例如：

```powershell
.\lc 14
```

等价于：

```powershell
cmake --build build --target 014_LongestCommonPrefix
.\build\bin\014_LongestCommonPrefix.exe
```

运行后对照输出中的 `当前结果` 和 `预期结果`。

## VSCode 断点调试单题

如果你想在源码里自己打断点，然后用 VSCode 的 `F5` 调试当前题目，可以在项目根目录执行：

```powershell
.\ld 1
.\ld 14
.\ld 146
```

`ld.cmd` 会调用 `scripts/ld_runner.ps1`，自动完成这些事情：

- 找到对应题目的 `.cpp`
- 构建对应的 CMake target
- 生成或更新 `.vscode/launch.json`
- 生成或更新 `.vscode/tasks.json`
- 用 VSCode 打开这道题的源码文件

例如：

```powershell
.\ld 14
```

执行后，你只需要：

1. 在这道题的 `.cpp` 里打断点
2. 回到 VSCode
3. 直接按 `F5`

这样启动的就是当前这道题对应的调试程序，不需要自己再手动切 target。

## 手动构建与运行

先配置：

```powershell
cmake -S . -B build
```

构建单题：

```powershell
cmake --build build --target 001_TwoSum
```

运行：

```powershell
.\build\bin\001_TwoSum.exe
```
