class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def int2str(num):
            return str(num)

        def str2intList(string):
            int_list = []
            for i in string:
                int_list.append(int(i))
            return int_list

        def intList2int(intList):
            string = ""
            for i in intList:
                string += str(i)
            if string:
                return int(string)
            else:
                return 0
        A = str2intList(int2str(abs(dividend)))
        a = str2intList(int2str(abs(divisor)))

        len_A = len(A)
        window = len(a)+1
        print("window: ", window)
        res = []

        if len_A < window-1:
            return 0
        quotient = 0
        i = 0
        rem = 0
        while i < len_A:
            print("i, len_A", i, len_A)
            if i + window<len_A:
                temp = A[i:i + window]
            else:
                temp = A[i:]
            if rem == 0:
                num_list = []
            else:
                num_list = str2intList(int2str(rem))
            num_list.extend(temp)
            num = intList2int(num_list)
            print("num", num)
            i += window
            print("quo", quotient)
            quotient = 0
            while num >= abs(divisor):
                num -= abs(divisor)
                quotient += 1
            rem = num
            res.append(quotient)
            print("quooo", quotient)
            print("rem", rem)

        if (divisor >= 0 and dividend >= 0) or (divisor <= 0 and dividend <= 0):
            return intList2int(res[0:])
        else:
            return 0-intList2int(res[0:])

S = Solution()
dividend = 2147483647

divisor = 2
result  = S.divide(dividend, divisor)

print("result = ", result)