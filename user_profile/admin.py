from django.contrib import admin

# Register your models here.
from .models import User, Education, Reference, Experience, Certification, Award, Skillset, Profile

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Reference)
admin.site.register(Experience)
admin.site.register(Certification)
admin.site.register(Award)
admin.site.register(Skillset)

