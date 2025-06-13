from datetime import datetime
import os
from django.http import JsonResponse
import time


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


class OffensiveLanguageMiddleware:
    """
    Middleware to limit the number of messages a user can send per minute based on their IP.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.message_log = {}  # { ip: [timestamps] }

    def get_client_ip(self, request):
        """
        Extract the client IP address from the request.
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def __call__(self, request):
        # Only limit POST requests to chat/message endpoints
        if request.method == 'POST' and '/messages/' in request.path:
            client_ip = self.get_client_ip(request)
            current_time = time.time()

            # Initialize log if IP is not tracked yet
            if client_ip not in self.message_log:
                self.message_log[client_ip] = []

            # Remove timestamps older than 60 seconds
            self.message_log[client_ip] = [
                timestamp for timestamp in self.message_log[client_ip]
                if current_time - timestamp < 60
            ]

            # If more than 5 messages in the last minute → Block
            if len(self.message_log[client_ip]) >= 5:
                return JsonResponse(
                    {"detail": "Rate limit exceeded: Maximum 5 messages per minute allowed."},
                    status=429
                )

            # Log this message timestamp
            self.message_log[client_ip].append(current_time)

        # Allow request to proceed
        response = self.get_response(request)
        return response


class RolepermissionMiddleware:
    """
    Middleware to restrict access to admin or moderator roles only.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Optional: Only restrict certain endpoints (e.g., admin-only routes)
        if '/messages/' in request.path or '/conversations/' in request.path:
            user = request.user

            # If user is not authenticated, block immediately
            if not user.is_authenticated:
                return JsonResponse({"detail": "Authentication required."}, status=403)

            # Assuming the user model has a 'role' field like user.role
            if not hasattr(user, 'role') or user.role not in ['admin', 'moderator']:
                return JsonResponse({"detail": "You do not have permission to access this resource."}, status=403)

        # Allow request to continue
        response = self.get_response(request)
        return response
