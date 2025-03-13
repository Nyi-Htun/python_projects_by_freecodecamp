class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        category_title = self.category
        while len(category_title) < 30:
            category_title = '*' + category_title + '*'

        deposit_str = ''
        for i in self.ledger:
            deposit = i['description']
            deposit = self._cal_str(False, deposit, 23)
            amount_str = str("{:.2f}".format(float(i['amount'])))
            amount_str = self._cal_str(True, amount_str, 7)
            deposit_str += deposit + amount_str + '\n'

        total = 'Total: ' + str(self.get_balance())
        return category_title + '\n' + deposit_str + total

    def _cal_str(self, isAmount, desc, length):
        while len(desc) < length:
            if isAmount:
                desc = ' ' + desc
            else:
                desc += ' '
        if len(desc) > length:
            desc = desc[:length]
        return desc
    
    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True
        return False
    
    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False
    
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True

def create_spend_chart(categories):
    title = 'Percentage spent by category\n'
    spents = []
    for category in categories:
        spent = 0
        for item in category.ledger:
           if item['amount'] < 0:
               spent += item['amount']
        spents.append(round(spent, 2))
    total = round(sum(spents), 2)
    spent_percentages = [(abs(spent) / abs(total)) * 100 for spent in spents]
    spent_percentages = [int(p) // 10 * 10 for p in spent_percentages]

    chart = ''
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + '|'
        for percent in spent_percentages:
            chart += ' o ' if percent >= i else '   '
        chart += ' \n'

    footer = '    ' + '-' * ((3 * len(categories)) + 1) + '\n'
    descriptions = list(map(lambda category: category.category, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    print(descriptions)
    for row in zip(*descriptions):
        footer += '   ' + ''.join('  ' + letter for letter in row) + '  \n'
    print(footer)
    return title + chart + footer.rstrip('\n')

# test case
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(create_spend_chart([food, clothing]))