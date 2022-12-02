def parse_calories():
    with open('inputs.txt') as f:
        lines = f.readlines()
    i = 1
    cal = 0
    elfdict = {}
    blanks = []
    for line in lines:
        if line == '\n':
            elfdict.update({i: cal})
            i += 1
            cal = 0
        else:
            lineval = line.split("\\")
            cal += int(lineval[0])
    return(sorted(elfdict.items(), key=lambda item: item[1], reverse=True))
def top_elves(elf_dict):
    val = 0
    for key, value in elf_dict[:3]:
        val += value
    print(val)
def main():
    top_elves(parse_calories())
main()