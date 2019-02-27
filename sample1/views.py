import json
from django.db.models import Count, Q
from django.shortcuts import render
from .models import Passenger
from .forms import SexChoice

def dashboard_view(request):
    age_dump = age(request)
    ticket_class_dump = ticket_class(request)
    context = {'age_chart':age_dump,
               'ticket_class_chart':ticket_class_dump,
               'form':SexChoice(),
               }

    if request.method == 'POST':
        context['form'] = SexChoice(request.POST)
    else:
        pass

    return render(request, 'sample1/dashboard_view.html', context)

def age_view(request):
    age_dump = age(request)
    context = {'age_chart':age_dump,
               'form':SexChoice(),
               }

    if request.method == 'POST':
        context['form'] = SexChoice(request.POST)
    else:
        pass
    return render(request, 'sample1/age_view.html', context)

def ticket_class_view(request):
    ticket_class_dump = ticket_class(request)
    context = {'ticket_class_chart':ticket_class_dump,
               'form':SexChoice(),
               }

    if request.method == 'POST':
        context['form'] = SexChoice(request.POST)
    else:
        pass
    return render(request, 'sample1/ticket_class_view.html', context)

def age(request):
    dataset = Passenger.objects.values('age').annotate(survived_age_count=Count('age', filter=Q(survived=True)),
              not_survived_age_count=Count('age', filter=Q(survived=False))).order_by('age')

    if request.method == 'POST' and request.POST['choice'] != 'male or female':
            dataset = Passenger.objects.values('age').filter(sex=request.POST['choice']).annotate(survived_age_count=Count('age', filter=Q(survived=True)),
                      not_survived_age_count=Count('age', filter=Q(survived=False))).order_by('age')
    else:
        pass

    categories = []
    survived_series_data = []
    not_survived_series_data = []

    for entry in dataset:
        categories.append('{}'.format(entry['age']))
        survived_series_data.append(entry['survived_age_count'])
        not_survived_series_data.append(entry['not_survived_age_count'])
    survived_series_data.pop()
    not_survived_series_data.pop()

    survived_series = {
        'name': 'Survived',
        'data': survived_series_data,
        'color':'steelblue'
    }

    not_survived_series = {
        'name': 'Not Survived',
        'data': not_survived_series_data,
        'color':'crimson',
    }

    chart = {
        'chart': {'type': 'line'},
        'title': {'text': 'Titanic Survivors by Age'},
        'xAxis': {'categories': categories},
        'yAxis': {'title':False},
        'series': [survived_series, not_survived_series],
        'plotOptions':{'line':{'marker':{'enabled':False, 'states':{'hover':{'enabled':True}}}}},
    }

    dump = json.dumps(chart)

    return dump

def ticket_class(request):
    dataset = Passenger.objects.values('ticket_class').annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
              not_survived_count=Count('ticket_class', filter=Q(survived=False))).order_by('ticket_class')

    if request.method == 'POST' and request.POST['choice'] != 'male or female':
        dataset = Passenger.objects.values('ticket_class').filter(sex=request.POST['choice']).annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))).order_by('ticket_class')
    else:
        pass

    categories = []
    survived_series_data = []
    not_survived_series_data = []

    for entry in dataset:
        categories.append('{} Class'.format(entry['ticket_class']))
        survived_series_data.append(entry['survived_count'])
        not_survived_series_data.append(entry['not_survived_count'])

    survived_series = {
        'name': 'Survived',
        'data': survived_series_data,
        'color': 'lightgreen'
    }

    not_survived_series = {
        'name': 'Not Survived',
        'data': not_survived_series_data,
        'color': 'darkblue'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'xAxis': {'categories': categories},
        'yAxis': {'title':False},
        'series': [survived_series, not_survived_series]
    }

    dump = json.dumps(chart)

    return dump