import csv
import string

spam = list()
smpl = ['sub', 'subscribe', 'suscribe', 'leave comment', 'leave message', 'leave like', 'like comment', 'comment like', 'comment', 'please like', 'please comment', 'please message', 'channle', 'tube', '{tube}', '[tube]', '(tube)', '{youtube}', '[youtube]', '(youtube)', 'youtube/', 'yt', 'http:', 'https:', 'watch?', '//', 'check out', 'leave a ', 'check my', 'check', 'new in youtube', '.com', 'com', '.net', 'net', '.org', 'org', '.tv', 'tv', '.me', 'me', '.co', 'co', 'website', 'blog', 'video', 'follow me', 'follow us', 'follow', 't-shirts', 'v-necks', 'accessories', 'visit', 'gift card', 'giftcard', 'on ', 'twitter', 'facebook', 'youtube', 'omel', 'kick', 'instakgram', '@', 'search' , 'ig', 'fb', 'gc', 'tw']

string = input("please insert ur string> ")
string_low = string.lower()
string_list = string_low.split(' ')

for sp in smpl:
    if sp in string_list:
        spam.append('1')
    else:
        spam.append('0')

print(spam)
input("Please enter to exit...")
