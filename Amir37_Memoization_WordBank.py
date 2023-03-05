def can_construct(target, word_bank):
    if target == '':
        return True
    for word in word_bank:
        try:
            idx = target.index(word)
        except:
            idx = None
        if idx == 0:
            if can_construct(target[len(word):], word_bank) == True:
                return True

    return False


def can_construct_memoized(target, word_bank, memo = {}):
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in word_bank:
        try:
            idx = target.index(word)
        except:
            idx = None
        if idx == 0:
            suffix = target[len(word):]
            if can_construct_memoized(suffix, word_bank, memo) == True:
                memo[suffix] = True
                return True
    memo[target] = False
    return False


def count_construct_memoized(target, word_bank, memo = {}):
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    counter = 0
    for word in word_bank:
        try:
            idx = target.index(word)
        except:
            idx = None
        if idx == 0:
            suffix = target[len(word):]
            ans = can_construct_memoized(suffix, word_bank, memo)
            counter += ans
    memo[target] = counter
    return counter


def all_construct(target, word_bank):
    if target == "":
        return [[]]
    result = []
    for word in word_bank:
        try:
            idx = target.index(word)
        except:
            idx = None
        if idx == 0:
            suffix = target[len(word):]
            res = all_construct(suffix, word_bank)
            for i in res:
                result.append([word] + i)

    return result


def all_construct_memoized(target, word_bank, memo={}):
    if target == "":
        return [[]]
    if target in memo:
        return memo[target]
    result = []
    for word in word_bank:
        try:
            idx = target.index(word)
        except:
            idx = None
        if idx == 0:
            suffix = target[len(word):]
            res = all_construct_memoized(suffix, word_bank, memo)
            memo[suffix] = res
            for i in res:
                result.append([word] + i)

    return result






word_bank = {'pot', 'tat', 'o', 'at', 'potat', 'potato'}
target = "potato"

# word_bank = {'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'}
# target = "skateboard"
#
word_bank = {'e', 'ee', 'eee'}
target = "eeeeeeeeeeeeeeeeeeeef"


print(can_construct(target, word_bank))
print(can_construct_memoized(target, word_bank))
print(count_construct_memoized(target, word_bank))
print(all_construct(target, word_bank))
print(all_construct_memoized(target, word_bank))
