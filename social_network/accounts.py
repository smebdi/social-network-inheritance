
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
        self.following = []
        self.posts = []
        self.timeline = []

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        sorted_timeline = []
        for user in self.following:
            for post in user.posts:
                sorted_timeline.append(post)
        
        return sorted(sorted_timeline, key=lambda post: post.timestamp)

    def follow(self, other):
        self.following.append(other)
