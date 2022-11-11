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


def test_missing_values_costumer():
    try:
        test_costumer = {
            'corporate_name': 'custom',
            'address': 'addr',
            'declared_billing': '1235'
        }
        _ = CustomerBaseSchema(**test_costumer)
    except ValueError:
        assert True
    else:
        assert False


def test_invalid_account_costumer(custom_costumer):
    try:
        test_costumer = custom_costumer
        test_costumer['bank_data'][0]['account'] = 'abc'

        _ = CustomerBaseSchema(**test_costumer)
    except ValueError:
        assert True
    else:
        assert False

def test_invalid_bank_branch_costumer(custom_costumer):
    try:
        test_costumer = custom_costumer
        test_costumer['bank_data'][0]['bank_branch'] = 'abc'

        _ = CustomerBaseSchema(**test_costumer)
    except ValueError:
        assert True
    else:
        assert False