from cgi import print_directory
from mailbox import NoSuchMailboxError
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .backend import MyBackend

from .models import Usuario, Mensaje, Producto
from .forms import EmailForm, UsuarioForm, LoginForm, MensajeForm,  UserRegisterForm

MyBackend=MyBackend()

# Create your views here.


def index(request):
    return render (request,'aplicacion1/index.html')


def productos(request):
    return render (request,'aplicacion1/productos.html')

@login_required
def usuarios(request):  # listado de usuarios del sitio
    usuario=Usuario.objects.all()
    return render (request,'aplicacion1/usuarios.html',{"data":usuario})

def ejemplo(request):  # ejemplo de plantilla / solo para ensayo
    return render (request,'aplicacion1/ejemplo.html')


def  formulario_usuario(request):  # registro de usuario

    form = UsuarioForm()
    
    if request.method == "POST":
        form=UsuarioForm(data=request.POST)

        if form.is_valid():
            usuario=Usuario()
            usuario.rut=form.cleaned_data['rut']
            usuario.nombre=form.cleaned_data['nombre']
            usuario.apellido=form.cleaned_data['apellido']
            usuario.edad=form.cleaned_data['edad']
            usuario.email=form.cleaned_data['email']
            usuario.receive_newsletter=form.cleaned_data['receive_newsletter']
            usuario.save()
            messages.info(request, f"{usuario.nombre}, Gracias por registrarte con nosotros .")
        return redirect('ejemplo')
    else:
        form = UsuarioForm()
        return render (request, 'aplicacion1/formulario_usuario.html',{"form":form})


def login(request):   #ingreso de usuario admin
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            usuario=form.cleaned_data["nombre"]
            clave=form.cleaned_data["password"]
            user=authenticate(request, username=usuario, password=clave)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"Has ingresado como {usuario}.")
                return redirect ('bienvenido')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form= LoginForm()
    return render (request, 'aplicacion1/login.html', {"form":form})

@login_required (login_url="/login")
def bienvenido (request):  #mensaje de bienvenida usaurio admin
    return render (request, 'aplicacion1/bienvenido.html')

def salir (request):  #salir usuario admin
    logout (request)
    messages.info(request, "You have successfully logged out.") 
    return redirect ("/login")

def register(request):  #registro usuario admin
    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente.')
            return redirect ('login')
    
    else:
        form=UserRegisterForm()

    context = {'form':form}

    return render (request, 'aplicacion1/register.html', context)


def contacto(request):  #formulario contacto para envia mensajes q se almacenan en objecto mensajes
        form = MensajeForm()
        if request.method == "POST":
            form=MensajeForm(data=request.POST)

            if form.is_valid():
                message=Mensaje()
                message.nombre=form.cleaned_data['nombre']
                message.apellido=form.cleaned_data['apellido']
                message.email=form.cleaned_data['email']
                message.mensaje=form.cleaned_data['mensaje']
                message.save()

            return redirect('/contacto')
        else:
            form = MensajeForm()
            return render (request, 'aplicacion1/contacto.html',{"form":form})

def mostrar_mensaje (request):  #muestra mensajes recibidos
    mensaje=Mensaje.objects.all()
    return render (request,'aplicacion1/mensajes.html',{"data":mensaje})

def editar_mensaje(request, id):  #formulario editar mensaje
        mensaje=Mensaje.objects.get(pk=id)
        form = MensajeForm(instance=mensaje)
        if request.method == "POST":
            form=MensajeForm(data=request.POST, instance=mensaje)
            form.save()
            return redirect('/mostrar_mensaje')
        else:
            return render (request, 'aplicacion1/editar_mensaje.html',{"form":form})

def eliminar_mensaje(request, id):
        mensaje=Mensaje.objects.get(pk=id)
        mensaje.delete()
        return redirect('/mensaje_mail')

def mensaje_mail(request,email):
    email_list = Mensaje.objects.filter(email=email)
    return render(request, 'aplicacion1/mensaje_mail.html', {"correo":email_list})
  

def page_not_found_view(request, exception): #mensaje de error
    return render(request, '404.html', status=404)

def productos_lista(request):
    producto=Producto.objects.all()
    return render (request,'aplicacion1/productos_lista.html',{"data":producto})

