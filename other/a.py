s = list(map(int, input().split()))
result = "Even" if (s[0] * s[1]) % 2 == 0 else "Odd"
print(result)