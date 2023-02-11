import numpy
def solution(array):
    array.sort()
    answer = numpy.median(array)
    return answer