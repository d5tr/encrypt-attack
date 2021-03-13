from hashlib import md5
from hashlib import sha1
from hashlib import sha256
from hashlib import sha512
from hashlib import sha224
from hashlib import sha384
from hashlib import sha3_512
from hashlib import sha3_384
from hashlib import sha3_256
from hashlib import sha3_224
import sys
from colorama import *


print(Fore.RED+'''

███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗    █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗      ██████╗  ██╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝   ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝     ██╔═████╗███║
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║█████╗███████║   ██║      ██║   ███████║██║     █████╔╝█████╗██║██╔██║╚██║
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║╚════╝██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗╚════╝████╔╝██║ ██║
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║      ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗     ╚██████╔╝ ██║
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝      ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝      ╚═════╝  ╚═╝
                                                                                                                                   

INSTA = D_5TR !
make by ---> d5tr | 01 

'''+Fore.GREEN+Style.BRIGHT)



print('''
[1] md5
[2] sha1
[3] sha256
[4] sha512
[5] sha224
[6] sha384
[7] sha3_512
[8] sha3_384
[9] sha3_256
[10] sha3_224
''')

you_went = int(input('enter number hash --->'))

if you_went == 1:
    x = 0
    file = open(input('enter name file :'), 'r')
    xx = file.readlines()

    the_hash = input('enter your hash :')

    while x == 0:




        for files in xx :
            attack = md5(files.encode()).hexdigest()
            password = attack

            if the_hash == password :
                print(files," ---GOOD-ATTACK---> ",the_hash)
                print('''
                DONE !!
                INSTA = D_5TR
                ''')
                sys.exit()

            else:
                print('mot this :',files,'-->',password)

if you_went == 2:
    x = 0
    file = open(input('enter name file :'), 'r')
    xx = file.readlines()

    the_hash = input('enter your hash :')

    while x == 0:




        for files in xx :
            attack = sha1(files.encode()).hexdigest()
            password = attack

            if the_hash == password :
                print(files," ---GOOD-ATTACK---> ",the_hash)
                print('''
                DONE !!
                INSTA = D_5TR
                ''')
                sys.exit()

            else:
                print('mot this :',files,'-->',password)

if you_went == 3:
    x = 0
    file = open(input('enter name file :'), 'r')
    xx = file.readlines()

    the_hash = input('enter your hash :')

    while x == 0:




        for files in xx :
            attack = sha256(files.encode()).hexdigest()
            password = attack

            if the_hash == password :
                print(files," ---GOOD-ATTACK---> ",the_hash)
                print('''
                DONE !!
                INSTA = D_5TR
                ''')
                sys.exit()

            else:
                print('mot this :',files,'-->',password)

if you_went == 4:
    x = 0
    file = open(input('enter name file :'), 'r')
    xx = file.readlines()

    the_hash = input('enter your hash :')

    while x == 0:




        for files in xx :
            attack = sha512(files.encode()).hexdigest()
            password = attack

            if the_hash == password :
                print(files," ---GOOD-ATTACK---> ",the_hash)
                print('''
                DONE !!
                INSTA = D_5TR
                ''')
                sys.exit()

            else:
                print('mot this :',files,'-->',password)

if you_went == 5:
    x = 0
    file = open(input('enter name file :'), 'r')
    xx = file.readlines()

    the_hash = input('enter your hash :')

    while x == 0:




        for files in xx :
            attack = sha224(files.encode()).hexdigest()
            password = attack

            if the_hash == password :
                print(files," ---GOOD-ATTACK---> ",the_hash)
                print('''
                DONE !!
                INSTA = D_5TR
                ''')
                sys.exit()

            else:
                print('mot this :',files,'-->',password)

if you_went == 6:
    x = 0
    file = open(input('enter name file :'), 'r')
    xx = file.readlines()

    the_hash = input('enter your hash :')

    while x == 0:




        for files in xx :
            attack = sha384(files.encode()).hexdigest()
            password = attack

            if the_hash == password :
                print(files," ---GOOD-ATTACK---> ",the_hash)
                print('''
                DONE !!
                INSTA = D_5TR
                ''')
                sys.exit()

            else:

               print('mot this :',files,'-->',password)

if you_went == 7:
    x = 0
    file = open(input('enter name file :'), 'r')
    xx = file.readlines()

    the_hash = input('enter your hash :')

    while x == 0:




        for files in xx :
            attack = sha3_512(files.encode()).hexdigest()
            password = attack

            if the_hash == password :
                print(files," ---GOOD-ATTACK---> ",the_hash)
                print('''
                DONE !!
                INSTA = D_5TR
                ''')
                sys.exit()

            else:
                print('mot this :',files,'-->',password)

if you_went == 8:
    x = 0
    file = open(input('enter name file :'), 'r')
    xx = file.readlines()

    the_hash = input('enter your hash :')

    while x == 0:




        for files in xx :
            attack = sha3_384(files.encode()).hexdigest()
            password = attack

            if the_hash == password :
                print(files," ---GOOD-ATTACK---> ",the_hash)
                print('''
                DONE !!
                INSTA = D_5TR
                ''')
                sys.exit()

            else:
                print('mot this :',files,'-->',password)

if you_went == 9:
    x = 0
    file = open(input('enter name file :'), 'r')
    xx = file.readlines()

    the_hash = input('enter your hash :')

    while x == 0:




        for files in xx :
            attack = sha3_256(files.encode()).hexdigest()
            password = attack

            if the_hash == password :
                print(files," ---GOOD-ATTACK---> ",the_hash)
                print('''
                DONE !!
                INSTA = D_5TR
                ''')
                sys.exit()

            else:
                print('mot this :',files,'-->',password)

if you_went == 10:
    x = 0
    file = open(input('enter name file :'), 'r')
    xx = file.readlines()

    the_hash = input('enter your hash :')

    while x == 0:




        for files in xx :
            attack = sha3_224(files.encode()).hexdigest()
            password = attack

            if the_hash == password :
                print(files," ---GOOD-ATTACK---> ",the_hash)
                print('''
                DONE !!
                INSTA = D_5TR
                ''')
                sys.exit()

            else:
                print('mot this :',files,'-->',password)

