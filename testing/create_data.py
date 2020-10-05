from pathlib import Path


def create_directory_with_data(path: str, start: int = 0, end: int = 3) -> Path:
    target_path = Path.cwd() / path
    try:
        target_path.mkdir()
    except FileExistsError:
        pass
    for d in range(start, end):
        with open(target_path / f"{d}.txt", "w") as file:
            print(str(d), file=file)
    return target_path


if __name__ == '__main__':
    create_directory_with_data("01_fingerprint_recursive")
