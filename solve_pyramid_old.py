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
    path = get_path(rows, target, [], 0, 0)
    print("".join(path))


# uses accumulator to build path
def get_path(rows, target, path, row_index, current_row, current_total=1):
    # update the running total
    current_total = current_total * (rows[current_row][row_index])

    if (len(rows) == current_row + 1):  # bottom of the pyramid
        if current_total != target:
            return None
        return path
    if (current_total > target):  # solution cannot be this path
        return None

    # not at the bottom of the pyramid
    left_path = path.copy()
    left_path.append("L")
    right_path = path.copy()
    right_path.append("R")
    left = get_path(rows, target, left_path, row_index, current_row+1, current_total)

    if not left:
        right = get_path(rows, target, right_path, row_index+1, current_row+1, current_total)
        if not right:
            return None
        return right
    return left


def read_target(line):
    try:
        return int(line.split()[-1])
    except (IndexError):
        print("target line must be of form: \"Target: <target_number>\"")
        raise SystemExit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: python solve_pyramid.py <input_file_name.txt>")
        raise SystemExit()
    main(sys.argv)
