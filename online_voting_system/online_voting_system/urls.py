"""
URL configuration for online_voting_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Voters import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='homepage'),
    path('login',views.LoginPage,name='login'),
    path('resetvotes',views.ResetVotes,name='resetvotes'),
    path('viewresults',views.ViewResults,name='viewresults'),
    path('castevote/<slug:username>',views.CasteVote,name='castevote'),
    path('voterdashboard',views.VoterDashboard,name='voterdashboard'),
    path('admindashboard',views.AdminDashboard,name='admindashboard'),
    path('logout',views.LogoutPage,name='logout'),
    path('voterspage',views.VotersPage,name='voterspage'),
    path('candidatespage',views.CandidatesPage,name='candidatespage'),
    path('positionspage',views.PositionsPage,name='positionspage'),
    path('voterdetails/<int:id>',views.VoterDetails,name='voterdetails'),
    path('candidatedetails/<int:id>',views.CandidateDetails,name='candidatedetails'),
    path('positiondetails/<int:id>',views.PositionDetails,name='positiondetails'),
    path('addvoter',views.SignupPage,name='addvoter'),
    path('deletevoter/<int:id>',views.DeleteVoter,name='deletevoter'),
    path('updatevoter/<int:id>',views.UpdateVoter,name='updatevoter'),
    path('addcandidate',views.AddCandidate,name='addcandidate'),
    path('deletecandidate/<int:id>',views.DeleteCandidate,name='deletecandidate'),
    path('updatecandidate/<int:id>',views.UpdateCandidate,name='updatecandidate'),
    path('addposition',views.AddPosition,name='addposition'),
    path('deleteposition/<int:id>',views.DeletePosition,name='deleteposition'),
    path('updateposition/<int:id>',views.UpdatePosition,name='updateposition'),
    path('voter/candidatedetails',views.VCV,name='voter/candidatedetails'),
    
]
