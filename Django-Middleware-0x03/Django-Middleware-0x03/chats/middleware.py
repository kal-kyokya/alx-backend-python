from datetime import datetime
import os
from django.http import JsonResponse


class RequestLoggingMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)

        log_file_path = os.path.join(parent_dir, 'requests.log')

        with open(log_file_path, 'a') as log_file:
            log = f"\n{datetimenow()} - User: {request.user} - Path: {request.path}"
            print(log)
            log_file.write(log)
        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    """Restricts access to chat between 9 PM and 6 PM (So, outside this window access is blocked)
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get current server time (24-hour format)
        current_time = datetime.now().time()

        # Define the restricted window: 9 PM to 6 PM
        start_allowed = 18 # 6 PM
        end_allowed = 21   # 9 PM

        if not (start_allowed <= current_time.hour < end_allowed):
            return JsonResponse(
                {'detail': 'Chat access is restricted at this time'},
                status=403
            )

        response = self.get_response(request)
        return response
