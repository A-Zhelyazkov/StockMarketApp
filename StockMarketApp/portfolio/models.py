from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Portfolio(models.Model):
    PORTFOLIO_NAME_MAX_LEN = 50

    name = models.CharField(max_length=PORTFOLIO_NAME_MAX_LEN)
    description = models.TextField(
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='portfolios',
    )


class PortfolioItem(models.Model):
    MAX_TICKER_LEN = 8
    ticker = models.CharField(
        max_length=MAX_TICKER_LEN,
        unique=True,
    )
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name='portfolio_items',
    )

