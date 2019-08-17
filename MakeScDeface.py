#!/usr/bin/python

C= "\033[0;96m"
G= "\033[0;92m"
W= "\033[0;97m"
R= "\033[0;91m"
B= "\033[0;94m"
Y= "\033[0;33m"
M= "\033[0;35m"

    
import os
import sys
import time
import random
import socket

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
        
__banner__="""
 __________       ___________      ___________      ____________     __________     __________
|          \     |   ________|    |           |    |   ______   |   |          |   |   _______| 
|  ______   \    |  |             |    _______|    |  |      |  |   |   _______|   |  |
| |      |  |    |  |________     |   |_______     |  |______|  |   |  |           |  |_______
| |      |  |    |   ________|    |    _______|    |   ______   |   |  |           |   _______|
| |______|  |    |  |             |   |            |  |      |  |   |  |_______    |  |
|           /    |  |________     |   |            |  |      |  |   |          |   |  |_______
|__________/     |___________|    |___|            |__|      |__|   |__________|   |__________|

"""
print
print W+"###########################"
print M+"Create Sc Deface v1.0        "
print C+"Codded By:TnSadboys   "
print R+"Team : Devils  Union Hurted       "
print W+"###########################"
print
time.sleep(3)
mengetik(W+'Hallo Anjenk, kali ini gue buat tool Deface :)')
mengetik(C+'Kalo Lu Cewek Minta pap asw...')
print
mengetik('Masukan Title')
title = raw_input('Title : ')
print
mengetik('Masukan Nama underground')
heading = raw_input('Nama Underground : ')
print
mengetik('Masukan Link Gambar')
imagelink = raw_input('link gambar : ')
print
mengetik('Masukan Pesan masukan <br> untuk teks lanjutan')
pesan = raw_input('Pesan : ')
print
mengetik('Masukan Warna Teks')
warna = raw_input('Warna : ')
print
print 

fo = open("script.html","w")

messagescript1 = """<html><head><title>"""

messagescript2 = title

messagescript3 = """</title></head>
<body>
<br>
<link href='http://fonts.googleapis.com/css?family=Orbitron:700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Anton' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Josefin Sans' rel='stylesheet' type='text/css'>
<body bgcolor=black"""

messagescript4 = """><div class='CenterDiv'>
<center>
<h1><center><font color=\"red\" face=Orbitron>"""

messagescript5 = heading

messagescript6 =  """<h1></font>
<img src=""" 

messagescript7 = imagelink

messagescript8 = """ width=450px height=340px>
<body onload="init()"></body>
<body>
<div id="bulle"></div>"""

messagescript9 = """ <script language=\"JavaScript\">
var i=0
var j=0
var texteNE, affiche
var texte=\"<br><br><br><br><br><font face=Orbitron color="""

messagescript10 = warna

messagescript11 = """ size=4>"""

messagescript12 = pesan

messagescript13 = """<br><br></font><br></b></div>\"
var ie = (document.all);
var ne = (document.layers); 
function init(){
texteNE='';
machine_a_ecrire();
}
function machine_a_ecrire(){
texteNE=texteNE+texte.charAt(i)
affiche='<font face=Orbitron size=1 color=#ffffff><strong>Messenge : '+texteNE+'</strong></font>'
if (texte.charAt(i)=="<") {
j=1
}
if (texte.charAt(i)==">") {
j=0
}
if (j==0) {
if (document.getElementById) { // avec internet explorer
document.getElementById("bulle").innerHTML = affiche;
}
}
if (i<texte.length-1){
i++
setTimeout("machine_a_ecrire()",70)
}
else
return
}
</script><font face="Orbitron" size="1"><blink><span style="color: rgb(255, 255, 255);"><b><font color=lime size=4></font></b></u></blink><br></font></b>
<a href="/index.php"><img style="position:fixed;bottom:0px;z-index:1000;right:-10px;"  src="http://static1.squarespace.com/static/5706c12007eaa0b82399660d/5706c68bf0bc33987cae6c71/577d5c5d37c581fd0e25c10b/1469717705608/insult-145142_1280.png" type="image/gif" width="150"></a></body>
<!-- CSS --><style>
.CenterDiv{width:650px;border:1px #ff0000 solid;padding:5px;margin:0px auto; background: url('http://i.imgur.com/sDbaMsW.gif');}
</style>
<br>
<br>
<br>
"""

fo.write(messagescript1)
fo.write(messagescript2)
fo.write(messagescript3)
fo.write(messagescript4)
fo.write(messagescript5)
fo.write(messagescript6)
fo.write(messagescript7)
fo.write(messagescript8)
fo.write(messagescript9)
fo.write(messagescript10)
fo.write(messagescript11)
fo.write(messagescript12)
fo.write(messagescript13)

mengetik('File Disimpan dengan format script.html')

print B+("")
fo.close()