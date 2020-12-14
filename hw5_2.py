lines_n = 0
words_n = 0
for line in open('new_list.txt', 'r'):
    lines_n += 1
    words = line.split()
    words_n += len(words)
print(lines_n)
print(words_n)

#так и не понял, как посчитать слова в каждой строке.
