from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

def saludar(request):
    doc_externo=open("C:/Users/SENA/Desktop/django01/plantillas/PrimeraPlantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    cxt=Context()
    documento=plt.render(cxt)
    return HttpResponse(documento)


def fecha(request):
    fechaActual=datetime.datetime.now()
    documento= """<HTML>
                        <HEAD>
                            <TITLE>Esta es una estructura basica de un documento HTML</TITLE>
                        </HEAD>
                        <BODY>
                            <H1>Usted ingreso o actualizo esta vista en la fecha %s</H1>
                        </BODY>
                    </HTML>"""% fechaActual
    return HttpResponse(documento)


def tareasEnListadas(request):
    Tareas=["Aprender sobre la internet", "Aprender HTML", "Aprender Css", "Practicar Python", "Aprender Django", "Construir mi propia WEB"]
    doc_externo=loader.get_template("SegundaPlantilla.html")
    documento=doc_externo.render({"listado":Tareas})
    return HttpResponse(documento)

def games(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%X")
    
    fecha="%s/%s/%s a las %s" %(dia, mes, agno, hora)
    
    doc_externo=loader.get_template("games.html")
    documento=doc_externo.render({"fecha": fecha})
    return HttpResponse(documento)

def musica(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%X")
    
    fecha="%s/%s/%s a las %s" %(dia, mes, agno, hora)
    
    doc_externo=loader.get_template("musica.html")
    documento=doc_externo.render({"fecha": fecha})
    return HttpResponse(documento)

def tecnologia(request):
    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%X")
    
    fecha="%s/%s/%s a las %s" %(dia, mes, agno, hora)
    
    doc_externo=loader.get_template("tecnologia.html")
    documento=doc_externo.render({"fecha": fecha})
    return HttpResponse(documento)