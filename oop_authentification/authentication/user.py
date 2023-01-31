import hashlib


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = self._encrupt_pw(password)
        self.is_login_in = False

    def _encrupt_pw(self, password):
        """Encrypt the password with the username and return
        the sha digest."""
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Return True if the password is valid for this user, False otherwise"""
        encrypted = self._encrupt_pw(password)
        return encrypted == self.password
