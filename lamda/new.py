# x = [10,30,32,44]
# can = lambda a,b : 
# Count a number of vowels in strings 
# Find the LCM of 2 numbers 
# Find the student with the highest result.(using dictonary)
# and practice today's function 


# Find highest the frequency of a character in a string  
text = "khanjan is Great python programmer goooddd"

freq = lambda s: max(set(s)-{" "},key=lambda ch: s.count(ch))

print(freq(text))

# Find a factorial of 5 to 10
fact = lambda x: x*fact(x-1) if x != 0 else 1

print(fact(6))

# Check Palindrome from string 
ispalin = lambda s: s == s[::-1]

print(ispalin("level"))

# List answer  will be second highest
lst1 = [10,20,320,10,430,102,43,500]

second_high = lambda lst: sorted(lst,reverse=True)[1]

print(second_high(lst1))