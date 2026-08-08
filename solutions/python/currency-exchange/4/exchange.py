"""Functions for calculating steps in exchanging currency.
"""
def exchange_money(budget, exchange_rate):   #Calculate estimated value after exchange
    return int(budget / exchange_rate)
    
def get_change(budget, exchanging_value):
    return int(budget - exchanging_value)
def get_value_of_bills(denomination, number_of_bills):
    return int(denomination*number_of_bills)
    #Calculate the total value of currency at current denomination.
def get_number_of_bills(amount, denomination):#This helps us to know the no:of bills of your budget.
    return int(amount// denomination)

def get_leftover_of_bills(amount, denomination):
    return amount % denomination
def exchangeable_value(budget, exchange_rate, spread, denomination):
    '''This helps us to calculate the actual and the final budget of your money by taking all the required inputs and doing by some math'''
    precent = exchange_rate*(spread/100)
    new_rate = precent+exchange_rate
    updated_budget = budget/ new_rate
    split = updated_budget//denomination
    final = split*denomination
    return final