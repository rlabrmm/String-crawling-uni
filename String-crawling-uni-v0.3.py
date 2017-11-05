import csv
import string

smpl = ['Regular expression', 'cahnnel:', 'sub', 'subscribe', 'suscribe', 'leave', 'message', 'like', 'comment', 'comment', 'please', 'please message', 'channle', 'tube', '{tube}', 'you[tube]', '(tube)', '{youtube}', '[youtube]', '(youtube)', 'youtube/', 'yt', 'http:', 'https:', 'watch?', '//', 'check', 'out', 'leave', 'my', 'check', 'youtube', '.com', 'com', '.net', 'net', '.org', 'org', '.tv', 'tv', '.me', 'me', '.co', 'co', 'website', 'blog', 'video', 'follow', 't-shirts', 'v-necks', 'accessories', 'visit', 'gift', 'card', 'giftcard', 'on', 'twitter', 'facebook', 'youtube', 'omel', 'kick', 'instakgram', '@', 'search' , 'ig', 'fb', 'gc', 'tw']
regexp = ['http', 'watch', '//', 'com', 'net', 'org', 'tv', 'me', 'co', '@', 'tube']
csv_input = 'Empty'
csv_output = 'Empty'
class_clo = 'Empty'
content_clo = 'Empty'

def comp_classed():
    spam = [] 
    with open(csv_input, newline='', encoding='utf-8') as csvrw:
        with open(csv_output, 'w', newline='\n') as csvwr:
            spamwriter = csv.writer(csvwr, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(smpl)
            reader = csv.DictReader(csvrw)
            for row in reader:
                if row[class_clo] == '1':
                    string_low = row[content_clo].lower()
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
            print("The job has been finished and {} has been created".format(csv_output))

def comp_noclass():
    spam = [] 
    with open(csv_input, newline='', encoding='utf-8') as csvrw:
        with open(csv_output, 'w', newline='\n') as csvwr:
            spamwriter = csv.writer(csvwr, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(smpl)
            reader = csv.DictReader(csvrw)
            for row in reader:
                string_low = row[content_clo].lower()
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
            print("The job has been finished and {} has been created".format(csv_output))


while True:
    print("----------------------------------------------------------------------------------------------------------")
    inp = input("String crawling V0.2""\n""0- Run""\n""1- Word samples""\n""2- Regular expressions""\n""3- File names""\n""4- Column setings""\n""5- help""\n""6- Exit""\n""> ")
    if inp == '1':
        if input("1- Show Word samples""\n""2- Enter new Word samples""\n""> ") == '1':
            print(smpl)
        else:
            print("Enter done when you done....""\n""> ")
            smpl = ['Regular expression']
            while True:
                new_smpl = input()
                if new_smpl == "done":
                    break
                smpl.append(new_smpl)
                continue
    elif inp == '2':
        if input("1- Show Regular expression""\n""2- Enter new Regular expression""\n""> ") == '1':
            print(regexp)
        else:
            print("Enter done when you done....")
            regexp = []
            while True:
                new_reg = input()
                if new_reg == "done":
                    break
                regexp.append(new_reg)
                continue
    elif inp == '3':
        if input("1- Show File names""\n""2- Enter new File names""\n""> ") == '1':
            print(csv_input)
            print(csv_output)
        else:
            csv_input = input("Please enter your CSV file name""\n""> ")
            csv_output = input("Please enter the name that you want to save CSV result file as""\n""> ")
    elif inp == '4':
        if input("1- Show classification data and Text Data column""\n""2- Enter new classification data and Text Data column""\n""> ") == '1':
            print(class_clo)
            print(content_clo)
        else:
            class_clo = input("Please enter column name from input CSV file that have classification data on it ""\n""IF there is no classification column just enter number 0""\n""> ")
            content_clo = input("Please enter column name from input CSV file that have Text Data on it""\n""There should be some column like that so find it first""\n""> ")
    elif inp == '6':
        break
    elif inp == '5':
        print("Author: RmmRlAb""\n""With this mini app you can scan amount of data for finding a special words""\n" "and expressions in sentences as CSV file and mark the word done in every sentence""\n""for this you have to config some setings thru menu""\n""if your data hase been classified for being scaned or not you can add the premission in app in menu 4""\n")
        
    elif inp == '0':
        print("Running...")
        if not class_clo == '0':
            comp_classed()
        else:
            comp_noclass()
    else:
        continue          