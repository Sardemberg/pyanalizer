from controllers.ProblemDAO import ProblemDAO
from models.Problem import Problem

problemController = ProblemDAO()
problem = Problem(description="Testando inserção", priority=1)
problemController.show_all()