### Cara Menjalankan Project

Aktifkan virtual environment(venv) 

- Pada OS WIndows masuk ke Command Prompt
```
venv\Scripts\Activate
```

Pastikan venv aktif seperti pada gambar dibawah ini :

![alt text](image-7.png)

- Cek Dependency pada venv :
```
pip freeze
```
Maka Akan tampil seperti berikut :

![alt text](image-9.png)

- Install Dependency sendiri melalui requirement.txt :
```
pip install -r requirements.txt
```
- Cek Dependency dengan :

```
pip list
```

![alt text](image-10.png)

- Menonaktifkan venv :
```
deaktivate
```
Berikut tampilan venv tidak aktif :

![alt text](image-8.png)


- Menjalankan Project
```
python manage.py runserver
```

### Login

Untuk Login gunakan 3 Akses Berikut :

![alt text](image-1.png)

Manager (CRUD) -> u: @manager p: iniPassword

User (CRU) -> u: @user p: iniPassword

public (R) -> u: @public p: iniPassword

### Module List

Untuk mengakses module silahkan melalui url `/module`

![alt text](image.png)

Module hanya dapat diakses jika sudah klik `install` dan tidak dapat diakses jika module `di-uninstall`

### Akses Module

Untuk Akses Module cukup dengan mengakses `Open Module`

![alt text](image-2.png)

Preview Akses Manager

![alt text](image-3.png)

Preview Akses User

![alt text](image-4.png)

Preview Akses Public

![alt text](image-5.png)


### Logout

Untuk Melakukan Logout Sementara Melalui `/admin` dan klik tombol `logout`

![alt text](image-6.png)


