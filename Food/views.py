from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from .models import Food
from .forms import FoodForm
from django.db.models import Q

class FoodListView(View):
    def get(self, request):
        query = request.GET.get('q')
        if query:
            foods = Food.objects.filter(Q(product_name__icontains=query))
        else:
            foods = Food.objects.all()

        in_stock = request.GET.get('in_stock')
        if in_stock == 'true':
            foods = foods.filter(quantity__gt=0)
        elif in_stock == 'false':
            foods = foods.filter(quantity__lte=0)

        return render(request, 'food/food_list.html', {'foods': foods})

class FoodCreateView(View):
    def get(self, request):
        form = FoodForm()
        return render(request, 'food/food_form.html', {'form': form})

    def post(self, request):
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food_list')
        return render(request, 'food/food_form.html', {'form': form})

class FoodUpdateView(View):
    def get(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        form = FoodForm(instance=food)
        return render(request, 'food/food_form.html', {'form': form})

    def post(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
        return render(request, 'food/food_form.html', {'form': form})

class FoodDeleteView(View):
    def get(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        return render(request, 'food/food_confirm_delete.html', {'food': food})

    def post(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        food.delete()
        return redirect('food_list')

