def printList(list):
    s = ''
    for item in list:
        if type(item) == float:
            s += "{0:.2f}, ".format(item)
        else:
            s += str(item) + ', '
    print(s[:-2])

def printTable(variants, criteria, data):

    max_row = []
    max_row.append(0)

    print_data = []

    head = [""]

    for c in criteria:
        max_row.append(len(c))
        head.append(c)

    print_data.append(head)

    for i in range(len(variants)):
        tmp = []
        tmp.append(variants[i])
        if len(variants[i]) > max_row[0]:
            max_row[0] = len(variants[i])

        for j in range(len(data[i])):
            if type(data[i][j]) == float:
                if int(data[i][j]) == data[i][j]:
                    str_d = str(int(data[i][j]))
                else:
                    str_d = "{0:.2f}".format(data[i][j])
            else:
                str_d = str(data[i][j])
            tmp.append(str_d)
            if len(str_d) > max_row[j+1]:
                max_row[j+1] = len(str_d)

        print_data.append(tmp)

    print_data.insert(1, [i*'–' for i in max_row])

    s = ''
    for i in range(len(print_data)):
        for j in range(len(print_data[0])):
            s += print_data[i][j] + (max_row[j] - len(print_data[i][j])) * ' ' + ' | '
        s += '\n'

    print(s)

