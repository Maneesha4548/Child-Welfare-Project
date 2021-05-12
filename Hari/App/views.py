from django.shortcuts import render,redirect
from App.forms import UsrReg,UsPerm,DonateForm,UpdateForm,UpForm,ChpasForm,OccDonateForm,OrgForm,OrgUp
from django.core.mail import EmailMessage
from Hari import settings
from App.models import User,Donate,OccDonate,Orgdetails
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def register(request):
	if request.method=="POST":
		p=UsrReg(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/lg')
	p=UsrReg()
	return render(request,'html/register.html',{'y':p})

def mainpage(request):
	h=Donate.objects.filter(uid_id=request.user.id)
	o=OccDonate.objects.filter(uid_id=request.user.id)
	i=Donate.objects.all()
	kl={}
	for n in i:
		d = User.objects.get(id=n.uid_id)
		kl[n.id] = n.ways_to_donate,n.donating_to,n.sponsor_way,n.donating_date,d.username
	c=kl.values()
	j=OccDonate.objects.all()
	km={}
	for m in j:
		p = User.objects.get(id=m.uid_id)
		km[m.id] = m.donating_way,m.occ_name,m.donating_to,m.sponsor_way,m.donating_on,p.username
	f=km.values()
	return render(request,'html/mainpage.html',{'t':h,'ty':c,'o':o,'f':f})

def userreq(request):
	if request.method=="POST":
		u=request.POST.get('uname')
		e=request.POST.get('email')
		ut=request.POST.get('utype')
		ud=request.POST.get('uid')
		ms=request.POST.get('msg')
		f=request.FILES['fe']
		a="Hi welcome "+u+"<br/>" "Requested your Role as "+ut+"<br/>" "Your ID is:"+ud
		t = EmailMessage("UserRole Change",a,settings.EMAIL_HOST_USER,[settings.ADMINS[0][1],e])
		t.content_subtype='html'
		t.attach(f.name,f.read(),f.content_type)
		t.send()
		if t==1:
			return redirect('/ureq')
	return render(request,'html/userreq.html')

def perm(request):
	ty=User.objects.all()
	return render(request,'html/perm.html',{'q':ty})

def userdelete(request,u):
	c=User.objects.get(id=u)
	if request.method == "POST":
		c.delete()
		return redirect('/per')
	return render(request,'html/admindelete.html',{'d':c})



def gvper(request,k):
	r = User.objects.get(id=k)
	if request.method=="POST":
		k=UsPerm(request.POST,instance=r)
		if k.is_valid():
			k.save()
			return redirect('/per')
	k = UsPerm(instance=r)
	return render(request,'html/gvp.html',{'y':k})


def dashboard(request):
	return render(request,'html/dashboard.html')

def donate(request):
	w=Donate.objects.filter(uid_id=request.user.id)
	z=OccDonate.objects.filter(uid_id=request.user.id)
	if request.method == "POST":
		e=DonateForm(request.POST)
		f=OccDonateForm(request.POST)
		if e.is_valid():
			t=e.save(commit=False) 
			t.username=request.user.username
			t.email=request.user.email
			t.uid_id=request.user.id
			t.save()
			return redirect('/don')
		elif f.is_valid():
			r=f.save(commit=False)
			r.username=request.user.username
			r.email=request.user.email
			r.uid_id=request.user.id
			r.save() 
			return redirect('/don')    
	e=DonateForm()
	f=OccDonateForm()
	return render(request,'html/donate.html',{'a':e,'x':w,'b':f,'h':z})

def update(request,a):
	u=Donate.objects.get(id=a)
	if request.method == "POST":
		v=UpdateForm(request.POST,instance=u)
		if v.is_valid():
			v.save()
			return redirect('/don')
	z=UpdateForm(instance=u)
	return render(request,'html/update.html',{'p':z})


def delete(request,b):
	c=Donate.objects.get(id=b)
	if request.method == "POST":
		c.delete()
		return redirect('/don')
	return render(request,'html/userdelete.html',{'d':c})

def payment(request):
	return render(request,'html/payment.html')

def message(request):
	return render(request,'html/message.html')

def joinus(request):
	if request.method=="POST":
		u=request.POST.get('uname')
		e=request.POST.get('email')
		p=request.POST.get('ph')
		ms=request.POST.get('msg')
		a="Hi "+u+",""<br/>" "Thank you for Joining us" "<br/>" "We are conducting a Campaign on June 1st at Annamacharya Institute of Technology and Sciences, Tirupati," "<br/>" "Venkatapuram Village,Renigunta Mandal, Andhra Pradesh 517520." "<br/>" "Looking Forward to See you there at 9:00Am Sharp""<br/>" "We will also remaind you on a day before the Campaign"
		t = EmailMessage("Joining us",a,settings.EMAIL_HOST_USER,[settings.ADMINS[0][1],e])
		t.content_subtype='html'
		t.send()
		if t==1:
			return redirect('/')
	return render(request,'html/joinus.html')

def updateprofile(request):
	return render(request,'html/profileupdate.html')

def updatedetails(request):
	if request.method == "POST":
		p=UpForm(request.POST,instance=request.user)
		if p.is_valid():
			p.save()
		return redirect('/profile')
	p=UpForm(instance=request.user)
	q=Orgdetails.objects.get(id=request.user.id)
	return render(request,'html/updatedetails.html',{'u':p})

def change(request):
	if request.method == "POST":
		g=ChpasForm(user=request.user,data=request.POST)
		if g.is_valid():
			g.save()
			return redirect('/lg')
	g=ChpasForm(user=request)
	return render(request,'html/changepassword.html',{'c':g})

def occdetails(request,bi):
	o=OccDonate.objects.get(id=bi)
	if request.method == "POST":
		p=OccDonateForm(request.POST,instance=o)
		if p.is_valid():
			p.save()
			return redirect('/don')
	q=OccDonateForm(instance=o)
	return render(request,'html/occdetails.html',{'q':q})

def occdelete(request,ai):
	d=OccDonate.objects.get(id=ai)
	if request.method == "POST":
		d.delete()
		return redirect('/don')
	return render(request,'html/userdelete.html',{'d':d})


def orgupdate(request):
	if request.method == "POST":
		p=OrgForm(request.POST)
		u=OrgUp(request.POST)
		if p.is_valid() and u.is_valid():
			p.save()
			u.save()
		return redirect('/profile')
	p=OrgForm()
	u=OrgUp()
	return render(request,'html/updatedetails.html',{'u':p,'p':u})


def orgreq(request):
	if request.method == "POST":
		o=OrgForm(request.POST)
		if o.is_valid():
			o.save()
		return redirect('/mn')
	o=OrgForm()
	return render(request,'html/orgreq.html',{'o':o})


def details(request):
	return render(request,'html/details.html')