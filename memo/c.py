def get_status(file):
    with open(file) as fp:
        return fp.readline()

print get_status('./src/hello.txt')
