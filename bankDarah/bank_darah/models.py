from django.db import models

# Create your models here.
class Pengguna(models.Model):
    user_id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=100)
    nomor_hp = models.IntegerField(max_length=14)
    email = models.EmailField()
    golongan_darah = models.CharField(max_length=3)

    def __str__(self):
        return self.nama