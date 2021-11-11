from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from users.serializer import Rsvp_AEROCLUB_Serializer,Rsvp_AICLUB_Serializer,Rsvp_ALCHERCLUB_Serializer,Rsvp_ASTROCLUB_Serializer,Rsvp_BT_Serializer,Rsvp_CACLUB_Serializer,Rsvp_CCDCLUB_Serializer,Rsvp_CE_Serializer,Rsvp_CH_Serializer,Rsvp_CL_Serializer,Rsvp_CODINGCLUB_Serializer,Rsvp_CSE_Serializer,Rsvp_DES_Serializer,Rsvp_ECE_Serializer,Rsvp_EDCLUB_Serializer,Rsvp_EECLUB_Serializer,Rsvp_EEE_Serializer,Rsvp_FNCCLUB_Serializer,Rsvp_MA_Serializer,Rsvp_OTHERCLUB_Serializer,Rsvp_ME_Serializer,Rsvp_PH_Serializer,Rsvp_PRAKRITICLUB_Serializer,Rsvp_ROBOTICSCLUB_Serializer,Rsvp_SAILCLUB_Serializer,Rsvp_SWC_Serializer,Rsvp_Task_Serializer,Rsvp_TechnicheCLUB_Serializer,Rsvp_UGCLUB_Serializer
from .models import Rsvp_AEROCLUB,Rsvp_AICLUB,Rsvp_ALCHERCLUB,Rsvp_ASTROCLUB,Rsvp_BT,Rsvp_CACLUB,Rsvp_CCDCLUB,Rsvp_CE,Rsvp_CH,Rsvp_CL,Rsvp_CODINGCLUB,Rsvp_CSE,Rsvp_DES,Rsvp_ECE,Rsvp_EDCLUB,Rsvp_EECLUB,Rsvp_EEE,Rsvp_FNCCLUB,Rsvp_MA,Rsvp_OTHERCLUB,Rsvp_ME,Rsvp_PH,Rsvp_PRAKRITICLUB,Rsvp_ROBOTICSCLUB,Rsvp_SAILCLUB,Rsvp_SWC,Rsvp_Task,Rsvp_TechnicheCLUB,Rsvp_UGCLUB
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework import generics, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
import django_filters.rest_framework

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! please login and update your profile')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Profile has been updated!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile.html',{'title':'profile' , 'u_form':u_form , 'p_form':p_form})

class Rsvp_AEROCLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_AEROCLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_AEROCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_AEROCLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_AEROCLUB_Serializer
    queryset = Rsvp_AEROCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    
class Rsvp_AICLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_AICLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_AICLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_AICLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_AICLUB_Serializer
    queryset = Rsvp_AICLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_ALCHERCLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_ALCHERCLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_ALCHERCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_ALCHERCLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_ALCHERCLUB_Serializer
    queryset = Rsvp_ALCHERCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_ASTROCLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_ASTROCLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_ASTROCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_ASTROCLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_ASTROCLUB_Serializer
    queryset = Rsvp_ASTROCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_BT_List_API(generics.ListAPIView):
    serializer_class = Rsvp_BT_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_BT.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_BT_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_BT_Serializer
    queryset = Rsvp_BT.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_CACLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_CACLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_CACLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_CACLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_CACLUB_Serializer
    queryset = Rsvp_CACLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_CCDCLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_CCDCLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_CCDCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_CCDCLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_CCDCLUB_Serializer
    queryset = Rsvp_CCDCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_CE_List_API(generics.ListAPIView):
    serializer_class = Rsvp_CE_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_CE.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_CE_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_CE_Serializer
    queryset = Rsvp_CE.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_CH_List_API(generics.ListAPIView):
    serializer_class = Rsvp_CH_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_CH.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_CH_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_CH_Serializer
    queryset = Rsvp_CH.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_CL_List_API(generics.ListAPIView):
    serializer_class = Rsvp_CL_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_CL.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_CL_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_CL_Serializer
    queryset = Rsvp_CL.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_CODINGCLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_CODINGCLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_CODINGCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_CODINGCLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_CODINGCLUB_Serializer
    queryset = Rsvp_CODINGCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_CSE_List_API(generics.ListAPIView):
    serializer_class = Rsvp_CSE_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_CSE.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_CSE_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_CSE_Serializer
    queryset = Rsvp_CSE.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_DES_List_API(generics.ListAPIView):
    serializer_class = Rsvp_DES_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_DES.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_DES_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_DES_Serializer
    queryset = Rsvp_DES.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_ECE_List_API(generics.ListAPIView):
    serializer_class = Rsvp_ECE_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_ECE.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_ECE_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_ECE_Serializer
    queryset = Rsvp_ECE.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_EDCLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_EDCLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_EDCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_EDCLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_EDCLUB_Serializer
    queryset = Rsvp_EDCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_EECLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_EECLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_EECLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_EECLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_EECLUB_Serializer
    queryset = Rsvp_EECLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_EEE_List_API(generics.ListAPIView):
    serializer_class = Rsvp_EEE_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_EEE.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_EEE_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_EEE_Serializer
    queryset = Rsvp_EEE.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_FNCCLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_FNCCLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_FNCCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_FNCCLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_FNCCLUB_Serializer
    queryset = Rsvp_FNCCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_MA_List_API(generics.ListAPIView):
    serializer_class = Rsvp_MA_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_MA.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_MA_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_MA_Serializer
    queryset = Rsvp_MA.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_ME_List_API(generics.ListAPIView):
    serializer_class = Rsvp_ME_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_ME.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_ME_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_ME_Serializer
    queryset = Rsvp_ME.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_OTHERCLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_OTHERCLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_OTHERCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_OTHERCLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_OTHERCLUB_Serializer
    queryset = Rsvp_OTHERCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_PH_List_API(generics.ListAPIView):
    serializer_class = Rsvp_PH_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_PH.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_PH_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_PH_Serializer
    queryset = Rsvp_PH.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_PRAKRITICLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_PRAKRITICLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_PRAKRITICLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_PRAKRITICLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_PRAKRITICLUB_Serializer
    queryset = Rsvp_PRAKRITICLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_ROBOTICSCLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_ROBOTICSCLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_ROBOTICSCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_ROBOTICSCLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_ROBOTICSCLUB_Serializer
    queryset = Rsvp_ROBOTICSCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_SAILCLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_SAILCLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_SAILCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_SAILCLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_SAILCLUB_Serializer
    queryset = Rsvp_SAILCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_SWC_List_API(generics.ListAPIView):
    serializer_class = Rsvp_SWC_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_SWC.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_SWC_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_SWC_Serializer
    queryset = Rsvp_SWC.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_Task_List_API(generics.ListAPIView):
    serializer_class = Rsvp_Task_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_Task.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_Task_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_Task_Serializer
    queryset = Rsvp_Task.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_TechnicheCLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_TechnicheCLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_TechnicheCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_TechnicheCLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_TechnicheCLUB_Serializer
    queryset = Rsvp_TechnicheCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

class Rsvp_UGCLUB_List_API(generics.ListAPIView):
    serializer_class = Rsvp_UGCLUB_Serializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Rsvp_UGCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('yes__name', 'maybe__name', 'no__name','event__title')

class Rsvp_UGCLUB_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Rsvp_UGCLUB_Serializer
    queryset = Rsvp_UGCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

