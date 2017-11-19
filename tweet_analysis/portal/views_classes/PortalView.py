from django.shortcuts import render
from django.views import View


class PortalView(View):
    def get(self, request, *args, **kwargs):
        html_path = 'portal/run_analysis.html'
        return render(request, html_path)

    def post(self, request, *args, **kwargs):
        html_path = 'portal/run_analysis.html'
        return render(request, html_path)