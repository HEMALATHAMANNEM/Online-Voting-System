from django.contrib import admin
from .models import Voter,Candidate,Position,Votes
# Register your models here.


class VoterAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','email','phone','is_voted']

class CandidateAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','email','phone','bio','position','no_of_votes']

class PositionAdmin(admin.ModelAdmin):
    list_display=['name','no_of_seats']

class VotesAdmin(admin.ModelAdmin):
    list_display=['voter','position','candidate']
    #pass

admin.site.register(Voter,VoterAdmin)
admin.site.register(Candidate,CandidateAdmin)
admin.site.register(Position,PositionAdmin)
admin.site.register(Votes,VotesAdmin)
