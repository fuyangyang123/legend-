from random import*
TIMES = 10000
my_first_choice_n=0
my_change_choice_n=0
for i in range(TIMES):
	car_inDoor=randint(0,2)
	my_guess=randint(0,2)
	if car_inDoor==my_guess:
		my_first_choice_n+=1
	else:
		my_change_choice_n+=1
print("不改选择:{}".format(my_first_choice_n/TIMES))
print("更改选择:{}".format(my_change_choice_n/TIMES))
