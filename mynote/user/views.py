from hashlib import md5

from django.shortcuts import render, HttpResponse

from user.models import User


def reg_view(request):
    if request.method == "GET":
        return render(request, "user/register.html")

    elif request.method == "POST":

        """
        1、获取用户名
        2、查库，看看用户名是否存在
        3、存在提示已经注册
        4、不存在，入库，提示成功
        5、密码，两次一致
        """
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        pwd_confirm = request.POST.get("second_pwd")

        res = User.objects.filter(username=uname)  # 返回QuerySet
        if res.count() >= 1:
            # return render(request, "user/register.html")
            return HttpResponse("用户已经存在")
        elif res.count() < 1:
            if pwd == pwd_confirm:
                m = md5()
                m.update(pwd.encode())
                pwd = m.hexdigest()
                try:
                    user = res.create(username=uname, password=pwd)
                except Exception as e:
                    print("用户名已经注册 %s" % e)
                    return HttpResponse("用户已经存在")

                request.session["uname"] = uname
                request.session["uid"] = user.id
                return HttpResponse("注册成功")


            elif pwd != pwd_confirm:
                return HttpResponse("两次密码不一致")


def login_view(request):
    if request.method == "GET":
        return render(request, "user/login.html")

    elif request.method == 'POST':

        uname = request.POST.get("username")
        pwd = request.POST.get("password")

        # try:
        #     res = User.objects.get(username=uname, password=pwd_md5)
        #     if request.POST.get("select"):
        #         request.session["uname"] = uname
        #         request.session["id"] = res.id
        #     return HttpResponse("登录成功")
        # except Exception as e:
        #     return HttpResponse("登录失败%s" % e)
        try:
            res = User.objects.get(username=uname)
        except Exception as e:
            print("用户名不存在 %s" % e)
            return HttpResponse("用户名或密码不存在")
        m = md5()
        m.update(pwd.encode())
        pwd_md5 = m.hexdigest()
        if res.password != pwd_md5:
            return HttpResponse("用户名或密码不存在")

        request.session["uname"] = uname
        request.session["uid"] = res.id
        request.COOKIES.
        return HttpResponse("登录成功")


"""
hash密码：md5  sha-256

future：
1、定长输出，不管给的是什么，加密的密码都是定长输出。md5 是32位的16进制
2、不可逆，计算出后的结果，不能被破解。base64却是可以反破解
3、雪崩效益：只要明文密码修改了一点点，输出的结果都会全部重新计算，不会只计算修改的部分。
 场景：
 1、密码，通常会用hash进行计算
 2、文件的完整性校验。网络下载文件的时候，进行校验

"""
