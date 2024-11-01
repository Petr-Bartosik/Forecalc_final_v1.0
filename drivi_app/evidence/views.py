from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import DrevoZaznamForm
from .models import DrevoZaznam, WoodVolume
from .utils import najdi_objem
from django.contrib.auth.forms import UserCreationForm

# Úvodní stránka s aktuálním datem a časem
def uvodni_stranka(request):
    context = {
        'current_datetime': timezone.now(),
    }
    return render(request, 'evidence/uvodni_stranka.html', context)

# Registrace nového uživatele
def registrace(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Přesměrování po registraci na přihlašovací stránku
    else:
        form = UserCreationForm()
    return render(request, 'evidence/registrace.html', {'form': form})

# Zobrazení hlavního menu
@login_required
def menu(request):
    return render(request, 'evidence/menu.html')

# Vytvoření nového záznamu o dřevě
@login_required
def novy_zaznam(request):
    if request.method == 'POST':
        form = DrevoZaznamForm(request.POST)
        if form.is_valid():
            delka = form.cleaned_data['delka']
            prumer = form.cleaned_data['prumer']
            objem = najdi_objem(delka, prumer)
            if objem is not None:
                form.instance.objem = objem
                form.instance.user = request.user  # Přiřazení aktuálního přihlášeného uživatele
                form.save()
                return redirect('seznam_zaznamu')  # Přesměrování na seznam záznamů
            else:
                form.add_error(None, "Objem pro zadanou délku a průměr nebyl nalezen.")
    else:
        form = DrevoZaznamForm()
    return render(request, 'evidence/novy_zaznam.html', {'form': form})

# Zobrazení seznamu záznamů s celkovým objemem
@login_required
def seznam_zaznamu(request):
    zaznamy = DrevoZaznam.objects.filter(user=request.user)
    total_objem = sum(zaznam.objem for zaznam in zaznamy)
    return render(request, 'evidence/seznam_zaznamu.html', {'zaznamy': zaznamy, 'total_objem': total_objem})

# Úprava existujícího záznamu
@login_required
def upravit_zaznam(request, pk):
    zaznam = get_object_or_404(DrevoZaznam, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DrevoZaznamForm(request.POST, instance=zaznam)
        if form.is_valid():
            form.save()
            return redirect('seznam_zaznamu')
    else:
        form = DrevoZaznamForm(instance=zaznam)
    return render(request, 'evidence/upravit_zaznam.html', {'form': form})

# Smazání záznamu
@login_required
def smazat_zaznam(request, pk):
    zaznam = get_object_or_404(DrevoZaznam, pk=pk, user=request.user)
    if request.method == 'POST':
        zaznam.delete()
        return redirect('seznam_zaznamu')
    return render(request, 'evidence/smazat_zaznam.html', {'zaznam': zaznam})

# Zobrazení tabulky objemů
def volume_table(request):
    data = WoodVolume.objects.all()
    return render(request, 'evidence/volume_table.html', {'data': data})
