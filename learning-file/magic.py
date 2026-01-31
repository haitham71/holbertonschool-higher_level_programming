class Skill:

    def __init__(self):
        
        self.skills = ["HTML", "Css", "JS"]
    
    def __str__(self):
        return f"this is my skills {self.skills}"


    def __len__(self):
        
        return  len(self.skills)



profile = Skill()
print(len(profile))
print(profile)

profile.skills.append ("php")
profile.skills.append ("mySQL")

print(len(profile))

# print(profile.__class__)




# my_string = "saad"
# print(type(my_string))
# print(str.upper(my_string))
# print(my_string.__class__)