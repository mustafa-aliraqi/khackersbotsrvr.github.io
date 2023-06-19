#pylint:disable=E0001
from keep_alive import keep_alive
import random
import samino   #الدالة الي سويتها تحت هي الي طلعت اخطاء؟
import requests
import wikipedia
import os
import gtts
import time  
from PIL import Image
import seclibb
from bs4 import BeautifulSoup as S
import akinator
aki = akinator.Akinator()
from threading import Thread
keep_alive()
admin = "25f8186c-d5a6-4364-9ed3-d65d029517df"

client = samino.Client(trace=True) # الا
client.login("alkhacker8@gmail.com","error91283h")
print("bot is ready")
@client.event("on_text_message")
def test(data: samino.lib.Event):
    msg = data.message.content
    nickname = data.message.author.nickname
    userid = data.message.author.userId
    chatid = data.message.chatId
    comid = data.comId
    msgid= data.message.messageId
    rmsg = data.message.replyMessage.content
    rmsgid = data.message.replyMessage.messageId


    
    local = samino.Local(comid)
    coh = local.get_chat_info(chatid).coHosts
    h = local.get_chat_info(chatid).author.userId
  
  
    mention = str(data.message.mentionUserIds)
    mention = mention.replace("'","")
    mention = mention.replace("[","")
    mention = mention.replace("]","")
    local.activate_status()
    
    if userid=="f30f4c1b-6cfe-4153-86e4-a822a525460c":
        client.close()
        client.launch()
    for sb in open("sb.txt"):
        if sb in msg.split():
        	local.send_message(chatId=chatid,message="ممنوع السب يا قذر",replyTo=msgid)
        	try:
        		local.kick(chatId=chatid,userId=userid)
        		local.delete_message(chatId=chatid,messageId=msgid)
        	except:pass
        	
    if msg.startswith("*inv"):
        if userid in coh or userid == h or userid==admin:
            chats = local.get_online_users(size=100).userId
            local.start_chat(chats,"تعالو",msg[5:])
            for chat in chats:
                local.start_chat(chat,message=msg[5:])
      
    if msg=="*islam":
        local.send_message(chatid,"[B]الادوات \n\n*quran [page] = ارسال صفحة محددة من القرآن\n*rqp = ارسال صفحة عشوائية من القرآن \n  \n\n\nالبوت جاسم",replyTo=msgid)
  
    if msg.startswith("*ship"):
        if msg=="*ship":
            pass
        else:
            ship = random.randint(0,100)
            if ship<50:
                lop = f"مقدار التوافق\n{ship}%\n\nلايبدو لي انكم اصدقاء😔"
                local.send_message(chatid,lop,replyTo=msgid)
            else:
                lop = f"مقدار التوافق\n{ship}%\n\nاضن انكم اصدقاء منذ مدة طويلة🙄"
                local.send_message(chatid,lop,replyTo=msgid)
  
    if msg.startswith("*search"):
      	seer=msg.replace('*search','')
      	url = f"https://www.google.com/search?q={seer}"
      	r = requests.get(url)
      	soup = S(r.text, 'html.parser')
      	a = soup.find('div', class_='BNeawe').text
      	local.send_message( chatid,message=a)

    if msg.startswith("*rqp"):
        page = random.randint(0,604)
        response = requests.get(f"https://quran-images-api.herokuapp.com/show/page/{page}")
        file = open("hew.png","wb")
        file.write(response.content)
        file.close()
        local.send_message(chatid,"صفحة رقم {page}")
        local.send_message(chatid,fileType="image",file=open("hew.png","rb"))
        os.remove("hew.png")

    if msg.startswith("*fp"):
        local.comment("🕛بصمة",userid)


    if msg.startswith("*quran"):
        page = str(msg[7:])
        response = requests.get(f"https://quran-images-api.herokuapp.com/show/page/{page}")
        file = open("iii.png", "wb")
        file.write(response.content)
        file.close()
        local.send_message(chatid,"d",fileType="image",file=open("iii.png","rb"))
        os.remove("iii.png")

    if msg.startswith("*invite"):
        if userid in coh or userid==h:
            link = msg[8:]   
            aaa = client.get_from_link(link).objectId
            local.invite_to_chat(aaa,chatid)
            local.send_message(chatid,"[B]تمت الدعوة",replyTo=msgid)

    if msg.startswith("*fix"):
        if userid.admin:
            local.post_blog("البوت جاسم تحت الصيانة","لايمكنك استخدام جاسم الان يمكنك استخدام جاسم بعد الصيانة")
            local.send_message(chatid,"[B]تم",replyTo=msgid)
        else:
            pass
  
    if msg.startswith("*wiki"):
        lang = "ar"
        se = str(msg[6:])
        wikipedia.set_lang(lang)
        a = wikipedia.summary(se,sentences=2)
        local.send_message(chatid,a, embedTitle=f"{se}",embedType=0)

    if msg.startswith("*kick"):
        if userid==h or userid in coh or userid==admin:
            if msg[6:].startswith("http"):
                sdj=client.get_from_link(msg[6:]).objectId
                local.kick(chatid,sdj,False)
            else:
                local.kick(chatid,mention,False)

        
  
    if msg.startswith("*say"):
        txt = msg[5:]
        lang = "ar"
        name="i.mp3"
        gtts.gTTS(text=txt,lang=lang,slow=False).save(name)    
        local.send_message(chatid,file=open(name,"rb"),fileType="audio")
        os.remove(name)


    if msg.startswith("*buff"):
        response = requests.get(data.message.author.icon)
        file = open("e.png", "wb")
        file.write(response.content)
        file.close()
        img1 = Image.open(r"m.webp")
        img2 = Image.open(r""+'e.png')
        img2 = img2.resize((125, 125))
        img1.paste(img2, (120,90))
        img1.save("run.jpg")
        local.send_message(chatid,file=open('run.jpg', "rb"),fileType="image")
        os.remove("e.jpg")
        os.remove("run.jpg")

    if msg.startswith("جاسم"):
        local.send_message(chatid,random.choice(['مرحبا',"هلا","ها","عيون جاسم"]), replyTo=data.message.messageId)


    if msg.startswith("*RAEM"):
        if userid in coh or userid==h:
            m = seclibb.seclibb().generate_email()
            local.send_message(chatid,f"[B]{m} ",embedType=0,embedTitle="الايميل",replyTo=data.message.messageId)
        else:
            local.send_message(chatid,"ليست لديك الصلاحيه لهذا الامر",replyTo=data.message.messageId)

    if "http" in msg or "https" in msg:


        if "http://aminoapps.com" in msg:
            msg1 = " "+ msg + " "
            msg1 = msg1.replace(" ","***")
            msg1 = msg1[msg1.index("***http:"):][3:]
            msg1 = msg1[0: msg1.index("*")]
            ccc=client.get_from_link(msg1).comId
            if ccc==data.comId:
                pass
            elif userid in coh or userid==h or userid==admin:
                pass
            else:
                local.send_message(chatid,"ممنوع الروابط",replyTo=msgid)
                local.delete_message(chatid, msgid)
                local.kick(chatid,userid,False)

        elif userid in coh or userid==h or userid==admin:
            pass
        else:
            local.send_message(chatid,"ممنوع الروابط",replyTo=msgid)
            local.delete_message(chatid,msgid)
            local.kick(chatid,userid,False)
            


    if msg.startswith("*join"):
        link = msg[6:]
        if userid==admin:
            kws=client.get_from_link(link).objectId
            local.join_chat(kws)
            local.send_message(chatid,"[B]تم",replyTo=msgid)
        else:
            pass



    if msg.startswith("*kill"):
        link4 = msg[6:]
        if link4.startswith('https'):
            aaa = client.get_from_link(link4).objectId
            infoo2 = local.get_user_info(aaa)
            response = requests.get(data.message.author.icon)
            file = open("killer.png", "wb")
            file.write(response.content)
            file.close()
            response2 = requests.get(infoo2.icon)
            file2 = open("dead.png", "wb")
            file2.write(response2.content)
            file2.close()
            img1 = Image.open(r"sus.jpg")
            img2 = Image.open(r""+'killer.png')
            img3 = Image.open(r""+'dead.png')
            img2 = img2.resize((160, 160))
            img3 = img3.resize((160,160))
            img1.paste(img2, (128,220))
            img1.paste(img3, (578,280))
            img1.save("run2.jpg")
            local.send_message(chatid,file=open("run2.jpg","rb"), fileType="image")
            os.remove("run2.png")
            os.remove('killer.png')
            os.remove("dead.png")
        else:    
            infoo2 = local.get_user_info(mention)        
            response = requests.get(data.message.author.icon)        
            file = open("killer.png", "wb")        
            file.write(response.content)        
            file.close()        
            response2 = requests.get(infoo2.icon)        
            file2 = open("dead.png", "wb")        
            file2.write(response2.content)        
            file2.close()        
            img1 = Image.open(r"sus.jpg")        
            img2 = Image.open(r""+'killer.png')        
            img3 = Image.open(r""+'dead.png')        
            img2 = img2.resize((160, 160))        
            img3 = img3.resize((160,160))        
            img1.paste(img2, (128,220))        
            img1.paste(img3, (578,280))        
            img1.save("run2.jpg")        
            local.send_message(chatid,file=open("run2.jpg","rb"), fileType="image")       
            os.remove("run2.png")        
            os.remove('killer.png')        
            os.remove("dead.png")

    if msg.startswith("*msg"):
        local.send_message(chatid,msg[5:],replyTo=msgid)
  
    if msg.startswith("*del"):
        sss = int(msg[5:])
        if userid in coh or userid==h:
            msgs = local.get_chat_messages(chatid,sss).messageId
            for msgg in msgs:
                local.delete_message(chatid,msgg)
        else:
            pass
  
    if msg.startswith("*help"):
        local.send_message(chatid, "*islam = ادوات اسلامية\n*money = عرض عملة البوت\n*vip = عرض قائمة اوامر المشرفين\n*fun = عرض قائمه الالعاب\n\n\n\n[B]ميزات البوت \nطرد الشخص الذي يسب وحذف رسائل السب \nطرد الشخص الذي ينشر روابط وحذف روابطه\nالترحيب بالاعضاء الذين يدخلون الدردشه",replyTo=msgid)
      
        

    if msg.startswith('*fun'):
        local.send_message(chatid, "[B]الادوات\n*ship [link] = مقدار توافق بينك وبين شخص\n*kill [link] = ميمز مركب عليك قتل شخص في امونج اس \n*buff = ميمز مركب عليك تصبح مفتول العضلات \n*say [text] = البوت يقول كلمة من اختيارك \n*msg [text] = ارسال رسالة من اختيارك \n*wiki [text] = البحث في ويكيبيديا عن شي محدد\n*fp = وضع بصمة على بروفايلك",replyTo=data.message.messageId)


    if msg.startswith("*info"):
        link = msg[6:]
        if "@" in link:
            infoo = local.get_user_info(mention)            
            local.send_message(chatid, f"[B]UserId:  {mention}\n[B]nickname:  {infoo.nickname}\n[B]CreatedTime:  {infoo.createdTime}\n[B]Level:  {infoo.level}",replyTo=data.message.messageId)

        elif link=="me":
            infoo = local.get_user_info(userid)
            local.send_message(chatid,f"[B]UserId:  {userid}\n[B]nickname:  {nickname}\n[B]Created Time:  {infoo.createdTime}\n[B]Level:  {infoo.level}",replyTo=data.message.messageId)
        else:
            df = client.get_from_link(link).objectId            
            infoo = local.get_user_info(df)
            local.send_message(chatid, f"[B]UserId:  {df}\n[B]nickname:  {infoo.nickname}\n[B]CreatedTime:  {infoo.createdTime},\n[B]Level:  {infoo.level}",replyTo=data.message.messageId)

    if msg.startswith("*follow"):
        link = msg[8:]
        if link.startswith("http"):
            aoi = client.get_from_link(link).objectId
        else:
            aoi = mention
        if userid ==h or userid in coh:
            local.follow(aoi)
            local.send_message(chatid,"[B]تم",replyTo=msgid)
          
  
    if msg.startswith("*vip"):
        local.send_message(chatid,"[B]الاوامر\n*invite [link] = دعوة شخص مطرود\n*kick [link] = امر طرد شخص عن طريق منشن\n*info [link] = جلب اهم معلومات عن المستخدم \n*del [number] = حذف عدد رسايل محدد\n*fix = ارسال منشور الصيانة\n*join [link] = جعل البوت يدخل دردشة محدده\n*follow [link] = جعل البوت يتابع شخص\n*RAEM = ارسال ايميل عشوائي",replyTo=data.message.messageId)
        

@client.event("on_group_member_join")
def test2(data: samino.lib.Event):
    response = requests.get(data.message.author.icon)
    local = samino.Local(data.comId)
    file = open("i.png", "wb")
    file.write(response.content)
    file.close()
    local.send_message(data.message.chatId,"انضم عضو للدردشه",embedTitle=f"{data.message.author.nickname}",embedContent="اهلا بك في الدردشه",embedType=0,embedImage=open('i.png', "rb"))
    os.remove("i.png")
    if data.message.author.nickname == "mambll_1":
        local.kick(data.message.chatId, data.message.author.userId,False)

@client.event("on_group_member_leave")
def j(data: samino.lib.Event):
    local = samino.Local(data.comId)
    local.send_message(data.message.chatId,"غادر عضو الدردشه",embedTitle="عضو",embedContent="نتمنى ان نراك بالمرة القادمة",embedType=0)

@client.event("on_chat_tip")
def lol(data: samino.lib.Event):
    coins = data.message.tippingCoins
    local = samino.Local(data.comId)
    local.send_message(data.message.chatId,f"{data.message.author.nickname} شكرا على {coins}  قرش ")


client.launch()