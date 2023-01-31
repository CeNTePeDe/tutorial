import AuthException as Ex
import Authenticator

aythenticator = Authenticator.Authenticator()


class Authorizor:

    def __init__(self, aythenticator):
        self.aythenticator = aythenticator
        self.permission = {}

    def add_permission(self, perm_name):
        """Create a new permission that users can be added"""
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            self.permission[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """Grant the given permission to the user"""
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError("Permission doesn't exist")
        else:
            if username not in self.aythenticator.users:
                raise Ex.InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.aythenticator.is_logged_in(username):
            raise Ex.NotLoggedInError(username)
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise Ex.PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise Ex.NotPermissionError(username)
            else:
                return True


authorizor = Authorizor(aythenticator)
authorizor.add_permission("paint")
#authorizor.check_permission("paint", 'olga')
