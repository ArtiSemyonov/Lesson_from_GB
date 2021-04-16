import os
import pathlib


def parse():
    with open('started_script.yaml', 'r', encoding='utf-8') as f:
        current_dir_path = pathlib.Path.cwd()
        current_nesting_level = 0
        for line in f:
            processed_line = line.strip("- : \n\r")
            if line.endswith(':\n'):
                if current_nesting_level * 2 < line.index('-') or current_nesting_level == 0:
                    current_dir_path = current_dir_path.joinpath(processed_line)
                elif line.index('-') < current_nesting_level * 2:
                    current_dir_path = pathlib.Path(current_dir_path).parents[current_nesting_level]
                os.mkdir(current_dir_path)
            else:
                file_name = current_dir_path.joinpath(processed_line)
                if not os.path.exists(file_name):
                    open(file_name, 'w').close()
