# APKDOWN REWRITE
# KARJOK PANGESTY
# 2024 01 21


import requests
import bs4
import os
import time
import threading

# colors
x  = '\033[0m'  # reset
gr = '\033[90m' # grey
lr = '\033[91m' # light red
lg = '\033[92m' # light green
ly = '\033[93m' # light yellow
mg = '\033[95m' # magenta
cy = '\033[96m' # cyan
w  = '\033[97m' # white

# initial folder create
if 'results' not in os.listdir("."):
	os.mkdir("results")



def banner(position='home'):
	os.system('cls' if os.name == 'nt' else 'clear')
	if position == 'home':
		print(f'''
{mg}╔═╗╔═╗╦╔═{x}╔╦╗┌─┐┬ ┬┌┐┌{x} apkpure.net
{mg}╠═╣╠═╝╠╩╗{x} ║║│ │││││││{x} apk-dl.com
{mg}╩ ╩╩  ╩ ╩{x}═╩╝└─┘└┴┘┘└┘{x} Downloader
{mg}============================={x}
{gr}https://t.me/karjokpangesty{x}
''')
	elif position == 'apkpure':
		print (f'''
{lg}╔═╗╔═╗╦╔═{x}╔═╗┬ ┬┬─┐┌─┐
{lg}╠═╣╠═╝╠╩╗{x}╠═╝│ │├┬┘├┤
{lg}╩ ╩╩  ╩ ╩{x}╩  └─┘┴└─└─┘.com
{lg}============================={x}
''')
	elif position == 'apkdl':
		print(f'''
{cy}╔═╗╔═╗╦╔═{x}┌┬┐┬ 
{cy}╠═╣╠═╝╠╩╗{x} │││ 
{cy}╩ ╩╩  ╩ ╩{x}─┴┘┴─┘.com
{cy}============================={x}
''')

def home():
	banner('home')
	print(f'''
Available Services:

[{mg}1{x}] apkpure.net
[{mg}2{x}] apk-dl.com {gr}(in development){x}
[{mg}0{x}]{gr} exit{x}
''')

	try:
		selected_service = input(f"{x}Select {mg}>> {x}")
		while selected_service not in ["1","2","0"]:
			selected_service = input(f"{gr}Unknown option.{x} Select {mg}>> {x}")

		if selected_service == "1":
			apkpure()
		elif selected_service == "2":
			apkdl()
		else:
			exit(f'\nThanks')
	except:
		exit(f'\nThanks')



def apkpure(app_name=None):
	banner('apkpure')
	try:
		app_name = app_name if app_name else input(f"Search App Name {lg}>>{x} ")
		while not app_name:
			app_name = input(f"Please input App Name {lg}>>{x} ")
		print(f"Searching {lg}{app_name}{x}..")

		headers = {'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'}
		params = {"q":app_name}
		page_source = requests.get("https://m.apkpure.net/id/search",params=params, headers=headers).text
		page_content = bs4.BeautifulSoup(page_source,'html.parser')
		top_search_result = (page_content.find('div',{"class":"brand-info-top"}).find('a').get('href'),page_content.find('div',{"class":"brand-info-top"}).find('p',{"class":"p1"}).text.strip()) if page_content.find('div',{"class":"brand-info-top"}) else None
		first_search_result = (page_content.find('div',{"class":"first-apk"}).find('a').get('href'), page_content.find('div',{"class":"first-apk"}).find('p',{"class":"p1"}).text.strip()) if page_content.find('div',{"class":"first-apk"}) else None
		search_result_list = page_content.find('ul',{"class":"search-res"})
		search_result_data = []
		if search_result_list:
			search_result_data = list(zip([link.get("href") for link in search_result_list.findAll('a',{"class":"dd"})],[p.text.strip() for p in search_result_list.findAll('p',{'class':'p1'})]))
		if top_search_result:
			search_result_data.insert(0,top_search_result)
		if first_search_result:
			search_result_data.insert(0,first_search_result)

		if search_result_data:
			print(f"Search result(s) for query {lg}{app_name}{x}:")
			n = 1
			for link, app in search_result_data:
				package = link.split("/")[-1]
				print(f"{lg}{n}.{x} {app} {gr}({package}){x}")
				n += 1
			app_selected = input(f"Select App {lg}>>{x} ")
			while not app_selected or not app_selected.isdigit() or int(app_selected) not in range(len(search_result_data)):
				app_selected = input(f"Please select app {lg}>>{x} ")

			app_selected = search_result_data[int(app_selected)-1]
			package = app_selected[0].split("/")[-1]
			name = app_selected[1]
			link = app_selected[0]

			daemon_dl = threading.Thread(target=downloader,args=(f'https://d.apkpure.net/b/APK/{package}?version=latest',f"{name}_{package}_APKDOWN"))
			daemon_dl.start()
			while daemon_dl.is_alive():
				download_animation()
			print(f"\nDone. App saved to {ly}results/{name.replace(' ','_')}_{package}_APKDOWN.apk{x}")



		else:
			print(f"No result found for query {lg}{app_name}{x}. Try another app name to search")


	except KeyboardInterrupt:
		xb = input(f"\nExit/Back ? {lg}(x/b){x} {lg}>>{x} ")
		if xb == "b":
			home()
		else:
			exit(f'\nThanks')
	except Exception as e:
		exit('\nAn error occured: ',e)

def apkdl():
	banner('apkdl')
	print('still in development..')
	for i in range(0,3):
		print(f"\rgoing back to home after ({3-i})",end="",flush=True)
		time.sleep(1)
	home()


def download_animation():
	strings = list("Dowloading.. ")
	for index,item in enumerate(strings):
		new_string = strings
		new_string[index] = f"{lg}{item}{x}"
		print(f"\r{''.join(new_string)}",end="",flush=True)
		time.sleep(0.05)
def downloader(url,file_name):
	content = requests.get(url)
	with open(f"results/{file_name}.apk","wb") as file:
		file.write(content.content)

if __name__ == "__main__":
	home()