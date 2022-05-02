def solve(a, b, c, x):
  q = x // (a + c)
  r = x % (a + c)
  return (q * a + min(a, r)) * b


a, b, c, d, e, f, x = map(int, input().split())

takahashi = solve(a, b, c, x)
aoki = solve(d, e, f, x)

if takahashi > aoki:
  print("Takahashi")
elif takahashi < aoki:
  print("Aoki")
else:
  print("Draw")
