from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"
    common_result = 0
    result = 0
    if request.GET:
        form = CalcForm(request.GET)
        if form.is_valid():
            initial_fee = form.clean_initial_fee()
            rate = form.clean_rate()
            months_count = form.clean_months_count()
            common_result = round((initial_fee + initial_fee * (rate / 100)), 2)
            result = round((common_result / months_count), 2)
    else:
        form = CalcForm

    context = {
        'form': form, 'result': result, 'common_result': common_result
    }

    return render(request, template, context)
