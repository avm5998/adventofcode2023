
def checkleft(i, j, lines, taken):
    k = j-1
    number = 0
    mult_term = 1
    while k >= 0 and lines[i][k].isdigit():
        number += mult_term*int(lines[i][k])
        mult_term *= 10
        k -= 1
    k += 1
    if (i, k) in taken:
        return 0
    else:
        taken.add((i, k))
        return number


def checkright(i, j, lines, taken):
    k = j+1
    if (i, k) in taken:
        return 0

    number = 0
    n = len(lines[0])
    while k < n and lines[i][k].isdigit():
        number = number*10+int(lines[i][k])
        k += 1
    k -= 1
    taken.add((i, j+1))
    return number


def checktopbottom(i, j, lines, taken):
    if i < 0 or i >= len(lines):
        return 0

    if lines[i][j].isdigit():
        # possible to have one number across
        k = j-1
        while k > 0 and lines[i][k].isdigit():
            k -= 1
        k += 1
        if (i, k) in taken:
            return 0
        taken.add((i, k))
        number = 0
        while k < len(lines[0]) and lines[i][k].isdigit():
            number = number*10+int(lines[i][k])
            k += 1
        return number
    else:
        # check for two different numbers together
        return checkleft(i, j, lines, taken)+checkright(i, j, lines, taken)


def part1():
    taken = set()

    with open('datafiles/data3.txt', 'r') as file:
        lines = file.read().splitlines()
        ans = 0

        m, n = len(lines), len(lines[0])
        for i in range(m):
            for j in range(n):
                chr = lines[i][j]
                if not chr.isdigit() and chr != '.':
                    # print(chr)
                    ans += checkleft(i, j, lines, taken)
                    # print(ans)
                    ans += checkright(i, j, lines, taken)
                    # print(ans)
                    ans += checktopbottom(i-1, j, lines, taken)
                    # print(ans)
                    ans += checktopbottom(i+1, j, lines, taken)
                    # print(ans)
        print(ans)


def checkleftp2(i, j, lines):
    k = j-1
    number = 0
    mult_term = 1
    if k < 0 or not lines[i][k].isdigit():
        return []
    while k >= 0 and lines[i][k].isdigit():
        number += mult_term*int(lines[i][k])
        mult_term *= 10
        k -= 1
    k += 1
    return [number]


def checkrightp2(i, j, lines):
    k = j+1
    if k == len(lines[0]) or not lines[i][k].isdigit():
        return []
    number = 0
    n = len(lines[0])
    while k < n and lines[i][k].isdigit():
        number = number*10+int(lines[i][k])
        k += 1
    k -= 1
    return [number]


def checktopbottomp2(i, j, lines):
    if i < 0 or i >= len(lines):
        return 0

    if lines[i][j].isdigit():
        # possible to have one number across
        k = j-1
        while k > 0 and lines[i][k].isdigit():
            k -= 1
        k += 1
        number = 0
        while k < len(lines[0]) and lines[i][k].isdigit():
            number = number*10+int(lines[i][k])
            k += 1
        return [number]
    else:
        # check for two different numbers together
        ans = checkleftp2(i, j, lines)
        ans.extend(checkrightp2(i, j, lines))
        return ans


def part2():
    with open('datafiles/data3.txt', 'r') as file:
        lines = file.read().splitlines()
        ans = 0

        m, n = len(lines), len(lines[0])
        for i in range(m):
            for j in range(n):
                chr = lines[i][j]
                if chr == '*':
                    chr = []
                    chr.extend(checkleftp2(i, j, lines))
                    chr.extend(checkrightp2(i, j, lines))
                    chr.extend(checktopbottomp2(i-1, j, lines))
                    chr.extend(checktopbottomp2(i+1, j, lines))
                    if len(chr) == 2:
                        ans += chr[0]*chr[1]
        print(ans)


part1()
part2()
