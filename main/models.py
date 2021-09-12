from django.db import models
import re

# class ProfileManager(models.Manager):
#     def email_validator(request, postData):
#         errors = {}
#         regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#         if not (re.search(regex, postData['email'])):
#             errors['email'] = "Invalid email"
#         user = Profile.objects.filter(email=postData['email'])
#         if user:
#             errors['email'] = "Email already in use"
#         else:
#             print('this is a new user')

class Profile(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    registered_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=255)