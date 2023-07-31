import sys


# main function handles I/O
# calls the pyramid solver
def main(argv):
    # TODO: try/except open file
    in_file = open(argv[1], "r")
    lines = in_file.readlines()

    # get target
    target = read_target(lines[0])

    rows = [[int(num) for num in line.strip().split(",")] for line in lines[1:]]

    path = []
    get_path_reversed(rows, target, path, 0, 0, 1)
    path.reverse()
    print("".join(path))


def get_path_reversed(rows, target, path, row_index, current_row, current_total):
    '''Recursively builds the path in reverse by modifying the <path> array.

    Parameters:
        rows (list of list): rows in the pyramid, each row is a list of int
        target (int): target value
        path (list of str):  current traversal path, reversed, list of "R" or "L"
        row_index (int): index of current number being visited in the row
        current_row (int): index of current row in the pyramid
        current_total (int): current product of traversed numbers

    Returns:
        bool: whether or not traversed path results in target product

    '''
    # update the running total
    current_total = current_total * (rows[current_row][row_index])

    if (len(rows) == current_row + 1):  # bottom of the pyramid
        if current_total != target:
            return False
        return True
    if (current_total > target):  # solution cannot be this path
        return False

    left = get_path_reversed(rows, target, path, row_index, current_row+1, current_total)

    if not left:
        right = get_path_reversed(rows, target, path, row_index+1, current_row+1, current_total)
        if not right:
            return False
        path.append("R")
    else:
        path.append("L")
    return True


def read_target(line):
    try:
        return int(line.split()[-1])
    except (IndexError):
        print("target line must be of form: \"Target: <target_number>\"")
        raise SystemExit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python solve_pyramid2.py <input_file_name>")
        raise SystemExit()
    main(sys.argv)
