from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ClassifiedMessage
import joblib

model = joblib.load('spam_classifier_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

@api_view(['POST'])
def classify_api(request):
    messages = request.data.get('messages', [])

    if not isinstance(messages, list) or not messages:
        return Response({'error': 'يرجى إرسال قائمة من الرسائل داخل "messages"'}, status=400)

    results = []

    for msg in messages:
        vector = vectorizer.transform([msg])
        prediction = model.predict(vector)[0]
        
        # تخزين الرسالة والنتيجة في قاعدة البيانات
        ClassifiedMessage.objects.create(message=msg, label=prediction)

        results.append({'message': msg, 'label': prediction})

    return Response({'results': results})