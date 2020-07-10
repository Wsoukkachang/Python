def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as f:
        for line in f:
            #make variable "name"
            # then use split(when to stop)[index]
            name = line.split(",")[0]
            #append to list
            cast_list.append(name)
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)