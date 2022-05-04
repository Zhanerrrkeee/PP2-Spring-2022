open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def check(string):
    str = []
    for i in string:
        if i in open_list:
            str.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(str) > 0) and (open_list[pos] == str[len(str) - 1])):
                str.pop()
            else:
                return "No"
    if len(str) == 0:
        return "Yes"
    else:
        return "No"


list = str(input())

print(check(list))