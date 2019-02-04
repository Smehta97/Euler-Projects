#Euler Project p1
#Q: Sum all multiples of 3 or 5 under 1000

def sum(a_list):
    result = 0
    for x in range(len(a_list)):
        result += a_list[x]
    return result

my_list = []
for i in range(1000):
    if i%3 is 0 or i%5 is 0 and i not in my_list:
        my_list.append(i)

print sum(my_list)
