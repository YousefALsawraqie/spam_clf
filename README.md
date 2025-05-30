# 🧠 مشروع كاشف الرسائل العشوائية (Spam Detector)

هذا المشروع عبارة عن تطبيق بسيط يستخدم خوارزمية تعلم آلي لتصنيف الرسائل إلى "Spam" أو "Ham" (غير عشوائية). يعتمد على Django لبناء الواجهة الخلفية، ويتضمن واجهة HTML للمستخدم وواجهة API للتكامل مع تطبيقات أخرى.


---

المتطلبات

لتشغيل المشروع، يجب توفر المتطلبات التالية:

Python 3.8 أو أحدث

مكتبة Django

مكتبة scikit-learn

مكتبة pandas

مكتبة joblib


جميع المكتبات المطلوبة موجودة في ملف requirements.txt

#### تثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

---

##تشغيل المشروع

### لتشغيل المشروع على جهازك المحلي:

### 1. تأكد أنك داخل مجلد المشروع


### 2. شغّل السيرفر:


```bash
cd backend-django and api/spam_project_ready_v1 python manage.py runserver
```
### ثم افتح المتصفح على الرابط التالي:

http://127.0.0.1:8000/input/


---

#### طريقة العمل

يقوم المستخدم بإدخال رسالة بريد إلكتروني في الواجهة.

يتم إرسال الرسالة إلى خادم Django.

يتم تمرير الرسالة إلى نموذج تم تدريبه مسبقاً (محفوظ في ملف joblib).

النموذج يُرجع تصنيف الرسالة (Spam أو Ham).

يتم عرض النتيجة للمستخدم في صفحة منفصلة.



---



### استخدام Docker لبناء وتشغيل الحاوية Docker:

#### 1. لإنشاء صورة:


```bash
docker build -t spam-detector .
```
#### 2. لتشغيل الحاوية:


```bash
docker run -p 8000:8000 spam-detector
```

#### أو إذا كنت تستخدم docker-compose:
```bash
docker-compose up --build
```

### ثم افتح المتصفح على
 http://localhost:8000/input/


---

### المخطط البياني يوضح المخطط التالي سير العملية داخل المشروع(Mermaid):

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {
  'fontFamily': 'Arial',
  'primaryColor': '#FFD700',       /* أصفر ذهبي */
  'primaryBorderColor': '#FFA500', /* برتقالي */
  'primaryTextColor': '#000000',   /* أسود */
  'secondaryColor': '#87CEEB',     /* أزرق فاتح */
  'tertiaryColor': '#98FB98'       /* أخضر فاتح */
}}}%%
flowchart TD
    A["المستخدم يُدخل رسالة نصية"] --> B["الواجهة الأمامية (Frontend) ترسل الطلب إلى واجهة API"]
    B --> C["خادم API يستقبل الرسالة عبر Endpoint محدد"]
    C --> D["الرسالة تُمرّر إلى نموذج تعلم الآلة (Machine Learning Model)"]
    D --> E["النموذج يقوم بتحليل الرسالة وتحديد نوعها: Spam أو Ham"]
    E --> F["النتيجة تُعاد إلى خادم API"]
    F --> G["الـ API يُرسل النتيجة إلى الواجهة الأمامية (Frontend)"]
    G --> H["عرض النتيجة للمستخدم (مثلاً: 'هذه الرسالة بريد عشوائي')"]
```

### 📂 هيكلية المشروع (ملخص)
```bash
spam_clf/
├── backend-django and api/
│   └── spam_project_ready_v1/
│       ├── spam_app/
│       │   ├── views.py
│       │   ├── urls.py
│       │   ├── ...
│       ├── spam_project/
│       │   ├── settings.py
│       │   ├── ...
├── spam.csv
├── train_model.py
├── README.md
├── requirements.txt
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
└── diagram.mmd
```
### 👥 أعضاء الفريق
#### 1- YousefALsawraqie 
##### 2- Tameem-Alyameni
##### 3- Mokhtaralawi
##### 4- Zydan 

### 📧 للتواصل
لأي استفسار، الرجاء التواصل مع الفريق عبر Trello أو GitHub Issues.
