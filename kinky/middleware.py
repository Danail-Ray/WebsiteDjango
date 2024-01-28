
from django.middleware.csrf import CsrfViewMiddleware

class CustomCsrfMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        # Add your custom logic here
        # For example, you can check if the request method is safe (GET, HEAD, OPTIONS, TRACE)
        # and skip CSRF protection for those methods
        
        # BEGIN: Custom CSRF logic
        if request.method in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
            return None
        # END: Custom CSRF logic
        
        return super().process_view(request, callback, callback_args, callback_kwargs)
