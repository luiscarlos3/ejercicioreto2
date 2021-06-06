def calcular(Ii,Ih, BPi, BPh,c):
    return ((Ih-Ii)/(BPh-BPi))*(c-BPi)+Ii

def condicionMarron(Ii,Ih, BPi, BPh,c):
    alerta_marron = 0
    ICA=0
    suma = 0
    if c>=250.5 and c<350.5:
        alerta_marron+=1
        ICA = calcular(Ii,Ih, BPi, BPh,c)
        suma+=1
        return alerta_marron, ICA, suma
    else:
        return 0
        

def condicionMorado(Ii,Ih, BPi, BPh,c):
    alerta_morado = 0
    ICA = 0
    suma = 0
    if c>=150.5 and c<250.5:
        alerta_morado+=1
        ICA = calcular(Ii,Ih, BPi, BPh,c)
        suma+=1
        return alerta_morado, ICA, suma
    else:
        return 0
    

def condicionRojo(Ii,Ih, BPi, BPh,c):
    alerta_rojo = 0
    ICA = 0
    suma = 0
    if c>=65.5 and c<150.5:
        alerta_rojo+=1
        ICA = calcular(Ii,Ih, BPi, BPh,c)
        suma+=1
        return alerta_rojo, ICA, suma
    else:
        return 0

def condicioNaranja(Ii,Ih, BPi, BPh,c):
    alerta_naranja = 0
    ICA = 0
    suma = 0
    if c>=40.5 and c<65.5:
        alerta_naranja+=1
        ICA = calcular(Ii,Ih, BPi, BPh,c)
        suma+=1
        return alerta_naranja, ICA, suma
    else:
        return 0

def condicionAmarillo(Ii,Ih, BPi, BPh,c):
    alerta_amarillo = 0
    ICA = 0
    suma = 0
    if c>=15.5 and c<40.5:
        alerta_amarillo+=1
        ICA = calcular(Ii,Ih, BPi, BPh,c)
        suma+=1
        return alerta_amarillo, ICA, suma
    else:
        return 0   

def condicionverde(Ii,Ih, BPi, BPh,c):
    alerta_verde = 0    
    ICA = 0
    suma = 0
    if c >= 0 and c < 15.5:
        alerta_verde+=1        
        ICA = calcular(Ii,Ih, BPi, BPh,c)
        suma+1
        return alerta_verde, ICA, suma     
    
vueltas = 0
suma=0
i=0
while i <= 21 : 
    vueltas+=1        
    c=float(input(str(vueltas) + " Entrada "+ " "))   
    alerta_verde, ICA, suma = condicionverde(0, 50, 0 ,15.4, c)
    alerta_amarillo,ICA,suma = condicionAmarillo(51, 100, 15.5, 40.4,c)
    alerta_naranja, ICA, suma = condicioNaranja(101, 150, 40.5, 65.4, c)
    alerta_rojo, ICA, suma = condicionRojo(151, 200, 65.5, 150.4, c)
    alerta_morado, ICA, suma = condicionMorado(201,300, 150.5, 250.4, c)
    alerta_marron, ICA, suma = condicionMarron(301, 400, 250.5, 350.4, c)
    suma=suma+ICA
       
promedio = suma / vueltas
if 0<= promedio <= 50:
    alerta = "verde"
elif 50 < promedio <= 100: 
    alerta = "amarillo"
elif 100 < promedio <= 150:
    alerta = "naranja"
elif 150 < promedio <= 200:
    alerta = "rojo"
elif 200 < promedio <= 300:
    alerta = "morado"
elif 300 < promedio:
    alerta = "marron"

print (vueltas)
print ("{0:.2f}".format(promedio), alerta)

print ("verde", "{0:.2f}".format((alerta_verde/vueltas)*100)+"%")
print ("amarillo", "{0:.2f}".format((alerta_amarillo/vueltas)*100)+"%")
print ("naranja", "{0:.2f}".format((alerta_naranja/vueltas)*100)+"%")
print ("rojo", "{0:.2f}".format((alerta_rojo/vueltas)*100)+"%")
print ("morado", "{0:.2f}".format((alerta_morado/vueltas)*100)+"%")
print ("marron", "{0:.2f}".format((alerta_marron/vueltas)*100)+"%")


    
    




    