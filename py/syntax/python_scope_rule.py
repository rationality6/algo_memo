def f(nf, xf):
    nf = 2
    xf.append(4)
    print('In f():', nf, xf)

def main():
    nmain = 1
    xmain = [0,1,2,3]
    print('Before:', nmain, xmain)
    f(nmain, xmain)
    print('After: ', nmain, xmain)

main()
