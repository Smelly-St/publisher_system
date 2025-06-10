from django.db import models
from projects.models import Project
from authors.models import Author

class Contract(models.Model):
    contract_number = models.CharField('Номер договора', max_length=50)
    signed_date = models.DateField('Дата заключения')
    amount = models.DecimalField('Сумма', max_digits=10, decimal_places=2)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.contract_number} — {self.author}"