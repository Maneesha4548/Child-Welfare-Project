from django.urls import path
from App import views
from django.contrib.auth import views as av

urlpatterns=[
        path('',views.home,name="hm"),
        path('lg/',av.LoginView.as_view(template_name="html/login.html"),name="lg"),
        path('lgo/',av.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
        path('reg/',views.register,name="reg"),
        path('mn/',views.mainpage,name="mn"),
        path('ureq/',views.userreq,name="ureq"),
        path('per/',views.perm,name="per"),
        path('eper/<int:k>/',views.gvper,name="gp"),
        path('dash/',views.dashboard,name="dash"),
        path('don/',views.donate,name="don"),
        path('up/<int:a>/',views.update,name="up"),
        path('dele/<int:b>/',views.delete,name='dele'),
        path('pay/',views.payment,name="pay"),
        path('profile/',views.updateprofile,name="profile"),
        path('uppro/',views.updatedetails,name="uppro"),
        path('chpas/',views.change,name="chpas"),
        path('rst/',av.PasswordResetView.as_view(template_name="html/resetpassword.html"),name="rt"),
        path('rst_done/',av.PasswordResetDoneView.as_view(template_name="html/resetpassworddone.html"),name="password_reset_done"),
        path('rst_cf/<uidb64>/<token>/',av.PasswordResetConfirmView.as_view(template_name="html/reset_password_confirm.html"),name="password_reset_confirm"),
        path('rst_cmplt/',av.PasswordResetCompleteView.as_view(template_name="html/reset_password_complete.html"),name="password_reset_complete"),
        path('occdet/<int:bi>/',views.occdetails,name="occdet"),
        path('odel/<int:ai>/',views.occdelete,name="odel"),
        path('orgup/',views.orgupdate,name="orgup"),
]
