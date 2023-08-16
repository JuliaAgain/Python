#Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#print(*find_farthest_orbit(orbits))
#Вывод:
#2.5 10
def find_farthest_orbit(list_of_orbits):
    squares = [i[0]*i[1] for i in list_of_orbits if i[0]!= i[1]]
    maxS = max(squares)
    for cort in list_of_orbits:
        if cort[0]*cort[1] == maxS:
            return cort
    

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

