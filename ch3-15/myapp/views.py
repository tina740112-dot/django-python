from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')
  
def useradd(request):
    if request.method == 'POST':
        # 在這裡處理表單提交的邏輯
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        birthday = request.POST.get('birthday')
        print(f'username: {username}, password: {password}', 
              f'repassword: {repassword}, phone: {phone}',
              f'email: {email}, birthday: {birthday}')
        
        from django.contrib.auth import get_user_model
        from django.contrib import messages
        User=get_user_model()
        if User.objects.filter(username=username).exists():
          messages.error(request, "帳號已存在")
          return render(request, 'useradd.html')
        # 如果帳號不存在，繼續處理其他邏輯
        if password != repassword:
            messages.error(request, "密碼與確認密碼不一致")
            return render(request, 'useradd.html')

        # 如果驗證通過，將資料存入資料庫（此處省略具體實現）
        # 然後可以重定向到其他頁面，例如登入頁面
        user=User.objects.create_user(
          username=username, 
          password=password, 
          email=email, 
          tel=phone, 
          cBirthday=birthday
          )
        
        user.is_active = True
        user.is_staff = False
        user.save()
        messages.success(request, "使用者已成功建立")
        return render('/userlogin/')
       
      
      
    else:
        return render(request, 'useradd.html')
      
from django.contrib.auth import authenticate,login,logout

def userlogin(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      
      return redirect('/index/')
    else:

      messages.error(request, "使用者登入未成功，表單提交失敗")
      return render(request, 'userlogin.html')
  else:
    return render(request, 'userlogin.html')

        
def userlogout(request):
    logout(request)
    messages.success(request, "使用者已成功登出")
    return redirect('/index/')
  
def page1(request):
    return render(request, 'page1.html')
 