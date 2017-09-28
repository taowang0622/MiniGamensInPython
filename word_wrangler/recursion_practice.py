
def triangular_sum(num):
    """
    modeling the behavior of recursive function using recurrence relation
    triangular_sum(num) = num + triangular_sum(num - 1)
    """
    if num == 1:  # base case
        return 1
    return triangular_sum(num - 1) + num

def number_of_threes(num):
    """
    recurrence relation:
    number_of_threes(num) = number_of_threes(num / 10) + num % 10 == 3 ? 1 : 0
    """
    if(num == 0):
        return 0
    return number_of_threes(num // 10) + (1 if num % 10 == 3 else 0)

def is_member(my_list, elem):
    """
    recurrence relation:
    is_member(list, elem) = (list[-1] == elem) || is_member(list[:-1], elem)
    """
    if len(my_list) == 0:
        return False
    return (my_list[-1] == elem) or is_member(my_list[:-1], elem)

def remove_x(my_string):
    """
    remove_x(my_string) = (my_string[-1] == 'x' ? '': my_string[-1]) + remove_x(my_string[:-1])
    """
    if len(my_string) == 0:
        return ''
    return remove_x(my_string[:-1]) + ('' if my_string[-1] == 'x' else my_string[-1])

def insert_x(my_string):
    """
    insert_x(my_string) = my_string[0] + 'x' + insert_x(my_string[1:]) (len(my_string) >= 2)
    """
    if len(my_string) == 1:
        return my_string
    return my_string[0] + 'x' + insert_x(my_string[1:])

def list_reverse(my_list):
    """
    list_reverse(my_list) = my_list[-1] + list_reverse(my_list[1:-1]) + my_list[0] (len(my_list) >= 2)
    """
    if len(my_list) <= 1:
        return my_list
    return [my_list[-1]] + list_reverse(my_list[1:-1]) + [my_list[0]]
def test_list_reverse():
    """
    Some test cases for list_reverse
    """
    print "Computed:", list_reverse([]), "Expected: []"
    print "Computed:", list_reverse([1]), "Expected: [1]"
    print "Computed:", list_reverse([1, 2, 3]), "Expected: [3, 2, 1]"
    print "Computed:", list_reverse([2, 3, 1]), "Expected: [1, 3, 2]"

def gcd1(num1, num2):
    """
    method1:
    gcd(num1, num2) = num1 (num1 > num2 and num2 = 0)
    gcd(num1, num2) = gcd(num2, num1 % num2) (num1 > num2)
    """
    if num1 < num2:
        num1, num2 = num2, num1  #swap!!!!
    if num2 == 0:
        return num1
    return gcd1(num2, num1 % num2)

def gcd2(num1, num2):
    """
    method2:
    gcd(num1, num2) = num1 (num1 > num2 and num2 = 0)
    gcd(num1, num2) = gcd(max(num2, num1 - num2), min(num2, num1 - num2)) (num1 > num2)
    """
    if num1 < num2:
        num1, num2 = num2, num1  #swap!!!!
    if num2 == 0:
        return num1
    return gcd2(num2, num1 - num2)

def test_gcd(gcd):
    """
    Some test cases for gcd
    """
    print "Computed:", gcd(0, 0), "Expected: 0"
    print "Computed:", gcd(3, 0), "Expected: 3"
    print "Computed:", gcd(0, 2), "Expected: 2"
    print "Computed:", gcd(12, 4), "Expected: 4"
    print "Computed:", gcd(24, 18), "Expected: 6"

def slice(my_list, first, last):
    if len(my_list) - 1 >= last:
        my_list.pop()
        return slice(my_list, first, last)
    elif len(my_list) > (last - first):
        my_list.pop(0)
        return slice(my_list, first, last)
    else:
        return my_list

def test_slice():
    """
    Some test cases for slice
    """
    print "Computed:", slice([], 0, 0), "Expected: []"
    print "Computed:", slice([1], 0, 0), "Expected: []"
    print "Computed:", slice([1], 0, 1), "Expected: [1]"
    print "Computed:", slice([1, 2, 3], 0, 3), "Expected: [1, 2, 3]"
    print "Computed:", slice([1, 2, 3], 1, 2), "Expected: [2]"


print triangular_sum(3)
print number_of_threes(34534)
print number_of_threes(454)
print is_member(['c', 'a', 't'], 'e')
print is_member(['c', 'a', 't'], 'a')
print remove_x("catxxdogx")
print insert_x("catdog")
print insert_x("catdo")
print list_reverse([2, 3, 1])
print list_reverse([2, 3, 1, 4, 5])
test_list_reverse()
# test_gcd(gcd1)
test_gcd(gcd2)
test_slice()