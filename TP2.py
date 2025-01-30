import numpy as np
import time
from jmetal.algorithm.singleobjective.local_search import LocalSearch
from jmetal.operator import BitFlipMutation

from jmetal.util.observer import PrintObjectivesObserver
from jmetal.util.solution import print_function_values_to_file, print_variables_to_file
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.operator import PolynomialMutation

from FloatPairs import FloatPairs


def local_search_run(number_of_bits, min_value, max_value, max_evaluations, mutation_probability):
    # CrÃ©e une instance du problÃ¨me
    problem = FloatPairs(number_of_floats=number_of_bits, min_value=min_value, max_value=max_value)

    mutation_probability = mutation_probability / problem.number_of_variables()

    # Configure l'algorithme de recherche locale
    algorithm = LocalSearch(
        problem=problem,
        mutation=PolynomialMutation(probability=mutation_probability),
        termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations),
    )

    algorithm.observable.register(observer=PrintObjectivesObserver(100))

    # Mesure le temps de calcul
    start_time = time.time()
    algorithm.run()
    end_time = time.time()

    result = algorithm.solutions[0]
    print(result)
    # Retourne les rÃ©sultats sous forme de dictionnaire
    return {
        "fitness": - result.objectives[0],
        "solution": result.variables,
        "computing_time": end_time - start_time,
    }

def experiment_runs(runs=20, number_of_bits=512, min_value=-5.0, max_value=5.0, max_evaluations=10000, mutation_probability=None):
    results = []

    for run in range(runs):
        result = local_search_run(
            number_of_bits=number_of_bits,
            min_value=min_value,
            max_value=max_value,
            max_evaluations=max_evaluations,
            mutation_probability=mutation_probability
        )
        results.append(result)

    # Analyse statistique des rÃ©sultats
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
    }

    return stats

if __name__ == "__main__":
    # ParamÃ¨tres pour l'expÃ©rience
    number_of_bits = 512
    min_value = -1000.0
    max_value = 1000.0
    max_evaluations = 5000
    mutation_probability = 1
    runs = 20

    # Lancer les expÃ©riences
    stats = experiment_runs(
        runs=runs,
        number_of_bits=number_of_bits,
        max_evaluations=max_evaluations,
        mutation_probability=mutation_probability,
    )

    # Afficher la synthÃ¨se des rÃ©sultats
    print("\nSynthÃ¨se des résultats (20 runs):")
    print(f"Fitness moyenne : {stats['fitness_mean']:.2f}")
    print(f"Fitness mÃ©diane : {stats['fitness_median']:.2f}")
    print(f"Ã‰cart-type de la fitness : {stats['fitness_std']:.2f}")
    print(f"Temps de calcul moyen : {stats['time_mean']:.2f} s")
    print(f"Temps de calcul mÃ©dian : {stats['time_median']:.2f} s")
    print(f"Ã‰cart-type du temps de calcul : {stats['time_std']:.2f} s")