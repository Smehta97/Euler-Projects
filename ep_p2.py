#Euler Project p2
#Find sum of all even fibonacci number under 4 million

def sum(a_list):
    result = 0
    for x in range(len(a_list)):
        result += a_list[x]
    return result

def fib_lin(a):
	if (a <= 1):
		return a
	else:
		prev = 0
		current = 1
		i = 1
		while (i < a):
			next = current + prev
			prev = current
			current = next
			i = i + 1
		return current

itr = 0
my_list = []

for i in range(40):
    res = fib_lin(i)
    if res < 4000000:
        if res % 2 is 0 and res not in my_list:
            my_list.append(res)
    else:
        break;

print sum(my_list)
