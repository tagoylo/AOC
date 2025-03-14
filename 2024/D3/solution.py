import argparse
import re

def read_input(input):
    with open(input, 'r') as file:
        text = file.read()
    return text

def sum_of_products(text):
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    matches = pattern.findall(text)
    total_sum = sum(int(a) * int(b) for a, b in matches)
    return total_sum

def enabled_sum_of_products(text):
    all_do = re.split(r'do\(\)', text)
    total_sum = 0
    for item in all_do:
        if "don't()" in item:
            new = re.split(r'don\'t\(\)', item)[0]
            total_sum += sum_of_products(str(new))
        else:
            total_sum += sum_of_products(str(item))
    return total_sum

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input_file', type=str, help='The input file to process')
    args = parser.parse_args()

    text = read_input(args.input_file)
    result = sum_of_products(text)
    enabled = enabled_sum_of_products(text)
    print("Sum of products: ", result)
    print("Enabled sum of products: ", enabled)

if __name__ == '__main__':
    main()