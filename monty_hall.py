from random import randint

N = 1000

def simulate(N):
    K = 0

    for x in range(0, N) :
        doors = [0] * 3
        car = randint(0,2)
        doors[car] = 1
        
        my_choice = randint(0,2);
        #print('Car: ', car)
        #print('Me: ', my_choice)
        
        monty_choice = randint(0,2)
        
        while True:
            monty_choice = randint(0,2)
            if monty_choice != my_choice and monty_choice != car :
                break
            else :
                continue
                
        #print('Monty: ', monty_choice)
        
        # I switch
        my_choice_switch = randint(0,2)

        while True :
            my_choice_switch = randint(0,2)
            if my_choice_switch != my_choice and my_choice_switch != monty_choice :
                break
            else :
                continue

        #print('switch: ', my_choice_switch)
        
        K += doors[my_choice_switch];
        
    return float(K) / float(N)


print simulate(N)

