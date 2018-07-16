from datetime import datetime


class Post(object):
    # specify user=None so you can pass one to self in if needed
    def __init__(self, text, timestamp=None, user=None):
        self.text = text
        self.timestamp = timestamp
        self.user = user

    def set_user(self, user):
        self.user = user


class TextPost(Post): 
    def __init__(self, text, timestamp=None, user=None):
        super(TextPost, self).__init__(text, timestamp, user)

    def __str__(self):
        return '@{first_name} {last_name}: "{post}"\n\t{time}'.format(first_name=self.user.first_name,
        last_name=self.user.last_name, post=self.text, time=datetime.strftime(self.timestamp, '%A, %b %d, %Y'))


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None, user=None):
        super(PicturePost, self).__init__(text, timestamp, user)
        self.image_url = image_url

    def __str__(self):
        return '@{first_name} {last_name}: "{post}"\n\t{image_url}\n\t{time}'.format(first_name=self.user.first_name, 
        last_name=self.user.last_name, post=self.text, image_url=self.image_url, time=datetime.strftime(self.timestamp, '%A, %b %d, %Y'))


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None, user=None):
        super(CheckInPost, self).__init__(text, timestamp, user)
        self.latitude = latitude
        self.longitude = longitude
        self.user = user

    def __str__(self):
        return '@{first_name} Checked In: "{post}"\n\t{latitude}, {longitude}\n\t{time}'.format(first_name=self.user.first_name, 
        post=self.text, latitude=self.latitude, longitude=self.longitude, time=datetime.strftime(self.timestamp, '%A, %b %d, %Y'))

