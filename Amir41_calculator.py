def calculate(s):
    val = 0
    stack = []
    i = 0
    while i<len(s):
        if s[i] == "*":
            stack[-1]*= int(s[i+1])
            i += 2
        elif s[i].isnumeric():
            temp = ""
            while i<len(s) and s[i].isnumeric():
                temp += s[i]
                i += 1
            stack.append(int(temp))
        else:
            stack.append(s[i])
            i += 1
    val = 0
    op = "+"
    for ele in stack:
        if isinstance(ele, int):
            if op == 0:
                val += ele
            elif op == 1:
                val -= ele
            else:
                val *= ele
        else:
            op = ops.index(ele)
    return val





ops = ["+", "-", "*"]
s = "1*1+2-124*2-12*1"
print(calculate(s))



