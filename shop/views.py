from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from cart.forms import CartAddProductForm
from django.views import View
from blog.models import Blog
from django.core.mail import send_mail
import telebot
from .forms import ApplicationsForm
from django.views.generic import ListView
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# bot = telebot.TeleBot("1260971143:AAEVskAqdKb_rMMBfST-4WwQsqeOtNiu9Og")
bot = telebot.TeleBot("1344039009:AAHeFbFRHxLHNlmmTdXAZL1KHRr4QryxaRc")


def index(request):
    return render(request, 'shop/index.html')


def my_account(request):
	return render(request, 'shop/account.html')


def shopping(request):
	return render(request, 'cart/shopping-cart.html')


def checkout(request):
	return render(request, 'shop/checkout.html')


def contact(request):
    form = ApplicationsForm()
    return render(request, 'shop/contact.html', {'form': form})


def wishlist(request):
	return render(request, 'shop/wishlist.html')


def detail(request):
	return render(request, 'shop/product-details.html')


def shop(request):
    product = Product.objects.all()
    product_list = Product.objects.all()
    cart_product_form = CartAddProductForm()
    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 2)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'cart_product_form': cart_product_form,
                'producent': product,
                'products': products,
    }
    return render(request, 'shop/shop.html', context)


def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog.html', context)

class ApplicationsView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ApplicationsForm(request.POST)
            print(request.POST)
        if form.is_valid():
            form.save()
            mail = form.cleaned_data['mail']
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            subject = 'Новая заявка!'
            from_email = 'umutmarishbekova@gmail.com'
            to_email = ['ymyt.91@mail.ru', 'umutmamyrgazieva@gmail.com']
            message = 'Новая заявка!' + '\r\n' + '\r\n' + 'Почта: ' + mail + '\r\n' + '\r\n' + 'Имя: ' + name + '\r\n' + 'Коммент: ' + comment
            send_mail(subject, message, from_email, to_email, fail_silently=False)
            bot.send_message(569589994, message)
            # print(message)
        return redirect('shop:contact')

            # -481287996



class SearchResultsView(ListView):
    model = Product
    template_name = 'shop/search_results.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        )
        return object_list



class ShopListView(ListView):

    context_object_name = 'products'
    paginate_by = 10
    template_name = 'shop/shop.html'
    queryset = Product.objects.all()