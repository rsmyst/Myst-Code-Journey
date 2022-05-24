mynums = [1,2,3,4,5,1,9]
print(list(map(lambda nums:nums/5, mynums)))

print(list(filter(lambda n: n%2 == 0, mynums)))