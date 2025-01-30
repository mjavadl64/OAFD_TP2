import random
from jmetal.core.problem import Problem
from jmetal.core.solution import FloatSolution

class FloatPairs(Problem) :

    def init(self, number_of_floats, min_value, max_value) :

        self.number_of_floats = number_of_floats 
        self.min_value = min_value 
        self.max_value = max_value 

        self.lower_bound = [self.min_value] * number_of_floats 
        self.upper_bound = [self.max_value] * number_of_floats 

        self.number_of_objectives = 1 
 
        self.obj_directions = [self.MINIMIZE] 
        self.obj_labels = ['Pairs']

    def number_of_variables(self) -> int: 
        return self.number_of_floats 
 
    def number_of_objectives(self) -> int: 
        return 1 
 
    def number_of_constraints(self) -> int: 
        return 0 

    def evaluate(self, solution):
        variables = solution.variables
        pair_count = 0

        for i in range(len(variables) - 1):
            if (variables[i] < 0 and variables[i + 1] > 0) or (variables[i] > 0 and variables[i + 1] < 0):
                pair_count += 1

        solution.objectives[0] = - pair_count
        return solution

    def create_solution(self) -> FloatSolution:

        new_solution = FloatSolution(
            self.lower_bound, self.upper_bound,
            self.number_of_objectives, self.number_of_constraints()
        )

        new_solution.variables = [
            random.uniform(self.lower_bound[i], self.upper_bound[i])
            for i in range(self.number_of_variables())
        ]

        return new_solution

    def name(self) -> str:
        return 'FloatPairsMax'