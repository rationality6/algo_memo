class Test:
    def assert_equals(a, b):
        print(a == b)


notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def chords(root):
    major = [root, notes[(notes.index(root) + 4) % 12],
             notes[(notes.index(root) + 7) % 12]]
    minor = [root, notes[(notes.index(root) + 3) % 12],
             notes[(notes.index(root) + 7) % 12]]
    return [major, minor]


Test.assert_equals(chords("C"), [["C", "E", "G"], ["C", "D#", "G"]])
Test.assert_equals(chords("F"), [["F", "A", "C"], ["F", "G#", "C"]])
Test.assert_equals(chords("G"), [["G", "B", "D"], ["G", "A#", "D"]])
