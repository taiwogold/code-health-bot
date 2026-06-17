def check_none_issues(lines, file):
    issues = []

    for i, line in enumerate(lines):
        if ".date()" in line and "if" not in lines[i-1]:
            issues.append(f"{file}: Line {i+1} - Possible missing None check before .date()")

    return issues


def check_try_except(lines, file):
    issues = []

    for i, line in enumerate(lines):
        if "except:" in line:
            issues.append(f"{file}: Line {i+1} - Bare except detected")

    return issues


def check_hardcoded_values(lines, file):
    issues = []

    for i, line in enumerate(lines):
        if "input/" in line:
            issues.append(f"{file}: Line {i+1} - Hardcoded file path detected")

    return issues
