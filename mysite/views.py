# from django.shortcuts import HttpResponse,render,redirect
# def yimi(request):
#     #return HttpResponse('hello yimi!')
#     return render(request,"yimi.html")
# def xiaohei(request):
#     return HttpResponse('hello xiaohei!')
# def login(request):
#     error_msg=""
#     if request.method == "POST":
#         email=request.POST.get("email",None)
#         pwd=request.POST.get("pwd",None)
#         if email == "wuhanyong@yy.com" and pwd == "12345":
#             return redirect("http://www.yy.com")
#         else:
#             error_msg="邮箱或密码错误"
#     return render(request,"login.html",{"error":error_msg})
#
