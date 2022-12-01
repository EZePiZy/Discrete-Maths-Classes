

temperature = [-5, -4, -3, 12, -40, 4, 2, 18, 11, 5]


def get_temp(temperature):
    if (len(temperature) == 0 or len(temperature) == 1):
        return 0 
    else: 
        return min(temperature, key=abs)
    

# print(get_temp(temperature))
count = 0 
for i in words:
    for j in words:
        if words[i] == words[j]:
        count += 1 


def get_number_difference(words):
    set_word = set(words)
    lengt_dict = len (set_word)
    lenght_list = len(words)

    final = lenght_list - lengt_dict

    print(final)




    
    
def iterate(rows):
    for i in range(0,9):
        numbs.append(row[i])




final = []
def robot(instr):
    for i in instr:
        if instr[i] == 'up':
            final.append("^")
        elif instr[i] == 'down':
            final.append("v")
        elif instr[i] == 'left':
            final.append('<')
        elif instr[i] == 'right':
            final.append('>')
    
    for i in final:
        if i == (i)+1: 
            print('same')

   



