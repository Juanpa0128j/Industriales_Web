from django.shortcuts import render

def Hogar(request):

    ctx={"active_1":"#hero", "active_2": "#contacto", "active_3": "#acerca_de"}
    return render(request, "main.html", ctx)

def Construcciones(request):

    ctx={"active_1":"/#hero", "active_2": "/#contacto", "active_3": "/#acerca_de"}
    return render(request, "construcciones.html", ctx)
    
def Electricidad(request):

    ctx={"active_1":"/#hero", "active_2": "/#contacto", "active_3": "/#acerca_de"}
    return render(request, "electricidad.html", ctx)
    
def Electronica(request):

    ctx={"active_1":"/#hero", "active_2": "/#contacto", "active_3": "/#acerca_de"}
    return render(request, "electronica.html", ctx)
    
def Metalisteria(request):

    ctx={"active_1":"/#hero", "active_2": "/#contacto", "active_3": "/#acerca_de"}
    return render(request, "metalisteria.html", ctx)
    
def Diseno_de_Productos(request):

    ctx={"active_1":"/#hero", "active_2": "/#contacto", "active_3": "/#acerca_de"}
    return render(request, "diseno_de_productos.html", ctx)
