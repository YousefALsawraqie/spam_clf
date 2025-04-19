# استخدم صورة Python الرسمية
FROM python:3.10-slim

# تعيين مسار العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع إلى الحاوية
COPY . /app

# تثبيت المتطلبات
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt

# فتح منفذ 8000
EXPOSE 8000

# أمر التشغيل الافتراضي لتشغيل السيرفر
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]