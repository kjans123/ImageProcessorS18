from pymodm import fields, MongoModel

class User(MongoModel):
    """"defines database schema. For every user_id, there are 4 values,
        each of which are associated with the number of times the user
        has run one of the four image processing algorithms. In addition,
        for every user, there is a list of image links for every
        uploaded image as well as associated timestamps.
    """
    user_email = fields.EmailField(primary_key=True)
    num_histo_times = fields.IntegerField()
    num_contr_times = fields.IntegerField()
    num_log_times = fields.IntegerField()
    num_rever_times = fields.IntegerField()
    stored_pic = fields.ListField(field=fields.CharField())
    stored_pic_dates = fields.ListField(field=fields.DateTimeField())
