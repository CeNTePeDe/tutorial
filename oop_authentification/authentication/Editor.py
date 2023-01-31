import AuthException

import Authenticator
import Authorizor as auth

# set up a test user and permission
#Authenticator.Authenticator.add_user('joe', 'hdjdyth')
#auth.Authorizor.add_permission("test program")
#auth.Authorizor.add_permission("change program")
#auth.Authorizor.permit_user("test program", "joe")
name1 = Authenticator.Authenticator()
print(name1.add_user('Olga', 'password123'))





class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "test": self.test,
            "change": self.change,
            "quit": self.quit,
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username:  ")
            password = input("password:  ")
            try:
                logged_in = Authenticator.Authenticator.login(username, password)
            except AuthException.InvalidUsername:
                print("Sorry, that username does not exist")
            except AuthException.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            auth.Authorizor.check_permission(permission, self.username)
        except AuthException.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except AuthException.NotPermissionError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True

    def test(self):
        if self.is_permitted("test program"):
            print("Testing program now...")

    def change(self):
        if self.is_permitted("change program"):
            print("Changing program now...")

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print("""
                Please enter a command:
                \tlogin\tLigin
                \ttest\tTest the program
                \tchange\tChange the program
                \tquit\tQuit"""
                      )
                answer = input("enter a comand: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing module")


Editor().menu()
