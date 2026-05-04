class Twitter:
    #data structures:
    # self.tweets = {userId: [(time, tweetId), ...]}
    # self.following = {userId: set(followeeIds)} 
    # self.time = 0

    def __init__(self):
        self.tweet=defaultdict(list)
        self.following=defaultdict(set)
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweet[userId].append([self.time, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        res=[]
        self.following[userId].add(userId)
        follows=self.following[userId]
        for follower in follows:
            if follower in self.tweet and self.tweet[follower]:
                latest_time, latest_tweet_id=self.tweet[follower][-1]
                idx=len(self.tweet[follower])-1
                heapq.heappush(heap, (-latest_time, follower, latest_tweet_id, idx))
        while heap and len(res)<10:
           time, follower, latest_tweet_id, idx = heapq.heappop(heap)
           res.append(latest_tweet_id) 
           if idx>0:
            time, tweet_id=self.tweet[follower][idx-1]
            heapq.heappush(heap, (-time, follower, tweet_id, idx-1))
        return res                  


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.following[followerId].discard(followeeId)

        
