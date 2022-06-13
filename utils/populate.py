from controllers.CityDAO import CityDAO
from controllers.ProblemDAO import ProblemDAO
from controllers.CustomersDAO import CustomersDAO

from models.city import City
from models.consumer import Consumer
from models.Problem import Problem

city_controller = CityDAO()
problem_controller = ProblemDAO()
customer_controller = CustomersDAO()

print("Init populate")
print("...")
print("Populating cities...", end="")

cities = ["Juazeiro", "Crato", "Barbalha", "Potengi", "Missão velha"]
for city in cities:
    city_model = City(name=city)
    city_controller.create(city_model)

print("OK!")
print("Populating problems...", end="")

problems = [
    ["Cabo cortado", 1, "Identificamos que seu cabo deu problema, normalizaremos em duas horas"],
    ["Pagamento inválido", 1, "Identificamos um erro no seu pagamento, por isso, sua conexão foi suspensa"],
    ["Manutenção na área", 2, "Estamos realizando manutenção na sua área, normalizaremos em 30 minutos"],
    ["Roteador danificado", 3, "Seu roteador está danificado, estamos descolando uma equipe para normalização"]
]
for problem in problems:
    problem_model = Problem(description=problem[0], priority=problem[1], message=problem[2])
    problem_controller.create(problem_model)

print("OK!")
consumers = [
    {
        "name": "Lucas",
        "ip": "192.168.1.169",
        "city_id": 1,
        "problem_id": 0
    },
    {
        "name": "Márcio",
        "ip": "192.168.1.169",
        "city_id": 2,
        "problem_id": 0
    },
    {
        "name": "Pedro",
        "ip": "8.8.8.8",
        "city_id": 3,
        "problem_id": 0
    },
    {
        "name": "Régio",
        "ip": "8.8.8.8",
        "city_id": 4,
        "problem_id": 0
    },
    {
        "name": "Álvaro",
        "ip": "192.168.1.56",
        "city_id": 5,
        "problem_id": 0
    },
    {
        "name": "Antônio",
        "ip": "192.168.1.138",
        "city_id": 5,
        "problem_id": 0
    },
    {
        "name": "Edson",
        "ip": "192.168.1.139",
        "city_id": 3,
        "problem_id": 0
    },
    {
        "name": "Caio",
        "ip": "8.8.8.8",
        "city_id": 1,
        "problem_id": 0
    },
    {
        "name": "Marcelo",
        "ip": "8.8.8.8",
        "city_id": 2,
        "problem_id": 0
    },
    {
        "name": "Tiago",
        "ip": "8.8.8.8",
        "city_id": 2,
        "problem_id": 0
    }
]
for consumer in consumers:
    consumer_model = Consumer(name=consumer['name'], cellphone="88981994454", city_id=consumer['city_id'], ip=consumer['ip'], problem_id=0, id=0)
    customer_controller.create(Customers=consumer_model)
print("OK!")