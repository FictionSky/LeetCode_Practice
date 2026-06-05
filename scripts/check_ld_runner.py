import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main():
    failures = []

    ps1 = ROOT / "scripts" / "ld_runner.ps1"
    cmd = ROOT / "ld.cmd"
    readme = ROOT / "readme.md"
    launch = ROOT / ".vscode" / "launch.json"
    tasks = ROOT / ".vscode" / "tasks.json"

    if not ps1.exists():
        failures.append("missing scripts/ld_runner.ps1")
    if not cmd.exists():
        failures.append("missing ld.cmd")

    readme_text = readme.read_text(encoding="utf-8")
    for token in [".\\ld 14", "F5", "launch.json", "tasks.json"]:
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
            failures.append(f"ld 14 exited {completed.returncode}: {output[:500]}")
        for token in ["014_LongestCommonPrefix", "launch.json", "F5"]:
            if token not in output:
                failures.append(f"ld 14 output missing {token}")

    if launch.exists():
        launch_data = json.loads(launch.read_text(encoding="utf-8-sig"))
        configurations = launch_data.get("configurations", [])
        if not configurations:
            failures.append("launch.json has no configurations")
        else:
            config = configurations[0]
            if "014_LongestCommonPrefix.exe" not in config.get("program", ""):
                failures.append("launch.json program does not point to 014_LongestCommonPrefix.exe")
            if config.get("preLaunchTask") != "Build Active LeetCode Target":
                failures.append("launch.json preLaunchTask is incorrect")
    else:
        failures.append("missing .vscode/launch.json")

    if tasks.exists():
        task_data = json.loads(tasks.read_text(encoding="utf-8-sig"))
        tasks_list = task_data.get("tasks", [])
        if not tasks_list:
            failures.append("tasks.json has no tasks")
        else:
            task = tasks_list[0]
            command = task.get("command", "")
            if "014_LongestCommonPrefix" not in command:
                failures.append("tasks.json command does not build 014_LongestCommonPrefix")
    else:
        failures.append("missing .vscode/tasks.json")

    if failures:
        print("ld runner verification failed:")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("ld runner verification passed.")


if __name__ == "__main__":
    main()
