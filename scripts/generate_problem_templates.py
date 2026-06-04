import sys

from generate_round1_templates import (
    PROBLEMS_DIR,
    ROUND1_PROBLEMS,
    build_cpp,
    build_md,
    pascal_file_name,
    zero_pad,
)
from leetcode_problem_bank import ROUND2_PROBLEMS, ROUND3_PROBLEMS


ALL_PROBLEMS_BY_ROUND = {
    "round1": ROUND1_PROBLEMS,
    "round2": ROUND2_PROBLEMS,
    "round3": ROUND3_PROBLEMS,
}


def normalize_round_names(argv):
    filtered = [arg for arg in argv if arg != "--overwrite"]
    if not filtered or filtered == ["all"]:
        return ["round1", "round2", "round3"]

    selected = []
    for raw_name in filtered:
        name = raw_name.lower()
        if name not in ALL_PROBLEMS_BY_ROUND:
            valid = ", ".join(ALL_PROBLEMS_BY_ROUND.keys())
            raise ValueError(f"Unknown round '{raw_name}'. Valid options: {valid}, all")
        selected.append(name)
    return selected


def should_overwrite(argv):
    return "--overwrite" in argv


def generate(round_names, overwrite_existing):
    PROBLEMS_DIR.mkdir(exist_ok=True)
    created = []
    skipped = []

    for round_name in round_names:
        for problem in ALL_PROBLEMS_BY_ROUND[round_name]:
            pid = zero_pad(problem["id"])
            folder = PROBLEMS_DIR / pid
            folder.mkdir(exist_ok=True)

            md_path = folder / f"{pid}.md"
            cpp_path = folder / f"{pid}_{pascal_file_name(problem['title'])}.cpp"

            if round_name == "round1" and problem["id"] == 1 and md_path.exists() and cpp_path.exists():
                skipped.append(f"{round_name}:{pid}")
                continue

            created_this_problem = False
            if overwrite_existing or not md_path.exists():
                md_path.write_text(build_md(problem), encoding="utf-8")
                created_this_problem = True

            if overwrite_existing or not cpp_path.exists():
                cpp_path.write_text(build_cpp(problem), encoding="utf-8")
                created_this_problem = True

            if created_this_problem:
                created.append(f"{round_name}:{pid}")
            else:
                skipped.append(f"{round_name}:{pid}")

    if overwrite_existing:
        print(f"本次重建或补齐了 {len(created)} 个题目模板。")
    else:
        print(f"本次新建或补齐了 {len(created)} 个题目模板。")
    print(f"已跳过 {len(skipped)} 个题目。")


def main():
    argv = sys.argv[1:]
    round_names = normalize_round_names(argv)
    overwrite_existing = should_overwrite(argv)
    generate(round_names, overwrite_existing)


if __name__ == "__main__":
    main()
