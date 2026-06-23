class Household:
    def __init__(self, money, employed = True):
        self.money = money
        self.employed = employed
        self.wage = 20 if employed else 0

    def recieve_wage(self):
        self.money += self.wage

class Firm:
    def __init__(self):
        self.price = 10
        self.inventory = 0
        self.revenue = 0
    
    def produce(self):
        self.inventory += 5
    
    def sell_to(self, household):
        if household.money >= self.price and self.inventory > 0:
            household.money -= self.price
            self.revenue += self.price
            self.inventory -= 1
            return self.price
        return 0

households = [
    Household(100),
    Household(80),
    Household(50),
    Household(30, employed = False),
]

firms = [
    Firm(),
    Firm(),
]
total_gdp = 0

for period in range(1, 11):
    print(f"\n--- Period {period} ---")

    for household in households:
        household.recieve_wage()

    for firm in firms:
        firm.produce()

    period_gdp = 0

    for household in households:
        for firm in firms:
            period_gdp += firm.sell_to(household)

    total_gdp += period_gdp

    unemployed = sum(1 for household in households if not household.employed)
    unemployment_rate = unemployed / len(households)

    average_price = sum(firm.price for firm in firms) / len(firms)

    print(f"GDP this period: {period_gdp}")
    print(f"Total GDP: {total_gdp}")
    print(f"Unemployment Rate: {(unemployment_rate * 100):.2%}%")
    print(f"Average Price: {average_price:.2f}")