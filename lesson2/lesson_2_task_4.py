def fizz_buzz(n):
    for x in range(1,n+1):
        a = ""
        if (x % 3 ==0):
            a = a + "Fizz"
        if (x % 5 ==0): 
            a = a + "Buzz"
        print(x, a)


fizz_buzz(20)