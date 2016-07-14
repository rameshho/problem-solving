__author__ = 'rameshho'

'''
    It will list prime numbers starting from 2 to the number which you give
'''
def primenumbers ( endcount ):
    list_of_prime = [2]
    if not isinstance(endcount, int):
        raise TypeError
    for num in range ( 3, endcount ):
        for primes in list_of_prime:
            if not num % primes:
                break
        else:
            list_of_prime.append ( num )
    #print(list_of_prime)
    return list_of_prime


if __name__ == "__main__":
    Number = input("Enter the number of prime numbers you want : ")
    print(Number)
    #print(type(Number))
    print( primenumbers(Number) )