"""
Python script that generates 100 Excel files. Each Excel file should
contain 50 random person names, along with random ages, and random
email addresses.
"""

import os
import pandas as pd
from faker import Faker


fake = Faker('bg_BG')

def generate_data():
    """Data generation function"""

    data = {
        'name': [fake.name() for _ in range(50)],
        'age': [fake.random_int(min=18, max=90) for _ in range(50)],
        'email': [fake.email() for _ in range(50)]
    }

    return data


if __name__ == '__main__':
    os.makedirs('tmp', exist_ok=True)
    for i in range(1, 101):
        data = generate_data()
        df = pd.DataFrame(data)
        df.to_excel(f'tmp/file_{i}.xlsx', index=False)
