from MyKNNLIB import *
from sklearn import datasets

iris = datasets.load_iris()
D = iris.data
Y = iris.target

def partitionner(D,Y):
    TestData,TestTarget,LearningData,LearningTarget=[],[],[],[]
    for i in range(len(Y)):
        if i%4==0:
            TestData.append(D[i]);TestTarget.append(Y[i])
        else:
            LearningData.append(D[i]);LearningTarget.append(Y[i])
    return TestData,TestTarget,LearningData,LearningTarget
def convert_to_np_arrays(Listes):
    return tuple(list(map(lambda table:np.array(table),Listes)))

TestData,TestTarget,LearningData,LearningTarget=convert_to_np_arrays(partitionner(D,Y))
model=LearningData,LearningTarget,d2,5
matrice=ConfusionMatrix(TestData,TestTarget,model)
print(matrice)