reports = []
safe_reports = 0
safe_subreports = 0

with open("data.txt", "r") as file:
    for line in file:
        reports.append([int(item) for item in line.split(' ')])

for report in reports:
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    max_difference = max(abs(report[i] - report[i + 1]) for i in range(len(report) - 1))
    if (is_increasing or is_decreasing) and max_difference <= 3:
        safe_reports += 1

    subreports = [report[:i] + report[i+1:] for i in range(len(report))] # This line creates subreports with one less element compared to the original
    for subreport in subreports:
        is_increasing = all(subreport[j] < subreport[j + 1] for j in range(len(subreport) - 1))
        is_decreasing = all(subreport[j] > subreport[j + 1] for j in range(len(subreport) - 1))
        max_difference = max(abs(subreport[j] - subreport[j + 1]) for j in range(len(subreport) - 1))
        if (is_increasing or is_decreasing) and max_difference <= 3:
            safe_subreports += 1
            break # This ensures no duplicate +1 are assigned

print("The number of safe reports is", safe_reports)
print("The number of safe sub-reports is", safe_subreports)
