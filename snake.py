import random
import os
import time
from threading import Thread

length = 5
initial_length = length
alive = True
apple_x = 0
apple_y = 0
opposite_direction = "L"
last_direction = "R"
map_width=25
map_height=25
initial_x = 0
initial_y = 0
mode = "border" # Can be border or loop

map = [[]]
for y in range(map_height+1):
    for x in range(map_width+1):
        map[y].append(" ")
    map.append([])
del map[-1]

coords = []
for x in range(length+1):
    coords.append([map_width+1,map_height+1])
coords.append([initial_x,initial_y])

def draw_map(new_fruit, new_snake_x, new_snake_y, old_snake_x, old_snake_y):
    global apple_x, apple_y, length, initial_length,last_direction,coords

    if length == ((map_width+1) * (map_height+1)) - 1:
        print("YOU WON!")
        return 3
    
    while new_fruit == True: # Loop until Fruit is not on the snakes body
        apple_x = random.randint(0,map_height) # Random x coord
        apple_y = random.randint(0,map_height) # Random y coord
        #print(apple_x,apple_y)
        for x in range(length-1): # Loop over each pixel of the snakes body
            check_snake_x = coords[len(coords)-1-x][0] # Currenty checking x coord
            check_snake_y = coords[len(coords)-1-x][1] # Currenty checking y coord
            if apple_x == check_snake_x and apple_y == check_snake_y: # If apple is on this snake part
                #print("Apple on snake at ", check_snake_x,check_snake_y) 
                new_fruit = True # Loop again
                break # Exit this for loop
            if apple_x != check_snake_x or apple_y != check_snake_y: # If it's not on this snake part
                new_fruit = False
           
        #print(apple_x, apple_y)
    map[apple_y][apple_x] = "@"
    map[new_snake_y][new_snake_x] = last_direction
    if old_snake_x <= map_width and old_snake_y <= map_height:
        map[old_snake_y][old_snake_x] = " "
       
    for x in range(map_width*3+5):
        print("_",end="")
    print()
    for y in map:
        print("|",end="")
        for x in y:
            print(f" {x} ",end="")
        print("|")
    for x in range(map_width*3+5):
        print("_",end="")
    print()
    print("Score: ", length - initial_length)
   
def post_move(new_snake_x,new_snake_y):
    global length,apple_x,apple_y,coords,alive,last_direction,mode
    os.system("clear")
    if mode == "loop":
        if new_snake_x > map_width:
            new_snake_x = 0
        if new_snake_x < 0:
            new_snake_x = map_width
        if new_snake_y > map_height:
            new_snake_y = 0
        if new_snake_y < 0:
            new_snake_y = map_height
    elif mode == "border":
        if new_snake_x >= map_width + 1 or new_snake_x <= -1:
            print("x")
            alive = False
            return 1
        if new_snake_y >= map_height + 1 or new_snake_y <= -1:
            print("y")
            alive = False
            return 1
    
    current_coords = [new_snake_x,new_snake_y]
    coords.append(current_coords)
    if new_snake_x == apple_x and new_snake_y == apple_y:
        length += 1
        draw_map(True, new_snake_x, new_snake_y, coords[len(coords)-length][0], coords[len(coords)-length][1])
    else:
        draw_map(False, new_snake_x, new_snake_y, coords[len(coords)-length][0], coords[len(coords)-length][1])
       
    for x in range(1,length):
        check_snake_x = coords[len(coords)-1-x][0]
        check_snake_y = coords[len(coords)-1-x][1]
       
        if new_snake_x == check_snake_x and new_snake_y == check_snake_y:
            alive = False
            return("Dead")
               
           
   
draw_map(True, initial_x,initial_y, map_width,map_height)
while alive:
    new_snake_x = coords[len(coords) - 1][0]
    new_snake_y = coords[len(coords) - 1][1]
    direction = input()
    if direction.upper() == "D" and opposite_direction != "R":
        opposite_direction = "L"
        last_direction = "R"
        new_snake_x +=1
        value = post_move(new_snake_x,new_snake_y)
    elif direction.upper() == "A" and opposite_direction != "L":
        opposite_direction= "R"
        last_direction = "L"
        new_snake_x -=1
        value = post_move(new_snake_x,new_snake_y)
    elif direction.upper() == "W" and opposite_direction != "U":
        opposite_direction = "D"
        last_direction = "U"
        new_snake_y -=1
        value = post_move(new_snake_x,new_snake_y)
    elif direction.upper() == "S" and opposite_direction != "D":
        opposite_direction = "U"
        last_direction = "D"
        new_snake_y +=1
        value = post_move(new_snake_x,new_snake_y)
       
    if value == 1:
            break
       
   
   
print("###############################################################")
print("#   _                        __         _             __   _  #")
print("#  /       /\      /\  /\   |         /   \  \    /  |    | \ #")
print("# |  _    /__\    /  \/  \  |--      |     |  \  /   |--  |_/ #")
print("#  \_/   /    \  /        \ |__       \___/    \/    |__  | \ #")
print("#                                                             #")
print("###############################################################")
print("Final score: ",length-initial_length)
