from django.shortcuts import render
import joblib
from .models import Aissm

def index(request):
    return render(request, 'index.html')

def result(request):
    cls = joblib.load(r'C:\Users\om\Desktop\aissmsioit\models\model.joblib')
    data = [
        int(request.GET['age']),
        int(request.GET['sex']),
        float(request.GET['bmi']),
        int(request.GET['children']),
        int(request.GET['smoker']),
        int(request.GET['region'])
    ]
    answer = cls.predict([data])
    
    # Save the data to the database
    b = Aissm(
        age=int(request.GET['age']),
        sex=request.GET['sex'],
        bmi=float(request.GET['bmi']),
        children=int(request.GET['children']),
        smoker=request.GET['smoker'],
        region=request.GET['region'],
        charges=answer[0]
    )
    b.save()
    
    return render(request, 'index.html', {'answer': answer[0]})