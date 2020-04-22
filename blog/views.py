from django.shortcuts import render,get_object_or_404
from .models import Post,bidding1,advertise
from users.models import Profile

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
from django.http import JsonResponse,HttpResponse
from django.http import HttpResponseRedirect

def payment(request):
        return HttpResponseRedirect("http://localhost/praneeth/PayUMoney_form.php")
def displayadd(request):
        a = request.GET['district']
        b=int(request.GET['category'])
        try:
            df=advertise.objects.get(district=a,category=b)
            #raises exception:
                # blog.models.DoesNotExist: advertise matching query does not exist.
                # So exception is handled properly
            fun="C:/Users/PRANEETH REDDY/geo-adv/"
            imgurl=fun+df.img.url
            print(imgurl)
            image_data = open(imgurl, "rb").read()
            return HttpResponse(image_data, content_type="image/png")
        except:
            fun="C:/Users/PRANEETH REDDY/geo-adv/"
            imgurl=fun+"/media/pics/default.jpg"
            image_data = open(imgurl, "rb").read()
            return HttpResponse(image_data, content_type="image/png")



def publisher(request):
    return render(request,'blog/publisher.html')
@login_required
def bid(request):
    if request.method == 'POST':
        instance=request.user
        amount=int(request.POST['amount'])
        y=Profile.objects.all().order_by('-bid')
        users=User.objects.all()
        daate=bidding1.objects.all()[:1].get()
        
        x=Profile.objects.get(user_id=instance.id)
        x.bid=amount
        x.save()
        y=Profile.objects.all().order_by('-bid')
        return render(request,'blog/bid.html',{'y':y,'users':users,'daate':daate})
    else:   
        y=Profile.objects.all()
        users=User.objects.all()
        daate=bidding1.objects.all()[:1].get()

        
        

        return render(request,'blog/bid.html',{'y':y,'daate':daate,})

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
#--------------------------(or)---------------------------------------
class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    #paginate_by=5


class UserPostListView(ListView):
    model=Post
    template_name='blog/users_posts.html'
    context_object_name='x'
    #paginate_by=5
    
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



#-------------------------------------------------------------------------
class PostDetailView(DetailView):
    model=Post
# detailview expects the id of post from url and grabs it.

class PostCreateView( LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
        #UserPassesTestMixin calls test_func to validate the post and logged in user.
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        return False
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class UserProfileView(DetailView):
    model=User
    slug_field="username"
    template_name="blog/user_detail.html"
