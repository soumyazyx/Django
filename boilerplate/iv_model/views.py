from django.shortcuts import render
from .models import Employee


def home(request):
    # emp1 = Employee(name="Soumya", addr="hyd")
    # emp1.save()
    employee_records = []
    print(Employee.objects.all())
    for record in Employee.objects.all():
        print(record.name)
        print(record.addr)
        employee_records.append({'name': record.name, 'addr': record.addr})
    print(employee_records)
    return render(request, 'iv_model/home.html', {'records': employee_records})
