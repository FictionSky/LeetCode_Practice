def ex(input_text, output_text, explanation):
    return {"input": input_text, "output": output_text, "explanation": explanation}


def d(summary, examples, constraints, local_cases, approach=None, mutates=None):
    data = {
        "summary": summary,
        "examples": examples,
        "constraints": constraints,
        "approach": approach or [],
        "local_cases": local_cases,
    }
    if mutates:
        data["mutates"] = mutates
    return data


CATEGORY_APPROACH = {
    "array_greedy": ["先明确一次扫描中要维护的状态。", "尽量把额外空间压到常数级。"],
    "backtracking": ["先定义递归层含义，再枚举当前位置的选择。", "进入下一层前做选择，返回时撤销选择。"],
    "binary_search": ["先判断是在数组中二分，还是在答案空间中二分。", "写代码前确定左右边界和循环不变量。"],
    "binary_tree": ["先定义递归函数对一个子树返回什么。", "需要全局答案时，区分返回值和答案更新。"],
    "bit_manipulation": ["用小二进制样例观察位变化规律。", "优先利用异或、移位、掩码等位运算性质。"],
    "design": ["先列出每个操作的目标复杂度。", "再选择能同时支持查询和更新的数据结构组合。"],
    "dynamic_programming": ["先写清楚状态定义。", "再确定初始化、转移顺序和答案位置。"],
    "graph": ["先把输入关系建成邻接表或状态图。", "根据是否有方向、入度或层次选择 DFS/BFS/拓扑。"],
    "graph_grid": ["把每个格子看作节点。", "注意边界、访问标记和多源 BFS 的初始队列。"],
    "graph_weighted": ["先定义点、边和路径代价。", "根据边权特征选择 Dijkstra、Bellman-Ford 或二分 + BFS。"],
    "greedy": ["先写出局部最优选择。", "再确认这个选择不会破坏后续最优解。"],
    "heap_priority": ["先定义堆顶代表什么。", "再决定哪些元素入堆、何时出堆或失效。"],
    "linked_list": ["先画出指针变化过程。", "改 next 指针前保存后续节点，必要时使用 dummy。"],
    "math": ["先列几个小例子找规律。", "把数值转换和边界处理拆开写。"],
    "matrix": ["先明确行列遍历顺序。", "如果原地修改，注意旧状态是否还会被使用。"],
    "monotonic_queue": ["先定义单调结构维护递增还是递减。", "每个元素最多入队出队一次。"],
    "sliding_window": ["先定义窗口内维护的含义。", "窗口不满足条件时移动左边界并同步状态。"],
    "stack_queue": ["先判断需要普通栈、队列，还是单调栈。", "遇到匹配、消除或最近更大元素时优先考虑栈。"],
    "string_array": ["先拆出字符、单词或下标的处理规则。", "注意空串、空格和边界位置。"],
    "trie": ["先定义 Trie 节点保存的孩子和终止标记。", "搜索时按字符逐层转移，必要时 DFS 处理通配符。"],
    "two_pointers": ["先确定两个指针分别代表什么。", "根据当前和、区间或比较结果移动一侧指针。"],
    "union_find": ["先判断问题是否在维护连通块。", "用路径压缩和合并操作维护集合关系。"],
}


LOCAL_CASES = {
    2: [{"label": "示例 1", "lists": [[2, 4, 3], [5, 6, 4]], "expected": [7, 0, 8]}],
    4: [{"label": "示例 1", "args": [[1, 3], [2]], "expected": 2.0}],
    5: [{"label": "示例 1", "args": ["babad"], "expected": "bab"}],
    10: [{"label": "示例 1", "args": ["aa", "a"], "expected": False}],
    12: [{"label": "示例 1", "args": [3749], "expected": "MMMDCCXLIX"}],
    13: [{"label": "示例 1", "args": ["MCMXCIV"], "expected": 1994}],
    14: [{"label": "示例 1", "args": [["flower", "flow", "flight"]], "expected": "fl"}],
    16: [{"label": "示例 1", "args": [[-1, 2, 1, -4], 1], "expected": 2}],
    17: [{"label": "示例 1", "args": ["23"], "expected": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]}],
    18: [{"label": "示例 1", "args": [[1, 0, -1, 0, -2, 2], 0], "expected": [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]}],
    22: [{"label": "示例 1", "args": [3], "expected": ["((()))", "(()())", "(())()", "()(())", "()()()"]}],
    23: [{"label": "示例 1", "lists": [[1, 4, 5], [1, 3, 4], [2, 6]], "expected": [1, 1, 2, 3, 4, 4, 5, 6]}],
    24: [{"label": "示例 1", "lists": [[1, 2, 3, 4]], "expected": [2, 1, 4, 3]}],
    25: [{"label": "示例 1", "lists": [[1, 2, 3, 4, 5]], "args": [2], "expected": [2, 1, 4, 3, 5]}],
    28: [{"label": "示例 1", "args": ["sadbutsad", "sad"], "expected": 0}],
    30: [{"label": "示例 1", "args": ["barfoothefoobarman", ["foo", "bar"]], "expected": [0, 9]}],
    31: [{"label": "示例 1", "args": [[1, 2, 3]], "expected": [1, 3, 2]}],
    34: [{"label": "示例 1", "args": [[5, 7, 7, 8, 8, 10], 8], "expected": [3, 4]}],
    36: [{"label": "示例 1", "args": [[["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]], "expected": True}],
    39: [{"label": "示例 1", "args": [[2, 3, 6, 7], 7], "expected": [[2, 2, 3], [7]]}],
    40: [{"label": "示例 1", "args": [[10, 1, 2, 7, 6, 1, 5], 8], "expected": [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]}],
    41: [{"label": "示例 1", "args": [[1, 2, 0]], "expected": 3}],
    42: [{"label": "示例 1", "args": [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], "expected": 6}],
    44: [{"label": "示例 1", "args": ["aa", "a"], "expected": False}],
    45: [{"label": "示例 1", "args": [[2, 3, 1, 1, 4]], "expected": 2}],
    46: [{"label": "示例 1", "args": [[1, 2, 3]], "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]}],
    50: [{"label": "示例 1", "args": [2.0, 10], "expected": 1024.0}],
    51: [{"label": "示例 1", "args": [4], "expected": [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]}],
    52: [{"label": "示例 1", "args": [4], "expected": 2}],
    58: [{"label": "示例 1", "args": ["Hello World"], "expected": 5}],
    61: [{"label": "示例 1", "lists": [[1, 2, 3, 4, 5]], "args": [2], "expected": [4, 5, 1, 2, 3]}],
    68: [{"label": "示例 1", "args": [["This", "is", "an", "example", "of", "text", "justification."], 16], "expected": ["This    is    an", "example  of text", "justification.  "]}],
    71: [{"label": "示例 1", "args": ["/home//foo/"], "expected": "/home/foo"}],
    72: [{"label": "示例 1", "args": ["horse", "ros"], "expected": 3}],
    74: [{"label": "示例 1", "args": [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3], "expected": True}],
    76: [{"label": "示例 1", "args": ["ADOBECODEBANC", "ABC"], "expected": "BANC"}],
    78: [{"label": "示例 1", "args": [[1, 2, 3]], "expected": [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]}],
    79: [{"label": "示例 1", "args": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"], "expected": True}],
    81: [{"label": "示例 1", "args": [[2, 5, 6, 0, 0, 1, 2], 0], "expected": True}],
    82: [{"label": "示例 1", "lists": [[1, 2, 3, 3, 4, 4, 5]], "expected": [1, 2, 5]}],
    84: [{"label": "示例 1", "args": [[2, 1, 5, 6, 2, 3]], "expected": 10}],
    85: [{"label": "示例 1", "args": [[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]], "expected": 6}],
    86: [{"label": "示例 1", "lists": [[1, 4, 3, 2, 5, 2]], "args": [3], "expected": [1, 2, 2, 4, 3, 5]}],
    90: [{"label": "示例 1", "args": [[1, 2, 2]], "expected": [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]}],
    91: [{"label": "示例 1", "args": ["226"], "expected": 3}],
    92: [{"label": "示例 1", "lists": [[1, 2, 3, 4, 5]], "args": [2, 4], "expected": [1, 4, 3, 2, 5]}],
    97: [{"label": "示例 1", "args": ["aabcc", "dbbca", "aadbbcbcac"], "expected": True}],
    98: [{"label": "示例 1", "tree": ["2", "1", "3"], "expected": True}],
    103: [{"label": "示例 1", "tree": ["3", "9", "20", "null", "null", "15", "7"], "expected": [[3], [20, 9], [15, 7]]}],
    105: [{"label": "示例 1", "args": [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]], "expected": ["3", "9", "20", "null", "null", "15", "7"]}],
    106: [{"label": "示例 1", "args": [[9, 3, 15, 20, 7], [9, 15, 7, 20, 3]], "expected": ["3", "9", "20", "null", "null", "15", "7"]}],
    114: [{"label": "示例 1", "tree": ["1", "2", "5", "3", "4", "null", "6"], "expected": [1, 2, 3, 4, 5, 6]}],
    115: [{"label": "示例 1", "args": ["rabbbit", "rabbit"], "expected": 3}],
    116: [{"label": "示例 1", "tree": ["1", "2", "3", "4", "5", "6", "7"], "expected": [[1], [2, 3], [4, 5, 6, 7]]}],
    117: [{"label": "示例 1", "tree": ["1", "2", "3", "4", "5", "null", "7"], "expected": [[1], [2, 3], [4, 5, 7]]}],
    120: [{"label": "示例 1", "args": [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]], "expected": 11}],
    123: [{"label": "示例 1", "args": [[3, 3, 5, 0, 0, 3, 1, 4]], "expected": 6}],
    124: [{"label": "示例 1", "tree": ["-10", "9", "20", "null", "null", "15", "7"], "expected": 42}],
    126: [{"label": "示例 1", "args": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], "expected": [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]}],
    127: [{"label": "示例 1", "args": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], "expected": 5}],
    131: [{"label": "示例 1", "args": ["aab"], "expected": [["a", "a", "b"], ["aa", "b"]]}],
    134: [{"label": "示例 1", "args": [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]], "expected": 3}],
    135: [{"label": "示例 1", "args": [[1, 0, 2]], "expected": 5}],
    137: [{"label": "示例 1", "args": [[2, 2, 3, 2]], "expected": 3}],
    138: [{"label": "示例 1", "nodes": [[7, -1], [13, 0], [11, 4], [10, 2], [1, 0]], "expected": [[7, -1], [13, 0], [11, 4], [10, 2], [1, 0]]}],
    139: [{"label": "示例 1", "args": ["leetcode", ["leet", "code"]], "expected": True}],
    140: [{"label": "示例 1", "args": ["catsanddog", ["cat", "cats", "and", "sand", "dog"]], "expected": ["cats and dog", "cat sand dog"]}],
    143: [{"label": "示例 1", "lists": [[1, 2, 3, 4]], "expected": [1, 4, 2, 3]}],
    146: [{"label": "示例 1", "operations": ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"], "inputs": [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]], "expected": ["null", "null", "null", "1", "null", "-1", "null", "-1", "3", "4"]}],
    151: [{"label": "示例 1", "args": ["  hello world  "], "expected": "world hello"}],
    162: [{"label": "示例 1", "args": [[1, 2, 3, 1]], "expected": 2}],
    169: [{"label": "示例 1", "args": [[3, 2, 3]], "expected": 3}],
    173: [{"label": "示例 1", "operations": ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"], "inputs": [[["7", "3", "15", "null", "null", "9", "20"]], [], [], [], [], [], [], [], [], []], "expected": ["null", "3", "7", "true", "9", "true", "15", "true", "20", "false"]}],
    188: [{"label": "示例 1", "args": [2, [2, 4, 1]], "expected": 2}],
    189: [{"label": "示例 1", "args": [[1, 2, 3, 4, 5, 6, 7], 3], "expected": [5, 6, 7, 1, 2, 3, 4]}],
    190: [{"label": "示例 1", "args": [43261596], "expected": 964176192}],
    191: [{"label": "示例 1", "args": [11], "expected": 3}],
    199: [{"label": "示例 1", "tree": ["1", "2", "3", "null", "5", "null", "4"], "expected": [1, 3, 4]}],
    201: [{"label": "示例 1", "args": [5, 7], "expected": 4}],
    208: [{"label": "示例 1", "operations": ["Trie", "insert", "search", "search", "startsWith", "insert", "search"], "inputs": [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]], "expected": ["null", "null", "true", "false", "true", "null", "true"]}],
    210: [{"label": "示例 1", "args": [2, [[1, 0]]], "expected": [0, 1]}],
    211: [{"label": "示例 1", "operations": ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"], "inputs": [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]], "expected": ["null", "null", "null", "null", "false", "true", "true", "true"]}],
    212: [{"label": "示例 1", "args": [[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"]], "expected": ["oath", "eat"]}],
    213: [{"label": "示例 1", "args": [[2, 3, 2]], "expected": 3}],
    215: [{"label": "示例 1", "args": [[3, 2, 1, 5, 6, 4], 2], "expected": 5}],
    221: [{"label": "示例 1", "args": [[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]], "expected": 4}],
    222: [{"label": "示例 1", "tree": ["1", "2", "3", "4", "5", "6"], "expected": 6}],
    224: [{"label": "示例 1", "args": ["1 + 1"], "expected": 2}],
    227: [{"label": "示例 1", "args": ["3+2*2"], "expected": 7}],
    230: [{"label": "示例 1", "tree": ["3", "1", "4", "null", "2"], "args": [1], "expected": 1}],
    235: [{"label": "示例 1", "tree": ["6", "2", "8", "0", "4", "7", "9", "null", "null", "3", "5"], "node_values": [2, 8], "expected": 6}],
    236: [{"label": "示例 1", "tree": ["3", "5", "1", "6", "2", "0", "8", "null", "null", "7", "4"], "node_values": [5, 1], "expected": 3}],
    239: [{"label": "示例 1", "args": [[1, 3, -1, -3, 5, 3, 6, 7], 3], "expected": [3, 3, 5, 5, 6, 7]}],
    260: [{"label": "示例 1", "args": [[1, 2, 1, 3, 2, 5]], "expected": [3, 5]}],
    279: [{"label": "示例 1", "args": [12], "expected": 3}],
    287: [{"label": "示例 1", "args": [[1, 3, 4, 2, 2]], "expected": 2}],
    295: [{"label": "示例 1", "operations": ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"], "inputs": [[], [1], [2], [], [3], []], "expected": ["null", "null", "null", "1.500000", "null", "2.000000"]}],
    297: [{"label": "示例 1", "tree": ["1", "2", "3", "null", "null", "4", "5"], "expected": ["1", "2", "3", "null", "null", "4", "5"]}],
    309: [{"label": "示例 1", "args": [[1, 2, 3, 0, 2]], "expected": 3}],
    312: [{"label": "示例 1", "args": [[3, 1, 5, 8]], "expected": 167}],
    316: [{"label": "示例 1", "args": ["bcabc"], "expected": "abc"}],
    332: [{"label": "示例 1", "args": [[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]], "expected": ["JFK", "MUC", "LHR", "SFO", "SJC"]}],
    338: [{"label": "示例 1", "args": [5], "expected": [0, 1, 1, 2, 1, 2]}],
    368: [{"label": "示例 1", "args": [[1, 2, 3]], "expected": [1, 2]}],
    373: [{"label": "示例 1", "args": [[1, 7, 11], [2, 4, 6], 3], "expected": [[1, 2], [1, 4], [1, 6]]}],
    377: [{"label": "示例 1", "args": [[1, 2, 3], 4], "expected": 7}],
    378: [{"label": "示例 1", "args": [[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8], "expected": 13}],
    380: [{"label": "示例 1", "operations": ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"], "inputs": [[], [1], [2], [2], [], [1], [2], []], "expected": ["null", "true", "false", "true", "2", "true", "false", "2"]}],
    392: [{"label": "示例 1", "args": ["abc", "ahbgdc"], "expected": True}],
    394: [{"label": "示例 1", "args": ["3[a]2[bc]"], "expected": "aaabcbc"}],
    399: [{"label": "示例 1", "args": [[["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"]]], "expected": [6.0, 0.5, -1.0]}],
    402: [{"label": "示例 1", "args": ["1432219", 3], "expected": "1219"}],
    406: [{"label": "示例 1", "args": [[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]], "expected": [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]}],
    410: [{"label": "示例 1", "args": [[7, 2, 5, 10, 8], 2], "expected": 18}],
    416: [{"label": "示例 1", "args": [[1, 5, 11, 5]], "expected": True}],
    417: [{"label": "示例 1", "args": [[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]], "expected": [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]}],
    432: [{"label": "示例 1", "operations": ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"], "inputs": [[], ["hello"], ["hello"], [], [], ["leet"], [], []], "expected": ["null", "null", "null", "hello", "hello", "null", "hello", "leet"]}],
    437: [{"label": "示例 1", "tree": ["10", "5", "-3", "3", "2", "null", "11", "3", "-2", "null", "1"], "args": [8], "expected": 3}],
    456: [{"label": "示例 1", "args": [[1, 2, 3, 4]], "expected": False}],
    460: [{"label": "示例 1", "operations": ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"], "inputs": [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]], "expected": ["null", "null", "null", "1", "null", "-1", "3", "null", "-1", "3", "4"]}],
    474: [{"label": "示例 1", "args": [["10", "0001", "111001", "1", "0"], 5, 3], "expected": 4}],
    480: [{"label": "示例 1", "args": [[1, 3, -1, -3, 5, 3, 6, 7], 3], "expected": [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]}],
    494: [{"label": "示例 1", "args": [[1, 1, 1, 1, 1], 3], "expected": 5}],
    502: [{"label": "示例 1", "args": [2, 0, [1, 2, 3], [0, 1, 1]], "expected": 4}],
    503: [{"label": "示例 1", "args": [[1, 2, 1]], "expected": [2, -1, 2]}],
    518: [{"label": "示例 1", "args": [5, [1, 2, 5]], "expected": 4}],
    540: [{"label": "示例 1", "args": [[1, 1, 2, 3, 3, 4, 4, 8, 8]], "expected": 2}],
    547: [{"label": "示例 1", "args": [[[1, 1, 0], [1, 1, 0], [0, 0, 1]]], "expected": 2}],
    572: [{"label": "示例 1", "trees": [["3", "4", "5", "1", "2"], ["4", "1", "2"]], "expected": True}],
    621: [{"label": "示例 1", "args": [["A", "A", "A", "B", "B", "B"], 2], "expected": 8}],
    632: [{"label": "示例 1", "args": [[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]], "expected": [20, 24]}],
    639: [{"label": "示例 1", "args": ["*"], "expected": 9}],
    646: [{"label": "示例 1", "args": [[[1, 2], [2, 3], [3, 4]]], "expected": 2}],
    647: [{"label": "示例 1", "args": ["aaa"], "expected": 6}],
    648: [{"label": "示例 1", "args": [["cat", "bat", "rat"], "the cattle was rattled by the battery"], "expected": "the cat was rat by the bat"}],
    658: [{"label": "示例 1", "args": [[1, 2, 3, 4, 5], 4, 3], "expected": [1, 2, 3, 4]}],
    659: [{"label": "示例 1", "args": [[1, 2, 3, 3, 4, 5]], "expected": True}],
    673: [{"label": "示例 1", "args": [[1, 3, 5, 4, 7]], "expected": 2}],
    677: [{"label": "示例 1", "operations": ["MapSum", "insert", "sum", "insert", "sum"], "inputs": [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]], "expected": ["null", "null", "3", "null", "5"]}],
    684: [{"label": "示例 1", "args": [[[1, 2], [1, 3], [2, 3]]], "expected": [2, 3]}],
    692: [{"label": "示例 1", "args": [["i", "love", "leetcode", "i", "love", "coding"], 2], "expected": ["i", "love"]}],
    703: [{"label": "示例 1", "operations": ["KthLargest", "add", "add", "add", "add", "add"], "inputs": [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]], "expected": ["null", "4", "5", "5", "8", "8"]}],
    714: [{"label": "示例 1", "args": [[1, 3, 2, 8, 4, 9], 2], "expected": 8}],
    735: [{"label": "示例 1", "args": [[5, 10, -5]], "expected": [5, 10]}],
    740: [{"label": "示例 1", "args": [[3, 4, 2]], "expected": 6}],
    743: [{"label": "示例 1", "args": [[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2], "expected": 2}],
    752: [{"label": "示例 1", "args": [["0201", "0101", "0102", "1212", "2002"], "0202"], "expected": 6}],
    763: [{"label": "示例 1", "args": ["ababcbacadefegdehijhklij"], "expected": [9, 7, 8]}],
    778: [{"label": "示例 1", "args": [[[0, 2], [1, 3]]], "expected": 3}],
    786: [{"label": "示例 1", "args": [[1, 2, 3, 5], 3], "expected": [2, 5]}],
    787: [{"label": "示例 1", "args": [4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1], "expected": 700}],
    790: [{"label": "示例 1", "args": [3], "expected": 5}],
    802: [{"label": "示例 1", "args": [[[1, 2], [2, 3], [5], [0], [5], [], []]], "expected": [2, 4, 5, 6]}],
    820: [{"label": "示例 1", "args": [["time", "me", "bell"]], "expected": 10}],
    841: [{"label": "示例 1", "args": [[[1], [2], [3], []]], "expected": True}],
    857: [{"label": "示例 1", "args": [[10, 20, 5], [70, 50, 30], 2], "expected": 105.0}],
    862: [{"label": "示例 1", "args": [[1], 1], "expected": 1}],
    871: [{"label": "示例 1", "args": [100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]], "expected": 2}],
    875: [{"label": "示例 1", "args": [[3, 6, 7, 11], 8], "expected": 4}],
    886: [{"label": "示例 1", "args": [4, [[1, 2], [1, 3], [2, 4]]], "expected": True}],
    901: [{"label": "示例 1", "operations": ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"], "inputs": [[], [100], [80], [60], [70], [60], [75], [85]], "expected": ["null", "1", "1", "1", "2", "1", "4", "6"]}],
    904: [{"label": "示例 1", "args": [[1, 2, 1]], "expected": 3}],
    907: [{"label": "示例 1", "args": [[3, 1, 2, 4]], "expected": 17}],
    918: [{"label": "示例 1", "args": [[1, -2, 3, -2]], "expected": 3}],
    931: [{"label": "示例 1", "args": [[[2, 1, 3], [6, 5, 4], [7, 8, 9]]], "expected": 13}],
    934: [{"label": "示例 1", "args": [[[0, 1], [1, 0]]], "expected": 1}],
    973: [{"label": "示例 1", "args": [[[1, 3], [-2, 2]], 1], "expected": [[-2, 2]]}],
    987: [{"label": "示例 1", "tree": ["3", "9", "20", "null", "null", "15", "7"], "expected": [[9], [3, 15], [20], [7]]}],
    990: [{"label": "示例 1", "args": [["a==b", "b!=a"]], "expected": False}],
    1004: [{"label": "示例 1", "args": [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2], "expected": 6}],
    1011: [{"label": "示例 1", "args": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5], "expected": 15}],
    1026: [{"label": "示例 1", "tree": ["8", "3", "10", "1", "6", "null", "14", "null", "null", "4", "7", "13"], "expected": 7}],
    1035: [{"label": "示例 1", "args": [[1, 4, 2], [1, 2, 4]], "expected": 2}],
    1048: [{"label": "示例 1", "args": [["a", "b", "ba", "bca", "bda", "bdca"]], "expected": 4}],
    1091: [{"label": "示例 1", "args": [[[0, 1], [1, 0]]], "expected": 2}],
    1129: [{"label": "示例 1", "args": [3, [[0, 1], [1, 2]], []], "expected": [0, 1, -1]}],
    1143: [{"label": "示例 1", "args": ["abcde", "ace"], "expected": 3}],
    1155: [{"label": "示例 1", "args": [1, 6, 3], "expected": 1}],
    1162: [{"label": "示例 1", "args": [[[1, 0, 1], [0, 0, 0], [1, 0, 1]]], "expected": 2}],
    1202: [{"label": "示例 1", "args": ["dcab", [[0, 3], [1, 2]]], "expected": "bacd"}],
    1235: [{"label": "示例 1", "args": [[1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]], "expected": 120}],
    1293: [{"label": "示例 1", "args": [[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1], "expected": 6}],
    1319: [{"label": "示例 1", "args": [4, [[0, 1], [0, 2], [1, 2]]], "expected": 1}],
    1372: [{"label": "示例 1", "tree": ["1", "null", "1", "1", "1", "null", "null", "1", "1", "null", "1"], "expected": 3}],
    1425: [{"label": "示例 1", "args": [[10, 2, -10, 5, 20], 2], "expected": 37}],
    1438: [{"label": "示例 1", "args": [[8, 2, 4, 7], 4], "expected": 2}],
    1466: [{"label": "示例 1", "args": [6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]], "expected": 3}],
    1482: [{"label": "示例 1", "args": [[1, 10, 3, 10, 2], 3, 1], "expected": 3}],
    1493: [{"label": "示例 1", "args": [[1, 1, 0, 1]], "expected": 3}],
    1514: [{"label": "示例 1", "args": [3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2], "expected": 0.25}],
    1531: [{"label": "示例 1", "args": ["aaabcccd", 2], "expected": 4}],
    1539: [{"label": "示例 1", "args": [[2, 3, 4, 7, 11], 5], "expected": 9}],
    1631: [{"label": "示例 1", "args": [[[1, 2, 2], [3, 8, 2], [5, 3, 5]]], "expected": 2}],
    1658: [{"label": "示例 1", "args": [[1, 1, 4, 2, 3], 5], "expected": 2}],
    1673: [{"label": "示例 1", "args": [[3, 5, 2, 6], 2], "expected": [2, 6]}],
    1971: [{"label": "示例 1", "args": [3, [[0, 1], [1, 2], [2, 0]], 0, 2], "expected": True}],
    2092: [{"label": "示例 1", "args": [6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1], "expected": [0, 1, 2, 3, 5]}],
    2421: [{"label": "示例 1", "args": [[1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]]], "expected": 6}],
    2492: [{"label": "示例 1", "args": [4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]], "expected": 5}],
}


DESIGN_IDS = {380, 146, 173, 703, 295, 208, 211, 901, 677, 460, 432}


SUMMARY_OVERRIDES = {
    14: "给定一个字符串数组 `strs`，返回所有字符串共有的最长前缀；如果不存在公共前缀，返回空字符串。",
    2: "给定两个非空链表表示的非负整数，数字按逆序存储，每个节点存一位，返回两数相加后的逆序链表。",
    41: "给定一个未排序整数数组，找出没有出现的最小正整数，并要求尽量使用线性时间和常数额外空间。",
    146: "设计一个 LRU 缓存，支持 `get` 和 `put`，容量满时淘汰最久未使用的键。",
}


CONSTRAINT_OVERRIDES = {
    14: ["数组可能为空或只包含一个字符串。", "公共前缀必须从每个字符串的第一个字符开始。"],
    2: ["两个链表都按逆序存储数字。", "需要正确处理进位和链表长度不同的情况。"],
    41: ["目标时间复杂度是 O(n)。", "尽量只使用 O(1) 额外空间。"],
    146: ["`get` 和 `put` 都应接近 O(1)。", "更新已有键时也要刷新最近使用顺序。"],
}


def value_to_text(value):
    if isinstance(value, str):
        return f'"{value}"'
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    return str(value)


def default_value_for_type(type_name):
    clean_type = type_name.replace("const ", "").replace("&", "").strip()
    if clean_type in {"int", "uint32_t"}:
        return 0
    if clean_type == "double":
        return 0.0
    if clean_type == "bool":
        return True
    if clean_type == "string":
        return "a"
    if clean_type.startswith("vector<int>"):
        return [1, 2, 3]
    if clean_type.startswith("vector<double>"):
        return [1.0, 2.0]
    if clean_type.startswith("vector<string>"):
        return ["a", "b"]
    if clean_type.startswith("vector<vector<int>>"):
        return [[1, 2], [3, 4]]
    if clean_type.startswith("vector<vector<char>>"):
        return [["1"]]
    return 1


def param_name(param):
    return param.split()[-1].replace("&", "").replace("*", "")


def param_type(param):
    name = param.split()[-1]
    return param[: -len(name)].strip().replace("&", "").strip()


def default_local_case(problem):
    kind = problem["kind"]
    if kind == "listnode":
        case = {"label": "示例 1", "lists": [[1, 2, 3]], "expected": [1, 2, 3]}
        extra_args = [default_value_for_type(param_type(param)) for param in problem.get("params", []) if param_type(param) != "ListNode*"]
        if extra_args:
            case["args"] = extra_args
        return [case]
    if kind == "random_list_node":
        return [{"label": "示例 1", "nodes": [[1, -1]], "expected": [[1, -1]]}]
    if kind == "treenode":
        return [{"label": "示例 1", "tree": ["1", "2", "3"], "expected": default_value_for_type(problem.get("return_type", "int"))}]
    if kind == "nextnode_tree":
        return [{"label": "示例 1", "tree": ["1", "2", "3"], "expected": [[1], [2, 3]]}]
    if kind == "codec_tree":
        return [{"label": "示例 1", "tree": ["1", "2", "3"], "expected": ["1", "2", "3"]}]
    if kind.startswith("design_"):
        class_name = {
            "design_randomizedset": "RandomizedSet",
            "design_lrucache": "LRUCache",
            "design_bstiterator": "BSTIterator",
            "design_kthlargest": "KthLargest",
            "design_medianfinder": "MedianFinder",
            "design_trie": "Trie",
            "design_worddictionary": "WordDictionary",
            "design_stockspanner": "StockSpanner",
            "design_mapsum": "MapSum",
            "design_lfu_cache": "LFUCache",
            "design_allone": "AllOne",
        }[kind]
        return [{"label": "示例 1", "operations": [class_name], "inputs": [[]], "expected": ["null"]}]

    args = [default_value_for_type(param_type(param)) for param in problem.get("params", [])]
    expected = default_value_for_type(problem.get("return_type", "int"))
    return [{"label": "示例 1", "args": args, "expected": expected}]


def example_from_case(problem, case):
    if "operations" in case:
        input_text = f"operations = {case['operations']}, inputs = {case['inputs']}"
    elif "lists" in case:
        input_text = f"lists = {case['lists']}"
        if "args" in case:
            input_text += f", args = {case['args']}"
    elif "tree" in case:
        input_text = f"root = {case['tree']}"
        if "args" in case:
            input_text += f", args = {case['args']}"
    elif "trees" in case:
        input_text = f"trees = {case['trees']}"
    elif "nodes" in case:
        input_text = f"nodes = {case['nodes']}"
    else:
        names = [param_name(param) for param in problem.get("params", [])]
        input_text = ", ".join(f"{name} = {value_to_text(value)}" for name, value in zip(names, case.get("args", [])))
    return ex(input_text, value_to_text(case["expected"]), "本地样例用于验证你的实现是否符合题目核心规则。")


def default_summary(problem):
    params = ", ".join(f"`{param_name(param)}`" for param in problem.get("params", []))
    if problem["id"] in SUMMARY_OVERRIDES:
        return SUMMARY_OVERRIDES[problem["id"]]
    if problem["kind"].startswith("design_"):
        return f"设计 `{problem['title']}` 所要求的数据结构，并实现题目列出的公开操作。"
    return f"给定 {params}，完成 `{problem['title']}` 对应的 `{problem.get('method', 'solve')}` 逻辑，并返回题目要求的结果。"


def default_constraints(problem):
    if problem["id"] in CONSTRAINT_OVERRIDES:
        return CONSTRAINT_OVERRIDES[problem["id"]]
    params = [f"`{param_name(param)}` 必须按原题含义处理。" for param in problem.get("params", [])]
    if not params:
        params = ["所有操作都作用在同一个对象实例上。"]
    params.append("注意空输入、重复值、边界下标和结果顺序等边界情况。")
    return params


def default_approach(problem):
    approach = list(CATEGORY_APPROACH.get(problem["category"], ["先明确状态含义。", "再把状态更新写成可验证的步骤。"]))
    if problem["kind"].startswith("design_"):
        approach.append("用操作序列逐步验证内部状态是否随调用正确变化。")
    return approach


def apply_round23_practice_data(problem):
    enriched = dict(problem)
    local_cases = LOCAL_CASES.get(problem["id"], default_local_case(problem))
    enriched.update(
        d(
            default_summary(problem),
            [example_from_case(problem, local_cases[0])],
            default_constraints(problem),
            local_cases,
            default_approach(problem),
        )
    )

    if enriched.get("return_type") == "void" and enriched["kind"] == "solution":
        for param in enriched.get("params", []):
            if "&" in param:
                enriched["mutates"] = param_name(param)
                break

    return enriched
