from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields.related import ForeignKey, OneToOneField

class Card(models.Model):
  class Suit(models.IntegerChoices):
    DIAMOND = 1
    SPADE = 2
    HEART = 3
    CLUB = 4

  class Number(models.IntegerChoices):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

  suit = models.IntegerField(choices = Suit.choices)
  number = models.IntegerField(choices = Number.choices)
  code = models.IntegerField(validators = [MaxValueValidator(52), MinValueValidator(1)])

class PocketHand(models.Model):
  card_one = ForeignKey(Card, on_delete=models.CASCADE, related_name="card_one")
  card_two = ForeignKey(Card, on_delete=models.CASCADE, related_name="card_two")
  code = models.IntegerField(validators = [MaxValueValidator(2652), MinValueValidator(1)])
  ranking = models.IntegerField(validators = [MaxValueValidator(169), MinValueValidator(1)])