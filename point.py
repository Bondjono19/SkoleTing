import math

class statistics:
    def variance(datapoints):
        datapoint_mean = statistics.mean(datapoints)
        return sum((datapoint - datapoint_mean) ** 2 for datapoint in datapoints) / (len(datapoints) - 1)

    def standard_deviation(datapoints):
        return math.sqrt(statistics.variance(datapoints))

    def mean(datapoints):
        return sum(datapoints) / len(datapoints)

    def median(datapoints):
        n = len(datapoints)

        if n % 2 == 0:
            return (datapoints[n//2-1] + datapoints[n//2])/2
        else:
            return datapoints[n//2]

    def midrange(datapoints):
        return (min(datapoints) + max(datapoints)) / 2

    def mode(datapoints):
        return max(set(datapoints), key=datapoints.count)

    def population_variance(datapoints):
        datapoint_mean = statistics.mean(datapoints)

        return sum(
            (datapoint - datapoint_mean) ** 2
            for datapoint in datapoints
        ) / len(datapoints)

    def range(datapoints):
        return max(datapoints) - min(datapoints)

    def sample_variance(datapoints):
        datapoint_mean = statistics.mean(datapoints)

        return sum(
            (datapoint - datapoint_mean) ** 2
            for datapoint in datapoints
        ) / (len(datapoints) - 1)


def main():
    input_numbers = input("Enter numbers separated by commas: ")
    datapoints = [float(datapoint) for datapoint in input_numbers.split(",")]
    datapoints.sort()

    print()
    print(f"Sorted datapoints: {' '.join(str(datapoint) for datapoint in datapoints)}")
    print(f"{'Variance':<20}:", f"{statistics.variance(datapoints):>10.2f}")
    print(f"{'Standard deviation':<20}:", f"{statistics.standard_deviation(datapoints):>10.2f}")
    print(f"{'Mean':<20}:", f"{statistics.mean(datapoints):>10.2f}")
    print(f"{'Median':<20}:", f"{statistics.median(datapoints):>10.2f}")
    print(f"{'Midrange':<20}:", f"{statistics.midrange(datapoints):>10.2f}")
    print(f"{'Mode':<20}:", f"{statistics.mode(datapoints):>10.2f}")
    print(f"{'Population variance':<20}:", f"{statistics.population_variance(datapoints):>10.2f}")
    print(f"{'Range':<20}:", f"{statistics.range(datapoints):>10.2f}")
    print(f"{'Sample variance':<20}:", f"{statistics.sample_variance(datapoints):>10.2f}")

if __name__ == "__main__":
    main()