from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pengguna

#POST
def simpan_pengguna(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        pekerjaan = request.POST['pekerjaan']
        nomor_hp = request.POST['nohp']
        email = request.POST['email']
        goldar = request.POST['goldar']
        
        pengguna = Pengguna(nama=nama,pekerjaan = pekerjaan, nomor_hp = nomor_hp, email=email, golongan_darah = goldar)
        pengguna.save()
        
        # Anda dapat menambahkan logika tambahan atau mengarahkan pengguna ke halaman lain
    return render(request, 'bank_darah/home.html')
#READ
def user_list(request):
    users = Pengguna.objects.all()
    return render(request, 'bank_darah/history.html', {'users': users})

#UPDATE
def update_user(request, user_id):
    user = get_object_or_404(Pengguna, user_id=user_id)

    if request.method == 'POST':
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.pekerjaan = request.POST['pekerjaan']
        user.nomor_hp = request.POST['nomor_hp']
        user.save()
    
    return render(request, 'bank_darah/update.html', {'user': user})

#DELETE
def delete_user(request, user_id):
    user = get_object_or_404(Pengguna, user_id=user_id)

    if request.method == 'POST':
        user.delete()

    return render(request, 'bank_darah/delete.html', {'user': user})

# Create your views here.
def home(request):
    return render(request, 'bank_darah/home.html')
def login(request):
    return render(request , 'bank_darah/login.html')

def math(aku):
    if aku == 'giat':
       nilai = berhasil
       return nilai
    else:
       nilai = 'gagal'
       return nilai
math(giat)

def study(pilih):
    if pilih == 'konsisten':
       nilai = 'bertahap'
       return nilai
    else:
       nilai='yakin'
       return nilai
study(bisa)

def hijau(input):
    return input

 
