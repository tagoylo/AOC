import argparse

def prep_list(input):
    with open(input, 'r') as file:
        text = file.read()
        lines = text.split("\n")
        reports = [line.split() for line in lines]
    return reports

def checker(report):
    status = False
    report = [int(i) for i in report]
    if all((report[i] <= report[i+1]) and (abs(report[i+1]-report[i]) in [1,2,3]) for i in range(len(report)-1)):
        status = True
    elif all((report[i] >= report[i+1]) and (abs(report[i]-report[i+1]) in [1,2,3]) for i in range(len(report)-1)):
        status = True
    return status

def checker_duplicate(report):
    rreport = []
    report = [int(i) for i in report]
    i = 0
    while i < len(report) - 1:
        if report[i] == report[i+1]:
            rreport=report.remove(report[i])
        else:
            i += 1
    return rreport

def count_safe(reports):
    safe = []
    unsafe = []
    for report in reports:
        checker(report)
        if checker(report):
            safe.append(report)
        else:
            unsafe.append(report)
    return safe, unsafe

def dampener(unsafe_reports):
    count = 0
    for report in unsafe_reports:
        if checker_duplicate(report):
            report = checker_duplicate(report)
        for i in range(len(report)):
            dreport = report[:i] + report[i+1:]
            if checker(dreport):
                count += 1
                break
            else:
                continue
    return count
        
def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input_file', type=str, help='The input file to process')
    args = parser.parse_args()

    reports = prep_list(args.input_file)
    count = len(count_safe(reports)[0])
    dampened = dampener(count_safe(reports)[1])
    print("Safe reports: ", count)
    print("Dampened reports: ", dampened)
    print("Total safe reports: ", count+dampened)

if __name__ == '__main__':
    main()