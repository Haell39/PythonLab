j = 0
for i in range(5):
    j += 2
    print('i =', i, ', j =', j) 
    if j == 6: 
        break

"""
Without the break keyword, the program should loop from i = 0 to i = 4
because we used the function range(5). However with the break
keyword, the program ends prematurely at i = 2. This is because when i =
2, j reaches the value of 6 and the break keyword causes the loop to
end.
"""

# ^^ Continue
j = 0
for i in range(5):
    j = j + 2
    print('\ni = ', i, ', j = ', j)
    if j == 6:
        continue
    print("I ll be skiped in j6")