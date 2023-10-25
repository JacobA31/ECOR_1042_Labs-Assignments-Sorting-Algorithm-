# ECOR 1042 Lab 1


__author__ = "Ihsan Aydin"
__student_number__ = "101264856"

# ======================================================
# Exercise 1


def replicate(x: str) -> str:
    """Returns the replicate of the string according to the number of letters

    Preconditions: x should be string

    Examples:
    >>> replicate('a')
    'a'
    >>> replicate('abc')
    'abcabcabc'
    >>> replicate('abcdef')
    'abcdefabcdefabcdefabcdefabcdefabcdef'
    """
    return x * len(x)

# ======================================================
# Exercise 2


def repeat_separator(word: str, sep: str, n: int) -> str:
    """Returns the word by multiplying the given number and seperates each word
    with given string

    >>>Preconditions: word and sep contains at least one character, n >= 0

    Examples:
    >>> repeat_separator("Word", "X", 3)
    "WordXWordXWord"
    >>> repeat_separator("This", "And", 2)
    "ThisAndThis"
    >>> repeat_separator("This", "And", 1)
    "This"
    """
    for i in range(n - 1):
        print(word + sep, end="")
    print(word)


# ======================================================
# Exercise 3

def has_pair(s: str, ch: str) -> bool:
    """Returns true or false depending on if the given character has two occurance
    next to each other

    Preconditions: ch is a single character string, s has at least two characters

    Examples:
    >>> has_pair('abccd', 'c')
    True
    >>> has_pair('abcdc', 'c')
    False
    >>> has_pair('aabc','b')
    False
    """
    k = 0
    for i in s:
        if i == ch:
            k += 1
            if k == 2:
                return True
        else:
            k = 0
    return False

# ======================================================
# Exercise 4


def middle_way(a: list, b: list) -> list:
    """Returns a new list containg the middle number of 2 list

    Preconditions: a and b lists contains only 3 values

    Examples:
    >>> middle_way([1,2,3],[4,5,6])
    [2,5]
    >>> middle_way([1,3,3],[4,7,6])
    [3,7]
    >>> middle_way([1,6,3],[4,1,6])
    [6, 1]
    """
    new_list = [a[1], b[1]]
    return new_list

# ======================================================
# Exercise 5


def make_ends(lis: list) -> list:
    """Returns a new list that contains the first and last value of given list

    Preconditions: lis must be a non-empty list

    Example:
    >>> make_ends([4,5,6,7])
    [4, 7]
    >>> make_ends([3,6,71])
    [3, 71]
    >>> make_ends([6,7,10,5,2,6])
    [6,6]
    """
    new_list = [lis[0], lis[-1]]
    return new_list

# ======================================================
# Exercise 6


def common_end(lis1: list, lis2: list) -> bool:
    """Returns true if both lists have the same first value or last

    Preconditions: lis1 and lis2 must be list

    Example:
    >>> common_end([1,2],[1,5,7,8])
    True
    >>> common_end([3,2],[5,5,7,8,2])
    True
    >>> common_end([3,2,2,4],[5,5,7,8,2])
    False
    """
    if lis1[0] == lis2[0] or lis1[-1] == lis2[-1]:
        return True
    else:
        return False

# ======================================================
# Exercise 7


def count_evens(n: list) -> int:
    """Returns the number of even numbers in the given list

    Preconditions: n is a non-empty list

    Example:
    >>> count_evens([1,4,7,8,1,2,3])
    3
    >>> count_evens([3,5,4,1,2,4,2])
    4
    >>> count_evens([3,10,20])
    2
    """
    x = 0
    for i in n:
        if i % 2 == 0:
            x += 1
        else:
            x = x
    return x


# ======================================================
# Exercise 8

def big_diff(lis: list) -> int:
    """Returns the difference between the biggest and lowest value inside the list

    Precondition: lis contains at least 2 integers

    Examples:
    >>> big_diff([10, 3, 5, 6])
    7
    >>> big_diff([3, 9, 7])
    6
    >>> big_diff([1, 25, 17])
    24
    """
    max_value = lis[0]
    min_value = lis[0]
    for i in range(1, len(lis)):
        if lis[i] > max_value:
            max_value = lis[i]
        elif lis[i] < min_value:
            min_value = lis[i]
    return max_value - min_value

# ======================================================
# Exercise 9


def has22(a: list) -> bool:
    """Returns true if the list contains 2 next to a 2

    Examples:
    >>> has22([1,2,2,3])
    True
    >>> has22([4,2,3,2])
    False
    >>> has22([10,2,4,2,2])
    True
    """
    for i in range(0, len(a) - 1, 1):
        if a[i] == 2 and a[i + 1] == 2:
            return True
    return False


# ======================================================
# Exercise 10

def centered_average(a: list) -> float:
    """Returns the centered average of the numbers in the list by deleting the
    biggest and smallest values

    Precondition: a contains at least 3 values

    Examples:
    >>> centered_average([1,1,5,5,10,8,7])
    5.2
    >>> centered_average([2,4,5,8,7])
    5.33
    >>> centered_average([15,4,7,2,24])
    8.67
    """
    new = 0
    for i in range(0, len(a)):
        new = new + a[i]
    return (new - max(a) - min(a)) / (len(a) - 2)


# ======================================================
# Exercise 11

def bank_statement(lis: list) -> list:
    """Returns a new list of sum of the deposits, sum of the withdrawals, and
    account balance by given the list(transactions)
    
    Examples:
    >>> bank_statement([500,045,-50,074,100.21])
    [600.25, -50.07, 550.18]
    >>> bank_statement([15.0,-17.3,10])
    [25.0, -17.3, 7.7]
    >>> bank_statement([1500.5,100.05,-1000,-50.0567])
    [1600.55, -1050.06, 550.49]
    """
    dep = 0
    wit = 0
    for i in range(0, len(lis), 1):
        if lis[i] > 0:
            dep = dep + lis[i]
        elif lis[i] < 0:
            wit = wit + lis[i]
    accbalance = [round(dep, 2), round(wit, 2), round(dep + wit, 2)]
    return accbalance

# ======================================================
# Exercise 12


def reverse(lis: list) -> list:
    """Returns the reverse of the given list
    
    Examples:
    >>> reverse([4, 2, 3, 2])
    [2,3,2,4]
    >>> reverse([1,2,3,4,5,6,7,8])
    [8, 7, 6, 5, 4, 3, 2, 1]
    >>> reverse([3,2,1])
    [1,2,3]
    """
    rev_lis = []
    for i in lis:
        rev_lis = [i] + rev_lis
    print(rev_lis)



