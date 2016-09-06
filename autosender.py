import pyautogui as p,time,subprocess as sub
sub.Popen('C:\\Program Files (x86)\\Microsoft Office Communicator\\communicator.exe')
time.sleep(1)


dict = ['john smith','greame smith','Good morning']

for i in range(0,2):
	p.typewrite(dict[i]);time.sleep(1)
	p.press('enter')
	p.typewrite(dict[3]);time.sleep(1)
	p.press('enter')	
	p.hotkey('alt','f4');time.sleep(1)


