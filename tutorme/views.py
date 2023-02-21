from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'tutorme/index.html'
    context_object_name = 'tutors'


