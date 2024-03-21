import os
import shutil

def distribute_files(source_dir, target_dirs):
    # Get list of files in source directory
    files = [(filename, os.path.getsize(os.path.join(source_dir, filename))) for filename in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, filename))]
    files.sort(key=lambda x: x[1], reverse=True)  # Sort files by size

    total_files = len(files)
    files_per_dir = total_files // len(target_dirs)
    remainder = total_files % len(target_dirs)

    current_dir_index = 0
    files_moved = 0

    for filename, _ in files:
        target_dir = target_dirs[current_dir_index]
        source_path = os.path.join(source_dir, filename)
        target_path = os.path.join(target_dir, filename)

        shutil.move(source_path, target_path)
        files_moved += 1

        if files_moved % files_per_dir == 0:
            if remainder > 0:
                remainder -= 1
            else:
                current_dir_index += 1

        if current_dir_index >= len(target_dirs):
            break

if __name__ == "__main__":
    source_directory = "~/dir"
    target_directories = [f"~/dir/{i}" for i in range(1, 9)]

    for dir_path in target_directories:
        os.makedirs(os.path.expanduser(dir_path), exist_ok=True)

    distribute_files(os.path.expanduser(source_directory), target_directories)

    print("Files distributed successfully.")
