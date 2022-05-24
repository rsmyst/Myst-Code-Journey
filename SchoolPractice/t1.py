# dict1 = {1:"key1", 2:"help me"}
# dict2 = {3:"sdhf", 4:"101023"}
# # for i in dict1:
# #     print(dict1[i])
# #     i+1
# # print(dict1.items())
# #
# #
# # for key in dict1:
# #    print(key, " : ",dict1[key])
# #
# # for key, val in dict1.items():
# #    print(key, ":", val)
# # print(dict1)
# # dict1[1] = "Hello"
# # print(dict1)
# # dict1[5] = "New"
# # print(dict1)
# print(dict1)
#
# # dict1.pop(2)
# # print(dict1)
#
# #print("key1" in dict1)
# print(len(dict1))
# seq = (1,"2"),(3, "491")
# d3 = dict(seq)
# print(d3)
# print(d3.get(0))
# d3.update(dict1)
# print(d3)
# del d3[1]
# print(d3)
# d3.update(dict2)
# print(d3)
# d4 = d3.copy()
# print(d4)
# x = d3.setdefault(8, "sdhfsdh")
# print(x)
# l = [1,3,4,6,5,10]
# poop = dict.fromkeys(l)
# print(poop)
# print(type(l))
# print(type(poop))
st = input("Enter a string: ")
dic = {} #creates an empty dictionary
for ch in st:
    if ch in dic: #if next character is already in dic
        dic[ch] += 1
    else:
        dic[ch] = 1 #if ch appears for the first time
for key in dic:
    print(key,':',dic[key])