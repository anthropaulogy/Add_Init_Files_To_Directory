import os


def add_init_py_to_subdirectories(target_directory):
    """
    Add a blank __init__.py file to each subdirectory within the target directory.
    :param target_directory: The path of the target directory.
    """
    if not os.path.isdir(target_directory):
        print(f"Error: '{target_directory}' is not a valid directory.")
        return

    for root, dirs, files in os.walk(target_directory):
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            init_file_path = os.path.join(dir_path, "__init__.py")

            # Check if the __init__.py file already exists
            if not os.path.exists(init_file_path):
                try:
                    # Create an empty __init__.py file
                    with open(init_file_path, "w") as init_file:
                        pass
                    print(f"Created: {init_file_path}")
                except Exception as e:
                    print(f"Failed to create __init__.py in {dir_path}: {e}")
            else:
                print(f"Exists: {init_file_path}")


if __name__ == "__main__":
    target_dir = input("Enter the path of the target directory: ").strip()
    add_init_py_to_subdirectories(target_dir)
