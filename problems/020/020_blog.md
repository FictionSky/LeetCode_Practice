---
title: LeetCode 020. 有效的括号（Valid Parentheses）—— 用栈维护括号匹配顺序
slug: leetcode-020-valid-parentheses-stack
status: draft
categories:
  - leetcode
tags:
  - stack
  - string
---

render{
## 1. 题目描述

[label color="blue" shape="round"]简单[/label]
[label color="indigo" shape="round"]字符串[/label]
[label color="green" shape="round"]栈[/label]

给定一个只包含 `(`、`)`、`[`、`]`、`{`、`}` 的字符串 `s`，判断字符串中的括号是否有效。

有效括号需要同时满足两点：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须按照正确顺序闭合。

### 示例 1
> **输入**：s = "()[]{}"
> **输出**：true
> **解释**：三组括号都能正确匹配。

### 示例 2
> **输入**：s = "([)]"
> **输出**：false
> **解释**：虽然括号数量对得上，但闭合顺序不正确。
}

## 2. 核心算法思维：栈（Stack）

shortcode{
[admonition color="blue" title="为什么这题天然适合用栈？" icon="lightbulb-o"]
这道题的关键不是“数量相等”，而是“最后打开的左括号，必须最先关闭”。这种“后进先出”的关系，正好就是栈最擅长处理的场景。
[/admonition]
}

render{
### 我当时的写题思路

我写这题时的思路比较直接，先不追求最短代码，而是先把括号匹配过程拆清楚：

1. 遍历字符串，遇到左括号就先入栈。
2. 遇到右括号时，先判断栈是不是空的。
3. 如果栈为空，说明这个右括号找不到对应的左括号，直接返回 `false`。
4. 如果栈不为空，就取出栈顶元素，分别判断是不是 `()`、`[]`、`{}` 这三种合法配对。
5. 如果能配对，就把栈顶弹出；如果不能配对，就说明顺序或类型错了，直接返回 `false`。
6. 整个字符串遍历结束后，再检查栈是否为空。为空说明全部匹配成功，否则说明还有左括号没被关掉。

这种写法的优点是思路顺、调试也方便，尤其适合作为“栈”这类题目的入门写法。

顺便说一句，这题虽然经常和“栈 / 队列”一起出现在基础数据结构分类里，但真正贴切的核心标签其实是 **栈**。因为我们需要的是“最后进来的左括号，最先出去匹配右括号”，这正是标准的后进先出。
}

## 3. 按照我当前思路的实现（C++）

```cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (char ch : s) {
            if (ch == '(' || ch == '[' || ch == '{') {
                st.push(ch);
                continue;
            }

            if (st.empty()) {
                return false;
            }

            char top = st.top();
            if (top == '(' && ch == ')') {
                st.pop();
            } else if (top == '[' && ch == ']') {
                st.pop();
            } else if (top == '{' && ch == '}') {
                st.pop();
            } else {
                return false;
            }
        }

        return st.empty();
    }
};
```

render{
这段代码和我实际写题时的思路是一一对应的：先把左括号压栈，再判断当前右括号能不能和栈顶匹配。它不是最花哨的写法，但逻辑非常直观。
}

## 4. 如果想写得更简洁：更好的方法

shortcode{
[admonition color="green" title="更推荐的写法：栈里直接压入“期望出现的右括号”" icon="check"]
相比每次取栈顶后写三组 `if-else` 做配对判断，更简洁的办法是：遇到左括号时，不压左括号本身，而是直接把“它未来应该匹配的右括号”压入栈。
[/admonition]
}

render{
这样做的好处有两个：

- 判断逻辑更短，不需要反复写三组配对分支。
- 栈顶语义更清楚，表示“当前最期待看到的右括号”。

另外还可以加一个小优化：如果字符串长度是奇数，可以直接返回 `false`。因为有效括号一定是成对出现的。
}

```cpp
class Solution {
public:
    bool isValid(string s) {
        if (s.size() % 2 == 1) {
            return false;
        }

        stack<char> st;
        for (char ch : s) {
            if (ch == '(') {
                st.push(')');
            } else if (ch == '[') {
                st.push(']');
            } else if (ch == '{') {
                st.push('}');
            } else {
                if (st.empty() || st.top() != ch) {
                    return false;
                }
                st.pop();
            }
        }

        return st.empty();
    }
};
```

## 5. 复杂度分析

render{
无论是我当前的写法，还是上面这个更简洁的写法，复杂度其实都一样：

- **时间复杂度**：$O(n)$
  - 每个字符最多入栈一次、出栈一次，整体只遍历字符串一遍。
- **空间复杂度**：$O(n)$
  - 最坏情况下，字符串全是左括号，需要把它们全部压入栈中。
}

## 6. 易错点与避坑指南

shortcode{
[alert color="red" title="避坑 1：不要只看数量，要看闭合顺序" icon="exclamation-triangle"]
像 `([)]` 这种字符串里，左右括号数量虽然对得上，但闭合顺序错了，所以答案仍然是 `false`。
[/alert]
}

shortcode{
[alert color="orange" title="避坑 2：遍历结束后一定要检查栈是否为空" icon="exclamation-triangle"]
如果字符串是 `"((("`，遍历过程中不会立刻报错，但最后栈里还留着没匹配完的左括号，因此不能直接返回 `true`。
[/alert]
}

shortcode{
[collapse title="点击查看一个很容易忽略的小细节" color="grey" icon="angle-right"]
当当前字符是右括号时，一定要先判断栈是否为空，再去访问 `top()`。否则像 `"]"` 这样的输入会直接触发非法访问。
[/collapse]
}

## 7. 互动与补充资料

render{
这道题很适合作为“栈”的入门题。它的重点不是死记模板，而是建立一种判断习惯：

当题目要求你维护“最近一个还没处理完的状态”时，就可以优先想想栈是不是合适的数据结构。

本题的代码已同步至我的个人 GitHub 仓库。

[github author="FictionSky" project="LeetCode_Practice" size="mini"][/github]
}
