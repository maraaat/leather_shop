from djongo import models


class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, null=True, verbose_name="URL")

    class Meta:
        db_table = 'category'
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["id"]

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, verbose_name="Цена")
    discount = models.DecimalField(default=0.0, max_digits=7, decimal_places=2, verbose_name="Скидка в %")
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    color = models.CharField(max_length=200, verbose_name='Цвет')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["id"]

    def __str__(self):
        return self.name
