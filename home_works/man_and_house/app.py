from gen import gen_house_objects, gen_consumer_object
from main import get_recs


def app():
    houses = gen_house_objects(100)
    consumer = gen_consumer_object()
    recs = get_recs(house_list=houses, consumer=consumer)
    return recs


print(app())

