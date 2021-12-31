from django.shortcuts import redirect, render
from .forms import InputFileForm
import pandas as pd
import openpyxl
from .models import UploadFile,DownloadFile

def excel_view(request):
    if request.method == 'POST':
        form = InputFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.data)
            new_filename=request.FILES['uploaded_file'].name.split('.')[0]
            print(request.FILES['uploaded_file'].name.split('.'))
            for item in UploadFile.objects.all():
                print(item.uploaded_file.url)
            read_file=pd.read_excel(request.FILES['uploaded_file'],engine='openpyxl')
            file_type='csv'
            read_file.to_csv(f'media/uploaded/{new_filename}.{file_type}'.format(new_filename,file_type),encoding='utf-8')
            DownloadFile(new_file_name=f'{new_filename}.csv').save()
            print(new_filename)
            return redirect('/download/')
            
    else:
        form = InputFileForm()                
    template_name='tocsv/main.html'
    return render(request,template_name,{'form':form})
    
def download(request):
    last_file=DownloadFile.objects.all().last()
    # print(type(last_file))
    template_name='tocsv/download.html'
    return render(request,template_name,{"last_file":last_file})