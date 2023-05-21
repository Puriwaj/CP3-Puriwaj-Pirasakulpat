####################
TT = 'Thai Tea     '
GT = 'Green Tea    '
CT = 'Camomile Tea '
RT = 'Rose Tea     '
LT = 'Lipton Tea   '
cTT = 40
cGT = 40
cCT = 50
cRT = 60
cLT = 30
####################
username = input('username : ')
password = input('password : ')
if username == 'ILoveMilkTea' and password == '1234':
    print('login successful')
    print('-----------------------------------')
    print('Welcome to Tea Shop')
    print(TT,'40 THB')
    print(GT,'40 THB')
    print(CT,'50 THB')
    print(RT,'60 THB')
    print(LT,'30 THB')
    print('-----------------------------------')
    print('Please fill quantity of your order')
    qTT = int(input('Thai Tea     x '))
    qGT = int(input('Green Tea    x '))
    qCT = int(input('Camomile Tea x '))
    qRT = int(input('Rose Tea     x '))
    qLT = int(input('Lipton Tea   x '))
    print('-----------------------------------')
    print('Order Summary')
    if qTT > 0:
        tTT = qTT*cTT
        print(TT,'x',qTT,'=',tTT,'THB')
    else: tTT = 0

    if qGT > 0:
        tGT = qGT*cGT
        print(GT,'x',qGT,'=',tGT,'THB')
    else: tGT = 0

    if qCT > 0:
        tCT = qCT*cCT
        print(CT,'x',qCT,'=',tCT,'THB')
    else: tCT = 0

    if qRT > 0:
        tRT = qRT*cRT
        print(RT,'x',qRT,'=',tRT,'THB')
    else: tRT = 0

    if qLT > 0:
        tLT = qLT*cLT
        print(LT,'x',qLT,'=',tLT,'THB')
    else: tLT = 0

    tALL = tTT + tGT + tCT + tRT + tLT
    print('')
    print('total =', tALL, 'THB')
    print('')
    print('             THANK YOU             ')
    print('-----------------------------------')

else:print('incorrect')


