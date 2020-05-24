"""PM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from trainer import views
from django.conf.urls import include, url


urlpatterns = [
    #path('admini/', admini.site.urls),
    path('', views.showHomePage, name='loginPage'),
    path('login/',LoginView.as_view(),name='login'),
    path('loginBtn/', views.loginBtn,name='loginBtn'),
    ##path('sign-in/', views.loginBtn, name='signin'),
    path('signUpBtn/', views.register, name='sign-up'),
    path('sign-up/', views.showRegister, name='sign-up'),
    path('admin/', views.admin, name='admin'),
    path('adminAfterUpdate/', views.adminAfterUpdate, name='admin'),
    #path('admin/<str:ID>/<str:userName>/<str:password>/<str:Email>', views.adminAfterUpdate, name='adminAfterUpdate'),
    path('trainer/', include('trainer.urls')),
    path('sign-in/',views.showLogin,name='show-login'),
    path('logout', views.logout, name='logout'),
    path('trainee/',views.trainee,name='trainee'),
    path('deleteUser/<str:userID>',views.delete_user,name="deleteUser"),
    path('updateUserDetails/<str:UserID>', views.showUpdateUser, name="updateUserDetails"),
    path('ShowCourts/', views.ShowCourts, name="ShowCourts"),
    path('backToAdmin/', views.backtoAdmin, name="backtoAdmin"),
    path('adminAfterFacilityUpdate/<str:origName>/<str:origType>/<str:origOwner>/<str:origNeighborhood>/<str:origOperator>', views.afterFacilityUpdate, name="afterFacilityUpdate"),
    path('delteFacilty/<str:facilityType>/<str:facilityName>/<str:facilityNeighborhood>/<str:facilityOperator>/<str:facilityOwner>', views.deleteFacility, name="deleteFacility"),
    path('updateFacilityDetails/<str:facilityType>/<str:facilityName>/<str:facilityNeighborhood>/<str:facilityOperator>/<str:facilityOwner>', views.showUpdateFacility, name="editFacility"),
    path('newFacilities/', views.addNewFacilities, name="newFacilities"),
    #path('newFacilities/<str:facilityType>/<str:facilityName>/<str:facilityStreet>/<str:facilityHouseNumbe>/<str:facilityNeighborho>/<str:facilityOperator>/<str:facilitySeats>/<str:facilityActivity>/<str:facilityFencing>/<str:facilityLighting>/<str:facilityHandicappe>/<str:facilityCondition>/<str:facilityOwner><str:facilityForSchool>/<str:facilityAssociatio>/<str:facilitySportType>/<str:facilitylat>/<str:facilitylon>', views.addNewFacilities, name="newFacilities"),
    ##facilityName=instance.Name facilityNeighborhood=instance.neighborho facilityOperator=instance.Operator facilityOwner = instance.Owner
    #url(r'^trainer/delete/(?P<value>.*)/$', views.delete_user, name='deleteUser'),
    #path('delete_user',views.delete_user,name='delete_user'),
]
