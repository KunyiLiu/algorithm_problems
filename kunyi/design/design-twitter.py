'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''

class MiniTwitter:
    
    def __init__(self):
        # do intialization if necessary
        self.follow_dict = {}
        self.time = 0 
        # {uid: [(time, message), ]
        self.message_dict = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        # write your code here
        if user_id not in self.message_dict:
            self.message_dict[user_id] = []
        if len(self.message_dict[user_id]) == 10:
            self.message_dict[user_id].pop(0)
            
        tweet = Tweet(user_id, tweet_text)
        self.message_dict[user_id].append((self.time, tweet))
        self.time += 1 
        return tweet

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        # write your code here
        to_user_ids = self.follow_dict.get(user_id, set())
        # |    &
        user_ids = to_user_ids | set([user_id])
        messages = []
        for user in user_ids:
            messages.extend(self.message_dict.get(user, []))
        print(user_ids, )
            
        messages = sorted(messages, key = lambda x: -x[0])
        return [_[1] for _ in messages[:10]]
        

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        # write your code here
        return [_[1] for _ in self.message_dict.get(user_id, [])][::-1]

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id not in self.follow_dict:
            self.follow_dict[from_user_id] = set()
            
        self.follow_dict[from_user_id].add(to_user_id)

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        if to_user_id in self.follow_dict.get(from_user_id, set()):
            self.follow_dict[from_user_id].remove(to_user_id)
