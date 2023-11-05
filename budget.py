class Category:
    def __init__(self, category):
        self.category = category  # Nome da categoria
        self.ledger = []  # Lista para armazenar os registros financeiros da categoria

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            # Realiza uma transferência para outra categoria
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Gera uma representação de string da categoria
        title = f"{self.category:*^30}\n"  # Título centralizado com asteriscos
        items = ""
        total = 0
        for item in self.ledger:
            description = item["description"][:23]
            amount = item["amount"]
            items += f"{description} {amount:.2f}\n"
            total += amount
        output = title + items + f"Total: {total:.2f}"  # Total da categoria
        return output


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = [
        sum(item["amount"] for item in category.ledger if item["amount"] < 0)
        for category in categories
    ]
    total_spent = sum(spendings)

    # Geração do gráfico de barras com base nas porcentagens gastas
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for spending in spendings:
            chart += "o " if spending >= i / 100 * total_spent else "  "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    max_name_length = max(len(category.category) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip()


# Exemplo de uso
food_category = Category("Food")
food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food")

clothing_category = Category("Clothing")
clothing_category.transfer(50, food_category)

auto_category = Category("Auto")
auto_category.deposit(1000, "initial deposit")
auto_category.withdraw(15, "gas")
auto_category.transfer(100, food_category)

# Imprime as categorias e o gráfico de barras
print(food_category)
print(clothing_category)
print(auto_category)
print(create_spend_chart([food_category, clothing_category, auto_category]))


'''Code summary:

The Category class allows you to create objects to represent budget categories. It has methods for depositing, withdrawing, transferring, verifying funds and generating a formatted string representation.

The create_spend_chart function generates a bar chart that shows the percentage spent in each category based on withdrawals made.

In the usage example, three categories are created and financial operations are performed. Then the string representation of the categories and the bar chart are printed.

The code is a working example that meets the challenge requirements. It demonstrates how to create a class in Python to manage budget categories and how to generate a bar chart based on data from those categories.'''
