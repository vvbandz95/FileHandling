#1

import os

def list_directory_contents(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name, "(Directory)" if entry.is_dir() else "(File)")
    except FileNotFoundError:
        print("Error: The specified directory does not exist.")
    except PermissionError:
        print("Error: Permission denied to access the directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    path = input("Enter the directory path: ")
    list_directory_contents(path)

if __name__ == "__main__":
    main()
