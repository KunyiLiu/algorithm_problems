#####  min heap #

class Twitter:
    import heapq
    def __init__(self):
        # Space: #user * #tweets + #user * #user
        # increase monotonically
        self.orderId = 0
        # userId: hashset(), then remove O(1)
        self.followed_users = {}
        # userId: [(orderId, tweetId)]
        self.user_tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        self.user_tweets[userId].append((self.orderId, tweetId))
        self.orderId += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # fetch the last 10 tweets for the userId itself + followed users
        # input the (orderId, tweetId) to the minheap, and keep the minheap number to 10
        # then return result with order
        # Time complexity: O(F* 10 log 10), F - max followed users
        heap = []
        users = set([userId])
        users.update(self.followed_users.get(userId, set()))

        for user in users:
            tws = self.user_tweets.get(user, [])
            for tw in tws[-10:]:
                heapq.heappush(heap, tw)
                if len(heap) > 10:
                    heapq.heappop(heap)

        result = []
        while heap:
            # from the small orderId (least recent) -> recent
            result.append(heapq.heappop(heap)[1])

        return result[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followed_users:
            self.followed_users[followerId] = set([])

        self.followed_users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followed_users:
            # unlike remove, discard does not raise error
            self.followed_users[followerId].discard(followeeId)
        

####    max heap #####

import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.followed = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        users = self.followed[userId] | {userId}

        heap = []

        # push latest tweet of each user
        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                time, tweetId = self.tweets[u][idx]

                heapq.heappush(heap, (-time, tweetId, u, idx - 1))

        res = []

        while heap and len(res) < 10:
            time, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)

            # push next tweet from the same user
            if idx >= 0:
                time, tweetId = self.tweets[user][idx]
                heapq.heappush(heap, (-time, tweetId, user, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].discard(followeeId)
