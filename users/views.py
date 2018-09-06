from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden" name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    # 当请求为POST时，才认为是提交了注册信息
    if request.method == 'POST':

        # request.POST 即提交的信息，一个类字典的数据结构
        # 实例化一个form
        form = RegisterForm(request.POST)

        # 验证form数据合法性
        if form.is_valid():
            # 保存用户数据
            form.save()

            if redirect_to:
                return redirect(redirect_to)
            else:
                # 注册成功，返回首页
                return redirect('/')

    else:
        # 请求不是POST，说明是在访问注册页面
        form = RegisterForm()
    return render(request, 'users/register.html', context={'form': form})



""" 模板
def form_process_view(request):
    if request.method == 'POST':
        # 请求为 POST，利用用户提交的数据构造一个绑定了数据的表单
        form = Form(request.POST)

        if form.is_valid():
            # 表单数据合法
            # 进行其它处理...
            # 跳转
            return redirect('/')
    else:
        # 请求不是 POST，构造一个空表单
        form = Form()

    # 渲染模板
    # 如果不是 POST 请求，则渲染的是一个空的表单
    # 如果用户通过表单提交数据，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'template.html', context={'form': form})
"""