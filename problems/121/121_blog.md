---
title: LeetCode 121. 买卖股票的最佳时机（Best Time to Buy and Sell Stock）—— 一次遍历维护历史最低价
slug: leetcode-121-best-time-to-buy-and-sell-stock-greedy
status: draft
categories:
  - leetcode
tags:
  - array
  - greedy
  - dynamic-programming
---

render{
## 1. 题目描述

[label color="blue" shape="round"]简单[/label]
[label color="indigo" shape="round"]数组[/label]
[label color="green" shape="round"]贪心[/label]
[label color="orange" shape="round"]动态规划[/label]

给定一个数组 `prices`，其中 `prices[i]` 表示某只股票在第 `i` 天的价格。

你只能选择 **某一天买入这只股票**，并选择 **未来某一天卖出**。你只能完成 **一次交易**。

请返回可以获得的最大利润。如果无法获得利润，就返回 `0`。

### 示例 1
> **输入**：prices = [7,1,5,3,6,4]
> **输出**：5
> **解释**：在价格为 1 的时候买入，在价格为 6 的时候卖出，最大利润是 5。

### 示例 2
> **输入**：prices = [7,6,4,3,1]
> **输出**：0
> **解释**：价格一直下降，没有任何一次交易能够赚钱，所以返回 0。
}

## 2. 核心算法思维：贪心扫描

shortcode{
[admonition color=blue title=这题最关键的不是‘哪天卖’，而是‘卖之前最便宜的买入价’ icon=lightbulb-o]
因为只能交易一次，所以如果我们决定“今天卖出”，那利润就完全取决于“今天之前最低的买入价格”。

也就是说，我们从左到右扫描数组时，只需要一直维护两个量：到当前位置为止出现过的最低价格，以及以今天作为卖出日时能够得到的最大利润。
[/admonition]
}

render{
### 写题思路

写这题时的思路是把“今天卖出能赚多少”和“全局最好答案”分开维护，这样逻辑会比较顺：

1. 从左到右扫描每一天的股价。
2. 维护一个 `min_price`，表示到当前为止见过的最低买入价。
3. 假设今天卖出，那么今天的利润就是 `prices[i] - min_price`。
4. 再用这个利润去更新全局最大利润。
5. 扫描结束后，得到的就是整段区间里唯一一次交易能拿到的最优答案。
}

## 3. 整理后的实现（C++）

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = prices[0];  // 到当前为止，见过的最低买入价
        int today_profit = 0;       // 如果选择今天卖出，当前这次交易能赚多少
        int best_profit = 0;        // 扫描到当前位置时的全局最优答案

        for (int i = 1; i < prices.size(); ++i) {
            // 先假设在今天卖出，那么买入价只能来自今天之前
            today_profit = prices[i] - min_price;

            // 用“今天卖出”的利润更新历史最佳答案
            best_profit = max(best_profit, today_profit);

            // 再把今天价格纳入后续天数的最低买入价候选
            min_price = min(min_price, prices[i]);
        }

        return best_profit;
    }
};
```

render{
这段代码和当前的解题路线是一致的，只是把变量名整理得更直白一些了。

它的好处是非常容易调试：

- `min_price` 负责回答“到现在为止，最便宜什么时候买”。
- `today_profit` 负责回答“如果今天卖出，这一笔能赚多少”。
- `best_profit` 负责回答“到今天为止，最优答案是多少”。
}

## 4. 如果想写得更简洁：更推荐的贪心写法

shortcode{
[admonition color=green title=更推荐的写法：只保留两个核心状态 icon=check]
这题其实不一定要显式维护 `today_profit`。因为它只在当前这一轮使用一次，所以可以直接把它合并进更新答案的表达式里。
[/admonition]
}

render{
这种写法的本质没有变，仍然是在做一件事：

- 先维护历史最低价。
- 再尝试用当前价格作为卖出价更新答案。

但代码会更短，也更像这道题最经典的标准解。
}

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_price = prices[0];  // 扫描过程中见过的最低价格
        int best_profit = 0;        // 当前能得到的最大利润

        for (int price : prices) {
            // 先更新到今天为止的最低买入价
            min_price = min(min_price, price);

            // 再尝试把今天当成卖出日，更新最大利润
            best_profit = max(best_profit, price - min_price);
        }

        return best_profit;
    }
};
```

render{
这段代码里看起来像是“先更新最低价，再计算利润”，似乎允许了“同一天买入又卖出”。

但这里没有问题，因为同一天买卖的利润就是 `0`，它不会让答案变大，也不会破坏“只能先买后卖”的约束。正因为这个利润是安全的，所以我们可以把代码写得更简洁。
}

## 5. 再换一个视角：为什么这题也常被看成动态规划？

render{
虽然这题最常见的做法是贪心，但它其实也可以写成很经典的 **状态机 DP**。

我们把每天结束时的状态分成两种：

- `hold`：到今天结束时，手里持有一股股票时的最大收益。
- `cash`：到今天结束时，手里没有股票时的最大收益。

由于本题只允许交易一次，所以状态转移非常简单：
}

math{
hold = \max(hold, -price_i)
}

math{
cash = \max(cash, hold + price_i)
}

render{
直觉上可以这么理解：

- `hold` 表示“已经买过一次，现在手里还拿着股票”。
- `cash` 表示“已经完成了这次交易，现在手里没有股票”。

这组状态在本题里看起来比贪心更绕一点，但它的优势是：**股票系列题往后做，几乎都能沿着这套状态机继续扩展。**
}

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int hold = -prices[0];  // 持有股票时的最大收益，等价于已经买入一次
        int cash = 0;           // 不持有股票时的最大收益，初始为 0

        for (int i = 1; i < prices.size(); ++i) {
            // 今天卖出，或者继续保持不持股状态
            cash = max(cash, hold + prices[i]);

            // 今天买入，或者保留之前更便宜的买入方案
            hold = max(hold, -prices[i]);
        }

        return cash;
    }
};
```

## 6. 复杂度分析

render{
无论是上面的贪心写法，还是状态机 DP 写法，复杂度都很优秀：

- **时间复杂度**：$O(n)$
  - 只需要把价格数组从左到右扫描一遍。
- **空间复杂度**：$O(1)$
  - 只维护常数个变量，不需要额外数组。
}

## 7. 易错点与避坑指南

shortcode{
[alert color=red title=避坑 1：买入一定要发生在卖出之前 icon=exclamation-triangle]
这题不是“找两个数做最大差值”这么简单，而是必须满足时间顺序。低价必须出现在高价之前，才能形成合法交易。
[/alert]
}

shortcode{
[alert color=orange title=避坑 2：如果始终赚不到钱，答案要返回 0 icon=exclamation-triangle]
像 `[7,6,4,3,1]` 这种单调下降数组，最大利润不是负数，而是直接选择“不交易”，所以结果应该是 `0`。
[/alert]
}

shortcode{
[collapse title=点击查看一个常见误区 color=grey icon=angle-right]
有些人会先把全局最低价和全局最高价找出来，再做差值。这种做法是错误的，因为全局最低价可能出现在全局最高价的后面，不满足“先买后卖”的题意。
[/collapse]
}

## 8. 相关扩展知识

render{
这道题其实是整个“股票系列”最基础的一题，后面很多题都可以看成是在它的基础上继续加限制条件：
}

shortcode{
[admonition color=indigo title=股票系列题怎么从 121 往后扩展？ icon=info-circle]
- `121`：只能交易一次，核心是维护历史最低价，或者写成两状态 DP。
- `122`：可以交易无限次，本质上是在所有上升区间里持续获利。
- `123`：最多交易两次，需要把状态扩展成两轮买卖。
- `188`：最多交易 `k` 次，是 `123` 的通用版本。
- `309`：加入冷冻期，卖出后不能立刻再买。
- `714`：加入手续费，状态转移时要把成本扣掉。
[/admonition]
}

render{
非常推荐把 `121` 这题里的两种理解都掌握住：

1. **贪心视角**：维护最低价和最大利润。
2. **DP 视角**：维护持股与不持股两个状态。

前者适合快速秒题，后者适合把股票系列一整串打通。

另外，这题还可以和 **最大子数组和** 做一个类比：

- 如果把相邻两天的价格差 `prices[i] - prices[i - 1]` 看成“每天的收益变化”，
- 那么“只做一次买卖”的最大利润，其实等价于“在这串收益变化里找一段最大连续和”。

这个视角不是最适合面试时首选的写法，但很适合帮助建立不同题型之间的联系。

本题的代码已同步至我的个人 GitHub 仓库。

[github author=FictionSky project=LeetCode_Practice size=mini][/github]
}
