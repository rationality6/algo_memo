# Convert a linked list to a string
class test:
    def assert_equals(result, anwser):
        print(result == anwser)


class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# def stringify(list):
#     current = list
#     result = ""
#     while None != current:
#         result += "{} -> ".format(current.data)
#         current = current.next
#     result += "None"
#     return result

def stringify(list):
    return "None" if list == None else str(list.data) + ' -> ' + stringify(list.next)

test.assert_equals(
    stringify(Node(0, Node(1, Node(2, Node(3))))), '0 -> 1 -> 2 -> 3 -> None')
test.assert_equals(stringify(None), 'None')
test.assert_equals(stringify(
    Node(0, Node(1, Node(4, Node(9, Node(16)))))), '0 -> 1 -> 4 -> 9 -> 16 -> None')
