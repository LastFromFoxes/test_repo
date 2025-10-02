from datetime import timedelta

import pytest
from django.utils import timezone
from faker import Faker
from rest_framework.test import APIClient

from apps.cards.models import (
    CardBrowsingHistory,
    Feature,
    ProductCard,
    PurchaseHistory,
    Tariff,
)
from apps.users.models import User

fake = Faker()


@pytest.fixture
def user():
    return User.objects.create_user(email=fake.unique.email())


@pytest.fixture
def user2():
    return User.objects.create_user(email=fake.unique.email(), password=fake.unique.password())


@pytest.fixture
def card():
    return ProductCard.objects.create(title=fake.sentence(nb_words=3), description=fake.sentence(nb_words=15))


@pytest.fixture
def create_card_factory(db):
    def wrapper(title: str, description: str):
        card = ProductCard.objects.create(title=title, description=description)
        return card

    return wrapper


@pytest.fixture
def product_factory(db):
    def wrapper(title: str, description: str):
        product = ProductCard.objects.create(title=title, description=description)
        return product

    return wrapper


@pytest.fixture
def add_card_to_purchase_factory(db):
    def wrapper(
        user_: User,
        tariff_id: int,
        usage_period,
        month_days_amount: int = 31,
    ):
        """Month days amount"""
        usage_period_days = month_days_amount * usage_period
        current_dt = timezone.now()
        purchased_until = current_dt + timedelta(days=usage_period_days)
        purchased = PurchaseHistory.objects.create(
            user=user_,
            tariff_id=tariff_id,
            purchased_until=purchased_until,
        )
        return purchased

    return wrapper


@pytest.fixture
def create_feature_factory(db):
    def wrapper(title: str, tariff: Tariff):
        feature = Feature.objects.create(title=title, tariff=tariff)
        return feature

    return wrapper


@pytest.fixture
def create_tariff_factory(db):
    def wrapper(title: str, price: int, card: ProductCard):
        tariff = Tariff.objects.create(title=title, price=price, card=card)
        return tariff

    return wrapper


@pytest.fixture
def add_card_to_liked_factory(db):
    def wrapper(user_: User, card_: ProductCard):
        rating = card_.rating
        rating.users_liked.add(user_)
        return rating

    return wrapper


@pytest.fixture
def api_client():
    return APIClient()
