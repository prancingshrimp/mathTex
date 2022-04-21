margin:left:25
margin:right:25
margin:top:25
margin:bottom:25
t:25,25:L:b:"LES - Erzwungene Konvektion im Vollkanal"
t:25,35:l:n:"Medium: \textbf{Luft}"

i:nu=135e-7
e:25,40:"\nu_{0} = $nu@3$ \, \frac{\mathrm{m^2}}{\mathrm{s}}"

i:kappa=189.8e-7
e:65,40:"\kappa_{0} = $kappa@4$ \, \frac{\mathrm{m^2}}{\mathrm{s}}"

i:rho=1.2758
e:110,40:"\rho_{0} = $rho@5$ \, \frac{\mathrm{kg}}{\mathrm{m^3}}"

i:alpha=3.6738e-3
e:145,40:"\alpha_{0} = $alpha@5$ \, \frac{\mathrm{1}}{\mathrm{K}}"

i:Tm=273.15
e:25,58:"T_{m} = $Tm@3$ \, \mathrm{K}"

i:Pr = None
c:$Pr$=$nu$/$kappa$
e:65,58:"Pr = \frac{\nu_{0}}{\kappa_{0}} = $Pr@3$"

t:25,80:l:n:"Strömungsgrößen:"

i:Re0=5000
e:25,85:"Re_{0} = $Re0@5$"

i:Re=None
c:$Re$=2/3*$Re0$
e:58,85:"Re = \frac{2}{3} Re_{0} = $Re@7$"

i:Retau=None
c:$Retau$=0.09*(4/3*$Re0$)**0.88
e:105,85:"Re_{\tau} = 0.09\,\left( \frac{4}{3} Re_{0} \right)^{0.88} = $Retau@5$"

i:dT=1
e:25,105:"\Delta T = $dT@0$ \mathrm{K}"

i:Th=None
c:$Th$=$Tm$+$dT$/2
e:58,105:"T_{h} = T_{m} + \frac{\Delta T}{2} = $Th@6$\,\mathrm{K}"

i:Tc=None
c:$Tc$=$Tm$-$dT$/2
e:115,105:"T_{c} = T_{m} - \frac{\Delta T}{2} = $Tc@6$\,\mathrm{K}"

i:delta=0.18
i:uref=None
c:$uref$=$Re0$*$nu$/$delta$
e:25,125:"u_{ref} = \frac{Re_{0} \nu_{0}}{\delta} = $uref@3$\,\frac{\mathrm{m}}{\mathrm{s}}"

i:um=None
c:$um$=2/3*$uref$
e:80,125:"u_{m} = \frac{2}{3} u_{ref} = $um@2$\,\frac{\mathrm{m}}{\mathrm{s}}"

i:utau=None
c:$utau$=$Retau$*$nu$/$delta$
e:125,125:"u_{\tau} = \frac{Re_{\tau} \nu_{0}}{\delta} = $utau@5$\,\frac{\mathrm{m}}{\mathrm{s}}"

t:25,155:l:n:"Kanalgeometrie:"

e:25,160:"\delta = $delta@2$ \mathrm{m}"

i:Lx=None
c:$Lx$=3*pi*$delta$
e:58,160:"L_{x} = 3\pi\delta = $Lx@6$\,\mathrm{m}"

i:Ly=None
c:$Ly$=2*$delta$
e:58,170:"L_{y} = 2\delta = $Ly@2$\,\mathrm{m}"

i:Lz=None
c:$Lz$=pi*$delta$
e:58,180:"L_{z} = \pi\delta = $Lz@6$\,\mathrm{m}"

t:25,205:l:n:"Netzgeometrie:"

i:delta_yplus_w=0.5
e:25,210:"\Delta y^{+}_{w} = $delta_yplus_w@1$"

i:delta_y_w=None
c:$delta_y_w$=$delta_yplus_w$*$nu$/$utau$
e:60,210:"\Delta y_{w} = \frac{\Delta y^{+}_{w}\;\nu_{0}}{u_{\tau}} = $delta_y_w@6$\,\mathrm{m}"

i:delta_yplus_c=12
e:25,225:"\Delta y^{+}_{c} = $delta_yplus_c@3$"

i:delta_y_c=None
c:$delta_y_c$=$delta_yplus_c$*$nu$/$utau$
e:60,225:"\Delta y_{c} = \frac{\Delta y^{+}_{c}\;\nu_{0}}{u_{\tau}} = $delta_y_c@6$\,\mathrm{m}"

i:r=None
c:$r$=$delta_y_c$/$delta_y_w$
e:25,245:"r = \frac{\Delta y_{c}}{\Delta y_{w}} = $r@3$"

i:r_minus=None
c:$r_minus$=1/$r$
e:60,245:"r^{-1} = $r_minus@5$"

t:95,251.4:n:n:"MeshSpace:"

i:Ny=114
e:120,245:"N_{y} = $Ny@5$"

newpage
margin:left:25
margin:right:25
margin:top:25
margin:bottom:25

i:delta_xplus=20
e:25,25:"\Delta x^{+} = $delta_xplus@5$"
i:delta_x=None
c:$delta_x$=$delta_xplus$*$nu$/$utau$
e:60,25:"\Delta x = \frac{\Delta x^{+}\;\nu_{0}}{u_{\tau}} = $delta_x@6$\,\mathrm{m}"

i:Nx=None
c:$Nx$=$Lx$/$delta_x$
e:60,40:"N_{x}=\frac{L_{x}}{\Delta x} = $Nx@5$"
t:105,47:n:n:"gewählt:"
c:$Nx$=96
e:125,40.4:"N_{x} = $Nx@5$"

i:delta_zplus=12
e:25,60:"\Delta z^{+} = $delta_zplus@5$"
i:delta_z=None
c:$delta_z$=$delta_zplus$*$nu$/$utau$
e:60,60:"\Delta z = \frac{\Delta z^{+}\;\nu_{0}}{u_{\tau}} = $delta_z@6$\,\mathrm{m}"

i:Nz=None
c:$Nz$=$Lz$/$delta_z$
e:60,75:"N_{z}=\frac{L_{z}}{\Delta z} = $Nz@5$"
t:105,82:n:n:"gewählt:"
c:$Nz$=54
e:125,75.4:"N_{z} = $Nz@5$"

i:Nges=None
c:$Nges$=$Nx$*$Ny$*$Nz$
e:25,90:"N_{x} \cdot N_{y} \cdot N_{z} = $Nges@10$"

t:70,96.4:n:n:"Aufteilung:"

i:nx=3
e:95,90:"n_{x} = $nx@2$"
i:ny=2
e:110,90:"n_{y} = $ny@2$"
i:nz=2
e:125,90:"n_{z} = $nz@2$"

t:25,106.4:n:n:"Prozessoranzahl:"
i:nges=None
c:$nges$=$nx$*$ny$*$nz$
e:62,99.4:"n_{x} \cdot n_{y} \cdot n_{z} = $nges@10$"

t:25,120:n:n:"Volumen pro Prozessor:"
i:nproc=None
c:$nproc$=$Nges$/$nges$
e:70,112.4:"\frac{N_{x} \cdot N_{y} \cdot N_{z}}{n_{x} \cdot n_{y} \cdot n_{z}} = $nproc@10$"

t:25,140:n:n:"Volumen:"
i:nvx=None
c:$nvx$=$Nx$/$nx$
e:50,133:"\frac{N_{x} }{n_{x}} = $nvx@3$"

i:nvy=None
c:$nvy$=$Ny$/$ny$
e:80,133:"\frac{N_{y} }{n_{y}} = $nvy@3$"

i:nvz=None
c:$nvz$=$Nz$/$nz$
e:110,133:"\frac{N_{z} }{n_{z}} = $nvz@3$"
