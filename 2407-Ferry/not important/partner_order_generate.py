import pytest
from faker import Faker
import random
from hypothesis import given, settings
from hypothesis.strategies import integers, text, lists, floats, composite, datetimes

fake = Faker()


@composite
def saas_partner_order_strategy(draw):
  
    saas_partner_order_type = {
        'code': draw(integers(min_value=1000, max_value=9999)),
        'type_name': draw(text(min_size=1)),
        'name': draw(text(min_size=1))
    }

    saas_sender = {
        'id': draw(integers(min_value=1, max_value=100)),
        'name': draw(text(min_size=1))
    }

    saas_hub = {
        'id': draw(integers(min_value=1, max_value=10)),
        'name': draw(text(min_size=1))
    }

    saas_vehicle_type = draw(lists(text(min_size=1), min_size=1, max_size=3))

    common_address = {
        'street': draw(text(min_size=1)),
        'city': draw(text(min_size=1)),
        'state': draw(text(min_size=1)),
        'zipcode': draw(text(min_size=1))
    }

    sm_sender_address = common_address

    common_service_fee = {
        'amount': draw(floats(min_value=10.0, max_value=100.0)),
        'currency': draw(text(min_size=1, max_size=3))
    }

    saas_flow_standard_task_validation_sequence = {
        'id': draw(integers(min_value=1, max_value=10)),
        'name': draw(text(min_size=1))
    }

    saas_flow_tenant_task_validation_sequence = saas_flow_standard_task_validation_sequence

    saas_partner_task_status_group = {
        'status_code': draw(integers(min_value=1, max_value=5)),
        'description': draw(text(min_size=1))
    }

  
    return {
        'id': draw(integers(min_value=1000, max_value=9999)),
        'tenant': draw(integers(min_value=1, max_value=100)),
        'flow': draw(integers(min_value=1, max_value=10)),
        'sender': saas_sender,
        'hub': saas_hub,
        'dispatch_pool': draw(integers(min_value=1, max_value=5)),
        'vehicle_type': saas_vehicle_type,
        'start_time': draw(datetimes()),
        'end_time': draw(datetimes()),
        'title': draw(text(min_size=1)),
        'route_description': draw(text(min_size=1)),
        'tags': draw(lists(text(min_size=1), min_size=1, max_size=5)),
        'overview': draw(text(min_size=1)),
        'content': draw(text(min_size=1)),
        'type': saas_partner_order_type,
        'start': common_address,
        'end': sm_sender_address,
        'service_fee': common_service_fee,
        'start_task_validation': saas_flow_standard_task_validation_sequence,
        'end_task_validation': saas_flow_tenant_task_validation_sequence,
        'status_group': saas_partner_task_status_group
    }


@given(saas_partner_order_strategy())
@settings(max_examples=10) 
def test_saas_partner_order_structure(order):

    assert isinstance(order['id'], int)
    assert isinstance(order['tenant'], int)
    assert isinstance(order['flow'], int)
    assert isinstance(order['sender'], dict)
    assert isinstance(order['hub'], dict)
    assert isinstance(order['dispatch_pool'], int)
    assert isinstance(order['vehicle_type'], list)
    assert isinstance(order['start_time'], str)
    assert isinstance(order['end_time'], str)
    assert isinstance(order['title'], str)
    assert isinstance(order['route_description'], str)
    assert isinstance(order['tags'], list)
    assert isinstance(order['overview'], str)
    assert isinstance(order['content'], str)
    assert isinstance(order['type'], dict)
    assert isinstance(order['start'], dict)
    assert isinstance(order['end'], dict)
    assert isinstance(order['service_fee'], dict)
    assert isinstance(order['start_task_validation'], dict)
    assert isinstance(order['end_task_validation'], dict)
    assert isinstance(order['status_group'], dict)

 
    assert order['id'] >= 1000 and order['id'] <= 9999
    assert order['tenant'] >= 1 and order['tenant'] <= 100
    assert order['flow'] >= 1 and order['flow'] <= 10
    assert order['dispatch_pool'] >= 1 and order['dispatch_pool'] <= 5


if __name__ == '__main__':
    pytest.main()
