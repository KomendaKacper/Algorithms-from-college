import numpy as np
import pickle
import matplotlib
import matplotlib.pyplot as plt
import string
import random

#1

x = np.linspace(-1, 1)
f = lambda x: x**3 - 3*x
y = f(x)
plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) = x^3 - 3x')
plt.grid(True)
x = np.linspace(-5, 5)
plt.plot(x,y)
x = np.linspace(0, 5)
plt.plot(x,y)
plt.legend(["<-1,1>","<-5,5>","<0,5>"])
plt.show()

#2
x = np.linspace(-10,10)

plt.figure()
plt.grid(True)
plt.plot (x,y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) = x^3 - 3x na zakresie <-1,1>')
plt.xlim (-1,1)

plt.figure()
plt.grid(True)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) = x^3 - 3x na zakresie <-10,-1>')
plt.xlim(-10,-1)

plt.figure()
plt.grid(True)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) = x^3 - 3x na zakresie <1,10>')
plt.xlim(1,10)

plt.show()

#3
def Q(m:int, v:int) -> int:
    energia = m/1000 * (v*10/36)**2/2
    return energia
print ("Ilość ciepła podczas hamowania dla tego obiektu wynosi ", round(Q(2500,60)), " dżuli czyli ", round(Q(2500,60)) * 0.00023885, " kilokalorii")

m = 3000
v = np.linspace(200,0)
y = Q(m,v)
plt.figure()
plt.xlim(200,0)
plt.plot(v,y)
plt.grid(True)
plt.xlabel("Prędkość obiektu [km/h]")
plt.ylabel("Ilość energii hamowania [J]")
plt.title("Wykres energii hamowania w skali liniowej")

plt.figure()
plt.xlabel("Prędkość obiektu [km/h]")
plt.ylabel("Ilość energii hamowania [J]")
plt.title("Wykres energii hamowania w skali logarytmicznej")
plt.xlim(200,0)
plt.semilogy()
plt.plot(v,y)
plt.grid(True)
plt.show()

#4
def compare_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                 xlabel: str,ylabel:str,title:str,label1:str,label2:str):
    
    plt.figure()
    plt.grid(True)
    plt.plot (x1,y1,'b',label = label1, linewidth = 4)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot (x2,y2,'r', label = label2, linewidth = 2)
    plt.legend()
    plt.show()
    return None

#5
x = np.linspace(-10,10)
g = x**2 - 2*np.sin(x) + 3
f = x+2
y = np.linspace(-10,10)
compare_plot (x,f,x,g,"x","y","Wykresy funkcji f(x) i g(x)", "f(x)","g(x)")

#6
def parallel_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                  x1label:str,y1label:str,x2label:str,y2label:str,title:str,orientation:str):
    if x1 == [] or x2 == [] or y1 == [] or y2 == []:
        return None
    
    if orientation == '-':
        r = 1
        c = 2
    elif orientation == '|':
        r = 2
        c = 1
    plt.figure()
    plt.grid(True)
    plt.axis('equal')

    plt.subplot(r,c,1)
    plt.plot(x1,y1)
    plt.xlabel(x1label)
    plt.ylabel(y1label)
    plt.title(title)

    plt.subplot (r,c,2)
    plt.plot(x2,y2)
    plt.xlabel(x2label)
    plt.ylabel(y2label)
    plt.show()
    return None

#7
t_szerokie = np.linspace(0, 20, 1000)
x_szerokie = 0.1 * np.exp(0.2 * t_szerokie) * np.cos(t_szerokie)
y_szerokie = 0.1 * np.exp(0.2 * t_szerokie) * np.sin(t_szerokie)

t_zero = np.linspace(0, 0.5, 1000)
x_zero = 0.1 * np.exp(0.2 * t_zero) * np.cos(t_zero)
y_zero = 0.1 * np.exp(0.2 * t_zero) * np.sin(t_zero)

parallel_plot(x_szerokie,y_szerokie,x_zero,y_zero,"x","f(x)","x","f(x)","Wykresy spirali logarytmicznych w różnych przedziałach","|")

#8
def log_plot(x:np.ndarray,y:np.ndarray,xlabel:np.ndarray,ylabel:str,title:str,log_axis:str):
    plt.figure()
    plt.grid(True)
    plt.xlabel (xlabel)
    plt.ylabel (ylabel)
    plt.title (title)
    plt.plot(x,y)
    
    if log_axis == 'x':
        plt.xscale('log')
    elif log_axis == 'y':
        plt.yscale('log')
    elif log_axis == 'xy':
        plt.xscale('log')
        plt.yscale('log')
    
    plt.show()
    return None

#9
def Q(m:int, v:int) -> int:
    energia = m/1000 * (v*10/36)**2/2
    return energia

m = 3000
v = np.linspace(200,0)
y = Q(m,v)

log_plot(v,y,"Prędkość [km/h]","Energia [J]", "Wykres energii od prędkości dla osi x w skali logarytmicznej","x")
log_plot(v,y,"Prędkość [km/h]","Energia [J]", "Wykres energii od prędkości dla osi y w skali logarytmicznej","y")
log_plot(v,y,"Prędkość [km/h]","Energia [J]", "Wykres energii od prędkości dla osi x i y w skali logarytmicznej","xy")

#10
x1 = np.arange(-100,1,0.02)
y1 = np.cos(2*np.pi*x1)

plt.figure ()
plt.subplot (2,2,1)
plt.semilogx (x1,y1,marker = 'o', linestyle = '--', markersize = 3, label = "Krok = 0.02")
plt.title ("Wykres y = cos(2*pi*x) przy użyciu semilogx")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.subplot(2,2,2)
x2 = np.arange(-100,1,0.06)
y2 = np.cos(2*np.pi*x2)
plt.semilogx (x2,y2,marker = 'o', linestyle = '--', markersize = 3, label = "Krok = 0.06")
plt.title ("Wykres y = cos(2*pi*x) przy użyciu semilogx")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()


plt.subplot(2,2,3)
x3 = np.arange(-100,1,0.12)
y3 = np.cos(2*np.pi*x3)
plt.semilogx (x3,y3,marker = 'o', linestyle = '--', markersize = 3, label = "Krok = 0.12")
plt.title ("Wykres y = cos(2*pi*x) przy użyciu semilogx")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.subplot(2,2,4)
x = np.arange(-100,1,0.02)
y = np.cos(2*np.pi*x)
plt.plot (x,y,marker = 'o', linestyle = '--', markersize = 3, label = "Krok = 0.12")
plt.title ("Wykres y = cos(2*pi*x) bez użycia semilogx")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

plt.show()