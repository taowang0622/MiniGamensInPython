def make_binary(length):
    """
    :param length:
    :return: A list containing all binary representations of the specified length
    """
    # base case
    if length == 1:
        return ["0", "1"]
    # recursive case
    binary_strs = make_binary(length - 1)
    return ["0" + each for each in binary_strs] + ["1" + each for each in binary_strs]

def bin_to_dec(bin_num):
    """
    :param bin_num: a bit string
    :return: integer corresponding to the input bit string
    """
    # base case
    if len(bin_num) == 0:
        return 0
    # recursive case
    return bin_to_dec(bin_num[:-1]) * 2 + int(bin_num[-1])

def make_gray(length):
    """
    :param length:
    :return: a list containing all the RBC(reflected binary code) of the input length
    """
    if length == 0:
        return [""]
    sol_to_subprob = make_gray(length - 1)
    answer = []
    for bits in sol_to_subprob:
        answer.append("0" + bits)
    sol_to_subprob.reverse()
    for bits in sol_to_subprob:
        answer.append("1" + bits)
    return answer

def gray_to_bin(gray_code):
    """
    binary->gray:
        gray ^ (gray >> 1)
    gray->binary:
        b0 = g0 (b0 and g0 are the most significant bit respectively for binary code and gray code)
        bi = gi ^ b(i - 1) (i > 0)
    recurrence relation:
        gray_to_bin(grayCode) = grayCode[0]   (grayCode.length = 1)
        gray_to_bin(grayCode) = gray_to_bin(grayCode[:-1]) + grayCode[-1] ^ gray_to_bin(grayCode[:-1])[-1] ((grayCode.length > 1))
    :param gray_code: A gray code string
    :return: A corresponding binary code string
    """
    if len(gray_code) == 1:
        return  gray_code
    binary_code = gray_to_bin(gray_code[:-1])
    return binary_code + str(int(gray_code[-1]) ^ int(binary_code[-1]))


print make_binary(2)
print make_binary(3)
print make_binary(4)
print bin_to_dec("110")
print bin_to_dec("111")
print bin_to_dec("100")
print bin_to_dec("1111")
print make_gray(2)
print make_gray(3)
print make_gray(5)
print "gray:0011=>", gray_to_bin("0011")
print "gray:1111=>", gray_to_bin("1111")