

ans = 0
with open("datafiles/data2.txt", "r") as file:
    lines = file.readlines()
    linenumber = 1
    check = {'red': 12, 'green': 13, 'blue': 14}
    for line in lines:
        templine = line.split(':')[1].strip()
        turns = templine.strip().split(';')
        flag = True
        for turn in turns:
            temp = turn.strip().split(' ')
            for i in range(0, len(temp), 2):
                freq = int(temp[i])
                color = temp[i+1]
                if i < len(temp)-2:
                    color = color[:-1]
                if freq > check[color]:
                    flag = False
                    break
        if flag:
            ans += linenumber
        linenumber += 1
    print("ans is " + str(ans))

# part two
ans = 0
with open("datafiles/data2.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        r = g = b = 0
        templine = line.split(':')[1].strip()
        turns = templine.strip().split(';')
        for turn in turns:
            temp = turn.strip().split(' ')
            for i in range(0, len(temp), 2):
                freq = int(temp[i])
                color = temp[i+1]
                if i < len(temp)-2:
                    color = color[:-1]
                if color == 'red':
                    r = max(r, freq)
                elif color == 'green':
                    g = max(g, freq)
                else:
                    b = max(b, freq)
        ans += r*g*b
    print("ans is " + str(ans))
