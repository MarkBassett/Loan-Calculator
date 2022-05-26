import math
import argparse

def overpayment(amount, period, principal):
    overpayment = (amount * period) - principal
    print(f"Overpayment = {overpayment}")


parser = argparse.ArgumentParser(description="Loan calculator providing the number of monthly payments, annuity,"
                                             "loan principle or differentiate payment")
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--principal", type=int)
parser.add_argument("--payment", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()
params_dict = vars(args)
params_list = [l for l in params_dict.values() if l]
values_list = [l for l in params_dict.values() if not isinstance(l, str) and l]
values_neg = [l for l in values_list if l < 0]

error_msg = None
if not args.type:
    error_msg = "Incorrect parameters"
elif len(params_list) < 4:
    error_msg = "Incorrect parameters"
elif args.type == "diff" and args.payment:
    error_msg = "Incorrect parameters"
elif len(values_neg):
    error_msg = "Incorrect parameters"
elif not args.interest:
    error_msg = "Incorrect parameters"
if error_msg:
    print(error_msg)
else:
    i = args.interest / 100 / 12

    if args.type == "diff":
        p = args.principal
        n = args.periods
        payment = 0
        for m in range(1, n + 1):
            d = math.ceil((p / n + i * (p - ((p * (m - 1)) / n))))
            print(f'Month {m}: payment is {d}')
            payment += d
        print(f'Overpayment = {payment - p}')
    elif args.type == "annuity":
        p = args.principal
        a = args.payment
        n = args.periods
        if n:
            if a:
                p = math.floor(a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
                print(f'Your loan principal = {p}!')
                overpayment(a, n, p)
            else:
                a = math.ceil(p * ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
                print(f'Your monthly payment = {a}!')
                overpayment(a, n, p)
        else:
            n = math.ceil(math.log(a / (a - i * p), 1 + i))
            months = n
            month_text = "months" if n > 1 else "month"
            if n > 11:
                years = math.floor(n / 12)
                n = n % 12
                year_text = "years" if years > 1 else "year"
                if n > 0:
                    print(f'It will take {years} {year_text} and {n} {month_text} to repay this loan!')
                else:
                    print(f'It will take {years} {year_text} to repay this loan!')
            else:
                print(f'It will take {n} {month_text} to repay the loan')
            overpayment(a, months, p)