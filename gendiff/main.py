from gendiff.generate_diff import generate_diff
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate diff between two JSON files')
    parser.add_argument('file1', help='First JSON file')
    parser.add_argument('file2', help='Second JSON file')
    args = parser.parse_args()
    
    diff = generate_diff(args.file1, args.file2)
    print(diff)

if __name__ == '__main__':
    main()
