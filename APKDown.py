# APK DOWNLOADER
# Minggu, 23 Desember 2018, 11:03 AM WIB
# Update Senin, 24 Desember 2018, 4.:25 PM WIB
# Karjok Pangesty
# CRACKER NOOB SQUADS INDONESIA
# https://t.me/CRABS_ID

'''
JANGAN DI NAKALIN YA GAN..
MEMANG SIH, SCRIPT AMPAS.. TAPI SETIDAKNYA KAN AKU NGGAK RECODE GAN..
YA BANG YA, PLIS JANGAN NAKALIN AKUU..

Jangan di recode ya gayn.. tinggal makek aja.. kalo ada yang error tinggal laporin aja.. hehe





ttd,
NoEB SEJATIE YankCellalueTercaaxietiieOlechParaProyankKayaBabbieHehehehe
hehe
😂😂
'''


import subprocess as sp
sp.call('clear')
print('\nTunggu bentar cok ! :*')
sp.call('pip install -r .modul',shell=True,stdout=sp.DEVNULL,stderr=sp.STDOUT)
import os, threading,sys,time,requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

cy = '\033[92m'
cyy = '\033[96m'
lg = '\033[92m'
w  = '\033[97m'
lr = '\033[91m'
yl = '\033[93m'
h = '\033[95m'
x  = '\033[0m'
def home():
      sp.call('clear')
      print(h+'''
       ╔═╗╔═╗╦╔═'''+w+'''  ╔╦╗┌─┐┬ ┬┌┐┌┬  ┌─┐┌─┐┌┬┐┌─┐┬─┐'''+h+'''
       ╠═╣╠═╝╠╩╗'''+w+'''   ║║│ ││││││││  │ │├─┤ ││├┤ ├┬┘'''+h+'''
       ╩ ╩╩  ╩ ╩'''+w+'''  ═╩╝└─┘└┴┘┘└┘┴─┘└─┘┴ ┴─┴┘└─┘┴└─''')
      print(h+'#'*55)
      print(w+'C A C K E R  N O O B  S Q U A D S'.center(55))
      print(w+'h t t p s : / / t . m e / C R A B S _ I D'.center(55))
      print(h+'#'*55)
      print(h+'''
['''+w+'''1'''+h+''']'''+w+''' APKpure.com'''+h+'''
['''+w+'''2'''+h+''']'''+w+''' Apk-dl.com'''+h+'''
['''+w+'''0'''+h+''']'''+w+''' Minggat.com hehe''')
      pilih = input(w+'\nMasukin sini ya gayn, hehe '+h+'>> '+x)
      while pilih != '1' and pilih !='2' and pilih !='0':
            print(lr+'Pakek OTAK dong gayn.. hehe')
            pilih = input(w+'Masukin sini ya gayn, hehe '+yl+'>> '+x)
      if pilih =='1':
            apkprhome()
            apkpure()
            asu = apkprhome()
      elif pilih == '2':
            apkdlhome()
            apkdl()
            asu = apkdlhome()
            lg = '\033[96m'
          
      else:
            sp.call('clear')
            print(h+'\nLafyu gayn.. HEHEHE\n\n'+x)
            sys.exit()
      trd = threading.Thread(name='Donloder',target=donlot)
      trd.start()
      asu
      print (yl+'Sabar ya gayn.. bisa sambil ngupil dulu nunggunya, hehe\nKalo lama berarti servernya lagi error gayn.')
      while trd.isAlive():
            animasi()
      asu
      print (lg+'\nMantab gayn, Sukses !! ')
      print (lg+'Nama  : '+x+nm+'.apk')
      print (lg+'File  :'+x+' Hasil/'+nm+'.apk')
      print (lg+'#'*55)
      anu = input(yl+'Lagi nggak gayn ? y/n hehe : '+x)
      if anu == 'y':
            home()
      else:
            sp.call('clear')
            print(h+'\nLu burique gayn.. gw gans, tq :*\n\n'+x)
            sys.exit()
        

def apkprhome():
      sp.call('clear')
      print (lg+'''
                 ╔═╗╔═╗╦╔═'''+w+'''╔═╗┬ ┬┬─┐┌─┐'''+lg+'''
                 ╠═╣╠═╝╠╩╗'''+w+'''╠═╝│ │├┬┘├┤'''+lg+''' 
                 ╩ ╩╩  ╩ ╩'''+w+'''╩  └─┘┴└─└─┘''')
      print(lg+'#'*55)
      print(w+'D O W N L O A D E R'.center(55))
      print(lg+'@ k a r j o k . p a n g e s t y'.center(55))
      print(lg+'#'*55)

#++($)$)#?#?*+#)#;#)[¢}£[¢}¢}
def apkdlhome():
      sp.call('clear')
      print(cyy+'''
                    ╔═╗╔═╗╦╔═'''+w+''' ┌┬┐┬'''+cyy+'''  
                    ╠═╣╠═╝╠╩╗'''+w+'''  │││'''+cyy+'''  
                    ╩ ╩╩  ╩ ╩'''+w+''' ─┴┘┴─┘''')
      print(cyy+'#'*55)
      print(w+'D O W N L O A D E R'.center(55))
      print(cyy+'@ e k a . p a n g e s t y'.center(55))
      print(cyy+'#'*55)
      
     

def apkpure():
      global link,nm,linkfile,size
      no =0
      link =[]
      judul=[]
      developer=[]
      
      sc = input(lg+'\nCARI APLIKASI >> '+x)
      print (lg+'Hasil pencarian aplikasi '+w+sc.upper())
      print(lg+'='*45)
      # Mencari aplikasi..
      req = Request('https://m.apkpure.com/id/search?q='+sc.replace(' ','+'), headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      req = urlopen(req).read()
      sup = BeautifulSoup(req,'html.parser')
      
      # Mengambil data aplikasi
      for li in sup.find_all('a',attrs={'class':'dd'}):
            l = li.get('href')
            link.append(l)
      for i in sup.find_all('div',attrs={'class':'r'}):
            title = i.find('p',attrs={'class':'p1'})
            peng = i.find('p',attrs={'class':'p2'})
            judul.append(title.get_text())
            developer.append(peng.get_text())
      for ju,de in zip(judul,developer):
            no+=1 
            print(w,no,cy+'  Nama Aplikasi :'+x,ju[:20]+'..')
            print(cy+'     Developer     : '+x+de[:20]+'..'+cy)
            print('='*45)    
      print (w+str(len(link))+lg+' Aplikasi ditemukan'+x)
      
      do = int(input(lg+'\nPilih no berapa gayn ? : '+x))
      do = do - 1    
      nm = input(lg+'Masukkan nama output: '+x)
      linx='https://m.apkpure.com'+str(link[do])+'/download?from=details'
      r = Request(linx,headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      r = urlopen(r).read()
      sp = BeautifulSoup(r,'html.parser')
      donl = sp.find('div',attrs={'class':'fast-download-box'})
      don = donl.find('a',attrs={'class':'ga'})
      size = donl.find('span',attrs={'class':'fsize'})
      linkfile = don.get('href')


######################################################################
# APK-DL
############
def apkdl():
      global link1,nm,linkfile,size
      no =0
      link1 =[]
      judul1=[]
      developer1=[]
      
      sc = input(cyy+'\nCARI APLIKASI >> '+x)
      print (cyy+'Hasil pencarian aplikasi '+x+sc.upper())
      print(cyy+'='*45)
      # Mencari aplikasi..
      req = Request('https://apk-dl.com/search?q='+sc.replace(' ','%20'), headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      req = urlopen(req).read()
      sup = BeautifulSoup(req,'html.parser')
      
      # Mengambil data aplikasi
      for div in sup.find_all('div',class_='card no-rationale square-cover apps small'):
            di = div.find('div', class_='details')
            des = di.find('a', class_='title')
            link1.append(des.get('href'))
            judul1.append(des.text)
            dev = di.find('div',class_='subtitle-container')
            dev = dev.find('a')
            developer1.append(dev.text)
                    
      for ju,de in zip(judul1,developer1):
            no+=1 
            print(w,no,cyy+'  Nama Aplikasi :'+x,ju[:20]+'..')
            print(cyy+'     Developer     :  '+x+de[:20]+'..'+cyy)
            print('='*45)
    
      print (w+str(len(link1))+cyy+' Aplikasi ditemukan'+x)
      
      do = int(input(cyy+'\nPilih no berapa gan ? : '+x))
      do = do - 1    
      nm = input(cyy+'Masukkan nama output: '+x)
      
      
      linx='https://apk-dl.com/'+str(link1[do])
      r = Request(linx,headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      r = urlopen(r).read()
      sp = BeautifulSoup(r,'html.parser')
      donl = sp.find('div',class_='download-btn')
      donll = donl.find('a')
      lindonl = donll.get('href')
      
      
      rq = Request('http://apkfind.com'+lindonl,headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      rq = urlopen(rq).read()
      spq = BeautifulSoup(rq,'html.parser')
      downn =spq.find('div',class_='container-content')
      donn = downn.find('a')#, class_='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect fixed-size')
      
      rj = Request(donn.get('href'),headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      rj = urlopen(rj).read()
      spr = BeautifulSoup(rj,'html.parser')
      downnn =spr.find('div',class_='container-content')
      donnn = downnn.find('a')#, class_='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect fixed-size')
      linkfile='http:'+donnn.get('href')
      
      # generate link donlot
      


def donlot():
      try:
            os.mkdir('Hasil')
      except OSError:
            pass
      req = requests.get(linkfile, headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      with open('Hasil/'+nm+'.apk','wb') as dl:
            dl.write(req.content)
def animasi():
      zz = ['.   ','..  ','... ']
      for i in zz:
            print (yl+'\rIni lagi tak donlotin gayn'+i,end=''),;sys.stdout.flush();time.sleep(0.3)

  

if __name__=='__main__':
      home()

      
