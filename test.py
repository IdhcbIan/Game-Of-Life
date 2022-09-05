"""
A = [(5,5), (5,1)]
B = [(5,5), (3,3), (5,1)]

s = sum(x in A for x in B)
print(s)

"""
"""
w = 0
h = 0

x = 1
y = 1

block = int(input())

all = []

while h <1000:
    if w < 1000:
        all.append((x,y))
        y += 1
        w += block
    elif h < 1000:
        x += 1
        w = 0
        h += block
        y = 0
        y += 1
    else:
        pass
    


print(all)

"""
"""
for i in all:
    vizinhos = [(x-1, y+1), (x, y+1), (x+1, y+1), (x-1, y), (x+1, y), (x-1, y-1), (x, y-1), (x+1, y-1) ]
    alive = []
    
    
    s = sum(x in visinhos for x in alive)
    print(s)
"""


test_list = [1, 3, 4, 6, 7]
 
remove_list = [3, 6]
 

for i in remove_list:
    try:
        test_list.remove(i)
    except ValueError:
        pass

print(test_list)
    

















