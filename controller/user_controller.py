from model.entity.user import User

user_list = []

class UserController:
        def save(self, name, family, age,birth_date,username):
            try:
                user = User(id,name, family, age,birth_date,username)
                user_list.append(user)
                return True, f"user Saved Successfully {user}"
            except Exception as e:
                return False, f"user Saved Failed\n{e}"

        def edit(self, name, family, age, username):
            try:
                user = User(id,name, family,birth_date,username)
                #     edit to database
                return True, f"user Edited Successfully {user}"
            except Exception as e:
                return False, f"user Edited Failed\n{e}"

        def delete(self, id):
            try:
                #     remove from database
                return True, f"user Removed Successfully - {id}"
            except Exception as e:
                return False, f"user Removed Failed\n{e}"

        def find_all(self):
            try:
                return True, user_list
            except Exception as e:
                return False, f"Can't Load user"
