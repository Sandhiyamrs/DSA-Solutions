from collections import defaultdict, deque

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(deque)
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        feed = []
        users = self.following[userId] | {userId}
        for u in users:
            feed.extend(self.tweets[u])
        feed.sort(reverse=True)
        return [t[1] for t in feed[:10]]

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)
