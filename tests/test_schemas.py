import pytest
from app.model.schemas import CustomerBaseSchema


@pytest.fixture
def custom_costumer():
    return {
        'corporate_name': 'custom',
        'address': 'addr',
        'declared_billing': '1235',
        'bank_data': [
            {
                'bank': 'bank',
                'account': '123456',
                'bank_branch': '89874'
            },
        ]
    }


def test_valid_costumer(custom_costumer):
    try:
        _ = CustomerBaseSchema(**custom_costumer)
    except ValueError:
        assert False
    else:
        assert True
