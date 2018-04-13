from pymodm import connect
import models
import datetime

""""module that defines how data is stored to our database
"""

def create_user(email):

    """"function that creates user with specified email. Inputs blank or 0
        variables for all associated fields.

    :param email: takes as input user email
    :returns: new user in database
    """
    u = models.User(email,0,0,0,0,'Empty','no_date')
    u.save()

def save_image(user_email,image_num):

    """"function that creates link for uploaded image. Stores link
        and new timestamp in database.

    :param user_email: finds user with specified email
    :param image_num: takes as input a number that represents the
                      last img number plus one in DB
    :returns: new entry in link list that refers to where image is
              stored on the VCM and associated time stamp
    """
    user = models.User.objects.raw({"_id": user_email}).first()
    new_link = '/images/'+str(user_email)+str(image_num)+'.jpg'
    user.stored_pic.append(new_link)
    user.stored_pic_dates.append(datetime.datetime.now())
    user.save()

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
