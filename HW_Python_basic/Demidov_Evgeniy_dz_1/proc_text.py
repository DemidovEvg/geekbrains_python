measurers = {
    (0, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19): "процентов",
    (1,): "процент",
    (2, 3, 4): "процента", 
}
measure = ""
for proc in range(1, 101):
    _proc = proc
    _is_find_measure = False
    while not _is_find_measure:
        for measurer_key in measurers:         
                if abs(_proc) in measurer_key:
                    measure = measurers[measurer_key]
                    _is_find_measure = True
                    break
        _proc %= 10
    print(proc, measure)
