'''Exercise 1'''

# import json

# first = ['Ani', 'Jessy ', 'Ben'] 
# second = [1,2,3]
# mydict = {}
# for i, j  in zip(second, first):
#     mydict.setdefault(i, j)
# with open('dict.json', 'w') as file:
#     json.dump(mydict, file)
# f = open('dict.json')
# print(json.load(f))

'''Exercise 2'''

# lyrics = 'I was from the city, she was from the outside I was from the North, she was from the South sideI looked in the mirror, I said man Im alright Little did I know Id be crying all night Cause I was from the city, she was from the outside I was from the North, she was from the South side I looked in the mirror, I said man Im alright Little did I know Id be crying all night Cause I was from the city'
# with open('dict.json', 'w') as file:
#     json.dump(lyrics, file)
# f = open('dict.json')
# print(json.load(f))

'''Exercise 3'''

# num = int(input('Input The Number - '))
# sum = 0
# for i in range(1, num + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# with open('dict.json', 'w') as file:
#     json.dump(sum, file)
# f = open('dict.json')
# print(json.load(f))

'''Exercise 4'''

# text = input('Input Text -  ')
# vowels = 'a', 'i', 'e', 'o', 'u'
# sum = 0
# for i in text:
#     if i in vowels:
#         sum += 1
# with open('dict.json', 'w') as file:
#     json.dump(sum, file)
# f = open('dict.json')
# print(json.load(f))

'''Exercise 5'''

# text = 'Another pause and more eying and siding around each other'.lower()
# list1 = ['another', 'and']
# list2 = []
# mydict = {}
# all = text.split()
# sum1 = 0
# sum2 = 0
# for i in all:
#     if i == 'another':
#         sum1 += 1
#     if i == 'and':
#         sum2 += 1
# list2.append(sum1)
# list2.append(sum2)
# for i, j in zip(list1, list2):
#     mydict.setdefault(i, j)
# with open('dict.json', 'w') as file:
#     json.dump(mydict, file)
# f = open('dict.json')
# print(json.load(f))

'''Exercise 6'''

# my_list = ['a', 'b', 'c', 'a', 'b']
# mylist = []
# for i in my_list:
#     if i not in mylist:
#         mylist.append(i)
# with open('dict.json', 'w') as file:
#     json.dump(mylist, file)
# f = open('dict.json')
# print(json.load(f))


'''Exercise 7'''

# Es meky chgidem vonc lucem Ab jan
    
