class Check_For_User:

    """"class that checks to see if user exists. If user does exist,
    returns True for later use. If user does not exists, asks caller
    if they would like to create new user.

    :param input_email: called entered patient email
    :returns user_exists: returns Boolean True if user exists, False if not
    """
    def __init__(self, user_email):
        self.user_email = user_email
        self.user_exists = None
        self.check_user_email()

    def check_user_email(self):

        """"method that checks to see if user exists. If user does exist,
        returns True for later use. If user does not exists, asks caller
        if they would like to create new user.
        """

        from main import create_user
        from pymodm import connect
        import models
        import datetime
        connect("mongodb://vcm-3594.vm.duke.edu:27017/image_process_app")
        try:
            user = models.User.objects.raw({"_id": self.user_email}).first()
            self.user_exists = True
        except:
            print((str(self.user_email) + " was not found. Please re-enter"))
            self.user_exists = False
