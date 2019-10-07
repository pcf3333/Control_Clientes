from django.shortcuts import render


def control_clientes(request):
    return render(request=request, template_name="main/control-clientes.html")
	
def slugg(request,slug):
	return render(request=request, template_name="main/"+slug)