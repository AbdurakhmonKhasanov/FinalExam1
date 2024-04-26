from django.db.models import Model, CharField, EmailField, ImageField


class Student(Model):
    image = ImageField(upload_to='student', null=True)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = EmailField(unique=True)
    phone_number = CharField(max_length=15, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()