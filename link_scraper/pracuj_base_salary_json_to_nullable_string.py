from typing import Optional

class BaseSalary:
    def __init__(
        self,
        min_value: Optional[float],
        max_value: Optional[float],
        unit: Optional[str],
        currency: Optional[str]
    ):
        self.min_value = min_value
        self.max_value = max_value
        self.unit = unit
        self.currency = currency


def pracuj_base_salary_json_to_str(base_salary: Optional[dict]) -> Optional[BaseSalary]:
    if base_salary is not None:
        if (
            base_salary['minValue'] and 
            base_salary['maxValue'] and 
            base_salary['currency'] and 
            base_salary['value']
        ):
            return BaseSalary(
                min_value=base_salary['minValue'],
                max_value=base_salary['maxValue'],
                unit=base_salary['value'],
                currency=base_salary['currency']
            )
        else:
            for key in base_salary.keys():
                print(key)
            raise Exception(f"Base salary provided but couldn't be interpretted. Keys: {base_salary.keys()}")
    return base_salary