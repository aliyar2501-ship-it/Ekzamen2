from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Ad, Comment
from .forms import AdForm, CommentForm


def register(request):
    """Отображает и обрабатывает форму регистрации нового пользователя."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ad_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def ad_list(request):
    """Отображает список всех объявлений с пагинацией (доступно только авторизованным)."""
    ads = Ad.objects.all()
    paginator = Paginator(ads, 6)  # По 6 объявлений на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'board/ad_list.html', {'page_obj': page_obj})


@login_required
def ad_detail(request, pk):
    """Отображает детали объявления и форму добавления комментария."""
    ad = get_object_or_404(Ad, pk=pk)
    comments = ad.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ad = ad
            comment.author = request.user
            comment.save()
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = CommentForm()

    return render(request, 'board/ad_detail.html', {'ad': ad, 'comments': comments, 'form': form})


@login_required
def ad_create(request):
    """Обрабатывает создание нового объявления."""
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = AdForm()
    return render(request, 'board/ad_form.html', {'form': form, 'title': 'Создать объявление'})


@login_required
def ad_update(request, pk):
    """Обрабатывает редактирование объявления (только для автора)."""
    ad = get_object_or_404(Ad, pk=pk, author=request.user)
    if request.method == 'POST':
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = AdForm(instance=ad)
    return render(request, 'board/ad_form.html', {'form': form, 'title': 'Редактировать объявление'})


@login_required
def comment_delete(request, pk):
    """Удаляет комментарий (только для автора комментария)."""
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    ad_pk = comment.ad.pk
    if request.method == 'POST':
        comment.delete()
        return redirect('ad_detail', pk=ad_pk)
    return render(request, 'board/comment_confirm_delete.html', {'comment': comment})