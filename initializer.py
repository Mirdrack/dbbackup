import os
from pydrive.auth import GoogleAuth

if not os.path.exists('credentials.txt'):
	credentials = open('credentials.txt', 'w+')

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.