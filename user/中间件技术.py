from django.http import HttpRequest, HttpResponse


class SimpleMiddleware1:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(1, '-' * 30)
        print(isinstance(request, HttpRequest))
        print(request.GET)
        print(request.POST)
        print(request.body)

        # 之前相当于老版本的process_request
        # return HttpResponse(b'', status=404)
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        print(101, '-' * 30)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(request)
        print(2, '-' * 30)
        print(view_func.__name__, view_args, view_kwargs)
        # 观察view_func名字，说明在process_request之后，process_view之前已经做好了路径映射
        return None  # 继续执行其它的process_view或view
        # return HttpResponse('111', status=201)


class SimpleMiddleware2:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(3, '-' * 30)
        # return HttpResponse(b'', status=404)
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        print(102, '-' * 30)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(request)
        print(4, '-' * 30)
        print(view_func.__name__, view_args, view_kwargs)
        # return None # 继续执行其它的process_view或view
        return HttpResponse('2222', status=201)
