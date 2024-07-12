from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Combo
from .forms import ComboForm

class ComboListView(View):
    def get(self, request):
        search_query = request.GET.get('q', '')
        if search_query:
            combos = Combo.objects.filter(combo_name__icontains=search_query)
        else:
            combos = Combo.objects.all()
        return render(request, 'combo/combo_list.html', {'combos': combos, 'search_query': search_query})

class ComboCreateView(View):
    def get(self, request):
        form = ComboForm()
        return render(request, 'combo/combo_form.html', {'form': form})

    def post(self, request):
        form = ComboForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('combo_list')
        return render(request, 'combo/combo_form.html', {'form': form})

class ComboUpdateView(View):
    def get(self, request, pk):
        combo = get_object_or_404(Combo, pk=pk)
        form = ComboForm(instance=combo)
        return render(request, 'combo/combo_form.html', {'form': form})

    def post(self, request, pk):
        combo = get_object_or_404(Combo, pk=pk)
        form = ComboForm(request.POST, request.FILES, instance=combo)
        if form.is_valid():
            form.save()
            return redirect('combo_list')
        return render(request, 'combo/combo_form.html', {'form': form})

class ComboDeleteView(View):
    def post(self, request, pk):
        combo = get_object_or_404(Combo, pk=pk)
        combo.delete()
        return redirect('combo_list')
