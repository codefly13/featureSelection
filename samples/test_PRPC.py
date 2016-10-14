from samples.conf import svm
from samples.conf import accuracy_score
from samples.conf import gen_data
from samples.conf import PRPC
from samples.conf import *


def test_PRPC():
    tt = get_traintest()
    x_train, y_train, x_test, y_test, path = next(tt)
    PRPC_rank = PRPC.PRPC(x_train, y_train, x_test, num = 100)

    num_fea = 100  # number of selected features
    idx = PRPC_rank[:num_fea]

    run_num = 10
    clf = svm.LinearSVC()

    accuracy = 0
    for i in range(run_num):
        clf.fit(x_train[:, idx], y_train)
        y_predict = clf.predict(x_test[:, idx])
        accuracy += accuracy_score(y_test, y_predict)
    print('Accuracy : {0}'.format(accuracy / run_num))


if __name__ == "__main__":
    test_PRPC()