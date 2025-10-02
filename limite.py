#Calculo de limites
#Punto de analisis
xd=1.51
xi=1.51
xinf=100
#Evaluación derecha
for i in range(1,10):
    
    xd=xd+0.01
    xi=xi-0.01
    xinf=xinf+1000
    #función
    yd=(5*xd**3+2)/(2*xd**3-7)
    yi=(5*xi**3+2)/(2*xi**3-7)
    yinf=(5*xinf**3+2)/(2*xinf**3-7)
    print(yi,yd,yinf)
