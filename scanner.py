import os
from rules import check_none_issues, check_try_except, check_hardcoded_values

def scan_file(file_path):
    results = []

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    results.extend(check_none_issues(lines, file_path))
    results.extend(check_try_except(lines, file_path))
    results.extend(check_hardcoded_values(lines, file_path))

    return results


def scan_directory(directory):
    findings = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                findings.extend(scan_file(full_path))

    return findings


if __name__ == "__main__":
    directory = "sample_code"
    findings = scan_directory(directory)

    print("\n🔍 Code Health Report:\n")

    if not findings:
        print("✅ No issues found")
    else:
        for issue in findings:
            print(f"[WARNING] {issue}")
import json

if __name__ == "__main__":
    directory = "sample_code"
    findings = scan_directory(directory)

    report = {
        "total_issues": len(findings),
        "issues": findings
    }

    # ✅ Save JSON report
    with open("reports/output.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\n🔍 Code Health Report:\n")

    if not findings:
        print("✅ No issues found")
    else:
        for issue in findings:
            print(f"[WARNING] {issue}")

    print("\n✅ JSON report generated at reports/output.json")
