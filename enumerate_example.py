# for index, character in enumerate("abacdefgh"):
#     print(index, character) #enumerate returns character with index
for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)
