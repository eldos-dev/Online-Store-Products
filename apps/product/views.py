from django.http import Http404
from django.views.generic import ListView, DetailView

from .models import Product, Category


class HomePageView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'product/index.html'


class ProductsListView(ListView):
    model = Product
    template_name = 'product/products_list.html'
    context_object_name = 'products'

    # def get(self, request, category_slug):
    #     if not Category.objects.filter(slug=category_slug).exists():
    #         raise Http404('Нет такой категории')
    #     products = self.get_queryset().filter(category_id=category_slug)
    #     context = {
    #         'products': products
    #     }
    #     return render(request, 'product/products_list.html', context)

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if not Category.objects.filter(slug=category_slug).exists():
            raise Http404('Нет такой категории')
        queryset = queryset.filter(category_id=category_slug)
        return queryset

class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_details.html'



















#TODO: переписать вьюшку products list +
#TODO: Подключить картинки для товаров +
#TODO: Добавить детали продукта   + product_details
#TODO: Сделать переход из категории в листинг продуктов +
#TODO: переписать вьюшки на CBV

# =======================================================================================================================================
# def index(request):
#     categories = Category.objects.all()
#
#     context = {
#         'categories': categories
#     }
#     return render(request, 'product/index.html', context)


    # class ProductsListView(View):
    #     def get(self, request, category_slug):
    #         if not Category.objects.filter(slug=category_slug).exists():
    #             raise Http404('Нет такой категории')
    #         products = Product.objects.filter(category_id=category_slug)
    #         context = {
    #             'products': products
    #         }
    #         return render(request, 'product/products_list.html', context)


#
# def products_list(request, category_slug):
#     if not Category.objects.filter(slug=category_slug).exists():
#         raise Http404('Нет такой категории')
#     products = Product.objects.filter(category_id=category_slug)
#     context = {
#         'products': products
#     }
#     return render(request, 'product/products_list.html', context)
#


# def products_list(request, category_slug):
#     products = get_list_or_404(Product, category_id=category_slug)
#     context = {
#         'products': products
#     }
#     return render(request, 'product/products_list.html', context)

# def product_details(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     context = {
#         'product': product
#     }
#     return render(request, 'product/product_details.html', context)


# Первый вариант. Вывода продуктов, которые относятся к определенному категории
#product/category
# def products_list(request, category_slug):

# First second
#     if not Category.objects.filter(slug=category_slug).exist():
#       raise Http404
#     products = Product.objects.filter(category_id=category_slug) # products - это query_set
#     # SELECT * FROM product WHERE category_id=category_slug

    # products = get_list_or_404(Product, category_id=category_slug)

# Second option При проверке если категории нету, то выводит ошибку функция get_object_or_404. Если еть он выводит все продукты этого категории
# Thrid option
#     category = get_object_or_404(Category, slug=category_slug)
#     products = Product.objects.filter(category=category)

    # context = {
    # 'products': products
    # }
    # return render(request, 'product/products_list.html', context)

# ---------------------------------------------------------------------------
# Second option                                                             |
# products/?category=slug                                                   |
# def products_list_1(request):                                             |
#     category_slug = request.GET.get('category') #GET - это словарь
#     products = Product.objects.all()                                      |
#     if category_slug is not None:                                         |
#         products = products.filter(category_id=category_slug)             |
#     context = {                                                           |
#     'products': products                                                  |
#     }                                                                     |
#     return render(request, '', context)                                   |
# ---------------------------------------------------------------------------



# ====================================================================================================================
# all() - Выводит все объекты модели.        -> SELECT * FROM table;
# filter() - фильтрует результаты запроса.   -> SELECT * FROM table WHERE ...;
# exclude(category=1) - исключает из результатов объектов, отвечающие условию.  -> SELECT * FROM table WHERE category != 1;
# order_by('-name') - это сортировка результатов запроса. SELECT * FROM table ORDER_BY name desc;
# reverse() - изменяет порядок обратный.
# distinct() - исключает повторения
# Product.objects.values_list('category').distinct()


# class ProductImage(models.Model): # Моедль нужен для того чтобы много картинок привизать к продукту
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='products', null=True, blank=True)
#
#     def get_image_url(self):
#         if self.image:
#             return self.image.url
#         return ''
