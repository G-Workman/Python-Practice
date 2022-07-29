#!/usr/bin/env python3

def q1(sentence):
    '''
    Given a string of multiple words separated by single spaces,
    return a new string with the sentence reversed. The words    
    themselves should remain as they are. For example, given
    'it is accepted as a masterpiece on strategy', the returned
    string should be 'strategy on masterpiece a as accepted is it'.
    '''

    backwards = sentence.split()[::-1]
    l = []
    for i in backwards:
        l.append(i)
    return (" ".join(l))

def q2(n):
    '''
    Given a positive integer, return its string representation with
    commas seperating groups of 3 digits. For example, given 65535
    the returned string should be '65,535'.
    '''

    return  "{:,}".format(n)
    pass


def q3(lst0, lst1):
    '''
    Given two lists of integers, return a sorted list that contains
    all integers from both lists in descending order. For example,
    given [3,4,9] and [8,1,5] the returned list should be [9,8,5,4,3,1].
    The returned list may contain duplicates.
    '''
    combine = lst0 + lst1
    combine.sort(reverse = True)
    return combine

def q4(s1,s2,s3):
    '''
    Given 3 scores in the range [0-100] inclusive, return 'GO' if
    the average score is greater than 50. Otherwise return 'NOGO'.
    '''
    add = (s1 + s2 + s3)/3
    if add > 50:
        return 'GO'
    return 'NOGO'

def q5(integer, limit):
    '''
    Given an integer and limit, return a list of even multiples of the
    integer up to and including the limit. For example, if integer==3 and
    limit==30, the returned list should be [0,6,12,18,24,30]. Note, 0 is
    a multiple of any integer except 0 itself.
    '''
    nolist = []
    newlist = []
    x =  list(range(0,limit+1,integer))

    for i in x:
        i = int(i)
        if i % 2 != 0:
            nolist.append(int(str(i)))
        else:
            newlist.append(int(str(i)))
    return newlist

def q6(f0, f1):
    '''
    Given two filenames, return a list whose elements consist of line numbers
    for which the two files differ. The first line is considered line 0.
    '''
    diffs = []
    linenum = 0
    with open(f0) as fp0:
        with open(f1) as fp1:            
            file0 = fp0.readlines()
            file1 = fp1.readlines()
    for i in file0:
        if i != file1[linenum]:
            diffs.append(linenum)
        linenum += 1

    return diffs

def q7(lst):
    ''' 
    Return the first duplicate value in the given list.
    For example, if given [5,7,9,1,3,7,9,5], the returned value should
    be 7.
    '''
    ''' 
    num_set = set()
    no_duplicate = -1

    for i in range(len(lst)):

        if lst[i] in num_set:
            return lst[i]
        else:
            num_set.add(lst[i])

    return no_duplicate

    '''
    seen = []
    for i in lst:
        if i in seen:
            return i
        else:
            seen.append(i)

def q8(strng):
    ''' 
    Given a sentence as a string with words being separated by a single space,
    return the length of the shortest word.
    '''
    newstrng =  strng.split(' ')
    num = min(newstrng, key=len)
    num = len(num)
    return num 

def q9(strng):
    ''' 
    Given an alphanumeric string, return the character whose ascii value
    is that of the integer represenation of all of the digits in the string
    concatenated in the order in which they appear. For example, given
    'hell9oworld7', the returned character should be 'a' which has
    the ascii value of 97.
    '''
        
    chars = []
    for i in strng:
        if i.isnumeric():
            chars.append(i)

    return chr(int(''.join(chars)))

def q10(arr):
    ''' 
    Given a list of positive integers sorted in ascending order, return
    the first non-consecutive value. If all values are consecutive, return
    None. For example, given [1,2,3,4,6,7], the returned value should be 6. 
    '''
    i = 1 
    for x in arr:
        if i < len(arr) and arr[i] - arr[i-1] != 1:
            return arr[i]
        i += 1
    return None
