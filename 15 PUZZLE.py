

import random
import time


#fn. to display list

def list_printer(list):
    for i in list:
        for j in i:
            if len(str(j))==1:
                print('',j,end='   ')
            elif len(str(j))==2:
                print('',j,end='  ')
        print()
                
    
    
#fn. to find index of space
        
def space_index(list):
    for i in list:
            for j in i:
                if j==' ':
                    return(list.index(i),i.index(j))

#fn. to intercchange elements
                
def element_swapper(action):
    a,b=space_index(random_list)

    if action=='left' and b!=3:
        random_list[a][b+1],random_list[a][b]=random_list[a][b],random_list[a][b+1]
    elif action=='right' and b!=0:
        random_list[a][b-1],random_list[a][b]=random_list[a][b],random_list[a][b-1]
    elif action=='up' and a!=3:
        random_list[a][b],random_list[a+1][b]=random_list[a+1][b],random_list[a][b]
    elif action=='down' and a!=0:
        random_list[a-1][b],random_list[a][b]=random_list[a][b],random_list[a-1][b]
    else:
        print('----------------------------------------------------')
        print('   INVALID ACTION, try another one')
        print('----------------------------------------------------')
    print()

    return(random_list)
        
    
#fn . to decide action according to input number

def action_decider(a):

    if a==2:
        return('down')
    elif a==8:
        return('up')
    elif a==4:
        return('left')
    elif a==6:
        return('right')



#MAIN PROGRAM STARTS


print('++++++++++++++++++++++++++15 PUZZLES++++++++++++++++++++++++++')
print()
print()
print("""Welcome to 15 puzzles

---------INSTRUCTIONS---------
>You've to arrange the given list in asscending order with sequence of actions.
>For moving up -- 8
>For moving down -- 2
>For moving left -- 4
>For moving right -- 6

COME ON.... LET'S DOO YAA..............""")
print()
print()
enter=input('Press enter to continue. ')
print()

print('Preparing puzzle',end=' ')
for i in range(8):
    print('.',end=' ')
    time.sleep(0.85)
time.sleep(0.55)
print()
print()
print('Loading contents',end=" ")
for i in range(10):
    print('.',end=' ')
    time.sleep(0.45)
print()
print()
print('-------LOADING COMPLETE-------')
print()
time.sleep(0.35)
sorted_list=[[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,' ']]
random_list=[[],[],[],[]]
list_1=[]
for i in range(4):
    l=0
    while l<4:        
        random_no=random.randint(1,15)

        if random_no not in list_1:
            random_list[i].append(random_no)
            list_1.append(random_no)
            
            l=l+1

        else:
            continue
        if len(random_list[-1])==3:
            break
        
random_list[i].append(' ')



no_of_actions=0
nodes=[]
new_list=random_list
action_list=[]

while random_list!=sorted_list:

    list_printer(random_list)
    print()
    try:
        print('----------------------')
        action_no=int(input('Enter action : '))
        print('----------------------')
        if action_no not in[1,2,3,4,5,6,7,8,9]:
            raise ValueError
    
    except ValueError:
        print()
        print('----------------------------------------------------')
        print('   INVALID ACTION, try another one')
        print('----------------------------------------------------')
        print()
        continue
        
    
    print()
    
    no_of_actions+=1
    
    action=action_decider(action_no)
    action_list.append(action)
    
    
    random_list=element_swapper(action)
    nodes.append(new_list)


else:
    list_printer(random_list)
    print('-----------------------------------------------------------------------------')
    print("""    CONGRATULATION......You've completed the puzzle""")
    print('-----------------------------------------------------------------------------')
    print()
    
    print('number of action =',no_of_actions)


print()
action_display=input('Do you want to see different actions the you took [y/n] : ')
action_display=action_display.capitalize()
print()


if action_display=='Y':
    print(action_list)

print('-----------(>_<)  THANK YOU, VISIT AGAIN  (>_<)-----------')
