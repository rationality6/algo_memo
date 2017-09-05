import sys
indent = 0
shiftwidth = 4

for line in sys.stdin:
    if line.strip().startswith('then'):
        print('%s%s' % (' ' * indent, line.strip()))
        indent += shiftwidth
    elif line.strip().startswith('fi'):
        indent -= shiftwidth
        print('%s%s' % (' ' * indent, line.strip()))
    else:
        print('%s%s' % (' ' * indent, line.strip()))
