# Python bazasi bilan Docker imidjini tanlash
FROM python:3.9-slim

# Ishchi katalogni o'rnatish
WORKDIR /app

# Talablar faylini konteynerga nusxalash
COPY requirements.txt /app/
RUN  pip install --upgrade pip
# Talablarni o'rnatish
RUN pip install --no-cache-dir -r requirements.txt

# Django loyihasini konteynerga nusxalash
COPY . /app/

# Portni ochish
EXPOSE 8000

# Django serverni ishga tushirish
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
