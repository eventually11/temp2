from faker import Faker
import random


class SaasPartnerTaskFaker:
    def __init__(self):
        self.fake = Faker()

    def generate_saas_partner_task(self):
        return {
            "id": self.fake.random_number(digits=5),
            "tenant": self.fake.random_number(digits=5),
            "order": random.choice([None, self.fake.random_number(digits=5)]),
            "sender": self.fake.random_number(digits=5),
            "hub": self.fake.random_number(digits=5),
            "zone": random.choice([None, self.fake.zipcode()]),
            "flow": self.fake.random_number(digits=5),
            "task_pool": self.fake.random_number(digits=5),
            "partner": self.fake.random_number(digits=5),
            "title": self.fake.sentence(),
            "content": self.fake.text(),
            "date": self.fake.date(),
            "time_slot": f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}",
            "type": self.fake.random_element(elements=("type1", "type2", "type3")),
            "service_time": self.fake.random_number(digits=2),
            "start": [],
            "end": [],
            "service_fee": None,
            "items": {},
            "start_task_validation": {},
            "end_task_validation": {},
            "status_code": self.fake.random_element(elements=("pending", "in_progress", "completed")),
            "status_group": self.fake.random_element(elements=("group1", "group2", "group3")),
        }

    def generate_saas_partner_task_event_log(self):
        return {
            "id": self.fake.random_number(digits=5),
            "tenant": self.fake.random_number(digits=5),
            "task": self.fake.random_number(digits=5),
            "event": self.fake.random_element(elements=("event1", "event2", "event3")),
            "status_code": self.fake.random_element(elements=("status1", "status2", "status3")),
            "actual_time": self.fake.unix_time(),
            "coordinate": f"{self.fake.latitude()},{self.fake.longitude()}",
            "remark": self.fake.text(),
        }

    def generate_saas_partner_task_validation_step(self):
        return {
            "id": self.fake.random_number(digits=5),
            "tenant": self.fake.random_number(digits=5),
            "task": self.fake.random_number(digits=5),
            "dummy": self.fake.word(),
        }

    def generate_saas_partner_task_partner_fee(self):
        return {
            "id": self.fake.random_number(digits=5),
            "tenant": self.fake.random_number(digits=5),
            "task": self.fake.random_number(digits=5),
            "dummy": self.fake.word(),
        }

# Usage
faker = SaasPartnerTaskFaker()
fake_partner_task = faker.generate_saas_partner_task()
fake_partner_task_event_log = faker.generate_saas_partner_task_event_log()
fake_partner_task_validation_step = faker.generate_saas_partner_task_validation_step()
fake_partner_task_partner_fee = faker.generate_saas_partner_task_partner_fee()

print('Fake saas_partner_task:', fake_partner_task)
print('Fake saas_partner_task_event_log:', fake_partner_task_event_log)
print('Fake saas_partner_task_validation_step:', fake_partner_task_validation_step)
print('Fake saas_partner_task_partner_fee:', fake_partner_task_partner_fee)