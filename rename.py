import glob
import os

news_list = glob.glob("second_dataset/*")
cnt = 0

def clean(s):
	global cnt
	hello = "second_dataset/"
	hello += str(cnt)+".avi"
	cnt = cnt+1
	return hello


for news in news_list:
	os.rename(news, clean(news))