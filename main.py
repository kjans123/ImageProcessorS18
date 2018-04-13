from pymodm import connect
import models
import datetime

def create_user(email):
    u = models.User(email,0,0,0,0,'Empty','no_date')
    u.save()

def save_image(user_email,image_num):
    user = models.User.objects.raw({"_id": user_email}).first()
    new_link = '/'+str(user_email)+'/images/'+str(image_num)+'.txt'
    user.stored_pic.append(new_link)
    user.stored_pic_dates.append(datetime.datetime.now())

def add_histo(user_email):
    user = models.User.objects.raw({"_id": user_email}).first()
    old_count = user.num_histo_times
    new_count = old_count + 1
    user.num_histo_times = new_count

def add_contr(user_email):
    user = models.User.objects.raw({"_id": user_email}).first()
    old_count = user.num_contr_times
    new_count = old_count + 1
    user.num_contr_times = new_count

def add_log(user_email):
    user = models.User.objects.raw({"_id": user_email}).first()
    old_count = user.num_log_times
    new_count = old_count + 1
    user.num_log_times = new_count

def add_rever(user_email):
    user = models.User.objects.raw({"_id": user_email}).first()
    old_count = user.num_rever_times
    new_count = old_count + 1
    user.num_rever_times = new_count
