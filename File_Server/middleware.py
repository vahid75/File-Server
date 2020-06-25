from django.http import HttpResponseForbidden
import os
from django.conf import settings
from django.urls import reverse
from . import utils


def ip_middleware(get_response):
    def middleware(request):
        client_ip_address = request.META.get("HTTP_X_REAL_IP")
        request.client_ip_address = client_ip_address
        response = get_response(request)
        if request.get_full_path() in [reverse('register_via_ip')]:
            return response 

        ip_authorized = utils.authorize_with_ip(client_ip_address)
        if not ip_authorized:
            return HttpResponseForbidden('Forbidden. ask file server admin for access your privilages to server resources')

        return response
    return middleware



