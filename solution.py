import argparse

from core.solution_class import SolutionClass


def main():
    parser = argparse.ArgumentParser(description="Solution script possible arguments.")

    parser.add_argument('--days', type=int, help="total days(N)")
    parser.add_argument('--approach', type=str, help="approach(dynamic-programming/memoization/dynamic-programming-optimized")

    args = parser.parse_args()

    days = args.days
    approach = args.approach

    solution = SolutionClass(days)
    result = ""

    if approach == "dynamic-programming":
        result = solution.using_dynamic_programming()

    elif approach == "memoization":
        result = solution.using_memoization()

    elif approach == "dynamic-programming-optimized":
        result = solution.using_dynamic_programming_with_spaceoptimization()
    else:
        print("Approch not supported")

    print(result)

if __name__ == "__main__":
    main()
