from django.shortcuts import render
from django.shortcuts import render
import numpy as np
from PIL import Image
from .feature_extractor import FeatureExtractor
from datetime import datetime
import manage
from django.shortcuts import render, redirect
from .forms import UploadedImageForm
from .models import UploadedImage, StoredImage
from .schema import SaveImage,StoredImageType

def image_view(request):
  
    if request.method == 'POST':
        form = UploadedImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = form.cleaned_data['image']
            # name = form.cleaned_data['name']
            images = UploadedImage(image=img, name="")
            
            # uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".")+str(img)
            img = Image.open(img)
            # img.save(uploaded_img_path)
            
            fe = FeatureExtractor()
            features, img_paths = manage.feature_data_load()
            # img_paths = StoredImage.objects.values_list('image')
            
            print("len of data ===> ", len(features))
            print("len(img_paths) : ", len(img_paths))
            
            query = fe.extract(img)
            dists = np.linalg.norm(features-query, axis=1)  # L2 distances to features
            ids = np.argsort(dists)[:5] 
            print("ids => ", ids)
            scores =convert_array(img_paths)
            scores = [scores[i] for i in ids]
            print("\nScore => ", scores)

            current_port = request.META['SERVER_PORT']
        return render(request, 'index.html', {'form' : form, 'images': images, 'scores': scores, 'current_port': current_port})
    else:
        form = UploadedImageForm()
        current_port = request.META['SERVER_PORT']
        return render(request, 'index.html', {'form' : form, 'scores': [], 'current_port': current_port})
  

def convert_array(img_paths):
    path = []
    for p in img_paths:
        p = str(p)
        p = p.replace("'", "") 
        p = p.replace("(", "")
        p = p.replace(")", "")
        p = p.replace(",", "")
        path.append(p)
    return path