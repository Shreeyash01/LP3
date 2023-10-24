#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Item {
    int weight;
    int value;
    double valuePerWeight;

    Item(int w, int v) : weight(w), value(v) {
        valuePerWeight = static_cast<double>(value) / weight;
    }
};

bool compareItems(const Item& item1, const Item& item2) {
    return item1.valuePerWeight > item2.valuePerWeight;
}

double fractionalKnapsack(int W, vector<Item>& items) {
    sort(items.begin(), items.end(), compareItems);

    double totalValue = 0.0;
    int currentWeight = 0;

    for (const Item& item : items) {
        if (currentWeight + item.weight <= W) {
            totalValue += item.value;
            currentWeight += item.weight;
        } else {
            int remainingWeight = W - currentWeight;
            totalValue += item.valuePerWeight * remainingWeight;
            break;
        }
    }

    return totalValue;
}

int main() {
    int W = 50;
    vector<Item> items = {Item(10, 60), Item(20, 100), Item(30, 120)};

    double maxValue = fractionalKnapsack(W, items);
    cout << "Maximum value: " << maxValue << endl;

    return 0;
}