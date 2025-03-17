# Gunakan image Python resmi
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Tentukan working directory dalam container
WORKDIR /app

# Copy seluruh isi project ke dalam container
COPY . /app

# Buat virtual environment di dalam container
RUN python -m venv /app/venv

# Aktifkan venv yang sudah ada dan install dependencies
RUN /app/venv/bin/pip install --upgrade pip \
    && /app/venv/bin/pip install -r /app/requirements.txt

# Tambahkan EXPOSE untuk mendokumentasikan port yang digunakan
EXPOSE 8000

# Jalankan aplikasi
CMD ["/app/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
