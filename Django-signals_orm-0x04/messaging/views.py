from django.http import HttpResponse
from django.contrib.decorators import login_required
from django.contrib.auth import logout # Remove the authenticated user's ID from the request and flush their session data


@login_required
def delete_user(request):
    """Ensures a user's details are erased upon logging out
    Args:
    	request: The request object submitted for logout
    Return:
    	An Http response detailing the outcome of the logout attempt
    """
    if request.method == 'DELETE':
        user = request.user
        logout(request)
        user.delete()
        return HttpResponse('User deleted successfully')
    else:
        return HttpResponse('Method not allowed')
