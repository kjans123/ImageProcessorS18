from pymodm import connect
import models
import datetime

""""module that defines how data is stored to our database
"""


def create_user(user_email):

    """"function that creates user with specified email.
        Inputs initial image link (/0.jpg) and datetime of user creation.
        Also enters 0 for all for all process count fields.

    :param email: takes as input user email
    :returns: new user in database
    """
    u = models.User(user_email, 0, 0, 0, 0, [], [])
    new_link = '/images/'+str(user_email)+'/'+str(0)+'.jpg'
    u.stored_pic.append(new_link)
    u.stored_pic_dates.append(datetime.datetime.now())
    u.save()


def save_image(user_email, image_num):

    """"function that creates link for uploaded image. Stores link
        and new timestamp in database.

    :param user_email: finds user with specified email
    :param image_num: takes as input a number that represents the
                      last img number plus one in DB
    :returns: new entry in link list that refers to where image is
              stored on the VCM and associated time stamp
    """
    user = models.User.objects.raw({"_id": user_email}).first()
    new_link = '/images/'+str(user_email)+'/'+str(image_num)+'.jpg'
    user.stored_pic.append(new_link)
    user.stored_pic_dates.append(datetime.datetime.now())
    user.save()


def get_user_pre_pics_count(user_email):

    """"Function that gets the number of pre-proc
        images a user has stored on database

    :param user_email: finds user with specified email
    :returns image_count: gets the number of images the user
                          has uploaded
    """
    user = models.User.objects.raw({"_id": user_email}).first()
    image_list = user.stored_pic
    image_count = len(image_list)-1
    return image_count

def add_histo(user_email):

    """"function that adds one to number of times a particular user
        has run histogram equalization process

    :param user_email: finds user with specified email
    :returns: updated histogram count entry in database
              for particular user
    """
    user = models.User.objects.raw({"_id": user_email}).first()
    old_count = user.num_histo_times
    new_count = old_count + 1
    user.num_histo_times = new_count
    user.save()


def add_contr(user_email):

    """"function that adds one to number of times a particular user
        has run contrast stretching process

    :param user_email: finds user with specified email
    :returns: updated contrast strech count entry in database
              for particular user
    """
    user = models.User.objects.raw({"_id": user_email}).first()
    old_count = user.num_contr_times
    new_count = old_count + 1
    user.num_contr_times = new_count
    user.save()


def add_log(user_email):

    """"function that adds one to number of times a particular user
        has run log compression process

    :param user_email: finds user with specified email
    :returns: updated log compression count entry in database
              for particular user
    """
    user = models.User.objects.raw({"_id": user_email}).first()
    old_count = user.num_log_times
    new_count = old_count + 1
    user.num_log_times = new_count
    user.save()


def add_rever(user_email):

    """"function that adds one to number of times a particular user
        has run reverse video process

    :param user_email: finds user with specified email
    :returns: updated reverse video count entry in database
              for particular user
    """
    user = models.User.objects.raw({"_id": user_email}).first()
    old_count = user.num_rever_times
    new_count = old_count + 1
    user.num_rever_times = new_count
    user.save()


def print_user(user_email):
    user = models.User.objects.raw({"_id": user_email}).first()
    print(user.user_email)
    print(user.num_histo_times)
    print(user.num_contr_times)
    print(user.num_log_times)
    print(user.num_rever_times)
    print(user.stored_pic)
    print(user.stored_pic_dates)
