# Python3 program to illustrate Count of N-length strings
# consisting only of vowels sorted lexicographically
 
# to keep the string in lexicographically sorted order use
# start index
# to add the vowels starting the from that index

def countstrings(n, start):

   

    # base case: if string length is 0 add to the count

    if n == 0:

        return 1

    cnt = 0

     

    # if last character in string is 'e'

    # add vowels starting from  'e'

    # i.e    'e','i','o','u'

    for i in range(start, 5):

       

        # decrease the length of string

        cnt += countstrings(n - 1, i)

    return cnt

     

def countVowelStrings(n):

   

    #  char arr[5]={'a','e','i','o','u'};

    # starting from index 0 add the vowels to strings

    return countstrings(n, 0)
 

n = 2

print(countVowelStrings(n))
