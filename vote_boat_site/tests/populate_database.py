import os
from vote_boat.models import Poll,IdeaTag,Idea,User,Vote

def add_poll(title,admin_user_id,description=""):
    kws = dict(title=title,admin_user_id=admin_user_id,description=description)
    return Poll.objects.get_or_create(**kws)[0]

def add_idea_tag (tag):
    kws = dict(tag=tag)
    return IdeaTag.objects.get_or_create(**kws)[0]

def add_idea (poll_id,title,description=""):
    kws = dict(poll_id=poll_id,title=title,description=description)
    return Idea.objects.get_or_create(**kws)[0]

def add_user (username,first_name="",last_name="",email=None):
    kws = dict(username=username,first_name=first_name,last_name=last_name,email=email)
    for u in User.objects.all():
        if u.username == username:
            return u
    return User.objects.get_or_create(**kws)[0]

def add_vote (idea_id,user_id,vote_value):
    kws = dict(idea_id=idea_id,user_id=user_id,vote_value=vote_value)
    return Vote.objects.get_or_create(**kws)[0]

def populate():
    
    brian = add_user("brian")
    dylan = add_user("dylan")
    tim = add_user("tim")        
    dan = add_user("dan")            
    
    party_ideas = add_poll("party ideas",dylan)
    
    idea1 = add_idea(party_ideas,"kegger")
    add_vote(idea1,brian,1)
    add_vote(idea1,tim,0)
    add_vote(idea1,dan,0)        

    idea2 = add_idea(party_ideas,"dance party")
    add_vote(idea2,brian,1)
    add_vote(idea2,dylan,1)        

    idea3 = add_idea(party_ideas,"poker night")
    add_vote(idea1,brian,0)
    add_vote(idea1,tim,1)
    add_vote(idea1,dan,1)        
    add_vote(idea1,dylan,1)            

    idea4 = add_idea(party_ideas,"concert")            
    add_vote(idea1,brian,1)
    
    # Print out what we have added to the user.
    for p in Poll.objects.all():
        print(" -- {} -- ".format(p))
        for i in Idea.objects.all():
            print("  * {}".format(i))
            for v in Vote.objects.all():
                print("   - {}".format(v))
            
# Start execution here!
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "vote_boat_site.settings")
    populate()
