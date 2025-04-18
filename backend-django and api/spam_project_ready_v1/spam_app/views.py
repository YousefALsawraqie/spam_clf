from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import ClassifiedMessage
import joblib
from .serializers import StuSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


model = joblib.load('spam_classifier_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

def message_input(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            messages = form.cleaned_data['messages'].split('\n')
            results = []
            for message in messages:
                vector = vectorizer.transform([message])
                prediction = model.predict(vector)[0]
                label_text = "spam" if prediction == 1 else "ham"
                msg = ClassifiedMessage.objects.create(message=message, label=label_text)
                results.append(msg)
                print(results)
            return render(request, 'spam_app/result.html', {'results': results})
        
    else:
        form = MessageForm()
    return render(request, 'spam_app/input_form.html', {'form': form})


def classification_result(request):
    messages = ClassifiedMessage.objects.all()
    return render(request, 'spam_app/result.html', {'results': messages})




@api_view(['POST'])
def createnodes(request):
    nodes = ClassifiedMessage.objects.all()
    serializer = StuSerializer(nodes)
    return Response(serializer.data)


class NoteViewset(viewsets.ModelViewSet):
    queryset = ClassifiedMessage.objects.all()
    serializer_class = StuSerializer