import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main():
    failures = []

    ps1 = ROOT / "scripts" / "lc_runner.ps1"
    cmd = ROOT / "lc.cmd"
    readme = ROOT / "readme.md"

    if not ps1.exists():
        failures.append("missing scripts/lc_runner.ps1")
    if not cmd.exists():
        failures.append("missing lc.cmd")

    readme_text = readme.read_text(encoding="utf-8")
    for token in [".\\lc 14", "scripts/lc_runner.ps1", "cmake --build"]:
        if token not in readme_text:
            failures.append(f"readme.md missing {token}")

    if cmd.exists():
        completed = subprocess.run(
            [str(cmd), "14"],
            cwd=ROOT,
            capture_output=True,
            timeout=30,
        )
        output = completed.stdout.decode("utf-8", errors="replace") + completed.stderr.decode(
            "utf-8", errors="replace"
        )
        if completed.returncode != 0:
            failures.append(f"lc 14 exited {completed.returncode}: {output[:500]}")
        for token in ["014_LongestCommonPrefix", "\u5f53\u524d\u7ed3\u679c", "\u9884\u671f\u7ed3\u679c"]:
            if token not in output:
                failures.append(f"lc 14 output missing {token}")

    if failures:
        print("lc runner verification failed:")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("lc runner verification passed.")


if __name__ == "__main__":
    main()
