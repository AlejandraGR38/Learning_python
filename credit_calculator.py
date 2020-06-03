import math

import argparse

#functions

def diff(principal, periods, interest):
    i_ = interest / (100 * 12)
    m = 1
    sum_ = 0
    for x in range(1, periods + 1):
        ec_1 = principal / periods
        ec_2 = principal - ( principal *(m - 1) / periods)
        D = math.ceil(ec_1 + i_ * ec_2)
        m += 1
        sum_ += D
        print(f'Month {m}: paid out {D}')
    overpay = sum_ - principal
    print(f'Overpayment = {math.ceil(overpay)}')

def cred_principal(payment, periods, interest):
    i_ = interest / (100 * 12)

    num_ = i_ * pow(1 + i_, periods)
    den_ = pow(1 + i_, periods) - 1
    den_2 = num_ / den_
    principal = math.ceil(payment / den_2)

    overpay = payment * periods  - principal

    print(f'Overpayment = {math.ceil(overpay)}')

def payment(principal, periods, interest):
    i_ = interest / (100 * 12)

    num = principal * i_ * pow(1 + i_, periods)
    den = pow(1 + i_, periods) - 1
    payment = math.ceil(num / den)
    overpay = (payment * periods) - principal

    print(f'Your annuity payment = {payment}!')
    print(f'Overpayment = {math.ceil(overpay)}')

def periods(payment, principal, interest):
    i_ = interest / (100 * 12)
    ec_1 = payment / (payment - i_ * principal)
    periods = math.ceil(math.log(ec_1, (i_ + 1)))
    y = periods // 12
    m = periods % 12

    overpay = (payment * periods) - principal

    if m == 0:
        print(f'You need {y} years to repay this credit!')
    elif y == 0:
        print(f'You need {m} months to repay this credit!')
    else:
        print(f'You need {y} years and {m} months to repay this credit!')

    print(f'Overpayment = {math.ceil(overpay)}')

#input

parse = argparse.ArgumentParser()
parse.add_argument("--type", type = str)
parse.add_argument("--principal", type=int)
parse.add_argument("--payment", type=int)
parse.add_argument("--periods", type=int)
parse.add_argument("--interest", type=float)

args = parse.parse_args()

#differential payment

if args.type == 'diff':
    try:
        diff(args.principal, args.periods, args.interest)
    except:
        print('Incorrect parameters')

#annuity payment
elif args.type =='annuity':
    try:
        if args.payment and args.periods:
            cred_principal(args.payment, args.periods, args.interest)
        elif args.principal and args.periods:
            payment(args.principal, args.periods, args.interest)
        else:
            periods(args.payment, args.principal, args.interest)
    except:
        print('Incorrect parameters')

else:
    print('Incorrect parameters')
