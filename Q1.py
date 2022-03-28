# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 14:52:02 2021

@author: acer
"""
#Q1. If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

sum=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        sum+=i
print(sum)



#Q2. Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib(n):
    a=1
    b=2
    sum=0

    if n<0:
        print("Incorrect")
    elif n==1:
        sum=a
        return sum
    else:
        for i in range(1,n):
          f=a+b
          a=b
          b=f
          if a%2==0 and f<4000000:
              sum+=a
        return sum
print(fib(4000000))



#Q10. The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

sum=0
for num in range(1, 20):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           sum+=num
print(sum)


#Q9. A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

for a in range(0,1001):
    for b in range(a,1001):
        for c in range(b,1001):
            if(a+b+c==1000 and a**2+b**2==c**2):
                x=a*b*c
print(x)
    
   

#Q6. The sum of the squares of the first ten natural numbers is,
#The square of the sum of the first ten natural numbers is,
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

       
n=int(input())
z=(n*n)+n
x=(z*((2*n)+1))//6
y= z//2
print((y*y)-x)


#Q7. By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

for n in range(1,9):
    if n>1:
      for i in range(2,n):
        if n%i==0:
          break
        else:
          x=i
print(x)


#Q8. The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
def split(word):
    return [char for char in word]
    
s="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
a=split(s)
for i in range(len(a)-1):
    for j in range(i,i+4):
        print(j)
        

#Q7. By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            continue
    return True

p = 0
for x in range(10002):
    if is_prime(x):
        if p == 10001:
            print(x)
            break
        p += 1   
        
        
#Q5. 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
for i in range(1,11):
    if n%i==0:
        print(n)
        


    
        
        
    

    
    