from ensemble import Ensemble
import yaml
import keras.backend as K

if __name__ == '__main__':
    K.clear_session()

    with open('./settings/model/config.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    # train 
    train_model = Ensemble(mode='train', model_kind='rnn_cnn',sigma_lst=[1,2,3], default_n=20, epoch_num=4, epoch_min=100, epoch_step=50,**config)
    train_model.train_model_outer()
    
    # test
    test_model = Ensemble(mode='test', model_kind='rnn_cnn', sigma_lst=[1,2,3], default_n=20, epoch_num=4, epoch_min=100, epoch_step=50,**config)
    test_model.train_model_outer()

    test_model.retransform_prediction(mode='roll')
    test_model.evaluate_model(mode='roll')
