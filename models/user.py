from datetime import date

class User():
  def __init__(self, id, first_name, last_name, email, bio, username, password, profile_image_url):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.bio = bio 
    self.username = username
    self.password = password
    self.profile_image_url = profile_image_url
    self.created_on = date
    self.active = True