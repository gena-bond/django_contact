from django.db import models
from datetime import date

class Contact(models.Model):
    """Контакты"""
    last_name = models.CharField("Фамилия", max_length=100)
    name = models.CharField("Имя", max_length=100)
    middle_name = models.CharField("Отчество", max_length=100)

    mobile_phone = models.CharField("Мобильный телефон", max_length=20)
    work_phone = models.CharField("Рабочий телефон", max_length=20)

    organization = models.CharField("Организация", max_length=100)
    e_mail = models.EmailField()

    info = models.TextField("Описание", blank=True)

    create_data = models.DateField("Дата создания", default=date.today)
    edit_data = models.DateField("Дата редактирования", default=date.today)

    def save(self, *args, **kwargs):
        ''' On save, update change create_data and edit_data '''
        if not self.id:
            self.create_data = date.today()
        self.edit_data = date.today()
        return super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
