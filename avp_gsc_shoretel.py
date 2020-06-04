"""
	Google Cloud
	https://cloud.google.com/docs/authentication/getting-started#windows
	https://cloud.google.com/storage/docs/reference/libraries#windows
	https://pypi.org/project/google-cloud-storage/
"""


import requests
import os 
from google.cloud import storage
import datetime

#-- verify the key is accessible in the environment variables
google_creds = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]


def get_file():
	storage_client = storage.Client()

	
# 	# -- listing out buckets in a project 
	buckets = storage_client.list_buckets()
	
	
	for bucket in buckets:
		stra = f'{bucket}'
		if stra.find('shoretel') > 1:
			neo = stra
		else:
			pass
	the_bucket = neo.split(': ')[1].replace('>','')
	print(the_bucket)

	

# 	# -- working with individual buckets
#	# -- list objects

	blobs = storage_client.list_blobs(the_bucket)

	for blob in blobs:
		stro = f'{blob}'
		if stro.find('202005') > 0:
			teo = stro
		else:
			pass
	the_file = teo.split(', ')[1]
	print(the_file)




def download_file():
	storage_client = storage.Client()
	bucket_name = 'avp_shoretel'
	source_blob_name = '202004_shoretel_pbx.csv'
	destination_file_name = 'C:\\Users\\Joshua\\Desktop\\PROFESSIONAL\\dba AMERICAN VISION PARTNERS\\rural2.csv'
	
	bucket = storage_client.bucket(bucket_name)
	blob = bucket.blob(source_blob_name)
	blob.download_to_filename(destination_file_name)




# download_file()

get_file()
