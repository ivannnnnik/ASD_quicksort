# ASD_quicksort
Алгоритм выполняет сортировку элементов массива. Он берет любое число из списка. В нашем случае оно выбирается рандомно(далее q). Он закидывает в один список все числа меньшие q. Еще в один список закидывает все числа равные q. В последний список закидывает числа, большие q. 

Возвращает последовательное соединение первого списка, проведенного через этот алгоритм, второго списка в таком же состоянии и третьего списка тоже проведенного через этот алго. Получается, что сортировка постоянно делит изначальный список на подмассивы больше и меньше определенного числа из списка так, пока в каждом таком мини списке не останется по одному элементу
