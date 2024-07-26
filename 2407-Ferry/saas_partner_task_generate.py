import faker    
import radom

class SaasPartnerTaskFaker:
    def __init__(self):
        self.fake = Faker()

    def generate_saas_partner_task(self):
        return {
            "id": self.fake.random_number(digits=11, fix_len=True),
            #test check if id is valid 
            
            "tenant": self.fake.random_number(digits=8, fix_len=True),
            #digits=8
            "order": random.choice([None, self.fake.random_number(digits=11, fix_len=True)]),
            
            "sender": self.fake.random_number(digits=11, fix_len=True),
            "hub": self.fake.random_number(digits=11, fix_len=True),
            "zone": random.choice([None, self.fake.zipcode()]),
            "flow": self.fake.random_number(digits=4, fix_len=True),
            
            "task_pool": self.fake.random_number(digits=11, fix_len=True),
            "partner": self.fake.random_number(digits=11, fix_len=True),
            "title": self.fake.sentence(),
            "content": self.fake.text(),
            "date": self.fake.date(),
            "time_slot": f"{random.randint(0, 23):02d}{random.randint(0, 59):02d}",
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