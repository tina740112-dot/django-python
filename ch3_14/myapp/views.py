from django.shortcuts import render
from django.http import HttpResponse

def set_cookie(request, key, value):
    # print(f"Setting cookie: {key} = {value}")
    response = HttpResponse("Cookie set")
    response.set_cookie(key, value)
    return response

def get_cookie(request, key):
    if key in request.COOKIES:
        return HttpResponse(f"Cookie value: {request.COOKIES[key]}")
    else:
        return HttpResponse("Cookie not found")

def get_all_cookies(request):
    if request.COOKIES!=None:
        strcookies=""
        for key1,value1 in request.COOKIES.items():
            strcookies= strcookies + key1 + ":" + value1 + "<br>"
        # return HttpResponse('%s' %(strcookies))
        return HttpResponse(f"{strcookies}")
    else:
        return HttpResponse('Cookie 不存在!')	

def set_cookie2(request,key=None,value=None):
    response = HttpResponse('Cookie 有效時間1小時!')
    response.set_cookie(key,value,max_age=3600)
    return response		

def delete_cookie(request,key=None):
    if key in request.COOKIES:
        response = HttpResponse('Delete Cookie: '+key)	
        response.delete_cookie(key)
        return response
    else:
        return HttpResponse('No cookies:' + key)	
import datetime
def index(request):
    if "counter" in request.COOKIES:
        counter = int(request.COOKIES["counter"])
        counter += 1
    else:
        counter = 1
    response = render(request, "index.html", locals())

    #設定counter變數到期時間，
    tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1) #取得現在日期時間再將日期加1日
    # print(tomorrow) #2021-06-12 11:06:01.667359
    tomorrow = datetime.datetime.replace(tomorrow, hour=0, minute=0, second=0) #設定時分秒為0:0:0
    # print(tomorrow) #2021-06-12 00:00:00.087386
    expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT")#利用strftime函式將日期換成指定的格式
    response.set_cookie("counter",counter,expires=expires)#以expires參數設定到期時間
    return response

def set_session(request,key=None,value=None):
    request.session[key]=value
    return HttpResponse('Session 儲存完畢!')

def get_session(request,key=None):
    if key in request.session:
        return HttpResponse(f"{key}:{request.session[key]}")
    else:
        return HttpResponse('Session 不存在!')

def delete_session(request,key=None):
    if key in request.session:
        response = HttpResponse('Delete Session: '+key)	
        del request.session[key]
        return response
    else:
        return HttpResponse('No Session:' + key)

def vote(request):
    #print(request.session.items()) #check
    if not "vote" in request.session:
        request.session["vote"]=True
        msg="您第一次投票!"		
    else:		
        msg="您已投過票!"	

    return HttpResponse(msg)	

def set_session2(request, key=None, value=None):

    # 判斷 key 是否為空
    if key is None:
        return HttpResponse("Key 不可為空")

    # 將資料存入 Session
    # key = Session 名稱
    # value = Session 值
    request.session[key] = value

    # 設定 Session 過期時間為 10 秒
    # 10 秒後 Session 會自動失效
    request.session.set_expiry(10)

    # 回傳成功訊息
    return HttpResponse("Session 儲存完畢!")

# Django Messages 框架：
# ✔ 用來在不同頁面之間傳遞一次性訊息
# ✔ 自動儲存在 session
# ✔ 五種訊息類型 success/info/warning/error/debug
# ✔ HTML 使用 {% for msg in messages %} 顯示
# ✔ 顯示後會自動刪除
# ✔ 不需要自己傳遞 message 變數
# 不適合 messages 的場景:
# 長時間顯示狀態（例如 navbar 右上角的登入使用者）
# 需要在同一頁即時更新（建議用 AJAX 直接顯示）
# messages 只適合「說完就消失」的訊息，像「登入成功」「註冊完成」

from django.contrib import messages
def login(request):
    if request.session.get("username") == "admin":
        return render(request, "login.html", {"status": True})
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(f"username: {username}, password: {password}") 
        if username == "admin" and password == "12345":
            request.session["username"] = username
            messages.success(request, f"{username}您好，登入成功!")
            return render(request, "login.html", {"status": True})
            # return HttpResponse("登入成功!")
        else:
            messages.error(request, "帳號或密碼錯誤!")
            # return HttpResponse("登入失敗!")
            return render(request, "login.html", {"status": False})
        # return HttpResponse("已送出")
    else:
        return render(request, "login.html", {"status": False})

from django.shortcuts import redirect
def logout(request):
    if "username" in request.session:
        del request.session["username"]
        messages.info(request, "您已成功登出!")
    return redirect("login")