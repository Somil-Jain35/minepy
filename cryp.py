def machine ():
    keys = 'abcdefghijklmnopqrstuvwxyz!'
    value = keys[-1] , keys [0:1]
 
    encryptDict = dict(zip(keys,value))
    decryptDict = dict(zip(keys, value))

    message = input ("Enter the message:- ")
    mode = input ("Enter The mode:- | Encrypt(E) or Decrypt(D)")

    if mode.upper() == 'E':
        newmessage = ''.join([encryptDict[letter]
        for letter in message.lower()])

    elif mode.upper == 'D':
        newmessage = ''.join([decryptDict[letter]
        for letter in message.lower()])

    else:
      print ("Please enter right option")

    return newmessage

print(machine())
        

 
