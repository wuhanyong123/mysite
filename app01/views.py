from django.shortcuts import render,redirect,HttpResponse
from app01 import models
# Create your views here.
#登陆函数
def login(request):
    error_msg=""
    if request.method == "POST":
        email=request.POST.get("email",None)
        pwd=request.POST.get("pwd",None)
        if email == "wuhanyong@yy.com" and pwd == "12345":
            return redirect("http://www.yy.com")
        else:
            error_msg="邮箱或密码错误"
    return render(request,"login.html",{"error":error_msg})
#展示所有用户信息
def user_list(request):
    #利用ORM工具查询数据库
    ret=models.UserInfo.objects.all()
    print(ret[0].id,ret[0].name)
    return render(request,"user_list.html",{"user_list":ret})
#添加用户
def add_user(request):
    error_msg=""
    if request.method == "POST":
        #用户提交post
        add_name=request.POST.get("username",None)
        if add_name:
            #数据库新增记录
            models.UserInfo.objects.create(name=add_name)
            return redirect("/user_list/")
        else:
            error_msg="出版社名字不能为空"
    return render(request, "add_user.html",{"error":error_msg})
#删除用户
def delete_user(request):
    #从get请求的参数中拿到数据id
    del_id=request.GET.get("id",None)
    if del_id:
        #根据id查找数据
        del_obj=models.UserInfo.objects.get(id=del_id)
        #删除
        del_obj.delete()
        return redirect("/user_list/")
    else:
        return HttpResponse("数据不存在")
#编辑用户名
def edit_user(request):
    #用户提交新名字，更新用户名
    if request.method == "POST":
        edit_id=request.POST.get("id")
        new_name=request.POST.get("username")
        edit_user=models.UserInfo.objects.get(id=edit_id)
        edit_user.name=new_name
        edit_user.save()
        #跳转到用户列表页
        return redirect("/user_list/")
    #从get请求获取id参数
    edit_id=request.GET.get("id")
    if edit_id:
        user_obj=models.UserInfo.objects.get(id=edit_id)
        return render(request, "edit_user.html",{"new_name":user_obj})
