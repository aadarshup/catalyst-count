import os
import psycopg2
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.http import HttpResponse

# def home(request):
#     return render(request, 'myapp/home.html')

@login_required
def home(request):
    return render(request, 'myapp/home.html')

def upload_data(request):
    return render(request, 'myapp/upload_data.html')

def query_builder(request):
    # def query_builder(request):
    if request.method == 'POST':
        host = request.POST.get('host')
        port = request.POST.get('port')
        dbname = request.POST.get('dbname')
        user = request.POST.get('user')
        password = request.POST.get('password')
        try:
            conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
            return JsonResponse({'message': 'Connected to the database!'})
        except Exception as e:
            return JsonResponse({'message': f'Connection failed: {str(e)}'}, status=400)
    return render(request, 'myapp/query_builder.html')

    # return render(request, 'myapp/query_builder.html')

def users(request):
    return render(request, 'myapp/users.html')

# def upload_file(request):
#     if request.method == 'POST':
#         file = request.FILES['file']
#         file_path = os.path.join('C:\\Users\\prans\\OneDrive\\Documents\\Python Scripts\\DjangoProject\\folders', file.name)
#         with open(file_path, 'wb+') as destination:
#             for chunk in file.chunks():
#                 destination.write(chunk)
#         return JsonResponse({'message': 'File uploaded successfully!'})
#     return JsonResponse({'message': 'Invalid request!'}, status=400)

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        save_path = os.path.join(r'C:\Users\prans\OneDrive\Documents\Python Scripts\catalyst-count\folderfiles', uploaded_file.name)
        with open(save_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        return HttpResponse('File uploaded successfully!')
    # return HttpResponse('Failed to upload file.')
    return render(request, 'myapp/upload_data.html')