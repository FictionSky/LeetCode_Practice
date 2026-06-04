# LeetCode Problem Template Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为 `problems/001` 建立统一的题目说明文件和“未作答但可本地运行”的 C++ 练习模板，并验证可以编译运行。

**Architecture:** 在 `problems/001` 目录下保留一个 `001.md` 记录题目信息，同时将 `001_TwoSum.cpp` 调整为标准的 `Solution + main` 练习版。`Solution` 中只保留函数签名、必要注释和 `TODO`，真正的算法由用户自己填写。

**Tech Stack:** Markdown, C++17, CMake

---

### Task 1: Add problem statement document

**Files:**
- Create: `problems/001/001.md`

- [ ] **Step 1: Create the markdown file with the problem summary**

The file should include:

- problem description
- examples
- constraints
- hints instead of full answer
- complexity target

- [ ] **Step 2: Verify the file exists**

Run: `Get-ChildItem problems/001`
Expected: shows `001.md`

### Task 2: Replace the C++ file with an unsolved local practice template

**Files:**
- Modify: `problems/001/001_TwoSum.cpp`

- [ ] **Step 1: Define the expected template behavior**

The source file should:

- compile successfully
- keep `Solution::twoSum`
- keep `main`
- not contain the final algorithm answer
- include comments showing where the user should write code

- [ ] **Step 2: Replace the file with a commented template**

The file should include:

- headers
- empty or placeholder implementation in `twoSum`
- `TODO` comment in the answer area
- helper for printing vectors
- sample cases in `main`
- output showing current result and expected result

- [ ] **Step 3: Build and run the program**

Run: `cmake --build build --target 001_TwoSum` and then run `build/bin/001_TwoSum.exe`
Expected: build succeeds, program runs, and output makes it obvious that the answer area is still unfinished.
