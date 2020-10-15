from django.shortcuts import render

def Hogar(request):

    ctx={"active_1":"#hero", "active_2": "#contacto"}
    return render(request, "main.html", ctx)

def Construcciones(request):

    ctx={"active_1":"/#hero", "active_2": "/#contacto"}
    return render(request, "construcciones.html", ctx)
    
def Electricidad(request):

    ctx={"active_1":"/#hero", "active_2": "/#contacto"}
    return render(request, "electricidad.html", ctx)
    
def Electronica(request):

    ctx={"active_1":"/#hero", "active_2": "/#contacto"}
    return render(request, "electronica.html", ctx)
    
def Diseno_de_Productos(request):

    ctx={"active_1":"/#hero", "active_2": "/#contacto"}
    return render(request, "diseno_de_productos.html", ctx)
