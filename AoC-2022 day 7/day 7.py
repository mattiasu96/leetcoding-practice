####### first step #########
# Parsing input and do pattern matching with the commands
import re

input_path = "./input.txt"

directory_sizes = {}

if __name__ == "__main__":
    with open(input_path, 'r') as input_file:
        stack_path = []
        cur_dir = ""
        for line in input_file.readlines():
            if line == "$ cd /\n":
                stack_path = ['/']
            if line == "$ cd ..\n":
                stack_path.pop()
            if re.match("^\$ cd (\w+)$", line):
                dir_name = re.match("^\$ cd (\w+)$", line).groups()[0]
                stack_path.append(dir_name)

            # if re.match("^ (\w+)$", line):
            #     dir_name = re.match("^\$ cd (\w+)$", line).groups()[0]
            #     stack_path.append(dir_name)













