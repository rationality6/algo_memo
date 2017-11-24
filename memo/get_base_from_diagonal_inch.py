# 16:9 wide screen
def get_base169(D):
    from math import sqrt
    inch_to_cm = 2.54
    return inch_to_cm * (sqrt((256 * (D**2)) / 337))

# 16:10 wide screen
def get_base_1610(D):
    from math import sqrt
    inch_to_cm = 2.54
    return inch_to_cm * (sqrt((256 * (D**2)) / 356))

# 4:3 wide screen
def get_base_43(D):
    from math import sqrt
    inch_to_cm = 2.54
    return inch_to_cm * (sqrt((25 * (D**2)) / 16))


print(get_base169(15.4))
print(get_base169(40))
print(get_base169(48))

print(get_base_1610(15.4))
print(get_base_1610(40))
print(get_base_1610(48))

print(get_base_43(15.4))
print(get_base_43(40))
print(get_base_43(48))
