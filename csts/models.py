from django.db import models
from decimal import Decimal


class Port(models.Model):
    id = models.AutoField(primary_key=True)
    port_name = models.CharField(verbose_name="Порт", max_length=50)
    country_name = models.CharField(verbose_name="Страна", max_length=50)
    cost_up = models.DecimalField(verbose_name="Цена погрузки 1м3", max_digits=5, decimal_places=2,
                                  default=Decimal('000.00'))
    cost_down = models.DecimalField(verbose_name="Цена разгрузки 1м3", max_digits=5, decimal_places=2,
                                    default=Decimal('000.00'))

    class Meta:
        verbose_name = "Порт"
        verbose_name_plural = "Порты"

    def __str__(self):
        return self.port_name

    def get_port_name(self):
        return self.port_name


class TransportEdge(models.Model):
    id = models.AutoField(primary_key=True)
    source_port = models.ForeignKey(Port, on_delete=models.DO_NOTHING, related_name='source_port_set',
                                    verbose_name="Порт погрузки")
    target_port = models.ForeignKey(Port, on_delete=models.DO_NOTHING, related_name='target_port_set',
                                    verbose_name="Порт выгрузки")
    line_name = models.CharField(max_length=50, verbose_name="Наименование морской линии")
    cost_line = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('000.00'),
                                    verbose_name="Стоимость перевозки 1м3")
    travel_day = models.IntegerField(null=False, default=1, verbose_name="Транзитное время(дней)")

    class Meta:
        verbose_name = "Перевозка"
        verbose_name_plural = "Перевозки"

    def __str__(self):
        return str(self.source_port) + ' -> ' + str(self.target_port)


