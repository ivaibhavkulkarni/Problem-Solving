def print_frequncy(line):
    line = line.lower()
    set_of_char = set(line)
    set_of_char.discard(" ")
    set_of_char = sorted(set_of_char)
    for i in set_of_char:
        msg = "{}: {}"
        #print(line.count(i))
        print(msg.format(i,line.count(i)))

line = input()
print_frequncy(line)
