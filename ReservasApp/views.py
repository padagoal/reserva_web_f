from django.shortcuts import render
from .forms import ReservaForm
from datetime import datetime

# Create your views here.


def index(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        #form.fields['tile'].queryset = Tile.objects.filter(section__xxx=yyy)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'listo.html', {'form': form})
        else:
            print('Error')

            return render(request, 'error.html', {'form': form})

    else:
        form = ReservaForm()
        return render(request,'index.html',{'form':form})