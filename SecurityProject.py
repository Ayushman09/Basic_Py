alphabet='abcdefghijklmnopqrstuvwxyz0123456789'
key= 25
newmsg=''
ch=input('Enter E|e for encryption & D|d for encryption: ')
if(ch=='E' or ch=='e'):
 #Encryption
    message=input('Enter the message for encryption: ')
    for character in message:
        position= alphabet.find(character)
        newpos= (position+key)%37
        newchar= alphabet[newpos]
        print('Encrypted to',newchar)
        newmsg+=newchar
    print('The encrypted final message is: ', newmsg)
elif(ch=='D' or ch=='d'):
#Decryption
    message=input('Enter encrypted message for decryption: ')
    for character in message:
        position= alphabet.find(character)
        newpos= (position-key)%37
        newchar= alphabet[newpos]
        print('Encrypted to',newchar)
        newmsg+=newchar
    print('The decrypted final message is: ', newmsg)
else:
    print('Wrong Choice!')