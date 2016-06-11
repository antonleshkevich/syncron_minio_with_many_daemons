#!/usr/bin/python3

import argparse
import os
from minio import Minio
from minio.error import ResponseError
import time

parser = argparse.ArgumentParser()
parser.add_argument('path', type=str, help='You programm track')
parser.add_argument('quit', type=str, help='Exit key')
parser.add_argument('--s3', type=str, help='Your host')
parser.add_argument('--access_key', type=str, help='Your access key')
parser.add_argument('--secret_key', type=str, help='Your secret key')
parser.add_argument('--dir', type=str, help='Folder directory')
parser.add_argument('--bucket', type=str, help='Your bucket')
args = parser.parse_args()
minioClient = Minio(args.s3, access_key=args.access_key, 
	secret_key=args.secret_key, secure=False)

def find_last_modified(bucket): 
	data_time = []
	real_obj = []
	all_obj = all_objects(bucket)
	try:
		for obj in all_obj:
			real_obj.append(obj)
		for obj in real_obj:
			data_time.append(obj.last_modified)
			print(obj.object_name)
		return max(data_time)
	except Exception:
		return -1

def all_objects(bucket):
	objects = minioClient.list_objects(bucket, prefix='', recursive=True)
	return objects

if __name__ == '__main__':
	print(find_last_modified(args.bucket))