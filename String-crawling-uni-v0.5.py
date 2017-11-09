import csv
import string

#thease are first and default values for program that written down for finding spams in youtube comments.
#do not change two string at first.
smpl = ['Regular expression', 'ClassificatioN', 'cahnnel:', 'sub', 'subscribe', 'suscribe', 'leave', 'message', 'like', 'comment', 'comment', 'please', 'please message', 'channle', 'tube', '{tube}', 'you[tube]', '(tube)', '{youtube}', '[youtube]', '(youtube)', 'youtube/', 'yt', 'http:', 'https:', 'watch?', '//', 'check', 'out', 'leave', 'my', 'check', 'youtube', '.com', 'com', '.net', 'net', '.org', 'org', '.tv', 'tv', '.me', 'me', '.co', 'co', 'website', 'blog', 'video', 'follow', 't-shirts', 'v-necks', 'accessories', 'visit', 'gift', 'card', 'giftcard', 'on', 'twitter', 'facebook', 'youtube', 'omel', 'kick', 'instakgram', '@', 'search' , 'ig', 'fb', 'gc', 'tw']
regexp = ['http', 'watch', '//', 'com', 'net', 'org', 'tv', 'me', 'co', '@', 'tube']
#other default values 
csv_input = 'Empty'
csv_output = 'Empty'
class_clo = 'Empty'
content_clo = 'Empty'
class_clo = ''

def comp_classed(wordlist):
    #the fucntion that use for classified data 
    spam = []
    respam = []
    smpl2 = wordlist + regexp 
    with open(csv_input, newline='', encoding='utf-8') as csvrw:
        with open(csv_output, 'w', newline='\n') as csvwr:
            spamwriter = csv.writer(csvwr, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(smpl2)
            reader = csv.DictReader(csvrw)
            for row in reader:
                #class_clo is Classification coluwn
                if row[class_clo] == '1':
                    string_low = row[content_clo].lower()
                    string_list = string_low.split(' ')        
                    for sp in smpl:
                        if sp in string_list:
                            spam.append('1')
                        else:
                            spam.append('0')
                    #this part checking the word for finding Regular expressions 
                    spam[0] = '0'
                    for re in regexp:
                        if not string_low.find(re) == -1:
                             respam.append('1')
                             spam[0] = '1'
                        else:
                            respam.append('0')
                    spam = spam + respam
                    spamwriter = csv.writer(csvwr, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(spam)
                    spam = []
                    respam = []
            print("The job has been finished and {} has been created".format(csv_output))
            csv_output.close()
            csv_input.close()

def comp_noclass(wordlist):
    #this funtion will use for non classified data
    spam = []
    respam = []
    smpl2 = wordlist + regexp 
    with open(csv_input, newline='', encoding='utf-8') as csvrw:
        with open(csv_output, 'w', newline='\n') as csvwr:
            spamwriter = csv.writer(csvwr, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(smpl2)
            reader = csv.DictReader(csvrw)
            for row in reader:
                string_low = row[content_clo].lower()
                string_list = string_low.split(' ')        
                for sp in smpl:
                    if sp in string_list:
                        spam.append('1')
                    else:
                        spam.append('0')
                spam[0] = '0'
                for re in regexp:
                    if not string_low.find(re) == -1:
                        respam.append('1')
                        spam[0] = '1'
                    else:
                        respam.append('0')
                spam = spam + respam
                spamwriter = csv.writer(csvwr, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(spam)
                spam = []
                respam = []
            print("The job has been finished and {} has been created".format(csv_output))
            csv_output.close()
            csv_input.close()

def comp_classing(wordlist):
    #this baby will use for non classified data and do the classification for you
    spam = []
    respam = []
    smpl2 = wordlist + regexp 
    with open(csv_input, newline='', encoding='utf-8') as csvrw:
        with open(csv_output, 'w', newline='\n') as csvwr:
            spamwriter = csv.writer(csvwr, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(smpl2)
            reader = csv.DictReader(csvrw)
            for row in reader:
                string_low = row[content_clo].lower()
                string_list = string_low.split(' ')        
                for sp in smpl:
                    if sp in string_list:
                        spam.append('1')
                        spam[1] = '1'
                    else:
                        spam.append('0')
                for re in regexp:
                    if not string_low.find(re) == -1:
                        respam.append('1')
                        spam[0] = '1'
                        spam[1] = '1'
                    else:
                        respam.append('0')
                spam = spam + respam
                spamwriter = csv.writer(csvwr, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(spam)
                spam = []
                respam = []
            print("The job has been finished and {} has been created".format(csv_output))
            csv_output.close()
            csv_input.close()
        
while True:
    #and finaly this loop will keep app going and get inputs from user for the job
    print("----------------------------------------------------------------------------------------------------------")
    inp = input("String crawling V0.4""\n""0- Run String Crawling""\n""1- Run String Crawling with Classification""\n""2- Word samples""\n""3- Regular expressions""\n""4- File names""\n""5- Column setings""\n""6- help""\n""7- Exit""\n""> ")
    if inp == '2':
        if input("1- Show Word samples""\n""2- Enter new Word samples""\n""> ") == '1':
            print(smpl)
        else:
            print("Enter done when you done....""\n""> ")
            smpl = ['Regular expression', 'ClassificatioN']
            while True:
                new_smpl = input()
                if new_smpl == "done":
                    break
                smpl.append(new_smpl)
                continue
    elif inp == '3':
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
    elif inp == '4':
        if input("1- Show File names""\n""2- Enter new File names""\n""> ") == '2':
            csv_input = input("Please enter your CSV file name""\n""> ")
            csv_output = input("Please enter the name that you want to save CSV result file as""\n""> ")
        else:
            print("Input File: ", csv_input)
            print("\n", "Output File: ", csv_output)
    elif inp == '5':
        if input("1- Show classification data and Text Data column""\n""2- Enter new classification data and Text Data column""\n""> ") == '2':
            class_clo = input("Please enter column name from input CSV file that have classification data on it ""\n""IF there is no classification column just leave it empty and press Enter""\n""> ")
            content_clo = input("Please enter column name from input CSV file that have Text Data on it""\n""There should be some column like that so find it first""\n""> ")
        else:
            print("Classification column: ", class_clo)
            print("\n", "Text column: ", content_clo)
    elif inp == '7':
        break
    elif inp == '6':
        print("Author: RlabRmm""\n""With this mini app you can scan amount of data for finding a special words""\n" "and expressions in sentences as CSV file and mark the word done in every sentence""\n""for this you have to config some setings thru menu""\n""if your data hase been classified for being scaned or not you can add the premission in app in menu 4""\n")
    elif inp == '0':
        print("String Crawling is Running...""\n")
        if not class_clo == '':
            comp_classed(smpl)
        else:
            comp_noclass(smpl)
    elif inp == '1':
        print("String Crawling with Classification is Running...""\n")
        comp_classing(smpl)
    else:
        continue          
