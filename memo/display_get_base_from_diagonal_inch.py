from math import sqrt
inch_to_cm = 2.54


# 16:9 wide screen Base
def get_base169(D):
    return inch_to_cm * (sqrt((256 * (D**2)) / 337))

# 16:10 wide screen Base
def get_base_1610(D):
    return inch_to_cm * (sqrt((256 * (D**2)) / 356))

# 16:10 wide screen Height
def get_base_1610_H(D):
    return inch_to_cm * (sqrt((100 * (D**2)) / 356))

# 4:3 wide screen Base
def get_base_43(D):
    return inch_to_cm * (sqrt((25 * (D**2)) / 16))


if __name__ == "__main__":
    # print(get_base169(15.4))
    # print(get_base169(40))
    # print(get_base169(48))
    # print(get_base169(65))

    # print(get_base_1610(15.4))
    # print(get_base_1610(40))
    # print(get_base_1610(48))

    # print(get_base_1610_H(15.4))

    # print(get_base_43(15.4))
    # print(get_base_43(40))
    # print(get_base_43(48))
