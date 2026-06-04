from pathlib import Path
import re
import sys

from round1_practice_data import ROUND1_PRACTICE_DATA


ROOT = Path(__file__).resolve().parents[1]
PROBLEMS_DIR = ROOT / "problems"


CATEGORY_GUIDANCE = {
    "hash_map": {
        "pattern": "哈希表 / 哈希集合",
        "hints": [
            "先想清楚：在一次扫描过程中，哪些信息需要被及时记录下来。",
            "考虑是否可以用额外空间换取更快的查找速度。",
        ],
        "complexity": "如果查找可以做到常数时间，优先尝试 O(n) 时间复杂度。",
    },
    "two_pointers": {
        "pattern": "双指针",
        "hints": [
            "先定义每个指针分别表示什么，再去移动它。",
            "思考左指针或右指针变化时，答案如何被更新。",
        ],
        "complexity": "如果不需要排序，优先尝试 O(n)；如果需要排序，常见目标是 O(n log n)。",
    },
    "sliding_window": {
        "pattern": "滑动窗口",
        "hints": [
            "写代码前先定义清楚：当前窗口表示什么。",
            "明确窗口在什么条件下失效，以及应该如何收缩。",
        ],
        "complexity": "常见目标是单次遍历完成，也就是 O(n)。",
    },
    "binary_search": {
        "pattern": "二分查找",
        "hints": [
            "先判断你是在找精确值、边界位置，还是答案空间。",
            "写代码前，先用一句话说清楚循环不变量是什么。",
        ],
        "complexity": "优先尝试 O(log n) 时间复杂度。",
    },
    "linked_list": {
        "pattern": "链表",
        "hints": [
            "如果链表结构会变化，建议先把指针移动过程画出来。",
            "每次修改前后，都要明确每个指针到底指向哪里。",
        ],
        "complexity": "根据指针策略不同，通常目标是一遍或两遍扫描完成。",
    },
    "stack_queue": {
        "pattern": "栈 / 队列",
        "hints": [
            "先判断题目需要的是后进先出还是先进先出。",
            "如果是单调结构，先定义清楚它维护的是哪种顺序。",
        ],
        "complexity": "如果题目允许，优先考虑把单次操作做到均摊 O(1)。",
    },
    "binary_tree": {
        "pattern": "二叉树 DFS / BFS",
        "hints": [
            "先想清楚当前节点是在递归前、中、后哪个阶段处理。",
            "明确递归函数对“一个子树”返回的含义是什么。",
        ],
        "complexity": "大多数基础树题都可以先朝 O(n) 时间复杂度去设计。",
    },
    "graph": {
        "pattern": "图 / BFS / DFS / 拓扑排序",
        "hints": [
            "写代码前先定义：图中的点和边分别表示什么。",
            "判断关键状态是遍历顺序、入度，还是访问标记。",
        ],
        "complexity": "图遍历类题目的常见目标是 O(V + E)。",
    },
    "graph_grid": {
        "pattern": "网格图 / BFS / DFS",
        "hints": [
            "把每个格子看成一个节点，并先想清楚邻居如何找到。",
            "特别注意边界判断和访问状态更新的时机。",
        ],
        "complexity": "常见目标是 O(rows * cols)。",
    },
    "dynamic_programming": {
        "pattern": "动态规划",
        "hints": [
            "下笔前先用一句话写清楚状态定义。",
            "先从更小子问题如何转移到当前问题开始想。",
        ],
        "complexity": "先写出清晰正确的状态转移，再考虑优化空间或时间。",
    },
    "interval_greedy": {
        "pattern": "区间 / 贪心",
        "hints": [
            "如果区间之间的相对顺序重要，先考虑排序。",
            "要明确写出贪心选择是什么，以及它为什么成立。",
        ],
        "complexity": "很多区间题会先排序，所以常见目标是 O(n log n)。",
    },
    "matrix": {
        "pattern": "矩阵遍历 / 原地修改",
        "hints": [
            "先判断能不能安全地在原矩阵上直接修改。",
            "注意是否有行状态或列状态需要延后使用。",
        ],
        "complexity": "大多数基础矩阵题可以先按 O(rows * cols) 设计。",
    },
    "array_greedy": {
        "pattern": "数组 / 贪心扫描",
        "hints": [
            "从左到右扫描时，先找出最关键、必须维护的状态量。",
            "思考是否可以在每一步 O(1) 地更新当前最优答案。",
        ],
        "complexity": "如果题目允许，优先尝试 O(n) 时间和 O(1) 额外空间。",
    },
    "array_prefix": {
        "pattern": "数组 / 前后缀",
        "hints": [
            "思考答案是否同时依赖左边信息和右边信息。",
            "想一想是否可以在不用除法的情况下构造结果。",
        ],
        "complexity": "常见目标是 O(n) 时间复杂度。",
    },
    "string_array": {
        "pattern": "字符串 / 数组模拟",
        "hints": [
            "先把题目拆成几个简单的状态更新步骤。",
            "明确每个下标、单词片段或子串分别代表什么。",
        ],
        "complexity": "先写一个清晰正确的版本，再根据需要优化。",
    },
    "heap_priority": {
        "pattern": "堆 / 优先队列",
        "hints": [
            "先定义任意时刻堆顶元素应该代表什么。",
            "想清楚什么元素要入堆，以及元素何时会失效。",
        ],
        "complexity": "常见目标是 O(n log n) 或 O(k log n)，取决于题目规模。",
    },
    "backtracking": {
        "pattern": "回溯 / DFS 搜索",
        "hints": [
            "先写清楚一次递归调用负责解决哪一层问题。",
            "注意选择何时加入、何时撤销。",
        ],
        "complexity": "先把搜索树写对，剪枝优化放在后面考虑。",
    },
    "trie": {
        "pattern": "Trie / 前缀树",
        "hints": [
            "先想清楚一个字符转移如何表示。",
            "明确每个节点必须保存哪些信息。",
        ],
        "complexity": "很多 Trie 题的复杂度与插入字符总数有关。",
    },
    "graph_weighted": {
        "pattern": "带权图 / 最短路",
        "hints": [
            "在选择 BFS、Dijkstra 或 DP 前，先定义清楚“状态”是什么。",
            "注意某条路径代价何时已经确定，何时还可能继续变优。",
        ],
        "complexity": "如果使用优先队列，常见目标是 O((V + E) log V)。",
    },
    "union_find": {
        "pattern": "并查集 / 连通性",
        "hints": [
            "先判断题目本质是不是在维护连通块。",
            "明确什么时刻应该把两个点合并到同一集合。",
        ],
        "complexity": "结合路径压缩和按秩/按大小合并后，目标通常是近线性复杂度。",
    },
    "bit_manipulation": {
        "pattern": "位运算",
        "hints": [
            "建议先手写一个很小的二进制例子。",
            "多观察位的规律，而不是暴力枚举所有组合。",
        ],
        "complexity": "很多位运算题会追求 O(1) 额外空间，以及线性或对数时间。",
    },
    "monotonic_queue": {
        "pattern": "单调队列 / 双端队列",
        "hints": [
            "先定义双端队列里需要维护的单调顺序。",
            "想清楚一个旧元素在什么情况下会被新元素“淘汰”。",
        ],
        "complexity": "这类题常见目标是 O(n)。",
    },
    "greedy": {
        "pattern": "贪心",
        "hints": [
            "写代码前先明确贪心选择到底是什么。",
            "解释清楚为什么当前局部最优不会破坏全局最优。",
        ],
        "complexity": "很多贪心题的常见目标是 O(n) 或 O(n log n)。",
    },
    "math": {
        "pattern": "数学 / 数值规律",
        "hints": [
            "先手写几个小例子，再总结规律。",
            "把数值变化过程和最后的格式处理分开考虑。",
        ],
        "complexity": "先写最直接、最容易验证正确性的解法，再考虑优化。",
    },
    "design": {
        "pattern": "设计题 / 数据结构",
        "hints": [
            "先列出所有需要支持的操作，以及目标复杂度。",
            "再分析每个操作分别要修改哪些内部状态。",
        ],
        "complexity": "先保证接口设计清晰，再尽量满足题目要求的操作复杂度。",
    },
}


ROUND1_PROBLEMS = [
    {"id": 1, "title": "Two Sum", "category": "hash_map", "kind": "solution", "return_type": "vector<int>", "method": "twoSum", "params": ["vector<int>& nums", "int target"]},
    {"id": 217, "title": "Contains Duplicate", "category": "hash_map", "kind": "solution", "return_type": "bool", "method": "containsDuplicate", "params": ["vector<int>& nums"]},
    {"id": 242, "title": "Valid Anagram", "category": "hash_map", "kind": "solution", "return_type": "bool", "method": "isAnagram", "params": ["string s", "string t"]},
    {"id": 20, "title": "Valid Parentheses", "category": "stack_queue", "kind": "solution", "return_type": "bool", "method": "isValid", "params": ["string s"]},
    {"id": 121, "title": "Best Time to Buy and Sell Stock", "category": "array_greedy", "kind": "solution", "return_type": "int", "method": "maxProfit", "params": ["vector<int>& prices"]},
    {"id": 53, "title": "Maximum Subarray", "category": "dynamic_programming", "kind": "solution", "return_type": "int", "method": "maxSubArray", "params": ["vector<int>& nums"]},
    {"id": 238, "title": "Product of Array Except Self", "category": "array_prefix", "kind": "solution", "return_type": "vector<int>", "method": "productExceptSelf", "params": ["vector<int>& nums"]},
    {"id": 49, "title": "Group Anagrams", "category": "hash_map", "kind": "solution", "return_type": "vector<vector<string>>", "method": "groupAnagrams", "params": ["vector<string>& strs"]},
    {"id": 347, "title": "Top K Frequent Elements", "category": "hash_map", "kind": "solution", "return_type": "vector<int>", "method": "topKFrequent", "params": ["vector<int>& nums", "int k"]},
    {"id": 128, "title": "Longest Consecutive Sequence", "category": "hash_map", "kind": "solution", "return_type": "int", "method": "longestConsecutive", "params": ["vector<int>& nums"]},
    {"id": 125, "title": "Valid Palindrome", "category": "two_pointers", "kind": "solution", "return_type": "bool", "method": "isPalindrome", "params": ["string s"]},
    {"id": 167, "title": "Two Sum II - Input Array Is Sorted", "category": "two_pointers", "kind": "solution", "return_type": "vector<int>", "method": "twoSum", "params": ["vector<int>& numbers", "int target"]},
    {"id": 344, "title": "Reverse String", "category": "two_pointers", "kind": "solution", "return_type": "void", "method": "reverseString", "params": ["vector<char>& s"]},
    {"id": 283, "title": "Move Zeroes", "category": "two_pointers", "kind": "solution", "return_type": "void", "method": "moveZeroes", "params": ["vector<int>& nums"]},
    {"id": 11, "title": "Container With Most Water", "category": "two_pointers", "kind": "solution", "return_type": "int", "method": "maxArea", "params": ["vector<int>& height"]},
    {"id": 15, "title": "3Sum", "category": "two_pointers", "kind": "solution", "return_type": "vector<vector<int>>", "method": "threeSum", "params": ["vector<int>& nums"]},
    {"id": 643, "title": "Maximum Average Subarray I", "category": "sliding_window", "kind": "solution", "return_type": "double", "method": "findMaxAverage", "params": ["vector<int>& nums", "int k"]},
    {"id": 209, "title": "Minimum Size Subarray Sum", "category": "sliding_window", "kind": "solution", "return_type": "int", "method": "minSubArrayLen", "params": ["int target", "vector<int>& nums"]},
    {"id": 3, "title": "Longest Substring Without Repeating Characters", "category": "sliding_window", "kind": "solution", "return_type": "int", "method": "lengthOfLongestSubstring", "params": ["string s"]},
    {"id": 567, "title": "Permutation in String", "category": "sliding_window", "kind": "solution", "return_type": "bool", "method": "checkInclusion", "params": ["string s1", "string s2"]},
    {"id": 438, "title": "Find All Anagrams in a String", "category": "sliding_window", "kind": "solution", "return_type": "vector<int>", "method": "findAnagrams", "params": ["string s", "string p"]},
    {"id": 424, "title": "Longest Repeating Character Replacement", "category": "sliding_window", "kind": "solution", "return_type": "int", "method": "characterReplacement", "params": ["string s", "int k"]},
    {"id": 704, "title": "Binary Search", "category": "binary_search", "kind": "solution", "return_type": "int", "method": "search", "params": ["vector<int>& nums", "int target"]},
    {"id": 35, "title": "Search Insert Position", "category": "binary_search", "kind": "solution", "return_type": "int", "method": "searchInsert", "params": ["vector<int>& nums", "int target"]},
    {"id": 278, "title": "First Bad Version", "category": "binary_search", "kind": "bad_version", "return_type": "int", "method": "firstBadVersion", "params": ["int n"]},
    {"id": 374, "title": "Guess Number Higher or Lower", "category": "binary_search", "kind": "guess_number", "return_type": "int", "method": "guessNumber", "params": ["int n"]},
    {"id": 33, "title": "Search in Rotated Sorted Array", "category": "binary_search", "kind": "solution", "return_type": "int", "method": "search", "params": ["vector<int>& nums", "int target"]},
    {"id": 153, "title": "Find Minimum in Rotated Sorted Array", "category": "binary_search", "kind": "solution", "return_type": "int", "method": "findMin", "params": ["vector<int>& nums"]},
    {"id": 206, "title": "Reverse Linked List", "category": "linked_list", "kind": "listnode", "return_type": "ListNode*", "method": "reverseList", "params": ["ListNode* head"]},
    {"id": 21, "title": "Merge Two Sorted Lists", "category": "linked_list", "kind": "listnode", "return_type": "ListNode*", "method": "mergeTwoLists", "params": ["ListNode* list1", "ListNode* list2"]},
    {"id": 141, "title": "Linked List Cycle", "category": "linked_list", "kind": "listnode", "return_type": "bool", "method": "hasCycle", "params": ["ListNode* head"]},
    {"id": 876, "title": "Middle of the Linked List", "category": "linked_list", "kind": "listnode", "return_type": "ListNode*", "method": "middleNode", "params": ["ListNode* head"]},
    {"id": 19, "title": "Remove Nth Node From End of List", "category": "linked_list", "kind": "listnode", "return_type": "ListNode*", "method": "removeNthFromEnd", "params": ["ListNode* head", "int n"]},
    {"id": 83, "title": "Remove Duplicates from Sorted List", "category": "linked_list", "kind": "listnode", "return_type": "ListNode*", "method": "deleteDuplicates", "params": ["ListNode* head"]},
    {"id": 160, "title": "Intersection of Two Linked Lists", "category": "linked_list", "kind": "listnode", "return_type": "ListNode*", "method": "getIntersectionNode", "params": ["ListNode* headA", "ListNode* headB"]},
    {"id": 234, "title": "Palindrome Linked List", "category": "linked_list", "kind": "listnode", "return_type": "bool", "method": "isPalindrome", "params": ["ListNode* head"]},
    {"id": 155, "title": "Min Stack", "category": "stack_queue", "kind": "design_minstack"},
    {"id": 150, "title": "Evaluate Reverse Polish Notation", "category": "stack_queue", "kind": "solution", "return_type": "int", "method": "evalRPN", "params": ["vector<string>& tokens"]},
    {"id": 739, "title": "Daily Temperatures", "category": "stack_queue", "kind": "solution", "return_type": "vector<int>", "method": "dailyTemperatures", "params": ["vector<int>& temperatures"]},
    {"id": 232, "title": "Implement Queue using Stacks", "category": "stack_queue", "kind": "design_myqueue"},
    {"id": 225, "title": "Implement Stack using Queues", "category": "stack_queue", "kind": "design_mystack"},
    {"id": 1047, "title": "Remove All Adjacent Duplicates In String", "category": "stack_queue", "kind": "solution", "return_type": "string", "method": "removeDuplicates", "params": ["string s"]},
    {"id": 94, "title": "Binary Tree Inorder Traversal", "category": "binary_tree", "kind": "treenode", "return_type": "vector<int>", "method": "inorderTraversal", "params": ["TreeNode* root"]},
    {"id": 144, "title": "Binary Tree Preorder Traversal", "category": "binary_tree", "kind": "treenode", "return_type": "vector<int>", "method": "preorderTraversal", "params": ["TreeNode* root"]},
    {"id": 145, "title": "Binary Tree Postorder Traversal", "category": "binary_tree", "kind": "treenode", "return_type": "vector<int>", "method": "postorderTraversal", "params": ["TreeNode* root"]},
    {"id": 104, "title": "Maximum Depth of Binary Tree", "category": "binary_tree", "kind": "treenode", "return_type": "int", "method": "maxDepth", "params": ["TreeNode* root"]},
    {"id": 226, "title": "Invert Binary Tree", "category": "binary_tree", "kind": "treenode", "return_type": "TreeNode*", "method": "invertTree", "params": ["TreeNode* root"]},
    {"id": 100, "title": "Same Tree", "category": "binary_tree", "kind": "treenode", "return_type": "bool", "method": "isSameTree", "params": ["TreeNode* p", "TreeNode* q"]},
    {"id": 101, "title": "Symmetric Tree", "category": "binary_tree", "kind": "treenode", "return_type": "bool", "method": "isSymmetric", "params": ["TreeNode* root"]},
    {"id": 543, "title": "Diameter of Binary Tree", "category": "binary_tree", "kind": "treenode", "return_type": "int", "method": "diameterOfBinaryTree", "params": ["TreeNode* root"]},
    {"id": 102, "title": "Binary Tree Level Order Traversal", "category": "binary_tree", "kind": "treenode", "return_type": "vector<vector<int>>", "method": "levelOrder", "params": ["TreeNode* root"]},
    {"id": 112, "title": "Path Sum", "category": "binary_tree", "kind": "treenode", "return_type": "bool", "method": "hasPathSum", "params": ["TreeNode* root", "int targetSum"]},
    {"id": 200, "title": "Number of Islands", "category": "graph_grid", "kind": "solution", "return_type": "int", "method": "numIslands", "params": ["vector<vector<char>>& grid"]},
    {"id": 733, "title": "Flood Fill", "category": "graph_grid", "kind": "solution", "return_type": "vector<vector<int>>", "method": "floodFill", "params": ["vector<vector<int>>& image", "int sr", "int sc", "int color"]},
    {"id": 695, "title": "Max Area of Island", "category": "graph_grid", "kind": "solution", "return_type": "int", "method": "maxAreaOfIsland", "params": ["vector<vector<int>>& grid"]},
    {"id": 994, "title": "Rotting Oranges", "category": "graph_grid", "kind": "solution", "return_type": "int", "method": "orangesRotting", "params": ["vector<vector<int>>& grid"]},
    {"id": 542, "title": "01 Matrix", "category": "graph_grid", "kind": "solution", "return_type": "vector<vector<int>>", "method": "updateMatrix", "params": ["vector<vector<int>>& mat"]},
    {"id": 207, "title": "Course Schedule", "category": "graph", "kind": "solution", "return_type": "bool", "method": "canFinish", "params": ["int numCourses", "vector<vector<int>>& prerequisites"]},
    {"id": 133, "title": "Clone Graph", "category": "graph", "kind": "graph_node", "return_type": "Node*", "method": "cloneGraph", "params": ["Node* node"]},
    {"id": 463, "title": "Island Perimeter", "category": "graph_grid", "kind": "solution", "return_type": "int", "method": "islandPerimeter", "params": ["vector<vector<int>>& grid"]},
    {"id": 70, "title": "Climbing Stairs", "category": "dynamic_programming", "kind": "solution", "return_type": "int", "method": "climbStairs", "params": ["int n"]},
    {"id": 509, "title": "Fibonacci Number", "category": "dynamic_programming", "kind": "solution", "return_type": "int", "method": "fib", "params": ["int n"]},
    {"id": 1137, "title": "N-th Tribonacci Number", "category": "dynamic_programming", "kind": "solution", "return_type": "int", "method": "tribonacci", "params": ["int n"]},
    {"id": 198, "title": "House Robber", "category": "dynamic_programming", "kind": "solution", "return_type": "int", "method": "rob", "params": ["vector<int>& nums"]},
    {"id": 746, "title": "Min Cost Climbing Stairs", "category": "dynamic_programming", "kind": "solution", "return_type": "int", "method": "minCostClimbingStairs", "params": ["vector<int>& cost"]},
    {"id": 62, "title": "Unique Paths", "category": "dynamic_programming", "kind": "solution", "return_type": "int", "method": "uniquePaths", "params": ["int m", "int n"]},
    {"id": 64, "title": "Minimum Path Sum", "category": "dynamic_programming", "kind": "solution", "return_type": "int", "method": "minPathSum", "params": ["vector<vector<int>>& grid"]},
    {"id": 322, "title": "Coin Change", "category": "dynamic_programming", "kind": "solution", "return_type": "int", "method": "coinChange", "params": ["vector<int>& coins", "int amount"]},
    {"id": 56, "title": "Merge Intervals", "category": "interval_greedy", "kind": "solution", "return_type": "vector<vector<int>>", "method": "merge", "params": ["vector<vector<int>>& intervals"]},
    {"id": 57, "title": "Insert Interval", "category": "interval_greedy", "kind": "solution", "return_type": "vector<vector<int>>", "method": "insert", "params": ["vector<vector<int>>& intervals", "vector<int>& newInterval"]},
    {"id": 435, "title": "Non-overlapping Intervals", "category": "interval_greedy", "kind": "solution", "return_type": "int", "method": "eraseOverlapIntervals", "params": ["vector<vector<int>>& intervals"]},
    {"id": 55, "title": "Jump Game", "category": "interval_greedy", "kind": "solution", "return_type": "bool", "method": "canJump", "params": ["vector<int>& nums"]},
    {"id": 452, "title": "Minimum Number of Arrows to Burst Balloons", "category": "interval_greedy", "kind": "solution", "return_type": "int", "method": "findMinArrowShots", "params": ["vector<vector<int>>& points"]},
    {"id": 54, "title": "Spiral Matrix", "category": "matrix", "kind": "solution", "return_type": "vector<int>", "method": "spiralOrder", "params": ["vector<vector<int>>& matrix"]},
    {"id": 73, "title": "Set Matrix Zeroes", "category": "matrix", "kind": "solution", "return_type": "void", "method": "setZeroes", "params": ["vector<vector<int>>& matrix"]},
]


def enrich_round1_problem(problem):
    problem = dict(problem)
    practice_data = ROUND1_PRACTICE_DATA.get(problem["id"])
    if practice_data:
        problem.update(practice_data)
    return problem


ROUND1_PROBLEMS = [enrich_round1_problem(problem) for problem in ROUND1_PROBLEMS]


def zero_pad(problem_id: int) -> str:
    return f"{problem_id:03d}"


def slugify(title: str) -> str:
    text = title.lower().replace("ii", "ii").replace("iii", "iii")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def pascal_file_name(title: str) -> str:
    parts = re.findall(r"[A-Za-z0-9]+", title)
    return "".join(parts)


def default_return(return_type: str) -> str:
    mapping = {
        "bool": "false",
        "int": "0",
        "double": "0.0",
        "uint32_t": "0",
        "string": '""',
        "void": "",
        "vector<int>": "{}",
        "vector<char>": "{}",
        "vector<string>": "{}",
        "vector<double>": "{}",
        "vector<vector<int>>": "{}",
        "vector<vector<string>>": "{}",
        "ListNode*": "nullptr",
        "TreeNode*": "nullptr",
        "Node*": "nullptr",
    }
    return mapping.get(return_type, "{}")


def type_includes(problem):
    includes = {
        "#include <algorithm>",
        "#include <cstdint>",
        "#include <deque>",
        "#include <iostream>",
        "#include <list>",
        "#include <map>",
        "#include <numeric>",
        "#include <queue>",
        "#include <set>",
        "#include <stack>",
        "#include <string>",
        "#include <unordered_map>",
        "#include <unordered_set>",
        "#include <vector>",
    }
    joined = " ".join(problem.get("params", []))
    return_type = problem.get("return_type", "")
    if "uint32_t" in joined or return_type == "uint32_t":
        includes.add("#include <cstdint>")
    if problem.get("category") == "hash_map":
        includes.add("#include <unordered_map>")
        includes.add("#include <unordered_set>")
    if "string" in joined or return_type == "string":
        includes.add("#include <string>")
    return sorted(includes)


def build_md(problem):
    guide = CATEGORY_GUIDANCE[problem["category"]]
    title = problem["title"]
    pid = zero_pad(problem["id"])
    url = f"https://leetcode.com/problems/{slugify(title)}/"
    return f"""# {problem['id']}. {title}

## 题目链接

- {url}

## 题目要求

- 请先用中文把题意重述一遍，再开始写代码。
- 重点写清楚：输入是什么、输出是什么、什么情况算有效答案。

## 示例

- TODO：从题目页面补一个有代表性的示例。

## 约束条件

- TODO：读题后把关键数据范围补在这里。

## 推荐题型

- 主模式：`{guide['pattern']}`

## 提示

- {guide['hints'][0]}
- {guide['hints'][1]}

## 复杂度目标

- {guide['complexity']}

## 本地练习清单

- 先完整读一遍原题。
- 再用自己的中文把题意写一遍。
- 在 `{pid}_{pascal_file_name(title)}.cpp` 里补一个本地测试样例。
- 不看完整题解，先自己完成函数主体。
"""


def build_solution_body(problem):
    guide = CATEGORY_GUIDANCE[problem["category"]]
    return_type = problem["return_type"]
    params = ", ".join(problem["params"])
    default = default_return(return_type)
    return_stmt = "        return;\n" if return_type == "void" else f"        return {default};\n"
    return f"""class Solution {{
public:
    {return_type} {problem['method']}({params}) {{
        // TODO：
        // 这里是你自己写题解的核心区域。
        // 建议先用一句话写下你的思路，再开始补代码。
        // 然后想清楚：每一步要维护哪些状态。
        //
        // 入门提示：
        // - {guide['hints'][0]}
        // - {guide['hints'][1]}

{chr(10).join(f"        (void){p.split()[-1].replace('&', '').replace('*', '')};" for p in problem["params"])}
{return_stmt}    }}
}};
"""


def build_listnode_struct():
    return """struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

"""


def build_treenode_struct():
    return """struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

"""


def build_graph_node_struct():
    return """class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() : val(0) {}
    explicit Node(int value) : val(value) {}
    Node(int value, vector<Node*> neighbors) : val(value), neighbors(neighbors) {}
};

"""


def build_random_list_node_struct():
    return """class Node {
public:
    int val;
    Node* next;
    Node* random;
    Node(int value) : val(value), next(nullptr), random(nullptr) {}
};

"""


def build_next_node_struct():
    return """class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;
    Node() : val(0), left(nullptr), right(nullptr), next(nullptr) {}
    explicit Node(int value) : val(value), left(nullptr), right(nullptr), next(nullptr) {}
    Node(int value, Node* left, Node* right, Node* next)
        : val(value), left(left), right(right), next(next) {}
};

"""


def build_bad_version_stub():
    return """bool isBadVersion(int version) {
    (void)version;
    return false;
}

"""


def build_guess_stub():
    return """int guess(int num) {
    (void)num;
    return 0;
}

"""


def build_codec_class(problem):
    return f"""class Codec {{
public:
    string serialize(TreeNode* root) {{
        // TODO：把二叉树编码成字符串。
        (void)root;
        return "";
    }}

    TreeNode* deserialize(string data) {{
        // TODO：把字符串还原成二叉树。
        (void)data;
        return nullptr;
    }}
}};

int main() {{
    Codec codec;
    cout << "练习目标：{problem['id']}. {problem['title']}" << '\\n';
    cout << "请在当前文件补全 serialize() 和 deserialize()，再在下方添加你自己的本地测试。" << '\\n';
    cout << "当前结果：尚未执行真实样例" << '\\n';
    cout << "预期结果：请在补充测试后自行填写" << '\\n';
    (void)codec;
    return 0;
}}
"""


def build_design_class(problem):
    title = problem["title"]
    if problem["kind"] == "design_minstack":
        body = """class MinStack {
public:
    MinStack() {}

    void push(int val) {
        (void)val;
        // TODO：实现 push。
    }

    void pop() {
        // TODO：实现 pop。
    }

    int top() {
        // TODO：返回当前栈顶元素。
        return 0;
    }

    int getMin() {
        // TODO：返回当前最小值。
        return 0;
    }
};
"""
        main_target = "MinStack solution;"
    elif problem["kind"] == "design_randomizedset":
        body = """class RandomizedSet {
public:
    RandomizedSet() {}

    bool insert(int val) {
        (void)val;
        // TODO：实现 insert。
        return false;
    }

    bool remove(int val) {
        (void)val;
        // TODO：实现 remove。
        return false;
    }

    int getRandom() {
        // TODO：返回一个当前存储的值。
        return 0;
    }
};
"""
        main_target = "RandomizedSet solution;"
    elif problem["kind"] == "design_myqueue":
        body = """class MyQueue {
public:
    MyQueue() {}

    void push(int x) {
        (void)x;
        // TODO：实现 push。
    }

    int pop() {
        // TODO：实现 pop。
        return 0;
    }

    int peek() {
        // TODO：实现 peek。
        return 0;
    }

    bool empty() {
        // TODO：返回队列是否为空。
        return true;
    }
};
"""
        main_target = "MyQueue solution;"
    elif problem["kind"] == "design_trie":
        body = """class Trie {
public:
    Trie() {}

    void insert(string word) {
        (void)word;
        // TODO：实现 insert。
    }

    bool search(string word) {
        (void)word;
        // TODO：实现 search。
        return false;
    }

    bool startsWith(string prefix) {
        (void)prefix;
        // TODO：实现 startsWith。
        return false;
    }
};
"""
        main_target = "Trie solution;"
    elif problem["kind"] == "design_worddictionary":
        body = """class WordDictionary {
public:
    WordDictionary() {}

    void addWord(string word) {
        (void)word;
        // TODO：实现 addWord。
    }

    bool search(string word) {
        (void)word;
        // TODO：实现 search。
        return false;
    }
};
"""
        main_target = "WordDictionary solution;"
    elif problem["kind"] == "design_bstiterator":
        body = """class BSTIterator {
public:
    explicit BSTIterator(TreeNode* root) {
        (void)root;
        // TODO：初始化迭代器状态。
    }

    int next() {
        // TODO：返回下一个最小值。
        return 0;
    }

    bool hasNext() {
        // TODO：返回是否还有下一个值。
        return false;
    }
};
"""
        main_target = "BSTIterator solution(nullptr);"
    elif problem["kind"] == "design_kthlargest":
        body = """class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) {
        (void)k;
        (void)nums;
        // TODO：初始化数据结构。
    }

    int add(int val) {
        (void)val;
        // TODO：插入 val，并返回当前第 k 大元素。
        return 0;
    }
};
"""
        main_target = "vector<int> seed; KthLargest solution(1, seed);"
    elif problem["kind"] == "design_medianfinder":
        body = """class MedianFinder {
public:
    MedianFinder() {}

    void addNum(int num) {
        (void)num;
        // TODO：实现 addNum。
    }

    double findMedian() {
        // TODO：返回当前中位数。
        return 0.0;
    }
};
"""
        main_target = "MedianFinder solution;"
    elif problem["kind"] == "design_mapsum":
        body = """class MapSum {
public:
    MapSum() {}

    void insert(string key, int val) {
        (void)key;
        (void)val;
        // TODO：实现 insert。
    }

    int sum(string prefix) {
        (void)prefix;
        // TODO：返回此前缀的和值。
        return 0;
    }
};
"""
        main_target = "MapSum solution;"
    elif problem["kind"] == "design_stockspanner":
        body = """class StockSpanner {
public:
    StockSpanner() {}

    int next(int price) {
        (void)price;
        // TODO：返回当前跨度。
        return 0;
    }
};
"""
        main_target = "StockSpanner solution;"
    elif problem["kind"] == "design_lrucache":
        body = """class LRUCache {
public:
    explicit LRUCache(int capacity) {
        (void)capacity;
        // TODO：初始化缓存状态。
    }

    int get(int key) {
        (void)key;
        // TODO：返回对应值，不存在时返回 -1。
        return -1;
    }

    void put(int key, int value) {
        (void)key;
        (void)value;
        // TODO：插入或更新一条记录。
    }
};
"""
        main_target = "LRUCache solution(1);"
    elif problem["kind"] == "design_lfu_cache":
        body = """class LFUCache {
public:
    explicit LFUCache(int capacity) {
        (void)capacity;
        // TODO：初始化缓存状态。
    }

    int get(int key) {
        (void)key;
        // TODO：返回对应值，不存在时返回 -1。
        return -1;
    }

    void put(int key, int value) {
        (void)key;
        (void)value;
        // TODO：插入或更新一条记录。
    }
};
"""
        main_target = "LFUCache solution(1);"
    elif problem["kind"] == "design_allone":
        body = """class AllOne {
public:
    AllOne() {}

    void inc(string key) {
        (void)key;
        // TODO：实现 inc。
    }

    void dec(string key) {
        (void)key;
        // TODO：实现 dec。
    }

    string getMaxKey() {
        // TODO：返回任意一个最大频次的 key。
        return "";
    }

    string getMinKey() {
        // TODO：返回任意一个最小频次的 key。
        return "";
    }
};
"""
        main_target = "AllOne solution;"
    else:
        body = """class MyStack {
public:
    MyStack() {}

    void push(int x) {
        (void)x;
        // TODO：实现 push。
    }

    int pop() {
        // TODO：实现 pop。
        return 0;
    }

    int top() {
        // TODO：实现 top。
        return 0;
    }

    bool empty() {
        // TODO：返回栈是否为空。
        return true;
    }
};
"""
        main_target = "MyStack solution;"

    return body + f"""
int main() {{
    {main_target}
    cout << "练习目标：{problem['id']}. {title}" << '\\n';
    cout << "请先补全本文件中的设计类方法，再在下方添加你自己的本地测试。" << '\\n';
    cout << "当前结果：尚未执行真实样例" << '\\n';
    cout << "预期结果：请在补充测试后自行填写" << '\\n';
    (void)solution;
    return 0;
}}
"""


def build_standard_main(problem):
    instance_name = "solution"
    class_name = "Solution"
    return f"""
int main() {{
    {class_name} {instance_name};
    cout << "练习目标：{problem['id']}. {problem['title']}" << '\\n';
    cout << "请在当前文件补全 {problem['method']}()，再在下方添加你自己的本地测试。" << '\\n';
    cout << "当前结果：尚未执行真实样例" << '\\n';
    cout << "预期结果：请在补充测试后自行填写" << '\\n';
    (void){instance_name};
    return 0;
}}
"""


def build_cpp(problem):
    includes = type_includes(problem)
    sections = ["\n".join(includes), "", "using namespace std;", ""]

    kind = problem["kind"]
    if kind == "listnode":
        sections.append(build_listnode_struct())
        sections.append(build_solution_body(problem))
        sections.append(build_standard_main(problem))
    elif kind == "random_list_node":
        sections.append(build_random_list_node_struct())
        sections.append(build_solution_body(problem))
        sections.append(build_standard_main(problem))
    elif kind == "treenode":
        sections.append(build_treenode_struct())
        sections.append(build_solution_body(problem))
        sections.append(build_standard_main(problem))
    elif kind == "nextnode_tree":
        sections.append(build_next_node_struct())
        sections.append(build_solution_body(problem))
        sections.append(build_standard_main(problem))
    elif kind == "graph_node":
        sections.append(build_graph_node_struct())
        sections.append(build_solution_body(problem))
        sections.append(build_standard_main(problem))
    elif kind == "codec_tree":
        sections.append(build_treenode_struct())
        sections.append(build_codec_class(problem))
    elif kind == "bad_version":
        sections.append(build_bad_version_stub())
        sections.append(build_solution_body(problem))
        sections.append(build_standard_main(problem))
    elif kind == "guess_number":
        sections.append(build_guess_stub())
        sections.append(build_solution_body(problem))
        sections.append(build_standard_main(problem))
    elif kind.startswith("design_"):
        sections.append(build_design_class(problem))
    else:
        sections.append(build_solution_body(problem))
        sections.append(build_standard_main(problem))

    return "\n".join(sections).strip() + "\n"


legacy_build_md = build_md
legacy_build_cpp = build_cpp


def param_name(param):
    return param.split()[-1].replace("&", "").replace("*", "")


def param_value_type(param):
    name = param.split()[-1]
    return param[: -len(name)].strip().replace("&", "").strip()


def cpp_string(value):
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def cpp_bool(value):
    return "true" if value else "false"


def cpp_char(value):
    return "'" + value.replace("\\", "\\\\").replace("'", "\\'") + "'"


def cpp_literal(value, type_hint=None):
    if isinstance(value, bool):
        return cpp_bool(value)
    if isinstance(value, str):
        if type_hint and "char" in type_hint and len(value) == 1:
            return cpp_char(value)
        return cpp_string(value)
    if isinstance(value, float):
        return repr(value)
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        return "{" + ", ".join(cpp_literal(item, type_hint) for item in value) + "}"
    raise TypeError(f"Unsupported literal value: {value!r}")


def cpp_typed_literal(value, type_name):
    return f"{type_name}{cpp_literal(value, type_name)}"


def cpp_expected_expr(value, type_name):
    if type_name.startswith("vector<"):
        return cpp_typed_literal(value, type_name)
    return cpp_literal(value, type_name)


def cpp_tree_literal(values):
    return "{" + ", ".join(cpp_string(value) for value in values) + "}"


def cpp_tree_vector_expr(values):
    return "vector<string>" + cpp_tree_literal(values)


def sample_value_for_type(type_name):
    clean_type = type_name.replace("const ", "").strip()
    if clean_type in {"int", "uint32_t"}:
        return 0
    if clean_type == "double":
        return 0.0
    if clean_type == "bool":
        return False
    if clean_type == "string":
        return ""
    if clean_type == "char":
        return "a"
    if clean_type.startswith("vector<"):
        return []
    if clean_type.endswith("*"):
        return None
    return 0


def generic_mutated_param(problem):
    for param in problem.get("params", []):
        if "&" in param:
            return param_name(param)
    return param_name(problem["params"][0])


def problem_with_generic_local_case(problem):
    enriched = dict(problem)
    args = [sample_value_for_type(param_value_type(param)) for param in problem["params"]]
    expected_type = problem["return_type"]
    if problem["return_type"] == "void":
        mutated = generic_mutated_param(problem)
        enriched["mutates"] = mutated
        expected_type = param_value_type(next(param for param in problem["params"] if param_name(param) == mutated))
    enriched["local_cases"] = [
        {
            "label": "模板样例",
            "args": args,
            "expected": sample_value_for_type(expected_type),
        }
    ]
    return enriched


def build_generic_md(problem):
    guide = CATEGORY_GUIDANCE[problem["category"]]
    title = problem["title"]
    pid = zero_pad(problem["id"])
    url = f"https://leetcode.com/problems/{slugify(title)}/"
    hints = "\n".join(f"- {item}" for item in guide["hints"])

    return f"""# {problem['id']}. {title}

## 题目链接

- {url}

## 题目要求

- 先打开原题，确认输入、输出和有效答案的定义。
- 用中文把题意复述一遍，再开始补全代码。
- 本模板只保留练习入口，不直接提供完整题解。

## 示例

- 请从原题中选一个官方示例，手动写到你的练习记录里。

## 约束条件

- 请读题后记录输入规模、取值范围和需要特别处理的边界情况。

## 推荐题型

- 主模式：`{guide['pattern']}`

## 提示

{hints}

## 复杂度目标

- {guide['complexity']}

## 本地练习清单

- 先完整读一遍原题。
- 再用自己的中文把题意复述一遍。
- 在 `{pid}_{pascal_file_name(title)}.cpp` 的待实现区域补全算法。
- 运行本地样例，对照“当前结果”和“预期结果”。
"""


def has_round1_practice_data(problem):
    return "local_cases" in problem and "summary" in problem


def build_md(problem):
    if not has_round1_practice_data(problem):
        return build_generic_md(problem)

    guide = CATEGORY_GUIDANCE[problem["category"]]
    title = problem["title"]
    pid = zero_pad(problem["id"])
    url = f"https://leetcode.com/problems/{slugify(title)}/"

    examples = []
    for index, example in enumerate(problem["examples"], start=1):
        examples.append(
            f"### 示例 {index}\n\n"
            f"- 输入：`{example['input']}`\n"
            f"- 输出：`{example['output']}`\n"
            f"- 解释：{example['explanation']}"
        )

    constraints = "\n".join(f"- {item}" for item in problem["constraints"])
    approach_items = problem.get("approach", guide["hints"])
    approach = "\n".join(f"- {item}" for item in approach_items)
    hints = "\n".join(f"- {item}" for item in guide["hints"])

    return f"""# {problem['id']}. {title}

## 题目链接

- {url}

## 题目要求

{problem['summary']}

## 示例

{chr(10).join(examples)}

## 约束条件

{constraints}

## 解题思路

{approach}

## 推荐题型

- 主模式：`{guide['pattern']}`

## 提示

{hints}

## 复杂度目标

- {guide['complexity']}

## 本地练习清单

- 先完整读一遍原题。
- 再用自己的中文把题意复述一遍。
- 在 `{pid}_{pascal_file_name(title)}.cpp` 的待实现区域补全算法。
- 运行本地样例，对照“当前结果”和“预期结果”。
"""


def build_print_helpers():
    return """void printValue(bool value) {
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

"""


def build_solution_run_case(problem):
    return_type = problem["return_type"]
    params = problem["params"]
    declarations = []
    names = []
    for param in params:
        declarations.append(f"{param_value_type(param)} {param_name(param)}")
        names.append(param_name(param))

    if return_type == "void":
        mutated = problem["mutates"]
        expected_type = param_value_type(next(param for param in params if param_name(param) == mutated))
        run_case = f"""void runCase(const string& label, {", ".join(declarations)}, {expected_type} expected) {{
    Solution solution;
    solution.{problem['method']}({", ".join(names)});
    cout << label << '\\n';
    cout << "当前结果：";
    printValue({mutated});
    cout << '\\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\\n\\n";
}}
"""
    else:
        run_case = f"""void runCase(const string& label, {", ".join(declarations)}, {return_type} expected) {{
    Solution solution;
    {return_type} actual = solution.{problem['method']}({", ".join(names)});
    cout << label << '\\n';
    cout << "当前结果：";
    printValue(actual);
    cout << '\\n';
    cout << "预期结果：";
    printValue(expected);
    cout << "\\n\\n";
}}
"""

    calls = []
    for case in problem["local_cases"]:
        args = []
        for param, value in zip(params, case["args"]):
            args.append(cpp_literal(value, param_value_type(param)))
        expected_type = return_type
        if return_type == "void":
            expected_type = param_value_type(next(param for param in params if param_name(param) == problem["mutates"]))
        args.append(cpp_literal(case["expected"], expected_type))
        calls.append(f"    runCase({cpp_string(case['label'])}, {', '.join(args)});")

    return run_case + f"""
int main() {{
    cout << "练习目标：{problem['id']}. {problem['title']}" << '\\n';
    cout << "只需要补全 {problem['method']}() 的 TODO 区域，再重新运行本地样例。" << "\\n\\n";
{chr(10).join(calls)}
    return 0;
}}
"""


def build_list_helpers():
    return """ListNode* buildList(const vector<int>& values) {
    ListNode dummy;
    ListNode* tail = &dummy;
    for (int value : values) {
        tail->next = new ListNode(value);
        tail = tail->next;
    }
    return dummy.next;
}

vector<int> listToVector(ListNode* head, size_t limit = 100) {
    vector<int> values;
    while (head != nullptr && values.size() < limit) {
        values.push_back(head->val);
        head = head->next;
    }
    return values;
}

ListNode* buildCycleList(const vector<int>& values, int pos) {
    ListNode dummy;
    ListNode* tail = &dummy;
    ListNode* cycleEntry = nullptr;
    for (size_t i = 0; i < values.size(); ++i) {
        tail->next = new ListNode(values[i]);
        tail = tail->next;
        if (static_cast<int>(i) == pos) {
            cycleEntry = tail;
        }
    }
    if (tail != &dummy) {
        tail->next = cycleEntry;
    }
    return dummy.next;
}

ListNode* appendSharedTail(const vector<int>& prefix, ListNode* sharedTail) {
    if (prefix.empty()) {
        return sharedTail;
    }
    ListNode* head = buildList(prefix);
    ListNode* tail = head;
    while (tail->next != nullptr) {
        tail = tail->next;
    }
    tail->next = sharedTail;
    return head;
}

"""


def build_listnode_param_setup(problem, case):
    params = problem["params"]
    setup_lines = []
    call_args = []

    if len(params) == 1 and param_value_type(params[0]) == "vector<ListNode*>":
        list_vars = []
        for index, values in enumerate(case["lists"]):
            var_name = f"list{index + 1}"
            list_vars.append(var_name)
            setup_lines.append(f"        ListNode* {var_name} = buildList({cpp_literal(values)});")
        setup_lines.append(f"        vector<ListNode*> lists = {{{', '.join(list_vars)}}};")
        return "\n".join(setup_lines), ["lists"]

    list_index = 0
    extra_args = list(case.get("args", []))
    for param in params:
        if param_value_type(param) == "ListNode*":
            list_index += 1
            var_name = f"list{list_index}"
            values = case["lists"][list_index - 1]
            setup_lines.append(f"        ListNode* {var_name} = buildList({cpp_literal(values)});")
            call_args.append(var_name)
        else:
            call_args.append(cpp_literal(extra_args.pop(0), param_value_type(param)))

    return "\n".join(setup_lines), call_args


def build_listnode_run_case(problem):
    method = problem["method"]
    cases = []

    if method == "hasCycle":
        for case in problem["local_cases"]:
            cases.append(
                f"""    {{
        ListNode* head = buildCycleList({cpp_literal(case['values'])}, {case['pos']});
        bool actual = solution.{method}(head);
        cout << {cpp_string(case['label'])} << '\\n';
        cout << "当前结果：";
        printValue(actual);
        cout << '\\n';
        cout << "预期结果：";
        printValue({cpp_bool(case['expected'])});
        cout << "\\n\\n";
    }}"""
            )
    elif method == "getIntersectionNode":
        for case in problem["local_cases"]:
            shared = case["listA"][case["skipA"] :]
            prefix_a = case["listA"][: case["skipA"]]
            cases.append(
                f"""    {{
        ListNode* sharedTail = buildList({cpp_literal(shared)});
        ListNode* headA = appendSharedTail({cpp_literal(prefix_a)}, sharedTail);
        ListNode* headB = appendSharedTail({cpp_literal(case['listBPrefix'])}, sharedTail);
        ListNode* actual = solution.{method}(headA, headB);
        string actualText = actual == nullptr ? "null" : to_string(actual->val);
        cout << {cpp_string(case['label'])} << '\\n';
        cout << "当前结果：";
        printValue(actualText);
        cout << '\\n';
        cout << "预期结果：";
        printValue({cpp_string(case['expected'])});
        cout << "\\n\\n";
    }}"""
            )
    else:
        for case in problem["local_cases"]:
            setup, call_args = build_listnode_param_setup(problem, case)
            if problem["return_type"] == "void":
                actual_line = f"        solution.{method}({', '.join(call_args)});"
                print_actual = "        printValue(listToVector(list1));"
                expected = cpp_expected_expr(case["expected"], "vector<int>")
            elif problem["return_type"] == "bool":
                actual_line = f"        bool actual = solution.{method}({', '.join(call_args)});"
                print_actual = "        printValue(actual);"
                expected = cpp_bool(case["expected"])
            else:
                actual_line = f"        ListNode* actual = solution.{method}({', '.join(call_args)});"
                print_actual = "        printValue(listToVector(actual));"
                expected = cpp_expected_expr(case["expected"], "vector<int>")
            cases.append(
                f"""    {{
{setup}
{actual_line}
        cout << {cpp_string(case['label'])} << '\\n';
        cout << "当前结果：";
{print_actual}
        cout << '\\n';
        cout << "预期结果：";
        printValue({expected});
        cout << "\\n\\n";
    }}"""
            )

    return f"""
int main() {{
    Solution solution;
    cout << "练习目标：{problem['id']}. {problem['title']}" << '\\n';
    cout << "只需要补全 {method}() 的 TODO 区域，再重新运行本地样例。" << "\\n\\n";
{chr(10).join(case for case in cases if case)}
    return 0;
}}
"""


def build_random_list_helpers():
    return """Node* buildRandomList(const vector<pair<int, int>>& nodes) {
    if (nodes.empty()) {
        return nullptr;
    }

    vector<Node*> built;
    for (const auto& item : nodes) {
        built.push_back(new Node(item.first));
    }
    for (size_t i = 0; i + 1 < built.size(); ++i) {
        built[i]->next = built[i + 1];
    }
    for (size_t i = 0; i < nodes.size(); ++i) {
        int randomIndex = nodes[i].second;
        if (randomIndex >= 0) {
            built[i]->random = built[randomIndex];
        }
    }
    return built[0];
}

vector<vector<int>> randomListToPairs(Node* head, size_t limit = 100) {
    vector<Node*> nodes;
    unordered_map<Node*, int> indexByNode;
    Node* current = head;
    while (current != nullptr && nodes.size() < limit) {
        indexByNode[current] = static_cast<int>(nodes.size());
        nodes.push_back(current);
        current = current->next;
    }

    vector<vector<int>> result;
    for (Node* node : nodes) {
        int randomIndex = node->random == nullptr ? -1 : indexByNode[node->random];
        result.push_back({node->val, randomIndex});
    }
    return result;
}

"""


def cpp_pair_vector_literal(values):
    return "{" + ", ".join("{" + f"{item[0]}, {item[1]}" + "}" for item in values) + "}"


def build_random_list_run_case(problem):
    method = problem["method"]
    cases = []
    for case in problem["local_cases"]:
        expected = cpp_expected_expr(case["expected"], "vector<vector<int>>")
        cases.append(
            f"""    {{
        Node* head = buildRandomList({cpp_pair_vector_literal(case['nodes'])});
        Node* actual = solution.{method}(head);
        cout << {cpp_string(case['label'])} << '\\n';
        cout << "当前结果：";
        printValue(randomListToPairs(actual));
        cout << '\\n';
        cout << "预期结果：";
        printValue({expected});
        cout << "\\n\\n";
    }}"""
        )

    return f"""
int main() {{
    Solution solution;
    cout << "练习目标：{problem['id']}. {problem['title']}" << '\\n';
    cout << "只需要补全 {method}() 的 TODO 区域，再重新运行本地样例。" << "\\n\\n";
{chr(10).join(cases)}
    return 0;
}}
"""


def build_codec_body_only():
    return """class Codec {
public:
    string serialize(TreeNode* root) {
        // TODO：把二叉树编码成字符串。
        (void)root;
        return "";
    }

    TreeNode* deserialize(string data) {
        // TODO：把字符串还原成二叉树。
        (void)data;
        return nullptr;
    }
};
"""


def build_codec_run_case(problem):
    cases = []
    for case in problem["local_cases"]:
        cases.append(
            f"""    {{
        TreeNode* root = buildTree({cpp_tree_literal(case['tree'])});
        string encoded = codec.serialize(root);
        TreeNode* actual = codec.deserialize(encoded);
        cout << {cpp_string(case['label'])} << '\\n';
        cout << "当前结果：";
        printValue(treeToLevelVector(actual));
        cout << '\\n';
        cout << "预期结果：";
        printValue({cpp_tree_vector_expr(case['expected'])});
        cout << "\\n\\n";
    }}"""
        )

    return f"""
int main() {{
    Codec codec;
    cout << "练习目标：{problem['id']}. {problem['title']}" << '\\n';
    cout << "只需要补全 Codec 的 TODO 方法，再重新运行本地样例。" << "\\n\\n";
{chr(10).join(cases)}
    return 0;
}}
"""


def build_tree_helpers():
    return """TreeNode* buildTree(const vector<string>& values) {
    if (values.empty() || values[0] == "null") {
        return nullptr;
    }

    TreeNode* root = new TreeNode(stoi(values[0]));
    queue<TreeNode*> pending;
    pending.push(root);
    size_t index = 1;

    while (!pending.empty() && index < values.size()) {
        TreeNode* node = pending.front();
        pending.pop();

        if (index < values.size() && values[index] != "null") {
            node->left = new TreeNode(stoi(values[index]));
            pending.push(node->left);
        }
        ++index;

        if (index < values.size() && values[index] != "null") {
            node->right = new TreeNode(stoi(values[index]));
            pending.push(node->right);
        }
        ++index;
    }

    return root;
}

vector<string> treeToLevelVector(TreeNode* root) {
    vector<string> values;
    if (root == nullptr) {
        return values;
    }

    queue<TreeNode*> pending;
    pending.push(root);
    while (!pending.empty()) {
        TreeNode* node = pending.front();
        pending.pop();
        if (node == nullptr) {
            values.push_back("null");
            continue;
        }
        values.push_back(to_string(node->val));
        pending.push(node->left);
        pending.push(node->right);
    }

    while (!values.empty() && values.back() == "null") {
        values.pop_back();
    }
    return values;
}

TreeNode* findNode(TreeNode* root, int value) {
    if (root == nullptr) {
        return nullptr;
    }
    if (root->val == value) {
        return root;
    }
    TreeNode* left = findNode(root->left, value);
    if (left != nullptr) {
        return left;
    }
    return findNode(root->right, value);
}

vector<int> rightChainToVector(TreeNode* root, size_t limit = 100) {
    vector<int> values;
    TreeNode* current = root;
    while (current != nullptr && values.size() < limit) {
        values.push_back(current->val);
        current = current->right;
    }
    return values;
}

"""


def build_next_tree_helpers():
    return """Node* buildNextTree(const vector<string>& values) {
    if (values.empty() || values[0] == "null") {
        return nullptr;
    }

    Node* root = new Node(stoi(values[0]));
    queue<Node*> pending;
    pending.push(root);
    size_t index = 1;

    while (!pending.empty() && index < values.size()) {
        Node* node = pending.front();
        pending.pop();

        if (index < values.size() && values[index] != "null") {
            node->left = new Node(stoi(values[index]));
            pending.push(node->left);
        }
        ++index;

        if (index < values.size() && values[index] != "null") {
            node->right = new Node(stoi(values[index]));
            pending.push(node->right);
        }
        ++index;
    }

    return root;
}

vector<vector<int>> nextLevelsToVector(Node* root) {
    vector<vector<int>> levels;
    Node* levelStart = root;

    while (levelStart != nullptr) {
        vector<int> level;
        Node* current = levelStart;
        Node* nextStart = nullptr;
        while (current != nullptr) {
            level.push_back(current->val);
            if (nextStart == nullptr) {
                if (current->left != nullptr) {
                    nextStart = current->left;
                } else if (current->right != nullptr) {
                    nextStart = current->right;
                }
            }
            current = current->next;
        }
        levels.push_back(level);
        levelStart = nextStart;
    }

    return levels;
}

"""


def build_nextnode_run_case(problem):
    method = problem["method"]
    cases = []
    for case in problem["local_cases"]:
        cases.append(
            f"""    {{
        Node* root = buildNextTree({cpp_tree_literal(case['tree'])});
        Node* actual = solution.{method}(root);
        cout << {cpp_string(case['label'])} << '\\n';
        cout << "当前结果：";
        printValue(nextLevelsToVector(actual));
        cout << '\\n';
        cout << "预期结果：";
        printValue({cpp_expected_expr(case['expected'], 'vector<vector<int>>')});
        cout << "\\n\\n";
    }}"""
        )

    return f"""
int main() {{
    Solution solution;
    cout << "练习目标：{problem['id']}. {problem['title']}" << '\\n';
    cout << "只需要补全 {method}() 的 TODO 区域，再重新运行本地样例。" << "\\n\\n";
{chr(10).join(cases)}
    return 0;
}}
"""


def build_treenode_run_case(problem):
    method = problem["method"]
    cases = []
    for case in problem["local_cases"]:
        consumed_case_args = False
        if "args" in case and "tree" not in case and "trees" not in case:
            setup = ""
            call_args = []
            for param, value in zip(problem["params"], case["args"]):
                value_type = param_value_type(param)
                var_name = param_name(param)
                setup += f"        {value_type} {var_name} = {cpp_expected_expr(value, value_type)};\n"
                call_args.append(var_name)
            setup = setup.rstrip()
            consumed_case_args = True
        elif "trees" in case:
            setup = "\n".join(
                f"        TreeNode* tree{index + 1} = buildTree({cpp_tree_literal(values)});"
                for index, values in enumerate(case["trees"])
            )
            call_args = [f"tree{index + 1}" for index in range(len(case["trees"]))]
        else:
            setup = f"        TreeNode* root = buildTree({cpp_tree_literal(case['tree'])});"
            call_args = ["root"]
        for index, value in enumerate(case.get("node_values", []), start=1):
            var_name = f"node{index}"
            setup += f"\n        TreeNode* {var_name} = findNode(root, {value});"
            call_args.append(var_name)
        if not consumed_case_args:
            call_args.extend(cpp_literal(value) for value in case.get("args", []))

        if problem["return_type"] == "void":
            actual_line = f"        solution.{method}({', '.join(call_args)});"
            print_actual = "        printValue(rightChainToVector(root));"
            expected = cpp_expected_expr(case["expected"], "vector<int>")
        elif problem["return_type"] == "TreeNode*":
            actual_line = f"        TreeNode* actual = solution.{method}({', '.join(call_args)});"
            if isinstance(case["expected"], int):
                print_actual = "        printValue(actual == nullptr ? -1 : actual->val);"
                expected = str(case["expected"])
            else:
                print_actual = "        printValue(treeToLevelVector(actual));"
                expected = cpp_tree_vector_expr(case["expected"])
        else:
            actual_line = f"        auto actual = solution.{method}({', '.join(call_args)});"
            print_actual = "        printValue(actual);"
            expected = cpp_expected_expr(case["expected"], problem["return_type"])

        cases.append(
            f"""    {{
{setup}
{actual_line}
        cout << {cpp_string(case['label'])} << '\\n';
        cout << "当前结果：";
{print_actual}
        cout << '\\n';
        cout << "预期结果：";
        printValue({expected});
        cout << "\\n\\n";
    }}"""
        )

    return f"""
int main() {{
    Solution solution;
    cout << "练习目标：{problem['id']}. {problem['title']}" << '\\n';
    cout << "只需要补全 {method}() 的 TODO 区域，再重新运行本地样例。" << "\\n\\n";
{chr(10).join(cases)}
    return 0;
}}
"""


def build_bad_version_api():
    return """int firstBadVersionForLocalTest = 1;

bool isBadVersion(int version) {
    return version >= firstBadVersionForLocalTest;
}

"""


def build_guess_api():
    return """int secretNumberForLocalTest = 1;

int guess(int num) {
    if (num == secretNumberForLocalTest) {
        return 0;
    }
    return num > secretNumberForLocalTest ? -1 : 1;
}

"""


def build_api_run_case(problem, state_name, state_key):
    cases = []
    for case in problem["local_cases"]:
        cases.append(
            f"""    {{
        {state_name} = {case[state_key]};
        Solution solution;
        int actual = solution.{problem['method']}({case['n']});
        cout << {cpp_string(case['label'])} << '\\n';
        cout << "当前结果：";
        printValue(actual);
        cout << '\\n';
        cout << "预期结果：";
        printValue({case['expected']});
        cout << "\\n\\n";
    }}"""
        )
    return f"""
int main() {{
    cout << "练习目标：{problem['id']}. {problem['title']}" << '\\n';
    cout << "只需要补全 {problem['method']}() 的 TODO 区域，再重新运行本地样例。" << "\\n\\n";
{chr(10).join(cases)}
    return 0;
}}
"""


def build_graph_helpers():
    return """Node* buildSampleGraph() {
    Node* n1 = new Node(1);
    Node* n2 = new Node(2);
    Node* n3 = new Node(3);
    Node* n4 = new Node(4);
    n1->neighbors = {n2, n4};
    n2->neighbors = {n1, n3};
    n3->neighbors = {n2, n4};
    n4->neighbors = {n1, n3};
    return n1;
}

vector<vector<int>> graphToAdjList(Node* node) {
    if (node == nullptr) {
        return {};
    }

    unordered_map<Node*, bool> seen;
    queue<Node*> pending;
    vector<Node*> nodes;
    pending.push(node);
    seen[node] = true;

    while (!pending.empty()) {
        Node* current = pending.front();
        pending.pop();
        nodes.push_back(current);
        for (Node* neighbor : current->neighbors) {
            if (!seen[neighbor]) {
                seen[neighbor] = true;
                pending.push(neighbor);
            }
        }
    }

    size_t maxValue = 0;
    for (Node* current : nodes) {
        maxValue = max(maxValue, static_cast<size_t>(current->val));
    }
    vector<vector<int>> result(maxValue);
    for (Node* current : nodes) {
        for (Node* neighbor : current->neighbors) {
            result[current->val - 1].push_back(neighbor->val);
        }
    }
    return result;
}

"""


def build_graph_run_case(problem):
    case = problem["local_cases"][0]
    return f"""int main() {{
    Solution solution;
    Node* node = buildSampleGraph();
    Node* cloned = solution.{problem['method']}(node);
    cout << "练习目标：{problem['id']}. {problem['title']}" << '\\n';
    cout << "只需要补全 {problem['method']}() 的 TODO 区域，再重新运行本地样例。" << "\\n\\n";
    cout << {cpp_string(case['label'])} << '\\n';
    cout << "当前结果：";
    printValue(graphToAdjList(cloned));
    cout << '\\n';
    cout << "预期结果：";
    printValue({cpp_expected_expr(case['expected'], 'vector<vector<int>>')});
    cout << "\\n\\n";
    return 0;
}}
"""


def design_class_name(kind):
    return {
        "design_minstack": "MinStack",
        "design_randomizedset": "RandomizedSet",
        "design_myqueue": "MyQueue",
        "design_mystack": "MyStack",
        "design_trie": "Trie",
        "design_worddictionary": "WordDictionary",
        "design_bstiterator": "BSTIterator",
        "design_kthlargest": "KthLargest",
        "design_medianfinder": "MedianFinder",
        "design_mapsum": "MapSum",
        "design_stockspanner": "StockSpanner",
        "design_lrucache": "LRUCache",
        "design_lfu_cache": "LFUCache",
        "design_allone": "AllOne",
    }[kind]


def build_design_body_only(problem):
    return build_design_class(problem).split("\nint main() {", 1)[0]


def cpp_design_arg(value):
    if isinstance(value, str):
        return cpp_string(value)
    if isinstance(value, bool):
        return cpp_bool(value)
    if isinstance(value, float):
        return repr(value)
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        return "{" + ", ".join(cpp_design_arg(item) for item in value) + "}"
    raise TypeError(f"Unsupported design argument: {value!r}")


def design_result_line(operation, class_name):
    string_methods = {"getMaxKey", "getMinKey"}
    bool_methods = {"insert", "remove", "search", "startsWith", "empty", "hasNext"}
    double_methods = {"findMedian"}
    if operation in string_methods:
        return f"    actual.push_back(solution.{operation}());"
    if operation in bool_methods:
        return f"    actual.push_back(solution.{operation}(%s) ? \"true\" : \"false\");"
    if operation in double_methods:
        return f"    actual.push_back(to_string(solution.{operation}()));"
    return f"    actual.push_back(to_string(solution.{operation}(%s)));"


def build_design_run_case(problem):
    class_name = design_class_name(problem["kind"])
    case = problem["local_cases"][0]
    setup_lines = []

    if class_name == "BSTIterator":
        setup_lines.append(f"    TreeNode* root = buildTree({cpp_tree_literal(case['inputs'][0][0])});")
        constructor = "BSTIterator solution(root);"
    elif class_name == "KthLargest":
        setup_lines.append(f"    vector<int> initialNumbers = {cpp_expected_expr(case['inputs'][0][1], 'vector<int>')};")
        constructor = f"KthLargest solution({cpp_design_arg(case['inputs'][0][0])}, initialNumbers);"
    else:
        constructor_args = ", ".join(cpp_design_arg(item) for item in case["inputs"][0])
        constructor = f"{class_name} solution;" if not constructor_args else f"{class_name} solution({constructor_args});"

    lines = setup_lines + [f"    {constructor}", '    vector<string> actual = {"null"};']
    for operation, inputs in zip(case["operations"][1:], case["inputs"][1:]):
        args = ", ".join(cpp_design_arg(item) for item in inputs)
        if operation in {"push", "put", "addWord", "insert", "addNum", "inc", "dec"} and operation not in {"insert"}:
            lines.append(f"    solution.{operation}({args});")
            lines.append('    actual.push_back("null");')
        elif operation == "insert" and class_name not in {"RandomizedSet", "MapSum", "Trie"}:
            lines.append(f"    solution.{operation}({args});")
            lines.append('    actual.push_back("null");')
        elif operation == "insert" and class_name in {"MapSum", "Trie"}:
            lines.append(f"    solution.{operation}({args});")
            lines.append('    actual.push_back("null");')
        elif operation == "pop" and class_name == "MinStack":
            lines.append("    solution.pop();")
            lines.append('    actual.push_back("null");')
        else:
            template = design_result_line(operation, class_name)
            if "%s" in template:
                lines.append(template % args)
            else:
                lines.append(template)

    return f"""int main() {{
    cout << "练习目标：{problem['id']}. {problem['title']}" << '\\n';
    cout << "只需要补全 {class_name} 的 TODO 方法，再重新运行本地样例。" << "\\n\\n";
    cout << "示例 1" << '\\n';
{chr(10).join(lines)}
    cout << "当前结果：";
    printValue(actual);
    cout << '\\n';
    cout << "预期结果：";
    printValue({cpp_expected_expr(case['expected'], 'vector<string>')});
    cout << "\\n\\n";
    return 0;
}}
"""


def clean_legacy_exercise_output(cpp_text):
    return (
        cpp_text.replace("当前结果：尚未执行真实样例", "当前结果：练习模板已加载")
        .replace("预期结果：请在补充测试后自行填写", "预期结果：补全 TODO 后再对照官方示例")
    )


def build_generic_cpp(problem):
    if problem["kind"] != "solution":
        return clean_legacy_exercise_output(legacy_build_cpp(problem))

    problem = problem_with_generic_local_case(problem)
    sections = [
        "\n".join(type_includes(problem)),
        "",
        "using namespace std;",
        "",
        build_print_helpers(),
        build_solution_body(problem),
        build_solution_run_case(problem),
    ]
    return "\n".join(sections).strip() + "\n"


def round1_includes(problem):
    includes = set(type_includes(problem))
    if problem["kind"] in {"treenode", "graph_node"}:
        includes.add("#include <queue>")
    if problem["kind"] == "graph_node":
        includes.add("#include <algorithm>")
        includes.add("#include <unordered_map>")
    return sorted(includes)


def build_cpp(problem):
    if not has_round1_practice_data(problem):
        return build_generic_cpp(problem)

    sections = ["\n".join(round1_includes(problem)), "", "using namespace std;", "", build_print_helpers()]
    kind = problem["kind"]

    if kind == "listnode":
        sections.append(build_listnode_struct())
        sections.append(build_list_helpers())
        sections.append(build_solution_body(problem))
        sections.append(build_listnode_run_case(problem))
    elif kind == "random_list_node":
        sections.append(build_random_list_node_struct())
        sections.append(build_random_list_helpers())
        sections.append(build_solution_body(problem))
        sections.append(build_random_list_run_case(problem))
    elif kind == "treenode":
        sections.append(build_treenode_struct())
        sections.append(build_tree_helpers())
        sections.append(build_solution_body(problem))
        sections.append(build_treenode_run_case(problem))
    elif kind == "nextnode_tree":
        sections.append(build_next_node_struct())
        sections.append(build_next_tree_helpers())
        sections.append(build_solution_body(problem))
        sections.append(build_nextnode_run_case(problem))
    elif kind == "codec_tree":
        sections.append(build_treenode_struct())
        sections.append(build_tree_helpers())
        sections.append(build_codec_body_only())
        sections.append(build_codec_run_case(problem))
    elif kind == "graph_node":
        sections.append(build_graph_node_struct())
        sections.append(build_graph_helpers())
        sections.append(build_solution_body(problem))
        sections.append(build_graph_run_case(problem))
    elif kind == "bad_version":
        sections.append(build_bad_version_api())
        sections.append(build_solution_body(problem))
        sections.append(build_api_run_case(problem, "firstBadVersionForLocalTest", "bad"))
    elif kind == "guess_number":
        sections.append(build_guess_api())
        sections.append(build_solution_body(problem))
        sections.append(build_api_run_case(problem, "secretNumberForLocalTest", "secret"))
    elif kind.startswith("design_"):
        if kind == "design_bstiterator":
            sections.append(build_treenode_struct())
            sections.append(build_tree_helpers())
        sections.append(build_design_body_only(problem))
        sections.append(build_design_run_case(problem))
    else:
        sections.append(build_solution_body(problem))
        sections.append(build_solution_run_case(problem))

    return "\n".join(sections).strip() + "\n"


def main():
    PROBLEMS_DIR.mkdir(exist_ok=True)
    created = []
    skipped = []
    overwrite_existing = "--overwrite" in sys.argv[1:]

    for problem in ROUND1_PROBLEMS:
        pid = zero_pad(problem["id"])
        title = problem["title"]
        folder = PROBLEMS_DIR / pid
        folder.mkdir(exist_ok=True)

        md_path = folder / f"{pid}.md"
        cpp_path = folder / f"{pid}_{pascal_file_name(title)}.cpp"

        created_this_problem = False

        if overwrite_existing or not md_path.exists():
            md_path.write_text(build_md(problem), encoding="utf-8")
            created_this_problem = True

        if overwrite_existing or not cpp_path.exists():
            cpp_path.write_text(build_cpp(problem), encoding="utf-8")
            created_this_problem = True

        if created_this_problem:
            created.append(pid)
        else:
            skipped.append(pid)

    action = "Rebuilt or completed" if overwrite_existing else "Created or completed"
    print(f"{action} templates for {len(created)} Round 1 problems.")
    print(f"Skipped existing complete templates: {', '.join(skipped) if skipped else 'none'}")


if __name__ == "__main__":
    main()
