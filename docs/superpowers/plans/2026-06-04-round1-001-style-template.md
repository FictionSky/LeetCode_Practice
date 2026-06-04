# Round 1 001-Style Template Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the 75 Round 1 LeetCode templates so every `md` and `cpp` file feels like `problems/001`: concrete problem notes, concrete examples, and local sample runs that only require the user to fill the algorithm body.

**Architecture:** Keep the existing `problems/<id>/<id>_<Title>.cpp` structure and reuse the current Python generator. Add Round 1 rich practice metadata, render concrete Markdown from it, render C++ sample drivers by return type and special problem kind, then regenerate only Round 1 with overwrite enabled.

**Tech Stack:** Python 3, Markdown, C++17, CMake, PowerShell

---

### Task 1: Add Round 1 Template Verification

**Files:**
- Create: `scripts/check_round1_templates.py`

- [ ] **Step 1: Create the verification script**

Create `scripts/check_round1_templates.py` with these checks:

```python
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_round1_templates import ROUND1_PROBLEMS, pascal_file_name, zero_pad


ROOT = Path(__file__).resolve().parents[1]
PROBLEMS_DIR = ROOT / "problems"

BAD_MD_PHRASES = [
    "TODO：从题目页面补一个有代表性的示例",
    "TODO：读题后把关键数据范围补在这里",
]

BAD_CPP_PHRASES = [
    "尚未执行真实样例",
    "请在补充测试后自行填写",
]

REQUIRED_MD_TOKENS = [
    "## 题目链接",
    "## 题目要求",
    "## 示例",
    "## 约束条件",
    "## 提示",
    "## 复杂度目标",
]

REQUIRED_CPP_TOKENS = [
    "TODO",
    "当前结果",
    "预期结果",
    "runCase",
    "int main()",
]


def expected_paths(problem):
    pid = zero_pad(problem["id"])
    cpp_name = f"{pid}_{pascal_file_name(problem['title'])}.cpp"
    return PROBLEMS_DIR / pid / f"{pid}.md", PROBLEMS_DIR / pid / cpp_name


def main():
    failures = []

    if len(ROUND1_PROBLEMS) != 75:
        failures.append(f"Round 1 metadata count should be 75, got {len(ROUND1_PROBLEMS)}")

    for problem in ROUND1_PROBLEMS:
        md_path, cpp_path = expected_paths(problem)
        if not md_path.exists():
            failures.append(f"Missing markdown: {md_path}")
            continue
        if not cpp_path.exists():
            failures.append(f"Missing C++ template: {cpp_path}")
            continue

        md_text = md_path.read_text(encoding="utf-8")
        cpp_text = cpp_path.read_text(encoding="utf-8")

        for token in REQUIRED_MD_TOKENS:
            if token not in md_text:
                failures.append(f"{md_path}: missing {token}")
        for phrase in BAD_MD_PHRASES:
            if phrase in md_text:
                failures.append(f"{md_path}: contains placeholder phrase {phrase}")

        required_cpp_tokens = list(REQUIRED_CPP_TOKENS)
        if problem["kind"].startswith("design_"):
            required_cpp_tokens.remove("runCase")

        for token in required_cpp_tokens:
            if token not in cpp_text:
                failures.append(f"{cpp_path}: missing {token}")
        for phrase in BAD_CPP_PHRASES:
            if phrase in cpp_text:
                failures.append(f"{cpp_path}: contains placeholder phrase {phrase}")

    if failures:
        print("Round 1 template verification failed:")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("Round 1 template verification passed.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the verification script before changes**

Run: `python scripts/check_round1_templates.py`

Expected: FAIL, because the current Round 1 generated files still contain placeholder Markdown and C++ output such as “尚未执行真实样例”.

- [ ] **Step 3: Commit the failing verification script**

Run:

```powershell
git add scripts/check_round1_templates.py
git commit -m "test: add round1 template verification"
```

Expected: commit succeeds and only `scripts/check_round1_templates.py` is included.

### Task 2: Upgrade Round 1 Metadata

**Files:**
- Modify: `scripts/generate_round1_templates.py`

- [ ] **Step 1: Add rich metadata fields**

Extend each `ROUND1_PROBLEMS` entry with these keys:

```python
{
    "summary": "给定一个整数数组 nums 和目标值 target，找出两个不同下标，使它们对应的数字之和等于 target。",
    "examples": [
        {
            "input": "nums = [2, 7, 11, 15], target = 9",
            "output": "[0, 1]",
            "explanation": "nums[0] + nums[1] = 2 + 7 = 9。",
        },
    ],
    "constraints": [
        "数组长度至少为 2。",
        "每个输入只需要返回任意一个有效答案。",
    ],
    "local_cases": [
        {
            "label": "示例 1",
            "args": [[2, 7, 11, 15], 9],
            "expected": [0, 1],
        },
    ],
}
```

Use concrete Chinese summaries and examples for all 75 Round 1 problems. Keep the existing `id`, `title`, `category`, `kind`, `return_type`, `method`, and `params` fields unchanged.

- [ ] **Step 2: Add mutation metadata for void problems**

For `344`, `283`, and `073`, add `mutates` so the renderer knows which argument to print after the call:

```python
"mutates": "s"
```

or:

```python
"mutates": "nums"
```

or:

```python
"mutates": "matrix"
```

- [ ] **Step 3: Add special local cases for non-standard kinds**

For special Round 1 kinds, use these local case shapes:

```python
# bad_version
{"label": "示例 1", "n": 5, "bad": 4, "expected": 4}

# guess_number
{"label": "示例 1", "n": 10, "secret": 6, "expected": 6}

# listnode with one list
{"label": "示例 1", "lists": [[1, 2, 3, 4, 5]], "expected": [5, 4, 3, 2, 1]}

# listnode with two lists
{"label": "示例 1", "lists": [[1, 2, 4], [1, 3, 4]], "expected": [1, 1, 2, 3, 4, 4]}

# linked list cycle
{"label": "示例 1", "values": [3, 2, 0, -4], "pos": 1, "expected": True}

# tree
{"label": "示例 1", "tree": ["3", "9", "20", "null", "null", "15", "7"], "expected": 3}

# design
{
    "operations": ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
    "inputs": [[], [-2], [0], [-3], [], [], [], []],
    "expected": ["null", "null", "null", "null", "-3", "null", "0", "-2"],
}
```

Expected: all Round 1 problems have enough data to render concrete Markdown and C++ local sample drivers.

### Task 3: Render Concrete Markdown

**Files:**
- Modify: `scripts/generate_round1_templates.py`

- [ ] **Step 1: Replace `build_md` with a concrete renderer**

Render Markdown from `summary`, `examples`, `constraints`, category hints, and complexity goal:

```python
def build_md(problem):
    guide = CATEGORY_GUIDANCE[problem["category"]]
    title = problem["title"]
    pid = zero_pad(problem["id"])
    url = f"https://leetcode.com/problems/{slugify(title)}/"

    examples = []
    for index, example in enumerate(problem["examples"], start=1):
        examples.append(
            f"### 示例 {index}\n\n"
            f"- 输入：`{example['input']}`\n"
            f"- 输出：`{example['output']}`\n"
            f"- 解释：{example['explanation']}"
        )

    constraints = "\n".join(f"- {item}" for item in problem["constraints"])
    hints = "\n".join(f"- {item}" for item in guide["hints"])

    return f"""# {problem['id']}. {title}

## 题目链接

- {url}

## 题目要求

{problem['summary']}

## 示例

{chr(10).join(examples)}

## 约束条件

{constraints}

## 推荐题型

- 主模式：`{guide['pattern']}`

## 提示

{hints}

## 复杂度目标

- {guide['complexity']}

## 本地练习清单

- 先完整读一遍原题。
- 再用自己的中文把题意复述一遍。
- 在 `{pid}_{pascal_file_name(title)}.cpp` 的 `TODO` 区域补全算法。
- 运行本地样例，对照“当前结果”和“预期结果”。
"""
```

- [ ] **Step 2: Verify Markdown generation for one problem**

Run: `python scripts/generate_round1_templates.py --overwrite`

Expected: `problems/020/020.md` contains a concrete Valid Parentheses example and no “从题目页面补一个有代表性的示例”.

### Task 4: Render C++ Sample Drivers

**Files:**
- Modify: `scripts/generate_round1_templates.py`

- [ ] **Step 1: Add C++ literal helpers**

Add helpers that turn Python sample data into C++ literals:

```python
def cpp_string(value):
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def cpp_bool(value):
    return "true" if value else "false"


def cpp_char(value):
    return "'" + value.replace("\\", "\\\\").replace("'", "\\'") + "'"


def cpp_literal(value, type_hint=None):
    if isinstance(value, bool):
        return cpp_bool(value)
    if isinstance(value, str):
        return cpp_string(value)
    if isinstance(value, float):
        return repr(value)
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        if type_hint == "vector<char>":
            return "{" + ", ".join(cpp_char(item) for item in value) + "}"
        return "{" + ", ".join(cpp_literal(item) for item in value) + "}"
    raise TypeError(f"Unsupported literal value: {value!r}")
```

- [ ] **Step 2: Add generic print helpers to generated C++**

Generate helpers for booleans, strings, numbers, `vector<T>`, and `vector<vector<T>>`:

```cpp
void printValue(bool value) {
    cout << (value ? "true" : "false");
}

template <typename T>
void printValue(const T& value) {
    cout << value;
}

template <typename T>
void printVector(const vector<T>& values) {
    cout << "[";
    for (size_t i = 0; i < values.size(); ++i) {
        printValue(values[i]);
        if (i + 1 < values.size()) {
            cout << ", ";
        }
    }
    cout << "]";
}

template <typename T>
void printValue(const vector<T>& values) {
    printVector(values);
}
```

- [ ] **Step 3: Replace `build_standard_main` with real `runCase` generation**

For non-void normal `Solution` methods, generate a typed `runCase`:

```cpp
void runCase(const string& label, /* typed params */, const ReturnType& expected) {
    Solution solution;
    auto actual = solution.method(/* args */);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}
```

For `void` methods, call the method and print the mutated parameter named by `problem["mutates"]`.

- [ ] **Step 4: Add special builders**

Keep separate renderers for:

- `bad_version`
- `guess_number`
- `listnode`
- `treenode`
- `graph_node`
- `design_minstack`
- `design_myqueue`
- `design_mystack`

Each builder must print concrete sample output with “当前结果” and “预期结果”.

### Task 5: Regenerate Round 1

**Files:**
- Modify generated files under `problems/<Round 1 id>/`

- [ ] **Step 1: Regenerate only Round 1**

Run: `python scripts/generate_round1_templates.py --overwrite`

Expected: Round 1 files are overwritten with concrete `001` style templates. Round 2 and Round 3 files are unchanged.

- [ ] **Step 2: Run structure verification**

Run: `python scripts/check_round1_templates.py`

Expected: PASS with `Round 1 template verification passed.`

- [ ] **Step 3: Confirm 75 Round 1 directories still exist**

Run:

```powershell
python -c "import sys; sys.path.insert(0, 'scripts'); from generate_round1_templates import ROUND1_PROBLEMS, zero_pad; from pathlib import Path; missing=[zero_pad(p['id']) for p in ROUND1_PROBLEMS if not (Path('problems')/zero_pad(p['id'])).exists()]; print(len(ROUND1_PROBLEMS), missing)"
```

Expected: prints `75 []`.

### Task 6: Build and Run Representative Targets

**Files:**
- Read: `CMakeLists.txt`
- Read generated Round 1 `cpp` files

- [ ] **Step 1: Reconfigure CMake**

Run: `cmake -S . -B build`

Expected: configure succeeds.

- [ ] **Step 2: Build representative targets**

Run:

```powershell
cmake --build build --target 020_ValidParentheses
cmake --build build --target 206_ReverseLinkedList
cmake --build build --target 104_MaximumDepthofBinaryTree
cmake --build build --target 133_CloneGraph
cmake --build build --target 155_MinStack
```

Expected: all five targets build successfully.

- [ ] **Step 3: Run representative targets**

Run:

```powershell
build/bin/020_ValidParentheses.exe
build/bin/206_ReverseLinkedList.exe
build/bin/104_MaximumDepthofBinaryTree.exe
build/bin/133_CloneGraph.exe
build/bin/155_MinStack.exe
```

Expected: each program prints concrete sample labels plus “当前结果” and “预期结果”.

### Task 7: Commit Round 1 Regeneration

**Files:**
- Modify: `scripts/generate_round1_templates.py`
- Create: `scripts/check_round1_templates.py`
- Modify generated Round 1 files under `problems/`

- [ ] **Step 1: Review changed files**

Run: `git status --short`

Expected: changes include the generator, verification script, and Round 1 generated files. Existing unrelated dirty files remain untouched unless they are part of this task.

- [ ] **Step 2: Commit implementation**

Run:

```powershell
git add scripts/generate_round1_templates.py scripts/check_round1_templates.py problems
git commit -m "feat: rebuild round1 practice templates"
```

Expected: commit succeeds with Round 1 template changes.
