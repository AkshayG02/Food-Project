from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Food

# Create your views here.
class Home_page(ListView):
    model= Food 
    context_object_name = 'foods'
    paginate_by = 4
    template_name= 'testapp/home.html'

    def get_queryset(self):
        return Food.objects.all().order_by('-created_at') 

class FoodList(ListView):
    model= Food

class AddFood(CreateView):
    model = Food
    fields = "__all__"

class FoodDetails(DetailView):
    model = Food
    
    
class FoodUpdate(UpdateView):
    model = Food
    fields = "__all__"

class FoodDelete(DeleteView):
    model = Food

    def get_success_url(self):
        return reverse('food_list')

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

class CustomLoginView(LoginView):
    template_name = 'testapp/login.html'

class CustomSignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'testapp/signup.html'
    success_url = reverse_lazy('login')  # Redirect to login after successful signup

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'testapp/home.html'

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect('login')



#  add to card
# Add to Cart View
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Food, CartItem

# ✅ Add to Cart View (POST method)

@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    def post(self, request, food_id):
        food = get_object_or_404(Food, id=food_id)
        quantity = int(request.POST.get('quantity', 1))  # Get quantity from form

        cart_item, created = CartItem.objects.get_or_create(user=request.user, food=food)

        if created:
            cart_item.quantity = quantity  # Set the new quantity if the item is new
        else:
            cart_item.quantity += quantity  # Increase quantity if item exists

        cart_item.save()

        messages.success(request, f"{quantity} x {food.name} added to cart!")
        return redirect('cart')  # Ensure 'cart' is correctly mapped in urls.py

# ✅ Cart Page View
@method_decorator(login_required, name='dispatch')
class CartView(View):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.total_price() for item in cart_items)
        return render(request, 'testapp/cart.html', {'cart_items': cart_items, 'total': total})

# ✅ Remove Item from Cart
@method_decorator(login_required, name='dispatch')
class RemoveFromCartView(View):
    def post(self, request, cart_item_id):
        cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
        cart_item.delete()
        messages.success(request, "Item removed from cart.")
        return redirect('cart')
    


#contact page

from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ContactForm

class ContactView(FormView):
    template_name = 'testapp/contact.html'  # Renders this template
    form_class = ContactForm  # Uses the ContactForm
    success_url = reverse_lazy('contact')  # Redirects after successful form submission

    def form_valid(self, form):
        # Process the form data (e.g., send an email or save to DB)
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        
        # You can add logic here (e.g., send email, save to DB, etc.)
        print(f"New Contact Message - Name: {name}, Email: {email}, Message: {message}")

        messages.success(self.request, "Your message has been sent successfully!")
        return super().form_valid(form)

