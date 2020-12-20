from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from users.forms import CustomUserCreationForm
from .models import PublishedTree
import random, string, json, os, re
from dashboard.views import build_tree
from dashboard.models import DecisionTree
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.decorators.clickjacking import xframe_options_exempt
import opendecision.schema as api

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    context = {}
    return render(request, 'home.html', context)

def contact_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    context = {}
    return render(request, 'contact.html', context)

def test_view(request, *args, **kwargs):
    context = {}
    return render(request, 'test.html', context)

def get_schema_view(request, *args, **kwargs):
    export = api.schema.introspect()
    response = JsonResponse(export, safe=False, content_type='application/json', json_dumps_params={'indent': 2})
    response['Content-Disposition'] = 'attachment; filename="schema.json"'
    return response

def lang_view(request, *args, **kwargs):
    context = {}
    return render(request, 'set_language.html', context)

def handler403(request, exception):
    return render(request, '403.html', status=403)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def logout_redirect(request):
    return HttpResponseRedirect(os.environ.get('LOGOUT_REDIRECT_URL', '/'))

@xframe_options_exempt
def show_published_tree(request, slug):
    if request.GET.get('publish'):
        random_url = publish(request, slug)
        return redirect('/publish/' + random_url + '/?new=true')
    else:
        tree = PublishedTree.objects.get(url=slug)
        context = {'tree_data' : tree.tree_data}
        if request.GET.get('new'):
            context['url'] = slug
        if request.GET.get('embedded'):
            return render(request, 'publish_embedded.html', context)
        return render(request, 'publish.html', context)



@login_required
def publish(request, slug):
    random_url = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    tree_data = json.dumps(build_tree(slug, request), indent=4, default=str)
    t = PublishedTree(  url             = random_url,
                        tree_data       = tree_data,
                        decision_tree   = DecisionTree.objects.filter(owner=request.user).get(slug=slug),
                        owner           = request.user,
                        created_at      = datetime.now(),
                        )
    t.save()
    return random_url

def get_published_tree(request):
    tree_query = request.GET.get('selected_tree')
    if re.match("^[a-z]{10}$", tree_query):
        try:
            tree_data = json.loads(PublishedTree.objects.get(url=tree_query).tree_data)
            return JsonResponse(tree_data, safe=False)
        except:
            response = JsonResponse({"TreeNotFound": "No tree matching the query"})
            response.status_code = 404
            return response
    else:
        response = JsonResponse({"InvalidTreeIdentifier": "The tree identifier is invalid"})
        response.status_code = 400
        return response
