from multiprocessing import context
from django.shortcuts import redirect, render, reverse
from .forms import VoterForm,CandidateForm, PositionForm,VotesForm
from .models import Voter,Candidate,Position,Votes
from django.template import loader
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from tkinter import *

def SignupPage(request):
    form=VoterForm()
    field = form.fields['is_voted']
    field.widget = field.hidden_widget()
    if request.method=='POST':
        pass1=request.POST.get('password')
        pass2=request.POST.get('password2')
        uname=request.POST.get('username')
        email=request.POST.get('email')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            form=VoterForm(request.POST)
            if form.is_valid():
                form.save()
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
            form=VoterForm()
            return redirect('addvoter')
    context={
        'form':form,
    }
        
    return render (request,'addVoter.html',context)

# def AddVoter(request):
#     form=VoterForm()
#     if request.method=='POST':
#         form=VoterForm(request.POST)
#         form.save()
#         form=VoterForm()
#     context={
#         'form':form,
#     }
#     return render(request,'addVoter.html',context)

def LoginPage(request):
    msg=""
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        #user=authenticate(request,email=email,password=pass1)
        user=authenticate(request,username=username,password=pass1)
        #print(user,username)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admindashboard')
            else:
                return redirect('voterdashboard')
        else:
            i=Voter.objects.get(username=username)
            if i.password==pass1:
                login(request,user)
                return redirect('voterdashboard')
            else:
                msg="Username or Password is incorrect!!!"

    return render (request,'login.html',{'msg':msg})

@login_required(login_url='login')
@user_passes_test(lambda user:not user.is_staff)
def VoterDashboard(request):
    user=request.user.username
    i=Voter.objects.get(username=user)
    context={
        'i':i,
    }
    return render(request,'VoterDashboard.html',context)
   # return render(request,'VoterDashboard.html')

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def AdminDashboard(request):
    return render(request,'AdminDashboard.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def Home(request):
    return render(request,'index.html')

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def VotersPage(request):    
    data=Voter.objects.all()
    context={
        'data':data,
    }
    return render(request,'displayVoters.html',context)

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def CandidatesPage(request):
    data=Candidate.objects.all()
    context={
        'data':data,
    }
    return render(request,'displayCandidates.html',context)

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def PositionsPage(request):
    data=Position.objects.all()
    context={
        'data':data,
    }
    return render(request,'displayPositions.html',context)

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def AddCandidate(request):
    form=CandidateForm()
    field = form.fields['no_of_votes']
    field.widget = field.hidden_widget()
    if request.method=='POST':
        form=CandidateForm(request.POST)
        form.save()
        form=CandidateForm()
    
    data=Candidate.objects.all()
    
    context={
        'form':form,
        'data':data,
    }
    return render(request,'addCandidate.html',context)

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def AddPosition(request):
    form=PositionForm()
    if request.method=='POST':
        form=PositionForm(request.POST)
        form.save()
        form=PositionForm()
    
    data=Position.objects.all()
    
    context={
        'form':form,
        'data':data,
    }
    return render(request,'addPosition.html',context)

#Voter
@login_required(login_url='login')
def VoterDetails(request,id):
    i=Voter.objects.get(id=id)
    context={
        'i':i,
    }
    return render(request,'voterDetails.html',context)

# Delete View
@login_required(login_url='login')
def DeleteVoter(request,id):
    a=Voter.objects.get(pk=id)
    username=a.username
    u=User.objects.get(username=username)
    u.delete()
    a.delete()
    return redirect('/')
    

# Update View
@login_required(login_url='login')
@user_passes_test(lambda user:not user.is_staff)
def UpdateVoter(request,id):
    if request.method=='POST':
        data=Voter.objects.get(pk=id)
        form=VoterForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect(reverse('voterdashboard'))
    else:

        data=Voter.objects.get(pk=id)
        form=VoterForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'updateVoter.html',context)

#Candidate
@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def CandidateDetails(request,id):
    i=Candidate.objects.get(id=id)
    context={
        'i':i,
    }
    return render(request,'candidateDetails.html',context)


# Delete View
@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def DeleteCandidate(request,id):
    a=Candidate.objects.get(pk=id)
    a.delete()
    return redirect('/')
    

# Update View
@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def UpdateCandidate(request,id):
    if request.method=='POST':
        data=Candidate.objects.get(pk=id)
        form=CandidateForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:

        data=Candidate.objects.get(pk=id)
        form=CandidateForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'updateCandidate.html',context)

#Position
@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def PositionDetails(request,id):
    i=Position.objects.get(id=id)
    context={
        'i':i,
    }
    return render(request,'positionDetails.html',context)

# Delete View
@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def DeletePosition(request,id):
    a=Position.objects.get(pk=id)
    a.delete()
    return redirect('/')
    

# Update View
@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def UpdatePosition(request,id):
    if request.method=='POST':
        data=Position.objects.get(pk=id)
        form=PositionForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:

        data=Position.objects.get(pk=id)
        form=PositionForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'updatePosition.html',context)

@login_required(login_url='login')
def CasteVote(request,username):
    form=VotesForm()
    if request.method=='POST':
        form=VotesForm(request.POST)
        form.save()
        vdata=Voter.objects.get(username=username)
        vdata.is_voted=True
        vdata.save()
        form=VotesForm()
        username=request.POST.get('candidate')
        x=Candidate.objects.all()
        for a in x:
            if a == username:
                a.no_of_votes = a.no_of_votes+1
                a.save()
                break
        return redirect(reverse('logout'))
    
    vdata=Voter.objects.get(username=username)
    pdata=Position.objects.all()
    cdata=Candidate.objects.all()
    field = form.fields['voter']
    field.widget = field.hidden_widget()
    form.initial['voter'] = vdata
    context={
        'form':form,
        'vdata':vdata,
        'pdata':pdata,
        'cdata':cdata,
    }
    return render(request,'casteVote.html',context)

@login_required(login_url='login')
def ViewResults(request):
    candidate=Candidate.objects.all()
    data=[]
    max=-1
    res=[]
    for i in candidate:
        if i.no_of_votes > max:
            max=i.no_of_votes
            res.clear()
            res.append(i)
        elif i.no_of_votes == max:
            max=i.no_of_votes
            res.append(i)
        data.append(i)
    msg=False
    if data==[] and res==[]:
        msg=True
    context={
       'data':data,
       'res':res,
       'msg':msg,
       'a':False,
       'msg1':"",
    }
    return render(request,'viewResults.html',context)

@login_required(login_url='login')
@user_passes_test(lambda user:not user.is_staff)
def VCV(request):
    data=Candidate.objects.all()
    context={
        'data':data,
    }
    return render(request,'candVoterView.html',context)

@login_required(login_url='login')
@user_passes_test(lambda user:user.is_staff)
def ResetVotes(request):
    Votes.objects.all().delete()
    x=Voter.objects.all()
    data=[]
    res=[]
    for i in x:
        i.is_voted=False
        i.save()
    can=Candidate.objects.all()
    for i in can:
        i.no_of_votes=0
        i.save()
    context={
        'a':True,
        'msg':False,
        'msg1':"All votes are removed!",
        'data':data,
        'res':res,
    }
    return render(request,'viewResults.html',context)