from django.contrib.auth import update_session_auth_hash, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Game, Comment, GameResult, Gamer, GameEntry
from django.db.models import Min
from .forms import *
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('tablo')  # Перенаправляем пользователя на главную страницу после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def base(request):
    return render(request, "tablo.html")


@login_required
def tablo(request):
    meeting = Game.objects.all()
    game_results = []

    for game in meeting:
        winner_result = game.gameresult_set.filter(university=game.winner).aggregate(min_time=Min('time_taken'))
        min_time = winner_result.get('min_time')
        game_results.append({
            'game': game,
            'min_time': min_time,
        })

    return render(request, "tablo.html", {"game_results": game_results})


@login_required
def comments(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    comments = Comment.objects.filter(game=game)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.game = game
            new_comment.author = request.user
            new_comment.save()
    else:
        form = CommentForm()

    return render(
        request,
        "comments.html",
        {"game": game, "comments": comments, "form": form},
    )


@login_required
def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    results = game.gameresult_set.all()

    # Получить список зарегистрированных пользователей на эту гонку
    registered_users = game.gameentry_set.values_list('gamer__user__username', flat=True)

    # Обработка запроса для регистрации/снятия регистрации
    if request.method == 'POST':
        form = GameEntryForm(request.POST)
        if form.is_valid():
            gamer = form.cleaned_data['gamer']
            if gamer.user.username in registered_users:
                # Если пользователь уже зарегистрирован, снимаем регистрацию
                GameEntry.objects.filter(gamer=gamer, game=game).delete()
            else:
                # Регистрируем пользователя на гонку
                GameEntry.objects.create(gamer=gamer, game=game)
            return redirect('game_detail', game_id=game_id)
    else:
        form = GameEntryForm()

    context = {
        'game': game,
        'results': results,
        'registered_users': registered_users,
        'form': form,
    }
    return render(request, 'game_detail.html', context)


@login_required
def gamer_registration(request, game_id):
    if request.method == 'POST':
        game = get_object_or_404(Game, pk=game_id)
        user = request.user
        gamer = Gamer.objects.get(user=user)
        game_entry = GameEntry(game=game, gamer=gamer)
        game_entry.save()
        return redirect('game_detail', game_id=game_id)
    else:
        return redirect('game_detail', game_id=game_id)


@login_required
def gamer_unregistration(request, game_id):
    if request.method == 'POST':
        game = get_object_or_404(Game, pk=game_id)
        user = request.user
        gamer = Gamer.objects.get(user=user)
        GameEntry.objects.filter(game=game, gamer=gamer).delete()
        return redirect('game_detail', game_id=game_id)
    else:
        return redirect('game_detail', game_id=game_id)


def handle_form_errors(request, form):
    for field, errors in form.errors.items():
        for error in errors:
            messages.error(request, f"{field}: {error}")


def user_logout(request):
    logout(request)
    return redirect(reverse('base'))


@login_required
def profile(request):
    user = request.user  # Get the current user
    form = ProfileUpdateForm(instance=user)
    password_form = PasswordChangeCustomForm(user)

    if request.method == 'POST':
        if 'password_change' in request.POST:
            password_form = PasswordChangeCustomForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Пароль успешно изменен.')
                return redirect('profile')
            else:
                handle_form_errors(request, password_form)
                if not user.has_usable_password():
                    messages.error(request, 'Пароль не может быть изменен.')
        else:
            form = ProfileUpdateForm(request.POST, instance=user)
            if form.is_valid():
                user = form.save()
                try:
                    gamer = user.gamer
                except Gamer.DoesNotExist:
                    gamer = Gamer(user=user)

                university_id = form.cleaned_data.get('university')
                if university_id:
                    university = University.objects.get(pk=university_id)
                    gamer.university = university
                else:
                    gamer.university = None  # If no team is selected

                if 'description' in form.cleaned_data:
                    gamer.description = form.cleaned_data['description']
                if 'experience' in form.cleaned_data:
                    gamer.experience = form.cleaned_data['experience']
                gamer.save()
                messages.success(request, 'Информация о профиле успешно обновлена.')
                return redirect('profile')

    return render(request, 'profile.html', {'form': form, 'password_form': password_form})


def all_game_results(request):
    all_results = GameResult.objects.all()

    # Сортировка результатов по гонкам и времени прохождения
    sorted_results = sorted(all_results, key=lambda x: (x.game.id, x.time_taken))

    return render(request, "all_game_results.html", {"all_results": sorted_results})
