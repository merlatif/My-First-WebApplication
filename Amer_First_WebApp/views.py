import operator

from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import counter

# def home(request):
#     return render(request, 'index.html',{'key1':'I am coming from a Python code'})
# def result(request):
#     age=request.GET['user_age']
#     name = request.GET['user_name']
#     message=f'Hi {name} you are {age} years old'
#     return render(request, 'result.html', {'age':message})


# def home(request):
#     return render(request, 'index.html',{'key1':'I am coming from a Python code'})
# def result(request):
#     Article=request.GET['Article']
#     words=Article.split()
#     word_count=len(words)
#     dict_words={}
#     for word in words:
#         if word in dict_words:
#             dict_words[word]+=1
#         else:
#             dict_words[word]=1
#             var_dict=sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)
#     return render(request, 'result.html', {'Article':Article,'word_count':word_count,'dict_words':var_dict})



def home(request):
    return render(request, 'index.html',{'key1':'I am coming from a Python code'})
def result(request):
    Article=request.GET['Article']
    var_dict, word_count=counter.count(Article)

    return render(request, 'result.html', {'Article':Article,'word_count':word_count,'dict_words':var_dict})