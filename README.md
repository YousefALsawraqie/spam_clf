# 🧠 مشروع تصنيف البريد العشوائي (Spam Classifier)

مشروع بسيط يعتمد على تعلم الآلة (Machine Learning) لتصنيف لبريد العشوائي (SMS) إلى "Spam" أو "Ham" باستخدام خوارزمية Naive Bayes.

---

## ✅ فكرة المشروع

الهدف هو بناء نموذج قادر على التمييز بين الرسائل العادية (Ham) والرسائل العشوائية (Spam) بناءً على النصوص.  
تم تدريب النموذج باستخدام مجموعة بيانات عامة (SMS Spam Collection Dataset) وتخزينه بصيغة `pkl` ليُستخدم لاحقًا في واجهة Django.

---

## 🧪 كيفية تشغيل المشروع

### 1. تثبيت المتطلبات

```bash
pip install -r requirements.txt

## 2. تدريب النموذج (اختياري إذا أردت إعادة التدريب)
python train_model.py

## 3. تشغيل مشروع Django
cd backend-django\ and\ api\spam_project_ready_v1
python manage.py runserver

## 📊 مخطط توضيحي لتدفق البيانات (Mermaid)
flowchart TD
    A[قراءة بيانات CSV] --> B[معالجة البيانات]
    B --> C[تحويل النصوص إلى تمثيل رقمي - TF-IDF]
    C --> D[تدريب النموذج - Naive Bayes]
    D --> E[تخزين النموذج والـ Vectorizer]
    E --> F[واجهة Django لعرض النتائج]
## 📂 هيكلية المشروع (ملخص)
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

## 👥 أعضاء الفريق
YousefALsawraqie 
Tameem-Alyameni


## 📧 للتواصل
لأي استفسار، الرجاء التواصل مع الفريق عبر Trello أو GitHub Issues.