from django.shortcuts import render, redirect
from . import store

def index(request):
    return render(request, "core/index.html")

# Просмотр списка
def ticket_list(request):
    tickets = store.get_all()
    return render(request, "core/ticket_list.html", {"tickets": tickets})

# Карточка записи
def ticket_detail(request, ticket_id):
    ticket = store.get_by_id(ticket_id)
    if not ticket:
        return render(request, "core/error.html", {
            "error_title": "Заявка не найдена",
            "error_message": f"Заявки с ID {ticket_id} не существует."
        })
    return render(request, "core/ticket_detail.html", {"ticket": ticket})

# Создание заявки + ошибка
def ticket_create(request):
    error = None
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        priority = request.POST.get("priority", "Обычный")

        if not title:
            error = "Заявка не создана: тема не может быть пустой."
        elif len(title) < 3:
            error = "Заявка не создана: тема должна содержать минимум 3 символов."
        else:
            store.add(title, description, priority)
            return redirect("ticket_list")

    return render(request, "core/ticket_form.html", {"error": error})
