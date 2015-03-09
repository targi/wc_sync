import zipfile
import base64
import os
import os.path
import console
import sys
import errno


def buildInstallPath():
	APP_DIR = os.path.realpath(os.path.abspath(os.path.dirname(__file__)))
	HOME2 = os.path.join(os.environ['HOME'], 'Documents')
	return os.path.relpath(APP_DIR, HOME2)

INSTALL_PATH = buildInstallPath()
ZIP_FILE = os.path.join(INSTALL_PATH, 'repo.zip')

path = sys.argv[1]

try:
	os.makedirs(os.path.join(os.path.expanduser('~/Documents'), path))
except OSError, e:
	if e.errno != errno.EEXIST:
		raise e
	console.alert('Overwriting existing directory',button1='Continue')

zipF = os.path.join(os.path.expanduser('~/Documents'), ZIP_FILE)
with open(zipF, 'w') as zip:
	zip.write(base64.b64decode(sys.argv[2]))
	
z = zipfile.ZipFile(zipF)	
z.extractall(os.path.join(os.path.expanduser('~/Documents'), path))
os.remove(zipF)
console.hud_alert(path + ' Downloaded')
