
numbers = (["1","2","3","4","5","6"])

numbers += "7"#addition 
print(numbers)


del(numbers[0])#deletion
print(numbers)

del(numbers[4:])#deletion
print(numbers)


numbers.append('6')#list append / addition 
print(numbers)

numbers.append(['7','8']) #adding a list
print(numbers)

numbers.extend(['9','10','11'])#extends list at end 
print(numbers)

numbers.insert(0, '1')#inserts number into an index
print(numbers) 

Number = (["4","9","9","0","2","0","1"])
Number.sort()
print(Number)

Number.sort(reverse=True)# sorts numbers in reverse
print(Number)


print(Number.count(9))                                 

Number.remove("4")# removes an index by string 
print(Number)

