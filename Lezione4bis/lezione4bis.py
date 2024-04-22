
# Dato un intero x, restituisce True se x è palindromo, e False altrimenti.

def is_palindrome(x: int) -> bool:
    s: str = str(x)
    s1 = "".join(reversed(s))
    return s == s1
out = is_palindrome(-121)
print(out)

""" metodo Prof

s: str = str(x)
i: int = 0
while i < (s_lenght // 2): # for i in range(len(s))
    j = len(s) - (i+1)
    if s[i] != s[j]:
        return False
    i += 1
return True """

