import sys
import os

def count_lines_of_code(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            code_lines = 0
            in_multiline_comment = False
            for line in lines:
                line = line.strip()
                if not line or line.startswith('#') or line.startswith("'''") or line.startswith('"""'):
                    continue
                if line.endswith("'''") or line.endswith('"""'):
                    in_multiline_comment = not in_multiline_comment
                    continue
                if not in_multiline_comment:
                    code_lines += 1
            return code_lines
    except FileNotFoundError:
        sys.exit("Error: Specified file does not exist.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <filename.py>")

    file_path = sys.argv[1]
    if not file_path.endswith('.py'):
        sys.exit("Error: File must have a .py extension.")

    if not os.path.isfile(file_path):
        sys.exit("Error: Specified file does not exist.")

    lines_of_code = count_lines_of_code(file_path)
    print(lines_of_code)
