# !/usr/bin/python
# Creator : Anon6372098
# Team : D4RK SYST3M F41LUR3 S33K3R

# Persiapan Alat Tempur :V
import sys,socket

# Intro Dulu ea, kek biasa :V 
anon = """
   ###    ##    ##  #######  ##    ##    ########   #######  ########  ######## 
  ## ##   ###   ## ##     ## ###   ##    ##     ## ##     ## ##     ##    ##    
 ##   ##  ####  ## ##     ## ####  ##    ##     ## ##     ## ##     ##    ##    
##     ## ## ## ## ##     ## ## ## ##    ########  ##     ## ########     ##    
######### ##  #### ##     ## ##  ####    ##        ##     ## ##   ##      ##    
##     ## ##   ### ##     ## ##   ###    ##        ##     ## ##    ##     ##    
##     ## ##    ##  #######  ##    ##    ##         #######  ##     ##    ## 

 ######   ######     ###    ##    ## ##    ## ######## ########  
##    ## ##    ##   ## ##   ###   ## ###   ## ##       ##     ## 
##       ##        ##   ##  ####  ## ####  ## ##       ##     ## 
 ######  ##       ##     ## ## ## ## ## ## ## ######   ########  
      ## ##       ######### ##  #### ##  #### ##       ##   ##   
##    ## ##    ## ##     ## ##   ### ##   ### ##       ##    ##  
 ######   ######  ##     ## ##    ## ##    ## ######## ##     ##
 
\t\t+=================================================+
\t\t+      Creator  : Anon6372098                     +
\t\t+      Contact  : anon6372098.id@gmail.com        +                             
\t\t+      Team     : D4RK SYST3M F41LUR3 S33K3R      +
\t\t+      Homepage : https://www.dsfs-indo.zone.id/  +                                       
\t\t+      Thanks to: All Member of DSFS Official     +
\t\t+      GitHub   : https://github.com/Anon6372098/ +       
\t\t+=================================================+
"""
print anon

# Waktunya beraksi dengan dinamika permainan Python, hobi w ea :V

if len(sys.argv) <4:
        print "\n Penggunaan : python anonport.py <website> <awal port> <akhir port>"
        print "\n Contoh     : python anonport.py www.dsfs-indo.zone.id 1 8000"
        sys.exit(0)
 
web_anon=sys.argv[1]
awal_anon=sys.argv[2]
akhir_anon=sys.argv[3]
 
for port in range (int(awal_anon),int(akhir_anon)):
        try:
                print "\n[#] Memindai port",port
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                s.connect((socket.gethostbyname(web_anon), int(port)))
                print "\n[+] Ditemukan port yang terbuka :) : ",port
                s.close()
        except:
                pass