S = int(input())

s = S % 60
h = (21 + S / 60) % 24
print('{:0=2}:{:0=2}'.format(int(h),int(s)))

