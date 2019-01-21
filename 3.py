def palindrome(a):
    c = a[::-1]
    if a == c:
        print("true")
    else:
        print("false")
palindrome("ehe")
palindrome("eheh")
