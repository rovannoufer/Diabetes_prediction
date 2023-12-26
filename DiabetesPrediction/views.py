from django.shortcuts import render, redirect
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from django.contrib import auth
from django.contrib.auth.models import User
 
 
def predict(request):
    return render(request, 'predict.html')
 
def result(request):
    data = pd.read_csv("DiabetesPrediction/diabetes.csv")
    X = data.drop("Outcome", axis=1)
    Y = data["Outcome"]
 
    X_train, X_test, Y_train, Y_test = train_test_split (X, Y, test_size=0.2)
 
    model = LogisticRegression()
    model.fit(X_train, Y_train)
 
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
 
    pred = model.predict([[val1, val2, val3,
                           val4, val5, val6, val7, val8]])
 
    result1 = ""
    if pred == [1]:
        result1 = "Oops! You have DIABETES."
    else:
        result1 = "Great! You DON'T have diabetes."
 
    return render(request, "predict.html", {"result2": result1})

# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username = username, password = password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('predict')
#         else:
#             error_message = "Invalid username or password"
#             return render(request, 'login.html', {'error_message': error_message})
#     else:
#       return render(request, 'login.html')


# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2:
#             try:
#                 user = User.objects.create_user(username, email, password1)
#                 user.save()
#                 auth.login(request, user)
#                 return redirect('predict')
#             except:
#                 error_message = 'Error on creating account'
#                 return render(request, 'signup.html', {'error_message': error_message})
#         else:
#             error_message = 'Password don\'t match'
#             return render(request, 'signup.html', {'error_message': error_message})
#     return render(request, 'signup.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('login')