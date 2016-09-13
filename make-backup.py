import os
import time
import datetime
import config
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def create_drive_folder(folder, parentFolder, drive):
	folder_meta = {
		'title': folder,
		'parents': [{'id': parentFolder}],
		'mimeType': 'application/vnd.google-apps.folder',
	}

	drive_backup_folder = drive.CreateFile(folder_meta)
	drive_backup_folder.Upload()
	return drive_backup_folder['id']


DB_HOST = config.DB_HOST
DB_USER = config.DB_USER
DB_USER_PASSWORD = config.DB_USER_PASSWORD
DB_NAME = config.DB_NAME
DATE = time.strftime('%Y%m%d')
BACKUP_PATH = config.BACKUP_PATH
TODAYBACKUPPATH = BACKUP_PATH + DATE
BK_FOLDER_ID = config.BK_FOLDER_ID


gauth = GoogleAuth()
drive = GoogleDrive(gauth)

print 'Creating backup folder'
if not os.path.exists(TODAYBACKUPPATH):
	drive_backup_folder_id = create_drive_folder(DATE, BK_FOLDER_ID, drive)
	os.makedirs(TODAYBACKUPPATH)

print 'Checking for databases names file'
if os.path.exists(DB_NAME):
	print 'Databases file found...'
	print 'Starting backup of all dbs listed in file ' + DB_NAME

in_file = open(DB_NAME, 'r')
flength = len(in_file.readlines())
in_file.close()
dbfile = open(DB_NAME, 'r')

p = 1
while p <= flength:
	db = dbfile.readline()
	db = db[:-1]
	dumpcmd = 'mysqldump -u ' + DB_USER + ' --password=' + DB_USER_PASSWORD + ' ' + db + ' | gzip > ' + TODAYBACKUPPATH + '/' + db + '.gz'
	os.system(dumpcmd)

	file_meta = {'parents':  [{'id': drive_backup_folder_id}]}
	drive_file = drive.CreateFile(file_meta);
	drive_file.SetContentFile(TODAYBACKUPPATH + '/' + db + '.gz')
	drive_file['title'] = db + '.gz';
	drive_file.Upload()
	p = p + 1
dbfile.close()


print 'Backup script completed'
print 'Your backups has beed created in ' + TODAYBACKUPPATH + ' directory'
