class Test:
    def assert_equals(a, b):
        print(a == b)


char_list = {0: "Zero", 1: "One", 2: "Two", 3: "Three",
             4: "Four", 5: "Five", 6: "Six", 7: "Seven",
             8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen"}


def max_consec_zeros(n):
    binary_n = str(bin(int(n))[2:])
    count = 0
    max_count = 0
    for i in range(len(binary_n)):
        if int(binary_n[i]) == 0:
            count += 1
        else:
            count = 0
        max_count = max(max_count, count)
    print(binary_n)
    print(max_count)
    return char_list[max_count]


def max_consec_zeros(n):
    w = 'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen'.split()
    return w[max(map(len, bin(int(n))[2:].split('1')))]


max(map(len, bin(int(n))[2:].split('1')))

N = 88
print(max(*map(len, bin(int(N))[2:].split('1'))))
print(bin(N))

Test.assert_equals(max_consec_zeros("7"), "Zero")
Test.assert_equals(max_consec_zeros("33"), "Four")
Test.assert_equals(max_consec_zeros("77"), "Two")
Test.assert_equals(max_consec_zeros("100"), "Two")
Test.assert_equals(max_consec_zeros("105"), "Two")
Test.assert_equals(max_consec_zeros("113"), "Three")
Test.assert_equals(max_consec_zeros("160"), "Five")
Test.assert_equals(max_consec_zeros("180"), "Two")
Test.assert_equals(max_consec_zeros("223"), "One")
Test.assert_equals(max_consec_zeros("256"), "Eight")
Test.assert_equals(max_consec_zeros("777"), "Four")
Test.assert_equals(max_consec_zeros("992"), "Five")
Test.assert_equals(max_consec_zeros("1024"), "Ten")
Test.assert_equals(max_consec_zeros("1037"), "Six")
Test.assert_equals(max_consec_zeros("1088"), "Six")
# Test.assert_equals(max_consec_zeros("2017"), "Four")
# Test.assert_equals(max_consec_zeros("2048"), "Eleven")
# Test.assert_equals(max_consec_zeros("3050"), "One")
# Test.assert_equals(max_consec_zeros("4096"), "Twelve")
# Test.assert_equals(max_consec_zeros("6144"), "Eleven")
# Test.assert_equals(max_consec_zeros("6656"), "Nine")
# Test.assert_equals(max_consec_zeros("7188"), "Five")
# Test.assert_equals(max_consec_zeros("8192"), "Thirteen")
# Test.assert_equals(max_consec_zeros("9999"), "Four")
# Test.assert_equals(max_consec_zeros("10000"), "Four")
