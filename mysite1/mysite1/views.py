from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render


def test_01(request):
    return HttpResponse("test_01")


def test_02(request):
    return HttpResponse("test_02")


def test_03(request):
    return HttpResponse("test_03")


def index_view(request):
    return render(request,"index.html")
    # print(request.path_info)
    # return HttpResponse("index")


def calc_view(request, num1, mo, num2):
    if mo not in ["add", "sub", "mul"]:
        return HttpResponse("your mo is wrong")
    if mo == "add":
        return HttpResponse(num1 + num2)
    elif mo == "sub":
        return HttpResponse(num1 - num2)
    elif mo == "mul":
        return HttpResponse(num1 * num2)


def birthday(request, yy, mm, dd):
    result = "{year}年{month}月{dd}日".format(year=yy, month=mm, dd=dd)
    # return HttpResponse(content="hhhh", content_type="text/css", status=200)
    return HttpResponse(result)


def request_content(request):
    """
    请求的request常用属性
    :param request:
    :return:
    """
    print(request.path_info)  # 请求路径
    print(request.method)  # 请求路径
    print(request.GET)  # 返回GET的的query string的字符串的内容，类字典
    print(request.get_full_path())  # 和path_info不同，get_full_path会把后面的请求参数都获取到
    print(request.GET.getlist("a"))  # /request_content?a=10&a=100,相同的KEY
    print(request.META)
    print(request.META.get("REMOTE_ADDR"))
    # return HttpResponse("hh")
    return HttpResponseRedirect("/test/1")


HTML_CONTENT = """
<form method="post" action="/post_content">
    用户名：<input type="text" name="uname">
    <input type="submit" value="提交">
</form>


"""


def post_content(request):
    if request.method == "GET":
        return HttpResponse(HTML_CONTENT)
    elif request.method == "POST":
        print(request.POST.get("uname"))
        return HttpResponse("post哈哈哈")


# 模板调用
def html_render(request):
    name_info = {
        "str": "zz",
        "int": 18,
        "list": ["男", "女"],
        "dict": {"a": 1, "b": 2},
        "func": func,
        "object": MyR()
    }
    return render(request, "test_html.html", name_info)


def func():
    return "我是func"


class MyR:
    def club_func(self):
        return "我是方法club_func"


def my_calc(request):
    if request.method == "GET":
        return render(request, "my_calc_html.html")
    if request.method == "POST":
        op = request.POST.get("op", None)
        x = int(request.POST.get("x", None))
        y = int(request.POST.get("y", None))
        result = 0
        if op == "add":
            result = x + y
        elif op == "sub":
            result = x - y
        elif op == "mul":
            result = x * y
        elif op == "div":
            result = x / y
        return render(request, "my_calc_html.html", locals())


def my_news(request):
    from django.shortcuts import reverse
    from django.shortcuts import redirect
    url = reverse("my_music")
    # return redirect(url)  #重定向

    return HttpResponseRedirect(url)
    # return render(request, "base_html.html")


# if request.path_info == "music.html":
#     return render(request, "music.html")
# if request.path_info == "/sport.html":
#     return render(request, "sport.html")


def my_music(request):
    return render(request, "music.html")


def my_sport(request):
    return render(request, "sport.html")


def test_static(request):
    return render(request, "test_static.html")
