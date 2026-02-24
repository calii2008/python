from typing import optional

def get_name(name: optional[str] = none) -> str:
    if name:
        return name
    return "Anonymus"
print(get_name())

def process_value(value, union[int, str]) -> str:
    if isin