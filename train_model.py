import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. قراءة البيانات
df = pd.read_csv('spam.csv', encoding='latin-1')

# 2. تحديد الأعمدة المطلوبة فقط
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# 3. تحويل التصنيفات من نص إلى رقم
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# 4. موازنة البيانات (اختياري لكن مهم جداً)
ham_df = df[df['label'] == 0].sample(n=747, random_state=42)
spam_df = df[df['label'] == 1]
df = pd.concat([ham_df, spam_df]).sample(frac=1, random_state=42)

# 5. تقسيم البيانات
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.2, random_state=42
)

# 6. تحويل النصوص إلى ميزات رقمية
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 7. تدريب النموذج
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# 8. تقييم الأداء
y_pred = model.predict(X_test_vec)
print("accuracy:", accuracy_score(y_test, y_pred))
print(" classification report:\n", classification_report(y_test, y_pred))

# 9. حفظ النموذج والـ vectorizer
joblib.dump(model, 'spam_classifier_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')