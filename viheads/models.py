from django.db import models
from django.contrib.auth.models import User

class Idea(models.Model):
  """Идея"""
  title = models.CharField(
    max_length=100,
    verbose_name="Название идеи"
  )
  description = models.TextField(
    verbose_name="Описание идеи"
  )
  difficulty = models.ForeignKey(
    "Difficulty",
    on_delete=models.CASCADE,
    verbose_name="Тип сложности",
    related_name="ideas"
  )

  def __str__(self):
      return self.title


class Difficulty(models.Model):
  """Тип сложности"""
  TYPE_CHOICES = [
      (1, "Легкая"),
      (2, "Средняя"),
      (3, "Сложная"),
      (4, "Хардкор"),
  ]

  level = models.PositiveSmallIntegerField(
      choices=TYPE_CHOICES,
      unique=True,
      verbose_name="Уровень сложности"
  )

  def __str__(self):
      return self.get_level_display()


class Cart(models.Model):
  """Корзина"""
  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    verbose_name="Пользователь",
    related_name="carts"
  )

  def __str__(self):
      return f"Корзина пользователя {self.user.username}"


class CartItem(models.Model):
  """Вспомогательная таблица для корзины"""
  cart = models.ForeignKey(
    "Cart",
    on_delete=models.CASCADE,
    verbose_name="Корзина",
    related_name="cart_items"
  )
  idea = models.ForeignKey(
    "Idea",
    on_delete=models.CASCADE,
    verbose_name="Идея",
    related_name="cart_items"
  )
  quantity = models.IntegerField(
    default=1,
    verbose_name="Количество"
  )

  def __str__(self):
      return f"Кол-во: {self.quantity}. Идея: {self.idea.title}"

