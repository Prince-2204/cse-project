# # Inside your_project/middleware.py

# from django.shortcuts import redirect
# from django.urls import reverse

# class AuthRequiredMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if not request.user.is_authenticated and not request.path == reverse('login_page'):
#             return redirect('login_page')
#         response = self.get_response(request)
#         return response
