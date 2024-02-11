#loop to print from 1 to 10

output = []
for i in range(0,11):
    output.append(i)
print(output)

#Calculate Sum: Create a loop to calculate the sum of numbers from 1 to 50.

#for i in range(1,51):
    #print(sum(range(1,51))) #not correct code since sum will give back the sum in a sequence for each iteration in the loop. It will keep on producing the sum for all numbers from 1 to 50

#correct code for Calculate Sum: Create a loop to calculate the sum of numbers from 1 to 50.
    
total = 0
for i in range(1,51):
    total += i
print(total)

#Print Even Numbers: Print all even numbers between 1 and 20 using a for loop.

total_even = []
for i in range(0,21,2):
    total_even.append(i)
print(total_even)