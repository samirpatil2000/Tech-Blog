from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.shortcuts import render, get_object_or_404,redirect
from django.template.loader import get_template

from.models import Post,Category,PostView
from django.views.generic import ListView , DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm,ContactForm


# Create your views here.



def get_category_count():
    queryset=Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset

def test(request):
    return render(request,'post_food/ds.html')
# def join_us(request):
#     return render(request,'post_food/join_us.html')

# add to your views
def join_us(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('post_food/contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Curiosity is Here" + '',
            ['samirspatil742099@gmail.com'],
            headers={'Reply-To': contact_email}
        )
        email.send()
        return redirect('join_us')

    return render(request, 'post_food/join_us.html', {
        'form': form_class,
    })

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'post_food/home.html',context )


def index(request):
    featured=Post.objects.all()[0:3]
    latest=Post.objects.order_by('-date_posted')[0:3]
    cat=Category.objects.all()
    context = {
        'object_list': featured,
        'latest': latest,
        'categories':cat,

    }

    return render(request, 'post_food/index.html', context)


def blog(request):
    featured = Post.objects.all()[0:3]
    category_count = get_category_count()
    cat=Category.objects.all().annotate(Count('title'))

    category_link=zip(category_count,cat)
   # print(category_count)
    posts_list=Post.objects.all()
    latest = Post.objects.order_by('-date_posted')[0:3]
    paginator=Paginator(posts_list,4)
    page_request_var='page'
    page=request.GET.get(page_request_var)
    try:
        paginated_queryset=paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except EmptyPage: # showing last page
        paginated_queryset=paginator.page(paginator.num_pages)

    context={
        'queryset':paginated_queryset ,
        'page_request_var':page_request_var,
        'latest': latest,
        'category_count':category_count,
        'object_list': featured,
        'categories':cat,
        'category_link':category_link,

    }
    return render(request,'post_food/blog.html' , context)

def post(request ,id):
    category_count = get_category_count()
    post=get_object_or_404(Post,id=id)
    latest = Post.objects.order_by('-date_posted')[0:3]

    if request.user.is_authenticated :
      PostView.objects.get_or_create(user=request.user,post=post)


    # form=CommentForm(request.POST or None)
    # if request.method=="POST":
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.instance.post=post
    #         form.save()
    #         return redirect(reverse('post-detail',kwargs={
    #             'id':post.id}))

    context={
        'latest': latest,
        'post':post,
        'category_count': category_count
    }


    return render(request,'post_food/post_detail.html',context)




class PostListView(ListView):
    model = Post
    template_name = 'post_food/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']



class UserPostListView(ListView):
    model = Post
    template_name = 'post_food/user_post.html'
                                           #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'

    def get_queryset(self):
        user= get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
#
#

class CategaryPostLisView(ListView):
    model=Post
    template_name = 'post_food/categories.html'
    context_object_name = 'posts'
    def get_queryset(self):
        cat=get_object_or_404(Category,id=self.kwargs.get('id'))
        return Post.objects.filter(categories=cat.id)

#


class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content','thumbnail','categories']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)



@login_required
def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST":

        if form.is_valid():
            form.instance.author = request.user
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('index')
    #     else:
    #         return render(request, 'post_food/post_form.html', {'form': form})
    # else:
    #     form = PostForm()
    return render(request, 'post_food/post_form.html', {'form': form})


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields = ['title','content','thumbnail','categories']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url = '/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
