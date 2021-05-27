from django.shortcuts import render, HttpResponse, reverse, redirect, HttpResponseRedirect
from bookstore.models import Book


def all_book(request):
    books = Book.objects.filter(is_delete__exact=False)
    # books = Book.objects.values()
    # books = Book.objects.values_list()
    # (1, 'python', Decimal('10.63'), '', '清华大学出版社', Decimal('63.98'), '')
    # print(books)
    return render(request, "bookstore/all_book.html", locals())


def update_book_view(request, book_id: int):
    try:
        book = Book.objects.get(id__exact=book_id, is_delete=False)
    except Exception as e:
        print("book_id id error %s" % e)
        return HttpResponse("书本不存在")

    if request.method == "GET":
        return render(request, "bookstore/update_info.html", locals())

    elif request.method == "POST":

        price = request.POST.get("price")
        market_price = request.POST.get("market_price")
        book.market_price = market_price
        book.price = price
        book.save()

        # return HttpResponse("修改成功")
        url = reverse(all_book)
        return redirect(url)


def delete_book(request):
    book_id = request.GET.get("id")[0]
    if not book_id:
        return HttpResponse("服务异常", status=500)
    try:
        delete_target_book = Book.objects.get(id__exact=book_id, is_delete=False)
        # delete_target_book.delete()
        delete_target_book.is_delete = True
        delete_target_book.save()
        return HttpResponseRedirect("/bookstore/all_book")

    except Exception as e:
        return HttpResponse("删除失败，书本不存在")
