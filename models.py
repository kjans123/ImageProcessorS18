from pymodm import fields, MongoModel

class User(MongoModel):
    user_id = fields.EmailField(primary_key=True)
    num_histo_times = fields.IntegerField()
    num_contr_times = fields.IntegerField()
    num_log_times = fields.IntegerField()
    num_rever_times = fields.IntegerField()
    stored_pic = fields.ListField(field=fields.BinaryField())
