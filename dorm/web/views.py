from django.shortcuts import render, redirect
from django.http import HttpResponse
from web.models import *

test_user = 'User 2'

def dashboard(request):
    u = User.objects.get(name = 'User 2')

    l = list(map(lambda t: {
        'username': t.u0.name,
        'val': "%.2lf" % -t.get_val()
    }, Table.objects.filter(u1 = u))) \
    + list(map(lambda t: {
        'username': t.u1.name,
        'val': "%.2lf" % t.get_val()
    }, Table.objects.filter(u0 = u)))

    tl = list(map(lambda l: {
        'time': l.ctime.strftime('%Y-%m-%d %H:%M:%S %A'),
        'username': l.u1.name,
        'val': '%.2lf' % l.get_val(),
        'comment': l.comment
    }, Log.objects.filter(u0 = u)))

    gl = list(map(lambda l: {
        'time': l.ctime.strftime('%Y-%m-%d %H:%M:%S %A'),
        'username': l.u0.name,
        'val': '%.2lf' % l.get_val(),
        'comment': l.comment
    }, Log.objects.filter(u1 = u)))

    return render(request, 'dashboard.html', {
        'username': u.name,
        'userlist': l,
        'takelist': tl,
        'getlist': gl
    })

def add(request):
    u = User.objects.get(name = test_user)
    if request.method == 'GET':
        l = User.objects.all().exclude(name = test_user).exclude(name = 'User 0')
        return render(request, 'add.html', {
            'username': u.name,
            'userlist': list(map(lambda u: u.name, l))
        })
    elif request.method == 'POST':
        u1 = request.POST['u1']
        val = float(request.POST['val'])
        comment = request.POST['comment']
        l = Log()
        l.u0 = u
        l.u1 = User.objects.get(name = u1)
        l.set_val(val)
        l.comment = comment
        l.save()
        if l.u0.id < l.u1.id:
            t = Table.objects.get(u0 = l.u0, u1 = l.u1)
        else:
            t = Table.objects.get(u0 = l.u1, u1 = l.u0)
            val = -val
        t.add_val(val)
        t.save()
        return redirect(dashboard)
