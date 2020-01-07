tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


colWidth = [len(max(words_list, key = len)) for words_list in tableData]

def printTable(data):
    for i in range(len(data[0])):
        for word_list in data:
            print(word_list[i].rjust(3), end=' ')
        print('')

print(len(tableData))

printTable(tableData)