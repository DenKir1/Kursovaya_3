from utils.sort_newest import sort_five
from utils.read_json import read_file

path = './operations.json'

def main(path):
    return sort_five(read_file(path))


if __name__ == "__main__":
    print(*main(path), sep="\n", end='')
