from collections import deque
def get_parallel_courseIII(n, relations, k):
    # the state node would be a set of course in the same semester (<= k),
    # so use bitmask bfs, bitmask represents the tkaken course.
    # 11 -> means ourse 1, 2 done.
    # transition: (mask, step) -> up to the semester, i have taken (mask) course and those prerequites.
    # Choose next k of them to take (available + prerequites meet)

    prereq = [0] * n
    for u, v in relations:
        u -= 1
        v -= 1
        prereq[v] |= (1 << u)

    q = deque([(0, 0)])
    # state has visited
    visited = set([0])

    while q:
        mask, step = q.popleft()

        if mask == (1 << n) - 1:
            return step

        # find available course
        available = 0
        for i in range(n):
            if not ((1 << i) & mask) and (prereq[i] & mask) == prereq[i]:
                available |= (1 << i)

        next_masks = []
        # 1101, 1011..
        if bin(available).count("1") <= k:
            # take available course 
            next_masks.append(mask | available)
        else:
            subset = available
            while subset:
                if bin(available).count("1") == k:
                    next_masks.append(subset | available)
                # create subset of count = k from n
                subset = (subset - 1) & available

        for new_mask in next_masks:
            if new_mask not in visited:
                visited.add(new_mask)
                q.append((new_mask, step + 1))
