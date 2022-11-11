from pydantic import BaseModel, validator
import re

ONLY_NUMBERS_REGEX = re.compile("^[0-9]+$")

'''
Conjunto de dados básicos de um cliente:
- Razão social
- Telefone
- Endereço
- Data de cadastro
- Faturamento declarado
- Dados bancários (Um cliente pode ter mais de um banco)
    - Ag
    - Conta
    - Banco

'''


class BankDataSchema(BaseModel):
    bank: str
    account: str
    bank_branch: str

    @validator("account", "bank_branch")
    def check_only_numbers(cls, v: str, **kwargs: int) -> str:

        if not ONLY_NUMBERS_REGEX.match(v):
            raise ValueError("Invalid field, only numbers allowed!")

        return v


class CustomerBaseSchema(BaseModel):
    corporate_name: str
    address: str
    declared_billing: str
    bank_data: list[BankDataSchema]
