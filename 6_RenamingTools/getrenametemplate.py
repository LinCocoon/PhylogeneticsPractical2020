alllines = []
with open("oritemplate.txt", "r") as input_file:
    alllines = input_file.read().splitlines()

Dict = dict()
for line in alllines:
    Dict[str(line).split(" ")[0]] = (str(line).split(" ")[1])

def rename(file):
    with open(file, "r") as input_file:
        tree = str(input_file.read().splitlines()).strip("']").strip("['")

    for i in Dict.keys():
        tree = tree.replace(i, Dict[i])

    outF = open(f"{file}_renamed", "w")
    outF.write(tree)
