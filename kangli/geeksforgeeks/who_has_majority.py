'''
We hope you are familiar with using counter variables. Counting allows us to find how may times a certain element appears in an array or list.

You are given an array arr of size n. You are also given two elements x and y. Now, you need to tell which element (x or y) appears most in the array. In other words, print the element, x or y, that has highest frequency in the array. If both elements have the same frequency, then just print the smaller element.

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains 3 lines of input. The first line contains size of array denoted by n. The second line contains the elements of the array separated by spaces. The third line contains two integers x and y separated by a space.

Output Format:
For each testcase, in a newline, print the element with highest occurrence in the array. If occurrences are same, then print the smaller element.

Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function majorityWins() that takes array, n, x, y as parameters.

Constraints:
1 <= T <= 100
1 <= n <= 103
0 <= arri , x , y <= 108

Examples:
Input:
2
11
1 1 2 2 3 3 4 4 4 4 5
4 5
8
1 2 3 4 5 6 7 8
1 7
Output:
4
1

Explanation:
Testcase 1: n=11; elements = {1,1,2,2,3,3,4,4,4,4,5}; x=4; y=5
x frequency in arr is = 4 times
y frequency in arr is = 1 times
x has higher frequency, so we print 4
Testcase 2: n=8; elements = {1,2,3,4,5,6,7,8}; x=1; y=7
x frequency in arr is 1 times
y frequency in arr is 1 times
both have same frequency, so we look for the smaller element.
x=1 is smaller than y=7, so print 1

** For More Input/Output Examples Use 'Expected Output' option **
Author: Soul_xhacker
'''
def main():
    T = int(input())
    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]

        x, y = map(int, input().strip().split())

        majorityWins(arr, n, x, y)
        T -= 1

if __name__ == "__main__":
    main()


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# User function Template for python3
# Initial Template for Python 3
# Complete this function


def majorityWins(arr, n, x, y):
    x_count, y_count = 0, 0
    for elt in arr:
        if elt == x:
            x_count += 1
        elif elt == y:
            y_count += 1
    if x_count == y_count:
        print(x) if x < y else print(y)
        return
    print(x) if x_count > y_count else print(y)

