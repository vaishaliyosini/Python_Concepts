names = ["Robert Downey Jr", "Chris Evans", "Chris Hemsworth", "Mark Ruffalo"]
heros = ["Ironman", "Captain America", "Thor", "Hulk"]

# traditional dictionary using zip()
d = {}
for name, hero in zip(names, heros):
    d[name] = hero
for name in d:
    print(name + " - " + d[name])

'''
prints 
Mark Ruffalo - Hulk
Chris Hemsworth - Thor
Robert Downey Jr - Ironman
Chris Evans - Captain America
'''
print('next')
# meet dict comprehension
d = {name: hero for name, hero in zip(names, heros)}
for name in d:
    print(name + " - " + d[name])

'''
prints 
Mark Ruffalo - Hulk
Chris Hemsworth - Thor
Robert Downey Jr - Ironman
Chris Evans - Captain America
'''
print('next')
# dict comprehension with condition
d = {name: hero for name, hero in zip(names, heros) if name != "Mark Ruffalo"}
for name in d:
    print(name + " - " + d[name])

'''
prints 
Chris Hemsworth - Thor
Robert Downey Jr - Ironman
Chris Evans - Captain America
'''
