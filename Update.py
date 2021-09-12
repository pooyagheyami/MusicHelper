#In the name of God
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil


def main():
	main_direct = [u'AI',u'Config',u'Database',u'DCC1',u'GUI','GUI\\Main',u'GUI\\AuiPanel']
	sub_direct = {u'GUI':[u'Main',u'Temp']}
	main_file = {u'AI':[u'Analiz.py',u'Generats.py',u'OpnFil.py',u'WinDev.py'],
	             u'Config':[u'Init.py'],u'Database':[u'MenuSet2.py',u'PostGet.py',u'wxsq.py'],
	             u'DCC1':[u'AuiPan2.py',u'DBDev2.py',u'ListMenu1.py',u'ListPro2.py',
	                      u'MenuDev2.py',u'ProgDev2.py',u'Proper2.py',u'ToolBar2.py'],
	             u'GUI':[u'BG2.py',u'MainMenu2.py',u'MainTool.py',u'proman.py',u'Start.py',u'window2.py'],
	             u'GUI\\Main':[u'DBv1.py',u'MDv1.py',u'PAv1.py',u'PGv1.py',u'PPv1.py',u'TBv1.py',u'TPv1.py'],
	             u'GUI\\AuiPanel':[u'PAui.py',u'Rev.py',u'Stat.py']
	              }
	source_dirct = 'E:\\MyTest\\Temp5\\'
	target_dirct = os.getcwd()+'\\'
	for dirct in main_direct:
		for update_file in main_file[dirct]:
			shutil.copyfile(source_dirct+dirct+'\\'+update_file,target_dirct+dirct+'\\'+update_file)


if __name__ == '__main__':
	main()