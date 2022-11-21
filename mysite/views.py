from django.shortcuts import render, redirect
from .models import Doctor, Publicservant, Record, Specialize, Users, Country, Discover, Disease, Diseasetype
from .forms import DoctorForm, CountryForm, DiseaseForm, DiseasetypeForm, DiscoverForm, UserForm, SpecializeForm, ServantForm, RecordForm
from django.http import HttpResponseRedirect
from sqlalchemy import create_engine
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def home(request):
    country =  Country.objects.all()
    context = {
        'country': country
    }
    return render(request, "index.html", context)


def users(request):
    doctors = Doctor.objects.all()
    specializations = Specialize.objects.all()
    servants = Publicservant.objects.all()
    users = Users.objects.all()

    context = {
        'users': users,
        'doctors': doctors,
        'specializations': specializations,
        'servants': servants,
    }

    return render(request, "users.html", context)

def disease(request):
    countries = Country.objects.all()
    diseases = Disease.objects.all()
    diseasetypes = Diseasetype.objects.all()
    discoveries = Discover.objects.all()
    context = {
        'countries': countries,
        'diseases': diseases,
        'diseasetypes': diseasetypes,
        'discoveries': discoveries,
    }

    return render(request, "disease.html", context)

def record(request):
    records = Record.objects.all()

    context = {
        'records': records,
    }

    return render(request, "record.html", context)


def update_country(request, cname):
    country = Country.objects.get(pk=cname)
    form = CountryForm(request.POST or None, instance=country)
    if form.is_valid():
        form.save()
        return redirect('disease')

    context = {
        'country': country,
        'form': form,
    }

    return render(request, 'update_country.html', context)

def delete_country(request, cname):
    country = Country.objects.get(pk=cname)
    country.delete()
    return redirect('disease')

def add_country(request):
    submitted = False
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/disease?submitted=True')
    else:
        form = CountryForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_country.html', {'form':form})


def update_disease(request, disease_code):
    disease = Disease.objects.get(pk=disease_code)
    form = DiseaseForm(request.POST or None, instance=disease)
    if form.is_valid():
        form.save()
        return redirect('disease')

    context = {
        'disease': disease,
        'form': form,
    }

    return render(request, 'update_disease.html', context)

def delete_disease(request, disease_code):
    disease = Disease.objects.get(pk=disease_code)
    disease.delete()
    return redirect('disease')

def add_disease(request):
    submitted = False
    if request.method == "POST":
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/disease?submitted=True')
    else:
        form = DiseaseForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_disease.html', {'form':form})


def update_diseasetype(request, id):
    diseasetype = Diseasetype.objects.get(pk=id)
    form = DiseasetypeForm(request.POST or None, instance=diseasetype)
    if form.is_valid():
        form.save()
        return redirect('disease')

    context = {
        'diseasetype': diseasetype,
        'form': form,
    }

    return render(request, 'update_diseasetype.html', context)

def delete_diseasetype(request, id):
    diseasetype = Diseasetype.objects.get(pk=id)
    diseasetype.delete()
    return redirect('disease')

def add_diseasetype(request):
    submitted = False
    if request.method == "POST":
        form = DiseasetypeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/disease?submitted=True')
    else:
        form = DiseasetypeForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_diseasetype.html', {'form':form})


def update_discover(request, cname, disease_code):
    discover = Discover.objects.get(cname=cname, disease_code=disease_code)
    form = DiscoverForm(request.POST or None, instance=discover)
    if form.is_valid():
        form.save()
        return redirect('disease')

    context = {
        'discover': discover,
        'form': form,
    }

    return render(request, 'update_discover.html', context)

def delete_discover(request, cname, disease_code):
    discover = Discover.objects.get(cname=cname, disease_code=disease_code)
    discover.delete()
    return redirect('disease')

def add_discover(request):
    submitted = False
    if request.method == "POST":
        form = DiscoverForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/disease?submitted=True')
    else:
        form = DiscoverForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_discover.html', {'form':form})


def update_user(request, email):
    user = Users.objects.get(pk=email)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('users')

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'update_user.html', context)

def delete_user(request, email):
    user = Users.objects.get(pk=email)
    user.delete()
    return redirect('users')

def add_user(request):
    submitted = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users?submitted=True')
    else:
        form = UserForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_user.html', {'form':form})


def update_doctor(request, email):
    doctor = Doctor.objects.get(pk=email)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect('users')

    context = {
        'doctor': doctor,
        'form': form,
    }

    return render(request, 'update_doctor.html', context)

def delete_doctor(request, email):
    doctor = Doctor.objects.get(pk=email)
    doctor.delete()
    return redirect('users')

def add_doctor(request):
    submitted = False
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users?submitted=True')
    else:
        form = DoctorForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_doctor.html', {'form':form})


def update_specialize(request, id):
    specialize = Specialize.objects.get(pk=id)
    form = SpecializeForm(request.POST or None, instance=specialize)
    if form.is_valid():
        form.save()
        return redirect('users')

    context = {
        'specialize': specialize,
        'form': form,
    }

    return render(request, 'update_specialize.html', context)

def delete_specialize(request, id):
    specialize = Specialize.objects.get(pk=id)
    specialize.delete()
    return redirect('users')

def add_specialize(request):
    submitted = False
    if request.method == "POST":
        form = SpecializeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users?submitted=True')
    else:
        form = SpecializeForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_specialize.html', {'form':form})


def update_servant(request, email):
    servant = Publicservant.objects.get(pk=email)
    form = ServantForm(request.POST or None, instance=servant)
    if form.is_valid():
        form.save()
        return redirect('users')

    context = {
        'servant': servant,
        'form': form,
    }

    return render(request, 'update_servant.html', context)

def delete_servant(request, email):
    servant = Publicservant.objects.get(pk=email)
    servant.delete()
    return redirect('users')

def add_servant(request):
    submitted = False
    if request.method == "POST":
        form = ServantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users?submitted=True')
    else:
        form = ServantForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_servant.html', {'form':form})


def update_record(request, email, cname, disease_code):
    record = Record.objects.get(email=email, cname=cname, disease_code=disease_code)
    form = RecordForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('record')

    context = {
        'record': record,
        'form': form,
    }

    return render(request, 'update_record.html', context)

def delete_record(request, email, cname, disease_code):
    record = Record.objects.get(email=email, cname=cname, disease_code=disease_code)
    record.delete()
    return redirect('record')

def add_record(request):
    submitted = False
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/record?submitted=True')
    else:
        form = RecordForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_record.html', {'form':form})


def query(request):
    db = create_engine('mysql+mysqldb://root:L#733namnissan@localhost/hw2')
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list9 = []
    list10 = []
    list11 = []

    #query 1:     List the disease code and the description of diseases that are caused by 
    #             “bacteria” (pathogen) and were discovered before 1990.
    q1 = db.execute('SELECT DISTINCT disease_code, description '
                'FROM Discover NATURAL JOIN Disease '
                'WHERE first_enc_date < "1990-01-01" AND pathogen = "bacteria";')
    for disease_code, description in q1:
        list1.append([disease_code, description])


    #query 2:     List the name, surname and degree of doctors who are not specialized in 
    #             “infectious diseases”.
    q2 = db.execute('SELECT DISTINCT name, surname, degree ' 
                    'FROM Users NATURAL JOIN Doctor '
                    'WHERE Users.email NOT IN ( SELECT specialize.email ' 
				    		                    'FROM specialize NATURAL JOIN DiseaseType '
                                                'WHERE description = "infectious" );')
    for name, surname, degree in q2:
        list2.append([name, surname, degree])


    #query 3:   List the name, surname and degree of doctors who are specialized in more 
    #           than 2 disease types.
    q3 = db.execute('SELECT name, surname, degree '
                    'FROM Users NATURAL JOIN Doctor '
                    'WHERE Users.email IN ( SELECT Specialize.email ' 
                                            'FROM Specialize ' 
                                            'GROUP BY Specialize.email '
                                            'HAVING COUNT(*) > 2 );')
    for name, surname, degree in q3:
        list3.append([name, surname, degree])


    #query 4:   For each country list the cname and average salary of doctors who are 
    #           specialized in “virology”.
    q4 = db.execute('SELECT DISTINCT Users.cname, AVG(Users.salary) '
                    'FROM Users NATURAL JOIN Specialize NATURAL JOIN DiseaseType '
                    'WHERE DiseaseType.description = "virology" '
                    'GROUP BY (Users.cname);')
    for cname, avg in q4:
        list4.append([cname, avg])


    #query 5:   List the departments of public servants who report “covid-19” cases in 
    #           more than one country and the number of such public servants who work 
    #           in these departments. (i.e “Dept1 3” means that in the “Dept1” department 
    #           there are 3 such employees.)
    q5 = db.execute('SELECT PublicServant.department, COUNT(PublicServant.email) '
                    'FROM PublicServant NATURAL JOIN Record '
                    'WHERE Record.disease_code = "COV" '
                    'GROUP BY PublicServant.department '
                    'HAVING COUNT(Record.cname) > 1;')
    for dep, num in q5:
        list5.append([dep, num])


    #query 6:   Double the salary of public servants who have recorded covid-19 patients 
    #           more than 3 times.
    q6 = db.execute('SELECT PublicServant.email, Users.salary '
                    'FROM PublicServant NATURAL JOIN Record  '
                    'JOIN Users ON Users.email = PublicServant.email '
                    'WHERE Record.disease_code = "COV" ' 
                    'GROUP BY Record.email '
                    'HAVING COUNT(*) > 3;')
    for email, salary in q6:
        list6.append([email, salary])


    #query 7:   Delete the users whose name contain the substring “bek” or “gul” (e.g. Alibek, Gulsim)
    q7 = db.execute('SELECT DISTINCT email, name, surname FROM Users '
                    'WHERE LOWER(name) LIKE "%%bek%%" '
                    'OR LOWER(name) LIKE "%%gul%%";')
    for email, name, surname in q7:
        list7.append([email, name, surname])


    #query 9:   List the email, name, and department of public servants who have created 
    #           records where the number of patients is between 100000 and 999999
    q9 = db.execute('SELECT DISTINCT Users.email, Users.name, PublicServant.department '
                    'FROM PublicServant NATURAL JOIN Users '
                    'WHERE PublicServant.email IN ( SELECT Record.email '
                                                    'FROM Record '
                                                    'WHERE Record.total_patients >= 100000 AND Record.total_patients <= 999999);')
    for email, name, dep in q9:
        list9.append([email, name, dep])


    #query 10:  List the top 5 counties with the highest number of total patients recorded.
    q10 = db.execute( 'SELECT DISTINCT Record.cname, SUM(Record.total_patients) '
                    'FROM Record '
                    'GROUP BY Record.cname '
                    'ORDER BY SUM(Record.total_patients) DESC '
                    'LIMIT 5;')
    for name, num in q10:
        list10.append([name, num])


    #query 11:  Group the diseases by disease type and the total number of patients treated.
    q11 = db.execute('SELECT DISTINCT Disease.description, DiseaseType.description, SUM( Record.total_patients ) '
                    'FROM Disease NATURAL JOIN Record '
                    'JOIN DiseaseType ON DiseaseType.id = Disease.id '
                    'GROUP BY DiseaseType.description;')
    for desc1, desc2, total in q11:
        list11.append([desc1, desc2, total])

    context = {
        'q1': list1, 'q2': list2, 'q3': list3, 'q4': list4,
        'q5': list5, 'q6': list6, 'q7': list7, 'q9': list9,
        'q10': list10, 'q11': list11
    }

    return render(request, 'query.html', context)


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None: 
            login(request, user)
            fname = user.first_name
            return render(request, "index.html", {"fname": fname})
        
        else:
            messages.error(request, "Error")
            return redirect('signin')

    return render(request, "signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')
