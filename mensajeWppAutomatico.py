
import pywhatkit
mensajitos = ["Hellouuu","Mensaje random","EAAAAAAAA"]
hora = [23,23,23]
minutos = [5,7,9]
i=0
n=len(mensajitos)

while i < n:
    print (mensajitos[i])
    pywhatkit.sendwhatmsg("+54 9 11 6787-7359",mensajitos[i],hora[i],minutos[i],30)
    i=i+1
