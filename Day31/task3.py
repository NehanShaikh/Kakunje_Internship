# Followers of two influencers
influencer1_followers = {"Alice", "Bob", "Charlie", "David", "Eva"}
influencer2_followers = {"Charlie", "David", "Frank", "George", "Alice"}

mutual = influencer1_followers & influencer2_followers
print("Mutual followers:", mutual)

all_followers = influencer1_followers | influencer2_followers
print("All followers:", all_followers)

only_one = influencer1_followers ^ influencer2_followers
print("Followers who follow only one influencer:", only_one)
