from django.http import HttpResponse
from django.shortcuts import render


def first_view(request, to_print="default"):
    return HttpResponse(f"Hello {to_print}")
