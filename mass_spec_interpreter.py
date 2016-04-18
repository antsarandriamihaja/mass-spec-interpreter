Full_length = input("Enter the sequence of your protein, in single letter code, here: ")
protein = Full_length.upper()


dict = {
'G' : 57.052,
'A' : 71.079,
'S' : 87.078,
'P' : 97.117,
'V' : 99.133,
'T' : 101.105,
'C' : 103.144,
'I' : 113.160,
'L' : 113.160,
'N' : 114.104,
'D' : 115.089,
'Q' : 128.131,
'K' : 128.174,
'E' : 129.116,
'M' : 131.198,
'H' : 137.142,
'F' : 147.177,
'R' : 156.188,
'Y' : 163.170,
'W' : 186.213
}


unknown = []
for id in range (0, len(protein)):
    residue = protein[id]
    if not (residue in dict):
        unknown.append(id+1)
if len(unknown)>0:
    print("Unrecognized amino acid at the indicated positions: {}".format(unknown))

while True:
    try:
        fragment = float(input("Enter the mass (in Da) of your fragment here: "))
    except ValueError:
        print("Fragment must be a number indicating the size of your fragment in Da. Please enter a number.")
    else:
        break


while True:
    try:
        Error_margin = float(input("Enter an error margin (in Da) here: "))
    except ValueError:
        print("The margin of error has to be a number (in Da). Please enter a number.")
    else:
        break
fragment -= 18
def alpha():


    for i in range(0, len(protein)):
        character = protein[i]

        if character in dict:
            def mass_spec():
                list = []
                start_point = 0
                while start_point < len(protein):
                    total = 0
                    sequence = ""
                    for char in protein[start_point:]:
                        total += dict[char]
                        sequence += char
                        if total > fragment + Error_margin:
                            break
                        elif total < fragment - Error_margin:
                            continue
                        else:
                            list.append(sequence)
                    start_point += 1

                if len(list) > 0:
                    return (list)
                else:
                    return ("No match found. Please increase the margin of error.")


            return (mass_spec())



        else:
            return ("The amino acid at position '%' is invalid".format(i+1))


print(alpha())




















