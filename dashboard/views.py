from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Device

# Create your views here.
def index(request):
    return HttpResponse("The soon to be pennyworth dashboard")

def devices(request):
    device_list = Device.objects.order_by('mac')
    context = {
        'device_list': device_list,
    }
    return render(request, 'dashboard/devices.html', context)

def device(request, device_id):
    device = get_object_or_404(Device, id = device_id)
    return render(request, 'dashboard/device.html', {'device': device})

def device_change_label(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    try:
        new_label = request.POST['label']
    except (KeyError, Device.DoesNotExist):
        # Redisplay the device details
        return render(request, 'dashboard/device.html', {
            'device': device,
            'error_message': "Something went wrong with your input.",
        })
    else:
        device.label = new_label
        device.save()
        return HttpResponseRedirect(reverse('dashboard:devices'))
