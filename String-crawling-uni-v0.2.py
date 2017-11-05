import csv
import string

spam = list()
smpl = ['Regular expression', 'cahnnel:', 'sub', 'subscribe', 'suscribe', 'leave', 'message', 'like', 'comment', 'comment', 'please', 'please message', 'channle', 'tube', '{tube}', 'you[tube]', '(tube)', '{youtube}', '[youtube]', '(youtube)', 'youtube/', 'yt', 'http:', 'https:', 'watch?', '//', 'check', 'out', 'leave', 'my', 'check', 'youtube', '.com', 'com', '.net', 'net', '.org', 'org', '.tv', 'tv', '.me', 'me', '.co', 'co', 'website', 'blog', 'video', 'follow', 't-shirts', 'v-necks', 'accessories', 'visit', 'gift', 'card', 'giftcard', 'on', 'twitter', 'facebook', 'youtube', 'omel', 'kick', 'instakgram', '@', 'search' , 'ig', 'fb', 'gc', 'tw']
regexp = ['subscribe', 'suscribe', 'http:', 'https:', 'watch?', '//','.com', 'com', '.net', 'net', '.org', 'org', '.tv', 'tv', '.me', 'me', '.co', 'co', '@', 'tube', '{tube}', 'you[tube]', '(tube)', '{youtube}', '[youtube]', '(youtube)', 'youtube/']

with open('spam_input.csv', newline='', encoding='utf-8') as csvrw:
    with open('spam_res.csv', 'w', newline='\n') as csvwr:
        spamwriter = csv.writer(csvwr, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(smpl)
        reader = csv.DictReader(csvrw)
        for row in reader:
            if row['CLASS'] == '1':
                string_low = row['CONTENT'].lower()
                string_list = string_low.split(' ')        
                for sp in smpl:
                    if sp in string_list:
                        spam.append('1')
                    else:
                        spam.append('0')
                for re in regexp:
                    if not string_low.find(re) == -1:
                         spam[0] = '1'
                         break
                spamwriter = csv.writer(csvwr, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(spam)
                spam = []   
		print("The job has been finished and spam_res.csv has been created")
input("Please enter to exit...")