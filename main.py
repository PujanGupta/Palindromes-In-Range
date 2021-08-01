from itertools import count

def getPalindrome():
    yield 0
    for digits in count(1):
        first = 10 ** ((digits - 1) // 2)
        for s in map(str, range(first, 10 * first)):
            yield int(s + s[-(digits % 2)-1::-1])


def getAllPalindromesinRange(start, end):
    palindromGenerator = getPalindrome()
    palindromeList = []
    
    for palindrome in palindromGenerator:
        if palindrome > end:
            break
        if palindrome < start:
            continue
        
        palindromeList.append(palindrome)
        
    return palindromeList


while True:
    start = int(input("Start: "))
    end = int(input("End: "))
    print(f'The palindrome numbers in between {start} and {end} are {getAllPalindromesinRange(start, end)}')
