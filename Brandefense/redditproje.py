import praw

reddit = praw.Reddit(client_id="F1CCUMZkit985NAOrj0PHg",
                     client_secret="v66UaKpyY0qGQK3TtwaxmjPRIh6czw",
                     user_agent="script by u/kelebekbarbie",
                     redirect_uri="http://localhost:8080")

# Örnek olarak r/science subreddit'ini alalım
subreddit = reddit.subreddit("science")

# Subreddit'teki en yeni 10 postu alalım
for post in subreddit.new(limit=10):
    print(post.title)
    print(post.url)
    print(post.score)
    print(post.num_comments)
    print("----------")