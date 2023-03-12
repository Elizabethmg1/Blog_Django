from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import pageFormulario
from .models import page


@login_required
def inicio(request):
    return render(request,'blog_pages/inicio.html' )

def acerca_de_mi(request):
    return render(request,'blog_pages/acerca_de_mi.html' )

def pages(request):
    pages = page.objects.all()
    contexto = {"pages": pages}
    return render(request, "blog_pages/leerPaginas.html", contexto)

def leer_mas(request, pk):
    page_ = get_object_or_404(page, pk=pk)
    contexto = {"page": page_}
    return render(request, 'blog_pages/leer_mas.html', contexto)


@login_required
@staff_member_required
def edit_page(request, pk):
    page1 =page.objects.get(title=pk)
    if request.method == 'POST':
        miFormulario = pageFormulario(request.POST,request.FILES)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            page1.title = informacion['title']
            page1.subtitle = informacion['subtitle'] 
            page1.body = informacion['body']
            page1.author = informacion['author']
            page1.date = informacion['date']
            page1.image = informacion['image']
            page1.save()
            
            return render(request, "blog_pages/inicio.html")
        
    else:
        miFormulario = pageFormulario(initial={'title':page1.title, 
                                                   'subtitle':page1.subtitle, 
                                                   'body':page1.body, 
                                                   'author': page1.author,"date":page1.date,"image":page1.image})
        
    return render(request, "blog_pages/edit_page.html", {"miFormulario":miFormulario, "title":pk})

@login_required
@staff_member_required
def deletePage(request, pk):
    page1 = page.objects.get(title=pk)
    page1.delete()
    
    pages1 = page.objects.all()
    contexto= {"pages":pages1}
    return render(request, "blog_pages/leerPaginas.html", contexto)

@login_required
@staff_member_required
def create_page(request):
    if request.method == "POST":
        my_page = pageFormulario(request.POST,request.FILES)
        if my_page.is_valid():
            informacion = my_page.cleaned_data

            page1 = page(title = informacion['title'],subtitle = informacion['subtitle'],body = informacion['body'],author = informacion['author'],date = informacion['date'],image = informacion['image'])
            page1.save()
            return render(request,"blog_pages/leerPaginas.html")
    else:
        my_page = pageFormulario()
    
    return render(request, "blog_pages/create_page.html", {"my_page":my_page})
        