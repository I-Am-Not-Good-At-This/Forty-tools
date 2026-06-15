import sys
from pathlib import Path

def create_folders(path: Path) -> None:
    while True:
        ex_input = input("Number of exercises in this module: ")
        try:
            ex_number = int(ex_input)
            if ex_number < 0:
                raise ValueError
            break
        except ValueError:
            sys.stderr.write("Invalid number: please enter a positive integer.\n")

    for x in range(ex_number + 1):
        ex_path = path / f"ex{x}"
        if ex_path.exists():
            print(f"Directory {ex_path}/ already exists, skipping.")
        else:
            try:
                ex_path.mkdir(parents=True)
                (ex_path / ".gitkeep").touch()
                print(f"Directory {ex_path}/ successfully created.")
            except Exception as e:
                sys.stderr.write(f"Error creating directory {ex_path}/: {e}\n")

def get_path() -> Path:
    while True:
        raw = input("Path of the module's directory: ")
        path = Path(raw)
        if path.is_dir():
            return path
        print("Not a valid directory, try again... (Ctrl+C to quit)")

if __name__ == "__main__":
    path = get_path()
    create_folders(path)
    print("\033[32m✅ Done!\033[0m")