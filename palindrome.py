def palind(r):
    e = len(r) - 1
    s = 0
    while s<e:
        if r[e]!= r[s]:
            return False
        s += 1
        e -= 1
    return True
r = (9,8,7,6,6,7,8,9)
if palind(r):
    print ("It is a palindrome.")
else:
    print ("It is not a palindrome")
