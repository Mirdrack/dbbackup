# DBbackup

## Getting the Google Drive API Keys
1. Go to APIs Console and make your own project.
2. Search for ‘Google Drive API’, select the entry, and click ‘Enable’.
3. Select ‘Credentials’ from the left menu, click ‘Create Credentials’, select ‘OAuth client ID’.
4. Now, the product name and consent screen need to be set -> click ‘Configure consent screen’ and follow the instructions. Once finished:
    - Select ‘Application type’ to be Web application.
    - Enter an appropriate name.
    - http://localhost:8080 for ‘Authorized JavaScript origins’.
    - http://localhost:8080/ for ‘Authorized redirect URIs’.
    - ‘Save’.
5. Click ‘Download JSON’ on the right side of Client ID to download client_secret_<really long ID>.json.

## Installation
1. Clone the repository `git clone https://github.com/Mirdrack/dbbackup.git`
2. Rename the downloaded client_secret_<really long ID>.json to **“client_secrets.json”** and move it inside of the project folder
3. Create the virtual enviroment with `virtualenv .venv`
4. Activate the virtual enviroment with `source .venv/bin/activate`
5. Install dependencies with `pip install -r requirements.txt`

## Initialize first time
You have to install the project on your local computer to setup your account permissions to interact with the application
After install and setup the client_secrets.json file run **initializer.py** with `python initializer.py` on your local computer, this will prompt a browser window asking for the necessary permissions from your google account.

## Testing upload (optional on local environment)
You can test if **Google Drive** and your application are well configured running the test upload file with `python test-upload.py` is highly recommended check this if you are on your prodction server.

## Testing file listing (optional on local environment)
To setup the ID of the **Google Drive** backup folder you should list the files on your root of Google Drive using this `python file-list.py`. If you don't have a folder, create a new one on your browser.   
After list your files and folders copy the ID where you are going to store the backups and setup the **BK_FOLDER_ID** pararameter on **config.py**.

## Local backup
The script is going to store a local backup, you must create a folder and specify the full path on **BACKUP_PATH** parameter **config.py**

## Set Mysql parameters
On **config.py** you should configure **DB_HOST, DB_USER and DB_USER_PASSWORD** parameters.

## Set databases to backup
On the file **dbnames.txt** you should setup the names of the databases are going to be backed up, you must set one name per line and **LEFT A BLANK LINE AT THE END OF FILE**.

## Making the backups
After following this instrucctions you should be able to run the script with `python make-backup.py` this will create a local copy on the configured folder and another copy on your **Google Drive**

## EXTRA. Crontab
To make daily backups you should add the script to the crontab, to achieve this you should run `crontab -e` and configure the execution of the script, for example you can add a line like this one:  
`5 0 * * * reporsitory_path/run_backup.sh`  
to run the script 5 minutes before midnight.


