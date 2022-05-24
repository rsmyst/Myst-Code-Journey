tuple_1 = ("yea", 1,4,5)
print(tuple_1[2:])
print(type(3 + 1.5 + 4))
number = 25
square = number**2
square_root = number ** (1/2)
print(square, square_root)
s = 'hello'
print(s[1])
print(s[::-1])
print(s[-1])
list3 = [1,2,[3,4,'hello']]
print(list3[2][2])
list3[2][2] = "goodbye"
print(list3[2][2])

list4 = [5,6,2,1]
sort_list = list4.sort()
print(sort_list)
d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{"k2":'hell0'}}
print(d["k1"]["k2"])
d = {"m1":[{"nest_key":["this is deep",["helo"]]}]}
e = d["m1"][0]["nest_key"][1][0]
print(e)

d = {"k1":[1,2,{"k2":["this is tricky",{"tough":[1,2,["henlo"]]}]}]}
f = d["k1"][2]["k2"][1]["tough"][2][0]
print(f)

list4 = [5,4,2,1,5]
print(sorted(list4))
