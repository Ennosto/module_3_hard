def calc_sum(data_structure):
    summa = 0
    for i in data_structure:
        if isinstance(i, str):
            summa += len(i)
        elif isinstance(i, int or float):
            summa += i
        elif isinstance(i, dict):
            for key, value in i.items():
                summa += len(key)
                summa += value
        elif isinstance(i, (list, set, tuple)):
            for j in i:
                if isinstance(j, int or float):
                    summa += j
                elif isinstance(j, str):
                    summa += len(j)
                elif isinstance(j, dict):
                    for key, value in j.items():
                        summa += len(key)
                        summa += value
                elif isinstance(j, (list, set, tuple)):
                    for d in j:
                        if isinstance(d, int or float):
                            summa += d
                        elif isinstance(d, str):
                            summa += len(d)
                        elif isinstance(d, dict):
                            for key, value in d.items():
                                summa += len(key)
                                summa += value
                        elif isinstance(d, (list, set, tuple)):
                            for r in d:
                                if isinstance(r, int or float):
                                    summa += r
                                elif isinstance(r, str):
                                    summa += len(r)
                                elif isinstance(r, dict):
                                    for key, value in r.items():
                                        summa += len(key)
                                        summa += value
                                elif isinstance(r, (list, set, tuple)):
                                    for t in r:
                                        if isinstance(t, int or float):
                                            summa += t
                                        elif isinstance(t, str):
                                            summa += len(t)
                                        elif isinstance(t, (list, set, tuple)):
                                            for y in t:
                                                if isinstance(y, int or float):
                                                    summa += y
                                                elif isinstance(y, str):
                                                    summa += len(y)
    return summa


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calc_sum(data_structure)
print(result)






        




