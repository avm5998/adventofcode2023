
from collections import defaultdict


def part1():

    with open('datafiles/data4.txt', 'r') as file:
        lines = file.read().splitlines()
        ans = 0
        for line in lines:
            numbers = line.split(':')[1].strip()
            n = len(numbers)
            winners = set()
            i = 0
            number = 0
            while numbers[i] != '|':
                while numbers[i].isdigit():
                    number = number*10+int(numbers[i])
                    i += 1
                # print(number)
                winners.add(number)
                number = 0
                while numbers[i] == ' ':
                    i += 1
            matches = 0
            i += 2
            while i < n:
                while i < n and numbers[i].isdigit():
                    number = number*10+int(numbers[i])
                    i += 1
                if number in winners:
                    matches += 1
                # matches += winners[number]
                number = 0
                while i < n and numbers[i] == ' ':
                    i += 1
            ans += 2**(matches-1) if matches > 0 else 0
        print(ans)


def part2():

    with open('datafiles/data4.txt', 'r') as file:
        lines = file.read().splitlines()
        ans = 0
        cards = defaultdict(int)
        for index, line in enumerate(lines):
            numbers = line.split(':')[1].strip()
            n = len(numbers)
            winners = set()
            i = 0
            number = 0
            while numbers[i] != '|':
                while numbers[i].isdigit():
                    number = number*10+int(numbers[i])
                    i += 1
                # print(number)
                winners.add(number)
                number = 0
                while numbers[i] == ' ':
                    i += 1
            matches = 0
            i += 2
            matches = 0
            # checking numbers for matches
            while i < n:
                while i < n and numbers[i].isdigit():
                    number = number*10+int(numbers[i])
                    i += 1
                if number in winners:
                    matches += 1
                number = 0
                while i < n and numbers[i] == ' ':
                    i += 1
            cards[index+1] += 1
            for j in range(1, matches+1):
                cards[index+1+j] += cards[index+1]

        print(sum(cards.values()))


part1()
part2()
