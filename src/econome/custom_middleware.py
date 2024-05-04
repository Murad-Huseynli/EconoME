from django.utils.deprecation import MiddlewareMixin


class DefaultLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if 'HTTP_ACCEPT_LANGUAGE' in request.META:
            del request.META['HTTP_ACCEPT_LANGUAGE']

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
