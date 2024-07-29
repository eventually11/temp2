from faker import Faker
import random

class SaasFaker:
    def __init__(self):
        self.fake = Faker()

    def generate_saas_location_nearby(self):
        return {
            "id": self.fake.random_number(digits=5),
            "name": self.fake.company(),
            "coordinate": f"{self.fake.latitude()},{self.fake.longitude()}"
        }

    def generate_saas_work_order(self):
        return {
            "id": self.fake.random_number(digits=5),
            "tenant": self.fake.random_number(digits=5),
            "sender": {},
            "flow": {},
            "hub": {},
            "zone": random.choice([None, self.fake.random_number(digits=5)]),
            "start_date": self.fake.date(),
            "start_time": f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}",
            "end_date": self.fake.date(),
            "end_time": f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}",
            "start": {},
            "end": {},
            "items": {},
            "references": [],
            "fee": {},
            "reviewed": random.choice(["yes", "no", "not_applicable"]),
            "scheduled_time": self.fake.unix_time(),
            "auto_publish_time": self.fake.unix_time(),
            "status_code": {},
            "estimation": [],
            "distance": [],
            "channel": {}
        }

# Usage
saas_faker = SaasFaker()
fake_location = saas_faker.generate_saas_location_nearby()
fake_work_order = saas_faker.generate_saas_work_order()

print('Fake saas_location_nearby:', fake_location)
print('Fake saas_work_order:', fake_work_order)
