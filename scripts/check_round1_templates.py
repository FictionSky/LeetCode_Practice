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
    "int main()",
]

KINDS_WITH_EQUIVALENT_SAMPLE_DRIVER = {
    "bad_version",
    "guess_number",
    "listnode",
    "treenode",
    "graph_node",
}


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
        if (
            problem["kind"] not in KINDS_WITH_EQUIVALENT_SAMPLE_DRIVER
            and not problem["kind"].startswith("design_")
        ):
            required_cpp_tokens.append("runCase")

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
