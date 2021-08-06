def setPassword():
    characters = {4:['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'],5:['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C','A','B'],6:['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'],7:['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],0:["!","@",'+','&', '?','=', '$',"#","$","?",'+', '@', '!','&',"=", '#'],1:["0","1","2","3","7", '0',"8","9","4","5", '3', '2', '1',"6",'9', '5', '4', '8', '7', '6'],2:['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],3:['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']}
    length_input = int(input("Enter the length of password you need: "))
    password_for = input("Enter the name of platform to which password is: ").lower()
    id1 = str(id(length_input))
    id2 = str(id(password_for))[::-1]
    random_input = ""
    for i in range(len(id1)):
        if(id1[i]=='0' and id2[i]=='0'):
            continue
        else:
            random_input += str((int(id1[i])+int(id2[i]))%10)
    random_input = str(int(random_input[:len(random_input)//2]) + int(random_input[(len(random_input)//2)+1:]))
    while len(random_input) < length_input+3:
        random_input = str(int(random_input) * int(random_input[::-1])) + random_input[::-1]
    password=""
    for i in range(length_input):
        key = int(random_input[i])%8
        index = int(random_input[i+1:i+3]) % (len(characters[key]))
        password += characters[key][index]
    file_password = open("password.txt","a")
    print(password)
    check = input("To continue press enter")
    print(password_for +" : "+password,file=file_password)
    file_password.close()

def getPassword(string):
    file_password = open("password.txt","r")
    i = 0
    for line in file_password.readlines():
        if(string in line):
            i+=1
            print(line)
    if(i==0):
        print("That platform is not in file. Check spelling")
    check = input("To continue press enter")

user_input1 = input("Do you want to Set New Password(enter 1) or Get Password (enter 0)? To exit (press enter): ")
while user_input1 == '0' or user_input1 == '1':
    if(user_input1 == '1'):
        setPassword()
    else:
        user_input2 = input("Enter the platform for which you need password: ").lower()
        getPassword(user_input2)
    user_input1 = input("Do you want to Set New Password(enter 1) or Get Password (enter 0)? To exit (press enter): ")    

