#escape_by("jumping over")
#escape_by("running around")
#escape_by("going deeper")

#we cannot escape that way! The boulder is too big!
#We cannot escape that way! The boulder is moving too fast!
#That might work! Let's go deeper!

# The is function with single plan and name is 'plan'

def escape_by(plan):
    if (plan == "jumping over"):
        print("We canot escape that way, The boulder is too big")
    elif(plan =="running around"):
        print("We cannot escape that way, The boulder is moving too fast")
    elif(plan =="going deeper"):
        print("that might be a good idea, lets do it")
    else:
        print("not sure about the plan")

#call to the function

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
escape_by("lets listen")