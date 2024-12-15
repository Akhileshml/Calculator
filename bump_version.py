import re
import argparse

def increment_version(version, part='patch'):
    """
    Increment the specified part of the version.
    :param version: Current version string (e.g., '1.2.3').
    :param part: Part to increment ('major', 'minor', 'patch').
    :return: New version string.
    """
    if not re.match(r'^\d+\.\d+\.\d+$', version):
        raise ValueError("Invalid version format. Expected 'x.y.z' (e.g., '1.2.3').")
    
    major, minor, patch = map(int, version.split('.'))
    if part == 'major':
        major += 1
        minor = 0
        patch = 0
    elif part == 'minor':
        minor += 1
        patch = 0
    elif part == 'patch':
        patch += 1
    else:
        raise ValueError("Invalid part to increment. Choose from 'major', 'minor', or 'patch'.")
    
    return f"{major}.{minor}.{patch}"

def main():
    parser = argparse.ArgumentParser(description="Increment the version number in version.txt.")
    parser.add_argument('-p', '--part', choices=['major', 'minor', 'patch'], default='patch',
                        help="Which part of the version to increment (default: patch).")
    parser.add_argument('--dry-run', action='store_true', help="Preview the new version without modifying the file.")
    args = parser.parse_args()
    
    try:
        with open('version.txt', 'r+') as file:
            current_version = file.read().strip()
            new_version = increment_version(current_version, args.part)
            if args.dry_run:
                print(f"Dry run: Current version -> New version: {current_version} -> {new_version}")
            else:
                file.seek(0)
                file.write(new_version)
                file.truncate()
                print(f"Bumped version: {current_version} -> {new_version}")
    except FileNotFoundError:
        print("Error: 'version.txt' not found.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()





# import re

# def increment_version(version):
#     major, minor, patch = map(int, version.split('.'))
#     patch += 1
#     return f"{major}.{minor}.{patch}"

# with open('version.txt', 'r+') as file:
#     current_version = file.read().strip()
#     new_version = increment_version(current_version)
#     file.seek(0)
#     file.write(new_version)
#     file.truncate()

# print(f"Bumped version: {current_version} -> {new_version}")
