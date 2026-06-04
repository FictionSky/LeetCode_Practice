# Round 1 Template Batch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为 Round 1 的 75 道题在 `problems/` 下生成统一的 Markdown 说明文件和未作答 C++ 练习模板。

**Architecture:** 使用一份 Round 1 题目元数据作为唯一来源，通过统一模板批量生成 `problems/<题号>/<题号>.md` 和 `problems/<题号>/<题号>_<题目名>.cpp`。保留现有 `001` 模板，不处理 `002`。

**Tech Stack:** Markdown, C++17, PowerShell, CMake

---

### Task 1: Define Round 1 metadata source

**Files:**
- Create: `docs/superpowers/specs/2026-06-04-round1-template-batch-design.md`
- Create: `docs/superpowers/plans/2026-06-04-round1-template-batch.md`

- [ ] **Step 1: Confirm the Round 1 source list**

Use: `docs/leetcode-3-round-plan.md`

Expected: 75 Round 1 problems are the source of truth for IDs and titles.

- [ ] **Step 2: Keep the naming convention fixed**

Convention:

```text
problems/020/020.md
problems/020/020_ValidParentheses.cpp
```

### Task 2: Generate Round 1 folders and files

**Files:**
- Create: `problems/003/003.md`
- Create: `problems/003/003_LongestSubstringWithoutRepeatingCharacters.cpp`
- Create: `problems/011/011.md`
- Create: `problems/011/011_ContainerWithMostWater.cpp`
- Create: `...`
- Preserve: `problems/001/001.md`
- Preserve: `problems/001/001_TwoSum.cpp`

- [ ] **Step 1: Create one folder per Round 1 problem**

Each folder name must be a zero-padded three-digit problem ID.

- [ ] **Step 2: Create one Markdown file per Round 1 problem**

Each Markdown file must contain:

- title
- problem statement
- examples
- constraints
- hints
- complexity target

- [ ] **Step 3: Create one unsolved C++ template per Round 1 problem**

Each C++ template must contain:

- `Solution` class
- target method signature
- `TODO` block for user code
- helper print function if needed
- local `main`
- sample output comparing current vs expected

### Task 3: Verify generated structure and build integration

**Files:**
- Modify: `CMakeLists.txt` only if required by integration

- [ ] **Step 1: Verify problem folders exist**

Run: `Get-ChildItem problems`
Expected: Round 1 folders exist under `problems/`

- [ ] **Step 2: Verify representative files exist**

Run examples:

```powershell
Get-ChildItem problems/020
Get-ChildItem problems/217
Get-ChildItem problems/704
```

Expected: each folder contains one `md` and one `cpp`

- [ ] **Step 3: Re-run CMake configure**

Run: `cmake -S . -B build`
Expected: configure succeeds

- [ ] **Step 4: Build one representative target**

Run: `cmake --build build --target 020_ValidParentheses`
Expected: build succeeds

- [ ] **Step 5: Run the representative target**

Run: `build/bin/020_ValidParentheses.exe`
Expected: program runs and shows an unfinished-template style output

