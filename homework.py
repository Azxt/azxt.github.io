import sys        

def fun_op(num):        
   
    
    if(num=="0"):
        print("您選擇離開，程式已結束")
        sys.exit()

    elif (num=="1"):
        print("執行BMI程式")
        s1h=float(input(f"請輸入{name} 身高cm :"))
        s1w=float(input(f"請輸入 {name} 體重kg :"))
        sh1=s1h/100
        BMI=s1w/pow(sh1,2)
        
        print(f"Hi,{name}你的BMI為 : "+str(round(BMI,2)))
    
    elif (num=="2"):
        print("執行華氏轉攝氏")
        print("請輸入攝氏C")
        c=float(input())
        f= 9/5 * c + 32  #華氏 =9/5*攝氏+32
        print("華氏 = ",round(f,2),"度F")
        
        print("======================")
        
        print("請輸入華氏F")
        f=float(input())
        C = (f- 32) * 5/9    #攝氏=(華氏-32)*5/9
        
        print("攝氏 = ",round(C,2),"度C")
    elif(num=="3"):
        print("執行加油提示系統")
        oil=eval(input("請輸入公升數 :\n"))
    
        while oil<20:
            total=str(20-oil)
            print(f"在加 {total} 公升可以選擇贈品！")    
            ch=input("您還要再加嗎? 1.繼續加 2.不加了\n")
            if (ch=="1"):
                oil += eval(input("請問您還要加幾公升 : "))
            else:
                break
        else:
            if(oil>=20):
                print("加滿20公升可以選擇贈品")
    elif (num=="4"):
        print("執行猜數字")
        num=30
        range_start=0
        range_end=0
        code=int(input("請猜一個數字 : "))
        while code != num:
            if(code>num):
                range_end=code-1
                print("猜小一點，目前範圍為 {} 到 {} ".format(range_start,range_end)) 
            elif(code<num):
                range_start=code+1
                print("猜大一點，目前範圍為 {} 到 {}".format(range_start,range_end))
                
            print("請輸入數字 {}-{} :".format(range_start,range_end))
            code=int(input())
        else:
            print("猜中了!!!")
    elif (num=="5"):
        print("執行記帳本")
        meal = 0
        transportation = 0
        rent = 0
        miscellaneous = 0
        
        while True:
            toe = int(input("請輸入生活支出 1.餐費 2.交通費 3.房租 4.雜支 5.結束並顯示總額: "))
            if (toe == 1):
                meal += int(input("請輸入餐費: "))
            elif (toe == 2):
                transportation += int(input("請輸入交通費: "))
            elif (toe == 3):
                rent += int(input("請輸入房租: "))
            elif (toe == 4):
                miscellaneous += int(input("請輸入雜支: "))
            elif (toe == 5):
                total = meal + transportation + rent + miscellaneous
                print("總共 " + str(total) + " 元")
                break
            else:
                print("請輸入 1~5")
    elif (num=="6"):
        print("執行ATM")
        balance = 10000  # 初始餘額
    
        while True:
            print("\n=== ATM 系統 ===")
            print("1. 查詢餘額")
            print("2. 存款")
            print("3. 提款")
            print("4. 離開")
    
            choice = input("請選擇 1-4: ")
    
            if choice == "1":
                print(f"目前餘額為 {balance} 元")
    
            elif choice == "2":
                deposit = int(input("請輸入存款金額: "))
                if deposit > 0:
                    balance += deposit
                    print(f"成功存入 {deposit} 元，目前餘額 {balance} 元")
                else:
                    print("存款金額必須大於 0")
    
            elif choice == "3":
                withdraw = int(input("請輸入提款金額: "))
                if withdraw <= balance and withdraw > 0:
                    balance -= withdraw
                    print(f"成功提取 {withdraw} 元，目前餘額 {balance} 元")
                else:
                    print("提款失敗，金額不足或輸入錯誤")
    
            elif choice == "4":
                print("感謝光臨，歡迎再次使用")
                break
    
            else:
                print("請輸入有效選項 (1-4)")
    elif (num=="7"):
        ticket_price = 50
        mun_tickets = int(input("請輸入您要購買的票數 : "))
        money_received = float(input("請輸入您投入的金額 : "))
        
        total_price = mun_tickets * ticket_price
        
        while money_received < total_price:
            short = total_price - money_received
            print(f"金額不足! 您還差 {short} 元")
            add_more = input("是否要補錢? (y/n): ")
            
            if add_more.lower() == "y":
                extra = float(input("請輸入補投的金額 : "))
                money_received += extra
            else:
                print("購票取消。")
                break
        
        if money_received >= total_price:
            change = money_received - total_price
            print(f"購票成功! 您的找零為 : {change} 元")
            
    elif (num=="8"):
        import datetime
        import random

        morning_quotes=[
            "早安!新的一天開始啦!",
            "今天又是努力的一天，加油!",
            "別賴床了，夢想不會自己實現",
            ]
        afternoon_quotes=[
            "午安~記得補充水份",
            "別讓自己太忙，也要喘口氣",
            "午覺時間到，讓腦袋休息一下",
            ]
        evening_quotes=[
            "晚安~今天也辛苦你了",
            "放下煩惱，好好睡一覺",
            "世界很安靜，該讓自己慢下來了",
            ]

        update_time = datetime.datetime.now()
        hour=update_time.hour
        print("現在時間 : ", update_time.strftime("%Y-%m-%d %H:%M"))

        if 5<=hour<12:
            message=random.choice(morning_quotes)
        elif 12<=hour<18:
            message=random.choice(afternoon_quotes)
        else:
            message=random.choice(evening_quotes)

        print(message)
            
    elif(num=="9"):
        import random
        print("歡迎來到 IQ小測驗!")
        print("系統將隨機出 5 道數學題，看你能答對幾題!\n")
        score=0
        question_count=5
        for i in range(1,question_count+1):
            a=random.randint(1,20)
            b=random.randint(1,20)
            op=random.choice(["+","-","*",])
            
            if op=="+":
                ans=a+b
            elif op=="-":
                ans=a-b
            else:
                ans=a*b
                
            print(f"第 {i} 題:{a} {op} {b}=?")
            user=input("你的答案 :")
            
            if not user.isdigit() and not (user.startswith("-") and user[1:].isdigit()):
                print("輸入錯誤 ! 這題不算分")
                continue
            
            user=int(user)
            
            if user==ans:
                print("答對了!\n")
                score+=1
            else:
                print(f"答錯了 ! 正確答案是{ans}\n")
                
        print("測驗結束!")
        print(f"你的得分 : {score}/{question_count}")

        if score==question_count:
            print("完美! 你是天才中的天才!")
        elif score>=3:
            print("不錯!，頭腦滿靈光的!")        
        else:
            print("多喝水，多睡覺，下次一定更好")

            
print("歡迎進入 , 請先登入")
account ="ABC123"
passworld="aa123"
name="John"
count=3
for x in range(count):
    count-=1;
    acc=input("請輸入帳號 :")
    pwd=input("請輸入密碼 :")
    if (acc == account) and (pwd == passworld):
        print("登入成功"+name+"你好")        
        break
    elif(acc == "")or(pwd == ""):
        print("您的帳號或密碼是空值")        
    elif(acc !=account):
        print("帳號錯誤")
    elif(pwd !=passworld):
        print("密碼錯誤")
        
    if (count==0):
        print("帳號已鎖定，請找管理員")
        sys.exit();
    else:
        print("帳號密碼錯誤,剩餘"+str(count)+"次機會，將鎖定帳號")  

running=True
while running:
           
    x=input("選擇您要執行的程式:\n 0.結束程式 1.計算BMI 2.華氏攝氏轉換 3.加油提示系統 4.猜數字 5.記帳本 6.ATM 7.自動購票機 8.早安晚安提醒 9.IQ小測驗\n")                  
    fun_op(x)
   
    
    
