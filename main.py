import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

from ensemble import Ensemble
import yaml
import tensorflow.keras.backend as K


def reward_func(sigma_lst=[
        1, 2, 3], default_n=20, epoch_num=4, epoch_min=100, epoch_step=50):
    '''
    input
    sigma_lst - The component index from the ssa gene for example the gen [0, 1, 0] -> sigma_lst=[1] #the index where gen=1
    default_n - the window length for ssa - <= N /2 where N is the length of the time series - default 20
    epoch_num - The number of submodel used
    epoch_min - Min epoch of submodel
    epoch_step - number of epoch difference bw 2 submodels

    output
    a tuple contain 2 value (nse_q, nse_h)
    '''
    K.clear_session()

    with open('./settings/model/config.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    # train
    model = Ensemble(mode='train', model_kind='rnn_cnn', sigma_lst=sigma_lst,
                     default_n=default_n, epoch_num=epoch_num, epoch_min=epoch_min, epoch_step=epoch_step, **config)
    model.train_model_outer()

    # test
    model = Ensemble(mode='test', model_kind='rnn_cnn', sigma_lst=sigma_lst,
                     default_n=default_n, epoch_num=epoch_num, epoch_min=epoch_min, epoch_step=epoch_step, **config)
    model.train_model_outer()
    model.retransform_prediction(mode='roll')
    return model.evaluate_model(mode='roll')


if __name__ == '__main__':
    reward_func()
