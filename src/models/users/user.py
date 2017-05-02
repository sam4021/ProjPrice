import uuid

from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        '''
        This Method verifies that an email/password combo(as sent by the site form) is valid or not,
         Checks that the e-mail exists, and that the password associated to the email is correct.
        :param email: The User's email
        :param password: The sha512 hashed password
        :return: True if valid, False otherwise
        '''
        user_data = Database.find_one('users',{"email": email})
        if user_data is None:
            #Tell the user that their e-mail doesn't exist
            raise UserErrors.UserNotExistsError("Your user does not exist")
        if not Utils.check_hashed_password(password, user_data['password']):
            #Tells the user that their password is wrong
            raise UserErrors.IncorrectPasswordError("Your password was wrong")