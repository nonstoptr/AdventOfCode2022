import json
def main():
    tally_score()
def tally_score():
    with open('inputs.txt') as file:
        rounds = file.readlines()
    with open('rpsdict2.json') as file:
        rpsdict = json.load(file)
    total = 0
    for round in rounds:
        opponent = round.split(" ")[0]
        play = (round.split(" ")[1]).strip('\n')
        score = (rpsdict[play]['Value']) + (rpsdict[play][opponent])
        total += score
    print(total)
main()