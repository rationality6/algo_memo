# def foo(a, b, c, **args):
#     print "a = %s" % (a,)
#     print "b = %s" % (b,)
#     print "c = %s" % (c,)
#     print(args)
#
#
# foo(a="testa", b="excess", c="testc", d="testd", k="another_excess")


# def foo(a, b, c, *args):
#     print "a = %s" % (a,)
#     print "b = %s" % (b,)
#     print "c = %s" % (c,)
#     print args
#
#
# foo("testa", "testb", "testc", "excess", "another_excess")

def foo(a, b, c, **args):
    print "a=%s" % (a)
    print "b=%s" % (b)
    print "c=%s" % (c)
    print "args=%s" % (args)


argdict = dict(a="testa", b="testb", c="testc", excessarg="string")
foo(**argdict)
