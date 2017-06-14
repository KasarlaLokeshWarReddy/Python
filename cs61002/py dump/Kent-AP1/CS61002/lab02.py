
import stdio
import math


stdio.writeln("Calculating Plants and Soil needed")
stdio.writeln("Inputs needed")
lg = float( input("Enter length of garden (feet):"))
sbp = float( input("How much spacing do you want between plants (feet):"))
dog = float( input("What depth you want to dig (feet):"))
dof = float( input("How much depth do you want to fill (feet):"))

(diameter) = lg / 2

ca = math.pi * ((diameter/2)**2)

pic = math.trunc(ca/(sbp**2))

sa = (math.pi * ( (diameter/2)**2))/2

pis = math.trunc(sa/(sbp**2))

tpn = pic + (pis * 4)

cs = math.pi * ( (diameter/2)**2 ) * dog

cs = round((cs / 27),1)

ss = (math.pi * ( (diameter/2)**2 ) * dog)/2

ss = round((ss / 27),1)

ts = cs + (ss * 4)
ts = round(ts,1)

gv = (dof) * (lg**2)
tpa = (math.pi*((diameter/2)**2)*dog)*3
tf = gv - tpa

tf = tf / 27
tf = round(tf,1)

stdio.writeln("Plants needed each semicircle garden:"+str(pis))
stdio.writeln("Plants for the circle garden: "+str(pic))
stdio.writeln("Total number of plants needed for garden: "+str(tpn))
stdio.writeln("Soil needed for one semicircle garden: "+str(ss)+ " cubic yards")
stdio.writeln("Soil for circular garden: "+str(cs)+ " cubic yards")
stdio.writeln("Total soil needed for the garden: "+str(ts)+ " cubic yards")
stdio.writeln("Total fill needed for the garden: "+str(tf)+ " cubic yards")











