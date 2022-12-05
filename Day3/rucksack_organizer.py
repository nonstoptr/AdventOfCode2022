import string
def main():
    organizeRucksack()
def findCommon(string1, string2):
    match = False
    while match == False:
        for letters in string1:
            if letters in string2:
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
    with open('./inputs.txt') as file:
        sacks = file.readlines()
    for sack in sacks:
        linelength = len(sack)
        firstCompartment = sack[0:int((len(sack)/2))]
        secondCompartment = (sack[int((len(sack)/2)):]).strip('/n')
        common = (findCommon(firstCompartment,secondCompartment))
        sum+=convertPriority(common)
    print(sum)
main()