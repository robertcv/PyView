import matplotlib.pyplot as plt
import numpy as np

def criteriaContribution(dataClass):

    cmap = plt.get_cmap('prism')
    colors = [cmap(i) for i in np.linspace(0, 1, len(dataClass.criteria))]

    ax = plt.subplot(111)

    x = [i for i in range(len(dataClass.variants))]
    p = []
    data = []

    for j in range(len(dataClass.variants)):
        data.append(dataClass.weighted_data[j][0] * dataClass.criteria_weights[0])

    tmp_p = plt.bar(x, data, 0.4, color=colors[0])
    p.append(tmp_p)

    for i in range(1, len(dataClass.criteria)):
        tmp = []
        for j in range(len(dataClass.variants)):
            tmp.append(dataClass.weighted_data[j][i] * dataClass.criteria_weights[i])
        tmp_p = plt.bar(x, tmp, 0.4, bottom=data, color=colors[i])
        p.append(tmp_p)
        data = [sum(x) for x in zip(tmp, data)]


    plt.title('Criteria contribution')
    plt.xticks([x_ + 0.2 for x_ in x ], dataClass.variants)

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    ax.legend([pl[0] for pl in p], dataClass.criteria, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()


def Map(dataClass, craiterion1, craiterion2):
    data1 = dataClass.getCriterionValues(craiterion1)
    data2 = dataClass.getCriterionValues(craiterion2)
    variants = dataClass.variants

    max_x = max(data1) #najdemo največji x
    max_y = max(data2) #najdemo največji y

    x = [0] #hranimo robne točke
    y = [max_y] #hranimo robne točke

    f_x = data1[data2.index(max_y)]
    f_y = max_y

    #dodamo na seznam robnih točk
    x.append(f_x)
    y.append(f_y)

    while f_x != max_x: #dokler nismo prišli do točke z max x ponavljamo
        k = [] #shranimo si koeficiente premic
        desno = [i for i, x in enumerate(data1) if x > f_x] #najdemo točke ki so desno od zdejšne
        for i in desno:
            if data1[i]!=f_x:
                k_tmp = (data2[i]-f_y)/(data1[i]-f_x) #izračunamo koeficient
                k.append((k_tmp,i))
        tmp_i = max(k)[1] #najdeš točko z največjim koeficientom
        f_x = data1[tmp_i]
        f_y = data2[tmp_i]
        x.append(f_x)
        y.append(f_y)

    #dodamo še končno točko
    x.append(max_x)
    y.append(0)


    plt.fill_between(x, y, 0, interpolate=True)
    plt.scatter(data1, data2, s=350, c='w')
    for i in range(len(variants)):
        plt.annotate(variants[i], xy=(data1[i], data2[i]), xytext=(data1[i], data2[i]), horizontalalignment='center',
            verticalalignment='center',)

    plt.ylim([-5, 105])
    plt.xlim([-5, 105])

    plt.title('Map')
    plt.xlabel(craiterion1)
    plt.ylabel(craiterion2)

    plt.show()



def Sensitivity(dataClass, craiterion):
    y2 = dataClass.getCriterionValues(craiterion)
    y1 = dataClass.variants_result
    x1 = dataClass.getCriterionWeighted(craiterion)

    f = [0 for _ in range(len(y1))]
    for i in range(len(y1)):
        f[i] = y2[i] - (y2[i]-y1[i])/(1-x1)

    cmap = plt.get_cmap('prism')
    colors = [cmap(i) for i in np.linspace(0, 1, len(f))]

    p = []
    for i in range(len(f)):
        tmp_p = plt.plot([0,1],[f[i],y2[i]], color=colors[i])
        p.append(tmp_p)

    plt.plot([x1, x1], [0, 100], 'b--')

    plt.title('Sensitivity of ' + craiterion)
    plt.legend([pl[0] for pl in p], dataClass.variants, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()