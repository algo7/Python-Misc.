import numpy as np
from numpy.linalg import norm
from numpy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt
import matplotlib.animation as an
import math 



#------------------------- PHYSICAL PARAMETERS -------------------------
# Define force of Gravity
def F(M,m,pos1,pos2):
    r = norm(pos2-pos1)
    return #input the correct function

#------------------------- PHYSICAL PARAMETERS -------------------------
G = 6.7e-11 # Universal gravitational constant
Msun = 1.989e30 # Mass of sun (kg)
Me = 5.972e24 # Mass of Earth (kg)
Mm = 7.348e22 # Mass of Moon (kg)

esd = 1.496e11 # Earth-Sun distance (m)
emd = 3.844e8 # Earth-Moon distance (m)

Ve = 2.93e4 # Magnetude of velocity of Earth around the Sun (m/s)
Vm = 1.02e3 # Magnetude of velocity of Moon around the Earth (m/s)

dt = 100. # Time step (s)
t_end = 3.154e7 #one year in seconds
t = np.linspace(0.,t_end,t_end/dt)





#Create Arrays to Store the Position of Each Starts Respectively

Xsun = np.zeros(len(t))
Ysun = np.zeros (len(t))

Xearth = np.zeros(len(t))
Yearth = np.zeros(len(t))

Xmoon = np.zeros(len(t))
Ymoon = np.zeros(len(t))

#Initial Position of Earth / Sun

Xsun [0] = 0 
Ysun [0] = 0

Xearth[0] = esd  
Yearth[0] = 0

Xmoon[0] = esd
Ymoon[0] = emd


#Create Arrays to Store the Velocity of Each Starts Respectively
VxSun = np.zeros (len(t))
VySun = np.zeros (len(t))

Vxearth = np.zeros(len(t))
Vyearth = np.zeros(len(t))

Vxmoon = np.zeros(len(t))
Vymoon = np.zeros(len(t))

#Initial Velocity of Earth / Sun

Vxearth [0] = 0
Vyearth [0] = Ve

Vxmoon[0] = -Vm
Vymoon[0] = Ve

#VySun [0] = -Vyearth [0] * Me /Msun
VxSun [0] = (-(Vxearth [0] * Me) - (Mm * -Vm)) /Msun 
VySun [0] = (-(Vyearth [0] * Me) - (Mm * Vymoon [0])) /Msun



#Force Functions (x,y) 

def forcefuncx(x1,x2,y1,y2,m1,m2):
    return -(G*m1*m2*(x2-x1))/ (math.sqrt ((x2-x1)**2 + (y2-y1)**2))**3

def forcefuncy (x1,x2,y1,y2,m1,m2):
    return -(G*m1*m2*(y2-y1))/ (math.sqrt ((x2-x1)**2 + (y2-y1)**2))**3
    
    #calculate distance between two planets

    #calculate the force


## TUESDAY AM: create a plot of the gravitational force as a function of distance


## TUESDAY PM: solve the ODE

for i in range (0,len(t)-1):
    #Update:Velocity of the Earth (Affected by both the Moon and the Sun)
    Vxearth[i+1] = Vxearth[i] + (forcefuncx(Xsun[i], Xearth[i], Ysun[i], Yearth[i], Msun, Me) + forcefuncx(Xmoon[i], Xearth[i], Ymoon[i], Yearth[i], Mm, Me)) /Me*dt
    Vyearth[i+1] = Vyearth[i] + (forcefuncy(Xsun[i], Xearth[i], Ysun[i], Yearth[i], Msun, Me) + forcefuncy(Xmoon[i], Xearth[i], Ymoon[i], Yearth[i], Mm, Me)) /Me*dt

    #Update:Velocity of the Sun (Affected by both the Earth and the Moon)
    VxSun[i+1] = VxSun[i] + (forcefuncx(Xearth[i], Xsun[i], Yearth[i], Ysun[i], Me, Msun) + forcefuncx(Xmoon[i], Xsun[i], Ymoon[i], Ysun[i], Msun, Me)) /Msun*dt
    VySun[i+1] = VySun[i] + (forcefuncy(Xearth[i], Xsun[i], Yearth[i], Ysun[i], Me, Msun) + forcefuncy(Xmoon[i], Xsun[i], Ymoon[i], Ysun[i], Msun, Me)) /Msun*dt

    #Update: Velocity of the Moon (Affected by both the Earth and the Sun)
    Vxmoon[i+1] = Vxmoon[i] + (forcefuncx(Xsun[i], Xmoon[i], Ysun[i], Ymoon[i], Msun, Mm) + forcefuncx(Xearth[i], Xmoon[i], Yearth[i], Ymoon[i], Me, Mm)) /Mm*dt
    Vymoon[i+1] = Vymoon[i] + (forcefuncy(Xsun[i], Xmoon[i], Ysun[i], Ymoon[i], Msun, Mm) + forcefuncy(Xearth[i], Xmoon[i], Yearth[i], Ymoon[i], Me, Mm)) /Mm*dt

    #Update:Position of the Earth
    Xearth[i+1]= Xearth[i] + Vxearth[i+1] *dt
    Yearth[i+1]= Yearth[i] + Vyearth[i+1] *dt

    #Update:Position of the Sun
    Xsun[i+1]= Xsun[i] + VxSun[i+1] *dt
    Ysun[i+1]= Ysun[i] + VySun[i+1] *dt

    #Update:Position of the Moon
    Xmoon[i+1] = Xmoon[i] + Vxmoon[i+1] *dt
    Ymoon[i+1] = Ymoon[i] + Vymoon[i+1] *dt
    









f = rfftfreq(len(t),3.171e-6) 

XFearth = rfft(Xearth)
XFmoon = rfft(Xmoon)
XFsun = rfft(Xsun)

#Total Energy of the System = Potential Energy + Kinetic Energy


#Relative Distance Between the Earth, the Sun, and the Moon
rms = np.sqrt((Xmoon - Xsun)**2 + (Ymoon - Ysun)**2)
rem = np.sqrt((Xmoon - Xearth)**2 + (Ymoon - Yearth)**2)
res = np.sqrt((Xearth - Xsun)**2 + (Yearth - Ysun)**2)

#Magnitude of the Velocity of the Earth
MagE = np.sqrt(Vxearth**2 + Vyearth**2)

#Magnitud of the Velocity of the Sun

MagS =  np.sqrt(VxSun**2 + VySun**2)

#Magnitude of the Velocity of the Moon

MagM= np.sqrt(Vxmoon**2 +  Vymoon**2)



#Potential Energy of the Earth & Sun

Pes = -(G*Msun*Me /res)

#Potential Energy of the Earth & Moon

Pem = -(G*Me*Mm / rem)


#Potential Energy of the Moon & Sun

Pms = -(G*Msun*Mm / rms )

#Kinetic Energy of the Earth

Ke = (0.5*Me*MagE**2)

#Kinetic Energy of the Sun

Ks = (0.5*Msun*MagS**2)


#Kinetic Energy of the Moon

Km = (0.5*Mm*MagM**2)

#Total Energy of the System

Te = Pes + Pem + Pms + Ke + Ks + Km



## WEDNESDAY: calculate the frequency of the orbit using Fourier analysis
## THURSDAY







fig = plt.figure()

plt.title ('Orbits of the Earth, the Sun, and the Moon')
plt.plot(Xearth, Yearth,)
plt.plot(Xmoon,Ymoon)
plt.plot(Xsun,Ysun,)


fig2 = plt.figure()

plt.title ('Total Energy Over Time')
plt.plot(t,Te)


plt.title('XEarth V.S Time')
plt.plot(t,Xearth)



fig4 =  plt.figure()

plt.title('XMoon V.S Time')
plt.plot(t,Xmoon)



fig6 = plt.figure()
axf6 =  fig6.add_subplot(131)
plt.title ('Fourier Transform for the Freq. of the Earth Orbiting Around the Sun')
plt.plot(f,np.abs(XFearth))
plt.xlim((0,30))

ax2f6 =  fig6.add_subplot(132)
plt.title('FT for the Moon Orbiting Around the Sun')
plt.plot(f,np.abs(XFmoon))
plt.xlim((0,30))


ax3f6 = fig6.add_subplot(133)
plt.title('FT for the Sun')
plt.plot(f,np.abs(XFsun))
plt.xlim((0,30))


fig7 =  plt.figure()

plt.title('XSun V.S Time')
plt.plot(t,Xsun)
plt.show()


###ax1 = fig.add_subplot(131)
###plt.title ('Position of the Earth')
##plt.plot(Xearth, Yearth)
##
###ax2 = fig.add_subplot(132)
###plt.title ('Position of the Sun')
##plt.plot(Xsun, Ysun)
##
###ax3 = fig.add_subplot(133)
##plt.title ('Position of the Moon')
##plt.plot(Xmoon, Ymoon)
##
##fig2 = plt.figure()

# code to animate plot
# create figure
#fig = plt.figure()
# define axes
#ax = plt.axes(xlim=(0.,t_end),ylim=(0.,t_end))
#line1, = ax.plot([],[],lw=2)

# function to initialize lines for animation

##def init():
##    line1.set_data()
##   return line1,
##
##def animate_single(i):
##    line1.set_data()
##    return line1,
##
###animate and plot
##num_frames = 1000
##anim = an.FuncAnimation(fig, animate_single, init_func=init, blit=True, interval=1, frames=num_frames)





##for i in range (0, len(t)- 1):
##
##    rms[i] = (math.sqrt((Xmoon[i]- Xsun[i])**2) + (Ymoon[i] - Ysun[i])**2) 
##    rem[i] = (math.sqrt((Xmoon[i] - Xearth[i])**2 + (Ymoon[i] - Yearth[i])**2)
##    res[i] = (math.sqrt((Xearth[i] - Xsun[i])**2 + (Yearth[i] - Ysun[i])**2)
##



#print Te.size



   
##    if i%10==0:
##        plt.clf()
       
##        plt.plot(Xsun[i], Ysun[i],".")
##
##    #ax3 = fig.add_subplot(133)
##        plt.title ('Position of the Moon')
##        plt.plot(Xmoon[i], Ymoon[i],".")
##        plt.xlim(-esd, esd)
##        plt.ylim(-esd, esd)
##        plt.show(block=False)
##        plt.pause(0.01)

#ax1 = fig.add_subplot(131)
#ax2 = fig.add_subplot(132)
