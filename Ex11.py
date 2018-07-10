def check_prime(number):
    for I in (range(2,number)):
        if (number % I) == 0:
            return("Not Prime!")
            break
    return("It's a prime number!")
    


number = input("Enter a number? ")
number = int(number)

print(check_prime(number))
