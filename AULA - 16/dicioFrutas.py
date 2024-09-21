# 1
print("#1")
fruits = {
    "Banana" : "amarelo",
    "Mirtilus" : "azul",
    "Laranja" : "laranja"
}

print(fruits)
print()

#2
print("#2")
print(fruits["Banana"])
print()

#3
print('#3')
fruits["Maçã"]=["vermelho"]
print(fruits)
print()

#4
fruits["Banana"]=["verde"]
print(fruits)
print()

#5
print('#5')
print(fruits.pop('Mirtilus'))
print()

#6
print('6#')
for i in fruits.keys():
    print(i)


print(fruits.keys())

#7
print('#7')
print(fruits.values())
print()

for i in fruits.values():
    print(i)

for i in fruits:
    print(fruits[i])
print()

#8
print('#8')
print("Banana" in fruits)
print()


#9
print('#9')

new_fruits = {
    'Limão': "verde",
    'Uva' : 'roxo'
}
fruits.update(new_fruits)
print(fruits)
print()

#10
print("#10")
print(len(fruits))


