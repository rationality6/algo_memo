def get_status(file):
    return open(file).readline()


print(get_status('./src/hello.txt'))
print "d"
