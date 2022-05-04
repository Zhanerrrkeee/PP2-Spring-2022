a = input().split()
array = []

for i in a:
    array.append(i)


def call(array):
    pos = 0
    max = 0
    while pos < len(array):
        if pos > max:
            return False
        if pos + int(array[pos]) > max:
            max = pos + int(array[pos])
        if max >= len(array) - 1:
            return True
        pos += 1


if call(array):
    print("1")
else:
    print("0")


    