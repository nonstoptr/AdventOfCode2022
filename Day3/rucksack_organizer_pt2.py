import string
def main():
    organizeRucksack()
def findCommon(string1, string2, string3):
    match = False
    while match == False:
        for letters in string1.strip('\n'):
            if letters in string2:
                if letters in string3:
                    common = letters
                    match = True
    return common
def convertPriority(itemtype):
    if itemtype.isupper():
        itemValue = ((string.ascii_uppercase.index(itemtype))+27)
    if itemtype.islower():
        itemValue = (string.ascii_lowercase.index(itemtype))+1
    return itemValue
def organizeRucksack():
    sum = 0
    i = 0
    with open('/Users/thomasreed/repos/AdventOfCode2022/Day3/inputs.txt') as file:
        sacks = file.readlines()
    while (i+3) <= len(sacks):
        slice = sacks[i:(i+3)]
        common = (findCommon(slice[0], slice[1], slice[2]))
        print(common)
        sum+=convertPriority(common)
        i  += 3
    print(sum)
main()