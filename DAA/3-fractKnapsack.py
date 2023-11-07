class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.profit_per_weight = profit / weight

def fractional_knapsack(W, items):
    items.sort(key=lambda x: x.profit_per_weight, reverse=True)

    total_profit = 0.0
    current_weight = 0

    for item in items:
        if current_weight + item.weight <= W:
            total_profit += item.profit
            current_weight += item.weight
        else:
            remaining_weight = W - current_weight
            total_profit += item.profit_per_weight * remaining_weight
            break

    return total_profit

if __name__ == "__main__":
    W = 15
    items = [Item(2,10), Item(3,5), Item(5,15), Item(7,7), Item(1,6), Item(4,18), Item(1,3)]

    max_profit = fractional_knapsack(W, items)
    print("Maximum profit:", max_profit)
    
