import numpy as np
import time
import matplotlib.pyplot as plt
from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.operator import SPXCrossover
from jmetal.util.termination_criterion import StoppingByEvaluations
from FloatPairs import FloatPairs
from jmetal.operator import PolynomialMutation
from jmetal.operator import SBXCrossover

# Fonction pour exÃ©cuter l'algorithme avec des paramÃ¨tres modifiables
def genetic_algorithm_run(number_of_bits,min_value,max_value, population_size, offspring_population_size, max_evaluations, mutation_prob, crossover_prob):
    # ProblÃ¨me
    problem = FloatPairs(number_of_floats=number_of_bits, min_value=min_value, max_value=max_value)

    # OpÃ©rateurs
    mutation = PolynomialMutation(probability=mutation_prob/ problem.number_of_variables())
    crossover = SBXCrossover(probability=crossover_prob)

    # Algorithme
    algorithm = GeneticAlgorithm(
        problem=problem,
        population_size=population_size,
        offspring_population_size=offspring_population_size,
        mutation=mutation,
        crossover=crossover,
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations),
    )

    # ExÃ©cution et mesure du temps
    start_time = time.time()
    algorithm.run()
    end_time = time.time()

    # RÃ©sultats
    result = algorithm.solutions[0]

    return {
        "fitness": - result.objectives[0],
        "solution": result.variables,
        "computing_time": end_time - start_time
    }

# Fonction pour exÃ©cuter plusieurs runs et calculer les statistiques
def experiment_runs(runs, number_of_bits, min_value=-5.0, max_value=5.0, population_size=40, offspring_population_size=40, max_evaluations=5000, mutation_prob=1, crossover_prob=1):
    results = []

    for _ in range(runs):
        result = genetic_algorithm_run(
            number_of_bits=number_of_bits,
            min_value=min_value,
            max_value=max_value,
            population_size=population_size,
            offspring_population_size=offspring_population_size,
            max_evaluations=max_evaluations,
            mutation_prob=mutation_prob,
            crossover_prob=crossover_prob,
        )
        results.append(result)

    # Analyse des rÃ©sultats
    fitness_values = [res["fitness"] for res in results]
    computing_times = [res["computing_time"] for res in results]

    stats = {
        "fitness_mean": np.mean(fitness_values),
        "fitness_median": np.median(fitness_values),
        "fitness_std": np.std(fitness_values),
        "time_mean": np.mean(computing_times),
        "time_median": np.median(computing_times),
        "time_std": np.std(computing_times),
        "all_results": results,
        "ft" : fitness_values
    }

    return stats


if __name__ == "__main__":
    # ParamÃ¨tres pour les runs
    number_of_bits = 512
    min_value = -1000.0
    max_value = 1000.0
    population_size = 40
    offspring_population_size = 40
    max_evaluations = 5000
    mutation_prob = 1
    crossover_prob = 1
    runs = 20

    # ExÃ©cution des expÃ©riences
    stats = experiment_runs(
        runs=runs,
        number_of_bits=number_of_bits,
        population_size=population_size,
        offspring_population_size=offspring_population_size,
        max_evaluations=max_evaluations,
        mutation_prob=mutation_prob,
        crossover_prob=crossover_prob
    )

    # Affichage des rÃ©sultats synthÃ©tisÃ©s
    print("\nSynthÃ¨se des résultats aprÃ¨s 20 runs :")
    print(f"Fitness moyenne : {stats['fitness_mean']:.2f}")
    print(f"Fitness mÃ©diane : {stats['fitness_median']:.2f}")
    print(f"Ã‰cart-type de la fitness : {stats['fitness_std']:.2f}")
    print(f"Temps de calcul moyen : {stats['time_mean']:.2f} s")
    print(f"Temps de calcul mÃ©dian : {stats['time_median']:.2f} s")
    print(f"Ã‰cart-type du temps de calcul : {stats['time_std']:.2f} s")
    print(stats['ft'])