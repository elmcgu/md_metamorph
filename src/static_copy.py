# Import the 'os' and 'shutil' modules for working with the operating system and file operations
import os
import shutil

# Define a function to copy files recursively from a source directory to a destination directory
def copy_files_recursive(source_dir_path, dest_dir_path):
    # Check if the destination directory does not exist, create it
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    # Iterate through each file (and subdirectory) in the source directory
    for filename in os.listdir(source_dir_path):
        # Form the full paths for the source and destination files (or directories)
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        # Print a message indicating the copy operation
        print(f" * {from_path} -> {dest_path}")

        # Check if the current item is a file
        if os.path.isfile(from_path):
            # If it's a file, use 'shutil.copy' to copy it to the destination directory
            shutil.copy(from_path, dest_path)
        else:
            # If it's a directory, recursively call the function to copy its contents
            copy_files_recursive(from_path, dest_path)
