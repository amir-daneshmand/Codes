def can_construct(target, nums):
    table = [False]*(target+1)
    table[0] = True
    for i in nums:
        if i <= target:
            table[i] = True

    for i in range(1, len(table)):
        if table[i]:
            for num in nums:
                if i+num < len(table):
                    table[i+num] = True

    return table[-1]

def count_construct(target, nums):
    table = [0]*(target+1)
    table[0] = 1
    # for i in nums:
    #     if i <= target:
    #         table[i] = 1

    for i in range(len(table)):
        for num in nums:
            if i+num < len(table):
                table[i+num] += table[i]

    return table[target]

def how_sum(target, nums):
    table = [False]*(target+1)
    elements = {i:[] for i in range(target+1)}
    table[0] = True

    for i in range(len(table)):
        if table[i]:
            for num in nums:
                if i+num <= target:
                    table[i+num] = True
                    elements[i+num] = elements[i]+[num]

    return elements[target]


def best_sum(target, nums):
    table = [False]*(target+1)
    elements = {i:[] for i in range(target+1)}
    table[0] = True

    for i in range(len(table)):
        if table[i]:
            for num in nums:
                if i+num <= target:
                    table[i+num] = True
                    if elements[i+num] == [] or len(elements[i]+[num]) <= len(elements[i+num]):
                        elements[i+num] = elements[i]+[num]

    return elements[target]


def can_construct_word(target, word_bank):
    table = [False]*(len(target) + 1)
    table[0] = True
    for i in range(len(table)):
        if table[i]:
            string = target[i:]
            for word in word_bank:
                try:
                    idx = string.index(word)
                    # print(string, word, idx)
                except:
                    idx = None

                if idx == 0:
                    table[i+len(word)] = True
    return table

def count_construct_tabulated(target_word, word_bank):
    table = [0]*(len(target_word)+1)
    table[0] = 1

    for i in range(len(table)):
        if table[i] != 0:
            suffix = target_word[i:]
            for word in word_bank:
                try:
                    idx = suffix.index(word)
                except:
                    idx = None
                if idx == 0:
                    table[i+len(word)] += table[i]
    return table


target = 8
nums = [1, 2, 3, 4, 5]
print(can_construct(target, nums))
print(count_construct(target, nums))
#
# target = 8
# nums = [2,3,5]
# print(how_sum(target, nums))
# print(best_sum(target, nums))
#
# target_word = 'abcdef'
# word_bank = ['ab', 'abc','cd', 'def', 'abcd']
# print(can_construct_word(target_word, word_bank))
# print(count_construct_tabulated(target_word, word_bank))
#
# target_word = 'purple'
# word_bank = ['purp', 'p','ur', 'le', 'purpl']
# print(can_construct_word(target_word, word_bank))
# print(count_construct_tabulated(target_word, word_bank))
