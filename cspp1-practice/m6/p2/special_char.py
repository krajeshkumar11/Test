"""
special_char
"""
S = input()
S1 = ""
I = 0
while I < len(S):
    if S[I] == '!' or S[I] == '@' or S[I] == '#' or S[I] == '$':
        S1 = S1 + ' '
    elif S[I] == '%' or S[I] == '^' or S[I] == '&' or S[I] == '*':
        S1 = S1 + ' '
    else:
        S1 = S1 + S[I]
    I = I + 1
print(S1)
