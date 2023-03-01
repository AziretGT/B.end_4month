from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    # mylist  = [1,2,3,4]
    body = "<h1>Hello<h1>"
    # body = """
    # <!DOCTYPE html>
    #     <html>
    #     <head>
    #         <title>Geek Test</title>
    #     </head>
    #     <body>

    #         <h1>Зaголовок первого уровня</h1>
    #         <p>Параграф</p>

    #     </body> 
    #     </html>
    #  """
    headers = {"names": "Alex"}

# "Content-Type":"applivcation/vnd.ms-excel",
# "Content-Dispasition": "attachment"} 
    return HttpResponse( body,headers=headers,status=300)

def get_index(request):
    context = {
        "title": "Main page",
        "my_list": [1, 2, 3, 4],
    }
    return render(request, "posts/index.html", context=context)
    # # print (request.__dict__)
    # if request.method == "GET":
    #     return HttpResponse("Главная страница")
    # else :
    #     return HttpResponse("Не тот метод запроса")

def get_about(request):
    context ={
        "title" : "Страница о нас",
    }
    return render(request, "posts/about.html", context=context)

def get_contact(request):
    context ={
        "title" : "Контакты",
    }
    return render(request, "posts/contact.html", context=context)