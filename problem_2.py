import os

def find_files(suffix: str, path: str) -> list[str]:

    if not os.path.isdir(path):
        return [""]

    match_found = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            match_found.extend(find_files(suffix, item_path))

        elif os.path.isfile(item_path) and item.endswith(suffix):
            match_found.append(item_path)

    return match_found


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir/testdir")
    print(result)
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

    # Test Case 2
    print("Test Case 2: Empty directory ")
    result = find_files(".c", "./testdir/emptydir")
    print(result)

    # Test Case 3
    print("Test Case 3: Standard directory with no match")
    result = find_files(".java", "./testdir/testdir")
    print(result)