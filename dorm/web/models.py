from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 128)

class Table(models.Model):
    u0 = models.ForeignKey('User', on_delete = models.DO_NOTHING, related_name = 'table_u0')
    u1 = models.ForeignKey('User', on_delete = models.DO_NOTHING, related_name = 'table_u1')
    val = models.BigIntegerField(default = 0)
    
    def get_val(self):
        return self.val / 100.0

    def set_val(self, new_val):
        self.val = int(new_val * 100)

    def add_val(self, alt_val):
        self.val += int(alt_val * 100)

class Log(models.Model):
    u0 = models.ForeignKey('User', on_delete = models.DO_NOTHING, related_name = 'log_u0')
    u1 = models.ForeignKey('User', on_delete = models.DO_NOTHING, related_name = 'log_u1')
    val = models.BigIntegerField(default = 0)
    ctime = models.DateTimeField(auto_now_add = True)
    comment = models.CharField(max_length=1024)
    
    def get_val(self):
        return self.val / 100.0

    def set_val(self, new_val):
        self.val = int(new_val * 100)
