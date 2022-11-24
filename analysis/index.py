from aes512 import AES as AES_512

aes512 = AES_512()

while(True):
    print('\n\nAES 512')
    print('Press 1: For Encryption')
    print('Press 2: For Decryption')
    print('Any Other Key: To Exit')
    print('-='*10)
    choice = input('> ')

    if(choice == '1'):
        key = input('Enter Key (64): ')
        if(len(key) == 64):
            data = input('\nEnter Text:\n')
            encrypt = aes512.encrypt(key, data, 'b64')
            print(f'\nEncrypted Data:\n{encrypt}')
        else:
            print('Key Length should be 64.')
    elif(choice == '2'):
        key = input('Enter Key (64): ')
        if(len(key) == 64):
            data = input('\nEnter Cipher:\n')
            decrypt = aes512.decrypt(key, data, 'b64')
            print(f'\nDecrypted Data:\n{decrypt}')
        else:
            print('Key Length should be 64.')
    else:
        print('closing ...')
        break