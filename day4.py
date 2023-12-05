
from collections import defaultdict


def part1():

    with open('datafiles/trialdata.txt', 'r') as file:
        lines = file.read().splitlines()
        ans = 0
        for line in lines:
            numbers = line.split(':')[1].strip()
            n = len(numbers)
            winners = defaultdict(int)
            i = 0
            number = 0
            while numbers[i] != '|':
                while numbers[i].isdigit():
                    number = number*10+int(numbers[i])
                    i += 1
                #print(number)
                winners[number] += 1
                number = 0
                while numbers[i] == ' ':
                    i += 1
            matches = 0
            i += 2
            while i < n:
                while i<n and numbers[i].isdigit():
                    number = number*10+int(numbers[i])
                    i += 1
                matches += winners[number]
                number = 0
                while i < n and numbers[i] == ' ':
                    i += 1
            ans += 2**(matches-1) if matches > 0 else 0
        print(ans)

def part2():

    with open('datafiles/trialdata.txt', 'r') as file:
        lines = file.read().splitlines()
        ans = 0
        for index,line in enumerate(lines):
            numbers = line.split(':')[1].strip()
            n = len(numbers)
            winners = defaultdict(int)
            i = 0
            number = 0
            while numbers[i] != '|':
                while numbers[i].isdigit():
                    number = number*10+int(numbers[i])
                    i += 1
                #print(number)
                winners[number] += 1
                number = 0
                while numbers[i] == ' ':
                    i += 1
            matches = 0
            i += 2
            while i < n:
                while i<n and numbers[i].isdigit():
                    number = number*10+int(numbers[i])
                    i += 1
                matches += winners[number]
                number = 0
                while i < n and numbers[i] == ' ':
                    i += 1
            ans += 2**(matches-1) if matches > 0 else 0
        print(ans)

part1()
part2()