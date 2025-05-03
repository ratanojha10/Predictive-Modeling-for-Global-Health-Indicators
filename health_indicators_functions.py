import pandas as pd
import numpy as np


def non_available_columns(data, req_vars):

    for req_var in req_vars:
        if req_var not in data.keys():
            data[req_var] = [np.nan] * len(data)

    return data


def calc_mean_bmi(cluster):

    if "B19_01" not in cluster.keys():
        cluster["B19_01"] = [np.nan] * len(cluster)

    cluster = non_available_columns(cluster, ["B19_01"])

    valid_cases = cluster.query('1200 < V445 < 6000 & V213 != 1 & (V208 == 0 | B19_01 >= 2)')

    try:
        cluster_mean_bmi = round(np.mean(valid_cases["V445"])/100, 2)
    except:
        cluster_mean_bmi = np.nan
    try:
        cluster_median_bmi = round(np.median(valid_cases["V445"]) / 100, 2)
    except:
        cluster_median_bmi = np.nan

    # print("bmi", len(valid_cases), cluster_mean_bmi)

    return cluster_mean_bmi, cluster_median_bmi


def calc_stunned_percentage(cluster):
    stunned_cases = \
        cluster.query('HC70 < -200')

    valid_cases = \
        cluster.query('HC70 < 9990')
    if len(valid_cases) != 0:
        stunned_percentage = round(100 * (len(stunned_cases)/len(valid_cases)), 2)
        # print(stunned_percentage)
    else:
        # print(cluster["HC70"])

        stunned_percentage = np.nan

    return stunned_percentage


def calc_under5_mortality_rate(cluster):
    under_5_cases = cluster.query('B7 < 60')
    all_cases = cluster.query('B5 == 1 | B5 == 0')

    if len(all_cases) != 0:
        under5_mortality_rate = round(100 * (len(under_5_cases)/len(all_cases)), 2)
    else:
        under5_mortality_rate = np.nan

    # print(under5_mortality_rate)

    return under5_mortality_rate


def calc_fully_vaccinated_children_rate(cluster):

    cluster = non_available_columns(cluster, ["B19"])

    fully_vaccinated = \
        cluster.query('H0 == 1 & H1 == 1 & H0 == 1 & H2 == 1 & H3 == 1 & '
                      'H4 == 1 & H5 == 1 & H6 == 1 & H7 == 1 & H8 == 1 & H9 == 1 & B5 == 1 & 12 < B19 < 60')

    between_1_4 = cluster.query('B5 == 1 & 12 < B19 < 60')

    if len(between_1_4) != 0:
        fully_vaccinated_children_rate = round(100 * (len(fully_vaccinated) / len(between_1_4)), 2)
    else:
        fully_vaccinated_children_rate = np.nan

    # print(fully_vaccinated_children_rate)

    return fully_vaccinated_children_rate


def calc_unmet_need_rate(cluster):

    if "V626A" not in cluster.keys():

        if "V626" in cluster.keys():
            cluster["V626A"] = cluster["V626"]

    unmet_need = cluster.query('V626A == 1 | V626A == 2')

    # active_women = cluster.query('0 < V528 < 30')
    total_demand = cluster.query('V626A == 1 | V626A == 2 | V626A == 3 | V626A == 4')
    # active_women2 = cluster.query('V626A == 1 | V626A == 2 | V626A == 3 | V626A == 4 | V626A == 7')
    # active_women3 = cluster.query('V502 == 1 | 0 < V528 < 30')
    # print(len(active_women), len(active_women1), len(active_women2),len(active_women3))
    # print(len(cluster), len(unmet_need), len(total_demand))

    if len(total_demand) != 0:
        unmet_need_rate = round(100 * (len(unmet_need) / len(total_demand)), 2)
    else:
        unmet_need_rate = np.nan

    # print(unmet_need_rate)

    return unmet_need_rate


def calc_skilled_birth_attendant_rate(cluster):
    skilled_attendant = cluster.query('M3A == 1 | M3B == 1 | M3C == 1')

    all_birth_5year = cluster.query('M3A == 1 | M3B == 1 | M3C == 1 | M3D == 1 | M3E == 1 | M3F == 1 | M3G == 1 | '
                                    'M3H == 1 | M3I == 1 | M3J == 1 | M3K == 1 | M3L == 1 | M3M == 1 | M3N == 1')
    # print(len(skilled_attendant), len(all_birth_5year), len(cluster))

    if len(all_birth_5year) != 0:
        skilled_birth_attendant_rate = round(100 * (len(skilled_attendant) / len(all_birth_5year)), 2)
    else:
        skilled_birth_attendant_rate = np.nan

    # print(skilled_birth_attendant_rate)

    return skilled_birth_attendant_rate