import sys

def read_inputs(file)
    for line in file
        line = line.strip()
        yield line.split()
def main()
    file = sys.stdin
    lines = read_inputs(file)
    for words in lines
        for word in words
            print({}t{}.format(word, 1))
if __name__ == __main__
    main()