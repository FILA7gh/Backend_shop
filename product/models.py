from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    @property
    def products_list(self):
        return [product.title for product in self.product_set.all()]

    @property
    def products_count(self):
        return self.product_set.count()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    @property
    def category_name(self):
        try:
            return self.category.name
        except:
            return ''

    @property
    def rating(self):
        all_stars = [review.stars for review in self.reviews.all()]
        return round(sum(all_stars) / len(all_stars), 2) if len(all_stars) > 0 else 0

    def __str__(self):
        return self.title


class Review(models.Model):
    CHOICES = ((i, '*' * i) for i in range(1, 6))
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=CHOICES, default=1)

    def __str__(self):
        return self.text

    @property
    def product_title(self):
        return self.product.title
