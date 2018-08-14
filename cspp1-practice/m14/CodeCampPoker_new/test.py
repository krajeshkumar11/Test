def sum(n):
    sum = 0
    while n:
        sum += n%10
        n //=10
    return sum

a = [345,567,709]

print(max(a))
