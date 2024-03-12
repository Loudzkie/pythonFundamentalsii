# Repitition Statements
# Data types allowede to be iterated: Lists, ranges, Sets, Tuple, Dictionaries, Strings

# x = range(5,12)
petName = ["snowy", "blacky", "bruno"]

# for loop
# for(inititialzation;condition;incrementation/decre) - JAVA 
# for num in x:
#     print(num)

# slicing a lists
for name in petName[2:0:-1]:
    print(name)

    # Looping Dictionaries
    # key: value
user = {
        "first_name" : "Johhny",
        "Last_name" : "Depp",
        "age" : 25,
        "average" : 81.76,
        "list_subjects": ["Progaramming", "Mathematics", "English"]

}

    # ctrl + / - shortcut for comment

for key in user:
    print(key, ":", user[key])

    # Looping List of Dictionaries
    list_of_users = [
        {
        "first_name" : "Johhny",
        "Last_name" : "Depp",
        "age" : 25,
        "average" : 81.76,
        "list_subjects": ["Progaramming", "Mathematics", "English"] 
        },
        {
        "first_name" : "Prenzie",
        "Last_name" : "Depp",
        "age" : 26,
        "average" : 82,
        "list_subjects": ["Progaramming", "Mathematics", "English"]
        },
        {
        "first_name" : "Angel",
        "Last_name" : "Depp",
        "age" : 22,
        "average" : 81,
        "list_subjects": ["Progaramming", "Mathematics", "English"]
        },
    ]

    for key in list_of_users:
        for x in key:
            print(x, ":", key[x])

    # looping in reversed
    x = range(1,10)
    for i in x[::-1]:
        print(i)