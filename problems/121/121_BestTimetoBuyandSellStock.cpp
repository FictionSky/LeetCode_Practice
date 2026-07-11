#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void printValue(bool value) {
    cout << (value ? "true" : "false");
}

void printValue(const string& value) {
    cout << value;
}

void printValue(char value) {
    cout << value;
}

template <typename T>
void printValue(const vector<T>& values);

template <typename T>
void printValue(const T& value) {
    cout << value;
}

template <typename T>
void printVector(const vector<T>& values) {
    cout << "[";
    for (size_t i = 0; i < values.size(); ++i) {
        printValue(values[i]);
        if (i + 1 < values.size()) {
            cout << ", ";
        }
    }
    cout << "]";
}

template <typename T>
void printValue(const vector<T>& values) {
    printVector(values);
}


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - 从左到右扫描时，先找出最关键、必须维护的状态量。
        // - 思考是否可以在每一步 O(1) 地更新当前最优答案。
        int profit_old,profit_today,profit_best,min_price;
        profit_old= 0;
        profit_today = 0;
        profit_best = 0;
        
        for (int i = 0; i < (prices.size()); ++i){
            if(i == 0){
                min_price = prices[i];
            }
            else{
                min_price = min(min_price,prices[i-1]);
            }
            profit_today = prices[i] - min_price;
            profit_old = max(profit_old,profit_today);
        }
        profit_best = profit_old;
        return profit_best;
    }
};

void runCase(const string& label, vector<int> prices, int expected) {
    Solution solution;
    int actual = solution.maxProfit(prices);
    cout << label << '\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\n\n";
}

int main() {
    cout << "练习目标：121. Best Time to Buy and Sell Stock" << '\n';
    cout << "只需要补全 maxProfit() 的 TODO 区域，再重新运行本地样例。" << "\n\n";
    runCase("示例 1", {7, 1, 5, 3, 6, 4}, 5);
    runCase("示例 2", {7, 6, 4, 3, 1}, 0);
    runCase("示例 3", {3,2,6,5,0,3}, 4);
    return 0;
}
