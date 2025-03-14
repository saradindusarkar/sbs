from django.shortcuts import render
from django.db import IntegrityError
from datetime import date
from dlog.models import Dlog

def index(request):
    show_report = request.session.get("show_report", False)  # Retrieve session variable

    if request.method == "POST":
        if 'save' in request.POST:  # Handle save button
            today = date.today()
            try:
                existing_log = Dlog.objects.get(log_date=today)
            except Dlog.DoesNotExist:
                Dlog.objects.create(log_date=today)
            except IntegrityError:
                pass

        elif 'report' in request.POST:  # Handle report button
            request.session["show_report"] = not show_report  # Toggle session value
            request.session.modified = True  # Ensure session updates

    show_report = request.session.get("show_report", False)  # Re-fetch updated value

    context = {
        'all_dlogs': Dlog.objects.all() if show_report else None  # Conditionally fetch data
    }
    return render(request, 'index.html', context)
