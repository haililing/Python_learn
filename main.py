def normalize(name):
    s = ""

    for i in range(len(name)):
        ch = name[i]

        if i == 0:
            if "a" <= ch <= "z":
                ch = chr(ord(ch) - 32)
        else:
            if "A" <= ch <= "Z":
                ch = chr(ord(ch) + 32)

        s += ch

    return s


a = input("输入字符串：").split()

a = list(map(normalize, a))

print(a)