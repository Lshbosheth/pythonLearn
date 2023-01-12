message = 'hello Python World !  '
print(message.title())
print(message.upper())
print(message.lower())  # sass
print(message.rstrip())  # sass
aa = "dasdsads'a"
print(aa)
aa = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.” '
print(aa)
famous_person = 'Albert Einstein once'
message = '“A person who never made a mistake never tried anything new.”'
print(famous_person + ' said, ' + message)
print('\t' + famous_person.strip() + '\t' + ' said, ' + message)
print(famous_person.rstrip())
print(famous_person.lstrip())
print(famous_person.lower())
print(famous_person.upper())
print(famous_person.title())
age = 23
message = "Happy " + str(age) + 'rd Birthday!'
print(message)
print(3 / 2)
print(3.0 / 2)
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1].title())
message = "My first bicycl was a " + bicycles[0].title() + "."
print(message)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('xxxxx')
print(motorcycles)
motorcycles.insert(2, 'ffffff')
print(motorcycles)
del motorcycles[1]
print(motorcycles)
delPop = motorcycles.pop()
print(delPop)
print(motorcycles)
motorcycles.remove('ffffff')
print(motorcycles)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
aa = ['fsad', 'dadji', 'dakndna', 'dadabsda']
print(sorted(aa))
print(aa)
aa.reverse()
print(aa)
print(len(aa))
magicaians = ['alice', 'david', 'carolina']
for magicaiian in magicaians:
    print(magicaiian)
for e in magicaians:
    print(e.title() + ', that was a great trick!')
for value in range(1, 5):
    print(value)
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
list1 = []
for value in range(1, 11):
    list1.append(value ** 2)
print(list1)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
ff = [value ** 2 for value in range(1, 11)]
print(ff)
print(list(range(1, 21)))
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:2])
print(players[2:])
print(players[-3:])
my_foods = ['pizza', 'falafel', 'carrot', 'cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
my_foods.append('lk')
friend_foods.append('aa')
print(my_foods)
print(friend_foods)









