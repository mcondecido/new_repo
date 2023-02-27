from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'tutors'
    
    def get_queryset(self):
        """
        Return active tutors (not including those set to be
        published in the future).
        """
        return