from textblob import TextBlob
import json
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def cleaner(data):
    if 'content' in data.keys(): return True

str1=open('facebook-sumukhbharadwaj96/messages/inbox/zainabmuskaan_eg52kh7poq/message_1.json').read()
#csv_file=open('analyser.csv','a')
data=json.loads(str1)
persons=data['participants']
person1=persons[0]['name']
person2=persons[1]['name']
count1=0
count2=0
msgData=data['messages']

for i in msgData:
    if cleaner(i)==True:
        msg=i['content']
        tb_msg=TextBlob(msg)
        if(i['sender_name']==person1): 
            score1=+tb_msg.sentiment.polarity
            count1=+1
            #csv_file.write(i['sender_name']+','+i['content']+','+str(score1)+'\n')
        else: 
            score2=+tb_msg.sentiment.polarity
            count2=+1
            #csv_file.write(i['sender_name']+','+i['content']+','+str(score2)+'\n')

print('Sentiment Analysis')
print('Polarity of '+person1+': '+str((score1/count1)*100))
print('Polarity of '+person2+': '+str((score2/count2)*100))
if score2<0: print('Verdict: You don\'t have a good relationship with this person.')
elif score2>0: print('Verdict: You have a good relationship with this person.') 
else: pass