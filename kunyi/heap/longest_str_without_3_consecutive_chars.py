"""
priority queue + greedy
result + char (max freq) when no 3 consecutive
if meet 3 consecutive, record char and count, so that we can pop out the second
most frequent char in the next step of the loop
and push back the prev_char, prev_count to heap
"""
# Time Complexity is O(nlogk), Space O(n)


def ls3(A, B, C):
    import heapq
    heap = [(-A, 'a'), (-B, 'b'), (-C, 'c')]
    heapq.heapify(heap)
    prev_char, prev_count = '', 0
    result = []
    while len(heap) > 0:
        count, char = heapq.heappop(heap)
        if prev_char and prev_count:
            heapq.heappush(heap, (prev_count, prev_char))
            prev_char, prev_count = '', 0
        if len(result) > 1 and result[-2] == char and result[-1] == char:
            prev_char, prev_count = char, count
        else:
            result.append(char)
            if count != -1:
                heapq.heappush(heap, (count+1, char))

    return ''.join(result)


if __name__ == '__main__':
    print(ls3(1, 1, 6))
    print(ls3(1, 2, 3))
