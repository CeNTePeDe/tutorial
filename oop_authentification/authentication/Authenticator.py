import AuthException as Ex
import user


class Authenticator:
    def __init__(self):
        """Construct an aythenticator to manage users logging in and out"""
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise Ex.UserNameAlredyExist(username)
        if len(password) < 6:
            raise Ex.PasswordTooShort(username)
        self.users[username] = user.User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise Ex.InvalidUsername(username)

        if not user.check_password(password):
            raise Ex.InvalidPassword(username, user)

        user.is_login_in = True
        return True
