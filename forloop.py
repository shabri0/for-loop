#6)WAP to create a list of the* *cubes of only the even integers* 
 #*appearing in the input list (may have elements of other types* *also) using the following: (a). 'for' loop* 

input_list = [2, 5, 8, "hello", 3.5, 10, 7, 4]
cube_list = []
for item in input_list:
    if type(item) == int and item % 2 == 0:
        cube_list.append(item ** 3)
print("Cubes of even integers:", cube_list)