# Create a password manager.
#
# Write a class called PasswordManager
#
# Criteria:
# The class should have a list called old_passwords that holds all of the user’s past passwords.
# There should be a method called get_password that returns the current password and a method called set_password that sets the user’s password.
# Finally, create a method called is_correct that receives a string and returns a boolean True or False depending on whether the string is equal to the current password or not.
# Extra:
# The last item of the list old_passwords is the user’s current password.
# The set_password method should only change the password if the attempted password is different from all the user’s past passwords.
# Input example:
# No input is given
#
# Output example:
# No output is required

class PasswordManager:
    """
    A password manager
    """

    def __init__(self):
        """
        Instantiates a new password manager
        """
        self.old_passwords = list()

    def _is_unique(self, password):
        """
        Whether the given password has been used before
        :param password:
        :return:
        """
        return not any(password == old_password for old_password in self.old_passwords)

    def get_password(self):
        """
        Returns the current password
        :return:
        """
        return self.old_passwords[-1]

    def set_password(self, password):
        """
        Sets a new password
        Only if the given password has not been used before
        :param password:
        :return:
        """
        if not self._is_unique(password):
            return

        self.old_passwords.append(password)

    def is_correct(self, password):
        """
        Whether the given password matches the current password
        :param password:
        :return:
        """
        return password == self.get_password()
