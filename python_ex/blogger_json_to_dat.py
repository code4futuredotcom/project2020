# https://developers.google.com/blogger/docs/3.0/using
# pip install google_auth_oauthlib
# under Mac command + b to execute
'''
No module named 'googleapiclient'
    pip install google-api-python-client 
No module named 'google_auth_oauthlib'
    pip install google_auth_oauthlib
Add to Blogger need oauth2client
    pip install oauth2client
'''
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/blogger', ]

# we check if the file tBo store the credentials exists
if not os.path.exists('mdecourse_blogger_token.dat'):

    flow = InstalledAppFlow.from_client_secrets_file('mdecourse_blogger_desktop.json', SCOPES)
    credentials = flow.run_local_server()

    with open('mdecourse_blogger_token.dat', 'wb') as credentials_dat:
        pickle.dump(credentials, credentials_dat)
else:
    with open('mdecourse_blogger_token.dat', 'rb') as credentials_dat:
        credentials = pickle.load(credentials_dat)
service = build('blogger', 'v3', credentials=credentials)
g.es(service)