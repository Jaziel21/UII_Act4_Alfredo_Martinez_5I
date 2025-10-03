from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    clientes = [
        {"nombre": "Cliente A", "email": "clienteA@example.com", "telefono": "111-222-3333"},
        {"nombre": "Cliente B", "email": "clienteB@example.com", "telefono": "444-555-6666"},
        {"nombre": "Cliente C", "email": "clienteC@example.com", "telefono": "777-888-9999"},
    ]
    context = {
        'clientes': clientes
    }
    return render(request, 'index.html', context)