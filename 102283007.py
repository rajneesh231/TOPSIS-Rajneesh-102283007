import pandas as pd
import numpy as np
import sys


def getRanks(result):

    result['rank'] = result['Performance'].rank(
        ascending=False, method='min').astype('int')
    return result.iloc[:, 1:]


def performanceScore(EuclideanDistance):
    nrows, _ = EuclideanDistance.shape
    p = list()
    for i in range(nrows):
        x = EuclideanDistance.iloc[i, 2] / \
            (EuclideanDistance.iloc[i, 2]+EuclideanDistance.iloc[i, 1])
        p.append(float(f'{x:.2f}'))
    p = pd.DataFrame(p)
    y = pd.concat([EuclideanDistance.iloc[:, 0], p], axis=1,)
    y.columns = [EuclideanDistance.columns[0], "Performance"]
    return y


def Euclid_dist(data, row_names):
    nrows, ncols = data.shape
    Euclid_best = list()
    Euclid_worst = list()
    for i in range(len(row_names)):
        dist_best = 0
        dist_worst = 0
        for j in range(ncols):
            dist_best += (data.iloc[i, j]-data.iloc[-2, j])**2
            dist_worst += (data.iloc[i, j]-data.iloc[-1, j])**2
        Euclid_best.append(dist_best)
        Euclid_worst.append(dist_worst)
    Euclid_best = pd.DataFrame(np.sqrt(Euclid_best))
    Euclid_worst = pd.DataFrame(np.sqrt(Euclid_worst))
    return pd.concat([row_names, Euclid_best, Euclid_worst], axis=1)


def getIdeal(weighted_norm, impacts):
    i = 0
    ideal_best = list()
    ideal_worst = list()
    _, ncols = weighted_norm.shape
    if len(impacts) != ncols:
        raise ValueError(
            "Insufficient number of Impacts Provided. Number of columns and number of impacts do not match.")
    for _, col_data in weighted_norm.items():
        if impacts[i] == '-':
            ideal_best.append(min(col_data.values))
            ideal_worst.append(max(col_data.values))
        elif impacts[i] == '+':
            ideal_best.append(max(col_data.values))
            ideal_worst.append(min(col_data.values))
        else:
            raise ValueError("Impacts can only be + or -")
        i += 1

    ideal_best = pd.DataFrame(
        [ideal_best], columns=list(weighted_norm.columns))
    ideal_worst = pd.DataFrame(
        [ideal_worst], columns=list(weighted_norm.columns))
    weighted_norm = pd.concat([weighted_norm, ideal_best, ideal_worst], axis=0)
    return pd.DataFrame(weighted_norm, columns=weighted_norm.columns)


def weigh(normalized_data, weights):
    _, ncols = normalized_data.shape
    if len(weights) != ncols:
        raise ValueError(
            "Insufficient number of Weights Provided. Number of columns and number of weights do not match.")
    weighted = normalized_data.copy().values
    weighted *= weights
    return pd.DataFrame(weighted, columns=normalized_data.columns)


def normalize(num_data, root_square_sum):
    normalized = num_data.copy().values
    normalized /= root_square_sum
    return pd.DataFrame(normalized, columns=num_data.columns)


def parseArgs():
    if len(sys.argv) != 5:
        raise ValueError("Wrong number of args, 5 expected")
    input_file, weights, impacts, output_file = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    if ',' not in weights or ',' not in impacts:
        raise ValueError("Weights and impacts must be separated by commas.")
    weights = list(map(np.float32, weights.split(",")))
    impacts = impacts.split(",")
    return input_file, weights, impacts, output_file


def main():
    try:
        input_file, weights, impacts, output_file = parseArgs()
    except ValueError as e:
        sys.exit(e)

    try:
        if input_file.split(".")[1] == "xlsx":
            data = pd.read_excel(input_file)
        elif input_file.split(".")[1] == "csv":
            data = pd.read_csv(input_file)
        else:
            raise ValueError("Invalid file extension. Supported formats are .xlsx and .csv.")
    except FileNotFoundError:
        sys.exit(
            "File Not found. Kindly check the file path and provide the correct path.")
    except ValueError as e:
        sys.exit(e)

    data.to_csv("102283007-data.csv", index=False)

    try:
        if data.shape[1] < 3:
            raise ValueError('Number of columns in data less than 3')
        if not data.iloc[:, 1:].applymap(np.isreal).all().all():
            raise ValueError(
                'Non-numeric values found in columns from 2nd to last.')
        num_data = data.loc[:, "P1":"P5"]
        root_square_sum = np.sqrt((num_data ** 2).sum()).values
        normalized_data = normalize(num_data, root_square_sum)
        del (num_data, root_square_sum)
        normalized_data = weigh(normalized_data, weights)
        normalized_data = getIdeal(normalized_data, impacts)
        EuclideanDistance = Euclid_dist(normalized_data, data.iloc[:, 0])
        del (normalized_data)
        result = performanceScore(EuclideanDistance)
        del (EuclideanDistance)
        Ranked = getRanks(result)
        Ranked = pd.concat([data, Ranked], axis=1)
        del (result)
        Ranked.to_csv(output_file, index=False)
    except ValueError as e:
        sys.exit(e)


if __name__ == "__main__":
    main()
