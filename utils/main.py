from utils import required_str, sort_five, read_file

path = '../operations.json'


def main(path):
    return map(required_str, sort_five(read_file(path)))

if __name__ == "__main__":
    print(*main(path), sep='\n', end='')
