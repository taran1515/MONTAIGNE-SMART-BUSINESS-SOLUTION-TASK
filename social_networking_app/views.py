from django.shortcuts import render
from .models import Post,Comment,Profile,Plan
from .forms import PostForm,CommentForm,UserLoginForm,UserRegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def post_list(request):
    post = Post.objects.all()

    return render(request,'social_networking_app/post_list.html',{'post':post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            post= form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = PostForm()
    return render(request,'social_networking_app/post_create.html',{'form':form})

def post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    comments = Comment.objects.filter(post=post).order_by('-id')
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    if(request.method=='POST'):
        comment_form  = CommentForm(request.POST or None)
        if comment_form.is_valid():
            text = request.POST.get('text')
            comment = Comment.objects.create(post=post,user=request.user,text=text)
            comment.save()
            #return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
        'comments': comments,
        'comment_form': comment_form,
    }

    if request.is_ajax():
        html = render_to_string('social_networking_app/comment.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request,'social_networking_app/post_detail.html',{'post':post,
                                                                    'comments':comments,
                                                                    'comment_form':comment_form,
                                                                    'is_liked':is_liked,
                                                                    'total_likes':post.total_likes,})

def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    #post = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())





def user_login(request):
    if request.method =='POST':
        form =UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('post_list'))
                else:
                    return HttpResponse("User is not active")
            else:
                return HttpResponse("User is None")
    else:
        form = UserLoginForm()
        return render(request,'social_networking_app/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('register')

def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user =  form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect(post_list)
    else:
        form = UserRegistrationForm()
    return render(request,'social_networking_app/register.html',{'form':form})

def user_plan(request):
    if Plan.plan==1:
        maximum_comments=10
        return render(request,'social_networking_app/post_detail.html',{'maximum_comment':maximum_comment})
    elif Plan.plan==2:
        maximum_comments = 20
        return render(request, 'social_networking_app/post_detail.html', {'maximum_comment': maximum_comment})
    elif Plan.plan==3:
        maximum_comments = 30
        return render(request, 'social_networking_app/post_detail.html', {'maximum_comment': maximum_comment})
    else:
        return HttpResponse("Choose 1 of three Plans")



