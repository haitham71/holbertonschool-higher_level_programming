
class Member:
   

    not_allowed_names = ["hell", "osama"]

    users_num = 0
    @classmethod
    def shoe_users(cls):
        print(f"we have {cls.users_num} users in our system")

    @staticmethod
    def say_hi():
        print("hi")

    def __init__(self, name, mid_name, las_name, gen):
        
        self.name = name

        self.mname = mid_name

        self.lname = las_name

        self.gen = gen

        Member.users_num += 1


    def full_name(self):

        if self.name in Member.not_allowed_names:
             raise ValueError("name not allowed")
        else:
            return f" {self.name} {self.mname} {self.lname}"

    def wlc(self):
        if self.gen == "male":
            return f"welcome Mr.{self.name}"
        else:
            return f"welcome Ms.{self.name}"


    def get_all(self):
            return f"{self.wlc()} your full name is:{self.full_name()}"


    def del_user(self):
         Member.users_num -= 1
         return f"User {self.name} deleted"
    
print(Member.users_num)

memb_one = Member("khaled", "saad", "soud", "male")
memb_tow = Member("haitham", "saad", "alshehri", "male")
memb_three = Member("anwar", "abudl", "qwq", "female")
memb_four = Member("hell", "osama", "qwq", "female")

print(Member.users_num)

print("#" * 40)

print(memb_four.del_user())

print("#" * 40)

print(Member.users_num)

Member.shoe_users()

print("#" * 40)

Member.say_hi()
# print(memb_one.get_all())
# print(memb_tow.get_all())
# print(memb_three.get_all())
# print(memb_four.get_all())