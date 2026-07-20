"""Evaluate Division
Given equations in the form of a/b = k, where a and b are variables and k is a constant, evaluate queries of the form c/d and determine if they can be evaluated using the given equations.
You are given a list of equations of fractions along with their values and queries. Your task is to evaluate the queries based on the given equations and return the results. If a query cannot be evaluated, return -1.0 as its result.

Input Format:
First Line: Two integers nandq, separated by a space, where nis the number of equations andq is the number of queries.
Next n Lines: Each line contains two strings aandb representing an equation a/b.
Following Line: n floating-point numbers representing the values of the given n equations.
Next q Lines: Each line contains two strings candd representing a query c/d.
Output Format:
A list of floating-point numbers representing the answers to the given queries. If a query cannot be evaluated, its result is -1.0.
Examples:
Input:

2 5
a b
b c
2.0 3.0
a c
b a
a e
a a
x x
Output:

[6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given equations are a/b = 2.0 and b/c = 3.0.
For the query a/c, we can evaluate as a/b * b/c = 2.0 * 3.0 = 6.0.
For b/a, it's the inverse of a/b, so 1/2.0 = 0.5.
The query a/ecannot be evaluated since there's no information aboute, resulting in -1.0.
For a/a, any variable divided by itself is 1.0.
Since xis not in the equations,x/xalso cannot be evaluated, resulting in-1.0.
Constraints:
1 <= n <= 20
1 <= q <= 100
Equation forms: "a/b = k" where 1 <= |a|, |b| <= 5.
Each query is of the form "c/d" where 1 <= |c|, |d| <= 5."""


from collections import defaultdict
from typing import List

class Solution:
    def build_graph(self, equations, values):
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value
        return graph

    def dfs(self, graph, start, end, visited):
        if start not in graph or end not in graph:
            return -1.0

        if start == end:
            return 1.0

        visited.add(start)

        for neighbor, value in graph[start].items():
            if neighbor in visited:
                continue

            result = self.dfs(graph, neighbor, end, visited)
            if result != -1.0:
                return result * value

        return -1.0

    def calc_equation(self, equations, values, queries):
        graph = self.build_graph(equations, values)
        return [self.dfs(graph, a, b, set()) for a, b in queries]

# Example usage
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

solution = Solution()
output = solution.calc_equation(equations, values, queries)
print(output)  # Output: [6.0, 0.5, -1.0, 1.0, -1.0]


