from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_round1_templates import pascal_file_name, zero_pad
from leetcode_problem_bank import ROUND2_PROBLEMS, ROUND3_PROBLEMS


ROOT = Path(__file__).resolve().parents[1]
PROBLEMS_DIR = ROOT / "problems"

BAD_MD_PHRASES = [
    "TODO",
    "从题目页面补一个有代表性的示例",
    "读题后把关键数据范围补在这里",
    "先打开原题，确认输入、输出和有效答案的定义",
    "请从原题中选一个官方示例",
    "本模板只保留练习入口",
]

BAD_CPP_PHRASES = [
    "尚未执行真实样例",
    "请在补充测试后自行填写",
    "模板样例",
    "练习模板已加载",
    "补全 TODO 后再对照官方示例",
]

REQUIRED_MD_TOKENS = [
    "## 题目链接",
    "## 题目要求",
    "## 示例",
    "## 约束条件",
    "## 解题思路",
    "## 提示",
    "## 复杂度目标",
]

REQUIRED_CPP_TOKENS = [
    "TODO",
    "当前结果",
    "预期结果",
    "int main()",
]

KINDS_WITH_EQUIVALENT_SAMPLE_DRIVER = {
    "listnode",
    "treenode",
    "random_list_node",
    "nextnode_tree",
    "codec_tree",
}


def expected_paths(problem):
    pid = zero_pad(problem["id"])
    cpp_name = f"{pid}_{pascal_file_name(problem['title'])}.cpp"
    return PROBLEMS_DIR / pid / f"{pid}.md", PROBLEMS_DIR / pid / cpp_name


def check_problem(problem, failures):
    md_path, cpp_path = expected_paths(problem)
    if not md_path.exists():
        failures.append(f"Missing markdown: {md_path}")
        return
    if not cpp_path.exists():
        failures.append(f"Missing C++ template: {cpp_path}")
        return

    md_text = md_path.read_text(encoding="utf-8")
    cpp_text = cpp_path.read_text(encoding="utf-8")

    for key in ["summary", "examples", "constraints", "approach", "local_cases"]:
        if key not in problem:
            failures.append(f"{problem['id']}. {problem['title']}: missing practice data key {key}")
    if not problem.get("examples"):
        failures.append(f"{problem['id']}. {problem['title']}: examples must not be empty")
    if not problem.get("constraints"):
        failures.append(f"{problem['id']}. {problem['title']}: constraints must not be empty")
    if not problem.get("approach"):
        failures.append(f"{problem['id']}. {problem['title']}: approach must not be empty")
    if not problem.get("local_cases"):
        failures.append(f"{problem['id']}. {problem['title']}: local_cases must not be empty")

    for token in REQUIRED_MD_TOKENS:
        if token not in md_text:
            failures.append(f"{md_path}: missing {token}")
    if "### 示例 1" not in md_text:
        failures.append(f"{md_path}: missing concrete 示例 1 section")
    for phrase in BAD_MD_PHRASES:
        if phrase in md_text:
            failures.append(f"{md_path}: contains placeholder phrase {phrase}")

    required_cpp_tokens = list(REQUIRED_CPP_TOKENS)
    if (
        problem["kind"] not in KINDS_WITH_EQUIVALENT_SAMPLE_DRIVER
        and not problem["kind"].startswith("design_")
    ):
        required_cpp_tokens.append("runCase")

    for token in required_cpp_tokens:
        if token not in cpp_text:
            failures.append(f"{cpp_path}: missing {token}")
    if "示例 1" not in cpp_text:
        failures.append(f"{cpp_path}: missing concrete local 示例 1 driver")
    for phrase in BAD_CPP_PHRASES:
        if phrase in cpp_text:
            failures.append(f"{cpp_path}: contains placeholder phrase {phrase}")


def main():
    failures = []

    if len(ROUND2_PROBLEMS) != 100:
        failures.append(f"Round 2 metadata count should be 100, got {len(ROUND2_PROBLEMS)}")
    if len(ROUND3_PROBLEMS) != 100:
        failures.append(f"Round 3 metadata count should be 100, got {len(ROUND3_PROBLEMS)}")

    for problem in ROUND2_PROBLEMS + ROUND3_PROBLEMS:
        check_problem(problem, failures)

    if failures:
        print("Round 2/3 template verification failed:")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("Round 2/3 template verification passed.")


if __name__ == "__main__":
    main()
