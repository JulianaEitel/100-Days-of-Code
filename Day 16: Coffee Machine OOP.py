menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
should_end = False

while not should_end:

    choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if choice == "off":
        should_end = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)