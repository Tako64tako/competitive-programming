S = int(input())
for i in range(1,S+1):
    result = "FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i
    print(result)