from django.shortcuts import render
from django.views import View

from .forms import ConverterForm


class ConvertView(View):
    def get(self, request):
        """
        При get запросе отражаем пустую форму, результат задаём, как None, для последующей обработки в HTML.
        """

        form = ConverterForm()

        return render(
            request, "converter/converter.html", context={"form": form, "result": None}
        )

    def post(self, request):
        """
        При post запросе отражаем заполненную форму, получив аргументы из запроса,
        считаем результат (что элементарно, поэтому бизнес логика прямо во view) и отражаем его.
        """

        form = ConverterForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data["amount"]
            from_currency = form.cleaned_data["from_currency"]
            to_currency = form.cleaned_data["to_currency"]
            from_rate = from_currency.rate
            to_rate = to_currency.rate
            result = amount * (from_rate / to_rate)
        else:
            result = None

        return render(
            request,
            "converter/converter.html",
            context={"form": form, "result": result},
        )
