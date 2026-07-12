---
title: LeetCode 053. 最大子数组和（Maximum Subarray）—— 贪心与动态规划两种思路
slug: leetcode-053-maximum-subarray-greedy-dp
status: draft
categories:
  - leetcode
tags:
  - dynamic-programming
  - greedy
  - array
---

render{
## 1. 题目描述

[label color="blue" shape="round"]简单[/label]
[label color="indigo" shape="round"]数组[/label]
[label color="orange" shape="round"]贪心[/label]
[label color="green" shape="round"]动态规划[/label]

给定一个整数数组 `nums`，请找出一个具有**最大和**的连续子数组，并返回这个最大和。

注意：子数组必须是连续的一段，不能跳着选元素；数组至少包含一个元素。

### 示例 1
> **输入**：nums = [-2,1,-3,4,-1,2,1,-5,4]
> **输出**：6
> **解释**：连续子数组 [4,-1,2,1] 的和最大，为 6。

### 示例 2
> **输入**：nums = [1]
> **输出**：1

}

## 2. 核心问题：什么时候应该放弃前面的连续和？

shortcode{
[admonition color="blue" title="关键观察" icon="lightbulb-o"]
对于某个位置 `i` 来说，如果它前面累积出来的连续和已经小于等于 0，那么这段前缀再接上 `nums[i]` 只会让结果变差或不变。

因此，一旦当前连续和 `count <= 0`，就可以把它丢掉，从下一个位置重新开始累计。
[/admonition]
}

render{
这道题的难点不在“求和”，而在于判断**一段连续子数组是否还值得继续向右扩展**。

假设当前累计和为 `count`：
- 如果 `count > 0`，它对后面的元素有正向贡献，应该保留并继续扩展。
- 如果 `count <= 0`，它对后面的元素没有帮助，应该舍弃并重新开始。

这个判断可以导出两种常见写法：
1. **贪心算法**：当前和变成非正数时立即重置。
2. **动态规划**：定义“以当前位置结尾的最大子数组和”，再做状态转移。
}

## 3. 思路一：贪心算法

render{
贪心思路关注的是：**当前累计和是否还能给后续子数组带来收益**。

遍历数组时维护两个变量：
- `count`：当前正在累计的连续子数组和。
- `result`：遍历过程中见过的最大连续子数组和。

每访问一个元素 `nums[i]`：
1. 先将它加入当前连续和：`count += nums[i]`。
2. 用 `count` 更新全局最大值：`result = max(result, count)`。
3. 如果 `count <= 0`，说明当前这段连续和已经没有继续保留的价值，重置为 0。

这里必须先更新 `result`，再判断是否重置 `count`。这样可以正确处理全是负数的数组，例如 `[-3,-2,-5]`，答案应为 `-2`，而不是 `0`。
}

### 贪心算法实现（C++）

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // result 记录遍历过程中出现过的最大连续子数组和。
        // 初始化为 nums[0]，可以正确处理全负数数组。
        int result = nums[0];

        // count 表示当前正在累加的连续子数组和。
        int count = 0;

        for (int i = 0; i < nums.size(); ++i) {
            count += nums[i];

            // 当前连续和可能就是目前最优答案，先更新 result。
            result = max(result, count);

            // 如果当前连续和已经小于等于 0，
            // 它接到后面的元素前面只会拖累后续结果，因此直接丢弃。
            if (count <= 0) {
                count = 0;
            }
        }

        return result;
    }
};
```

## 4. 思路二：动态规划

render{
动态规划写法更适合系统理解这道题。

### 状态定义
令 `dp[i]` 表示：**以 `nums[i]` 结尾的最大连续子数组和**。

这里的“以 `nums[i]` 结尾”非常关键，因为最大子数组必须连续。如果一个子数组要以 `nums[i]` 结尾，它只有两种选择：
1. 接在前一个位置的最优连续子数组后面：`dp[i - 1] + nums[i]`。
2. 不接前面，直接从 `nums[i]` 重新开始：`nums[i]`。

所以状态转移方程为：
}

math{
dp[i] = \max(dp[i - 1] + nums[i], nums[i])
}

render{
最终答案不是 `dp[n - 1]`，而是所有 `dp[i]` 中的最大值。因为最大连续子数组不一定以最后一个元素结尾。
}

### 动态规划实现（C++）

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // dp 表示“以当前位置结尾”的最大连续子数组和。
        int dp = nums[0];

        // result 表示所有位置的 dp 最大值。
        int result = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            // 要么接上前一段连续子数组，要么从当前元素重新开始。
            dp = max(dp + nums[i], nums[i]);

            // 最大子数组可能结束在任意位置，因此每一步都要更新答案。
            result = max(result, dp);
        }

        return result;
    }
};
```

## 5. 贪心与动态规划的关系

render{
这两种写法看起来不同，本质上处理的是同一个问题。

- **动态规划视角**：如果 `dp[i - 1] > 0`，就接上前面的连续子数组；否则从 `nums[i]` 重新开始。
- **贪心视角**：如果当前累计和 `count <= 0`，就丢弃它，从后面重新累计。

也就是说，贪心算法里的“重置 `count`”，对应动态规划里的“选择 `nums[i]` 作为新的起点”。

可以把贪心写法理解为空间优化后的动态规划：它没有显式保存每一个 `dp[i]`，只保留了当前状态和全局最优答案。
}

shortcode{
[alert color="green" title="一句话总结" icon="check"]
前缀和为正就继续扩展，前缀和非正就果断舍弃；答案是在遍历过程中出现过的最大连续和。
[/alert]
}

## 6. 复杂度分析

render{
无论使用贪心算法还是空间优化后的动态规划，复杂度都是一样的：

- **时间复杂度**：$O(n)$
  - 只需要从左到右遍历数组一次。
- **空间复杂度**：$O(1)$
  - 只使用了常数个变量保存当前状态和最终答案。
}

## 7. 易错点与避坑指南

shortcode{
[admonition color="red" title="避坑 1：不能把答案初始化为 0" icon="exclamation-triangle"]
如果数组全是负数，例如 `[-2,-1,-3]`，最大连续子数组和应该是 `-1`。如果把答案初始化为 0，就会得到错误结果。

正确做法是将 `result` 初始化为 `nums[0]`。
[/admonition]

[admonition color="orange" title="避坑 2：先更新答案，再重置当前和" icon="warning"]
贪心写法中，`count += nums[i]` 后应先用 `count` 更新 `result`，再判断 `count <= 0` 是否需要重置。

这样才能在全负数场景下保留最大负数作为答案。
[/admonition]
}

render{
### 补充知识：为什么不是普通前缀和？

前缀和可以快速计算任意区间和，但本题要找的是“最大连续区间和”。如果枚举所有区间，再用前缀和计算每段区间和，仍然需要 $O(n^2)$ 的枚举成本。

Kadane 算法的价值在于：它不枚举所有区间，而是在遍历过程中不断判断“当前连续段是否值得保留”，从而把整体复杂度降到 $O(n)$。
}

## 8. 互动与补充资料

shortcode{
[collapse title="点击查看 Kadane 算法补充（选读）" color="grey" icon="angle-right"]
最大子数组和问题的经典线性解法通常被称为 Kadane 算法。它的核心思想是：对每个位置，只关心“以当前位置结尾的最大连续和”，并在遍历过程中维护全局最大值。

这种思想非常适合作为动态规划入门例题，因为它展示了状态定义、状态转移、空间优化三件事如何自然连接起来。
[/collapse]
}

render{
本题的代码已同步至个人 GitHub 仓库。

[github author="FictionSky" project="LeetCode_Practice" size="mini"][/github]
}
