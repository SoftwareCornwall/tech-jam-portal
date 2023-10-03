import os

def rename_files_in_directory(directory):
    """Renames all files in the given directory and its subdirectories
    by replacing spaces with underscores and making text lowercase."""
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            new_name = filename.replace(" ", "_").lower()
            new_filepath = os.path.join(foldername, new_name)
            if filepath != new_filepath: # Check to avoid unnecessary renaming
                os.rename(filepath, new_filepath)
                print(f"Renamed {filepath} to {new_filepath}")

if __name__ == "__main__":
    # Use the directory where the script is located as the starting directory
    starting_directory = os.path.dirname(os.path.abspath(__file__))
    
    rename_files_in_directory(starting_directory)