def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)


test_var_args('yasoob', 'python', 'eggs', 'test')


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("{} == {}".format(key, value))


greet_me(name="yasoob")


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg1:", arg2)
    print("arg1:", arg3)


test_args_kwargs("foo", "bar", "baz")


def test_args_kwargs(*argv):
    for count, arg in enumerate(argv):
        print("arg{}:".format(count), arg)


test_args_kwargs("foo", "bar", "baz")

dic = {'a': 'a', 'b': "b"}
print(dic)
for i, j in dic.items():
    print(i, j)
