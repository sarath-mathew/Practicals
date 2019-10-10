def main():
    sales = float(input("please enter the sales amount >"))
    bonus_determine = bonus_calc(sales)
    print(bonus_determine)
    while sales >= 0:
        sales = float(input("please enter the sales amount >"))
        bonus_determine = bonus_calc(sales)
        print(bonus_determine)
def bonus_calc(sales):
    while sales >= 0:
        bonus_amount = 0
        if sales >= 1000:
            bonus_amount = sales * 0.15
        elif sales < 1000:
            bonus_amount = sales * 0.10
    return bonus_amount


main()