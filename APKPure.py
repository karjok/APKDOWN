# APKPURE DOWNLOADER
# Minggu, 23 Desember 2018, 11:03 AM WIB
# Karjok Pangesty
# CRACKER NOOB SQUADS INDONESIA
# https://t.me/CRABS_ID

'''
JANGAN DI NAKALIN YA GAN..
MEMANG SIH, SCRIPT AMPAS.. TAPI SETIDAKNYA KAN AKU NGGAK RECODE GAN..
YA BANG YA, PLIS JANGAN NAKALIN AKUU..

ttd,
NoEB SEJATIE 
hehe
😂😂
'''


import subprocess as sp
import os, threading,sys,time
from urllib.request import Request, urlopen
try:
      from bs4 import BeautifulSoup
except ModuleNotFoundError:
      sp.call('cd && pip install beautifulsoup4', shell=True,stdout=sp.DEVNULL,stderr=sp.STDOUT)
try:
      import requests
except ModuleNotFoundError:
      sp.call('cd && pip install requests', shell=True,stdout=sp.DEVNULL,stderr=sp.STDOUT)


cy = '\033[92m'
lg = '\033[92m'
w  = '\033[97m'
lr = '\033[91m'
yl = '\033[93m'
x  = '\033[0m'

def menu():
      sp.call('clear')
      print (lg+'''
            ╔═╗╔═╗╦╔═'''+w+'''╔═╗┬ ┬┬─┐┌─┐'''+lg+'''
            ╠═╣╠═╝╠╩╗'''+w+'''╠═╝│ │├┬┘├┤'''+lg+''' 
            ╩ ╩╩  ╩ ╩'''+w+'''╩  └─┘┴└─└─┘''')
      print(lg+'#'*45)
      print(w+'D O W N L O A D E R'.center(45))
      print(lr+'https://t.me/CRABS_ID'.center(45))
      print(lg+'#'*45)
def search():
      global sc      
      sc = input(cy+'CARI APLIKASI : '+x).replace(' ','+')
      print(lg+'='*45)
     

def main():
      global link,nm,linkfile,size
      no =-1
      link =[]
      judul=[]
      developer=[]
      
      # Mencari aplikasi..
      req = Request('https://m.apkpure.com/id/search?q='+sc.replace(' ',''), headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
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
            print(yl,no,cy+'  Nama Aplikasi :'+x,ju[:20]+'..')
            print(cy+'     Developer     : '+x+de[:20]+'..'+cy)
            print('='*45)    
      print (yl+str(len(link))+lg+' Aplikasi ditemukan'+x)
      
      do = int(input(yl+'Pilih no berapa gan ? : '+x))    
      nm = input(yl+'Masukkan nama output: '+x)
      linx='https://m.apkpure.com'+str(link[do])+'/download?from=details'
      r = Request(linx,headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      r = urlopen(r).read()
      sp = BeautifulSoup(r,'html.parser')
      donl = sp.find('div',attrs={'class':'fast-download-box'})
      don = donl.find('a',attrs={'class':'ga'})
      size = donl.find('span',attrs={'class':'fsize'})
      linkfile = don.get('href')

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
            print (yl+'\rLagi ndonlot gayn'+i,end=''),;sys.stdout.flush();time.sleep(0.3)

  

if __name__=='__main__':
      menu()
      search()
      main()
      trd = threading.Thread(name='Donloder',target=donlot)
      trd.start()
      menu()
      while trd.isAlive():
            animasi()
      print (lg+'\nMantab gayn, Sukses !!')
      print (lg+'Nama  : '+x+nm+'.apk')
      print (lg+'Ukuran: '+x+size.get_text())
        