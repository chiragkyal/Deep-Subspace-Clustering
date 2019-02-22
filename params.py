from full_model import run_model, run_ae, run_ssc
from skopt.space import Integer, Real

all_params = [
  # 0
  {'model':run_model, 'dataset':'yaleB', 'n_rand':10, 'epochs_pretrain':201, 'epochs':101, 'space':
       [Real(10**-2, 10**0, "log-uniform", name='lr_pretrain'),
        Real(10**-3, 10**-1, "log-uniform", name='lr'),
        Real(10**0, 10**2, "log-uniform", name='alpha1'),
        Integer(2, 32, name='maxIter1'),
        Real(10**0, 10**2, "log-uniform", name='alpha2'),
        Integer(2, 32, name='maxIter2')]},
  {'model':run_model, 'dataset':'yaleB', 'n_rand':10, 'epochs_pretrain':201, 'epochs':101, 'space':
       [Real(10**-2, 10**0, "log-uniform", name='lr_pretrain'),
        Real(10**-3, 10**-1, "log-uniform", name='lr'),
        Real(10**0, 10**2, "log-uniform", name='alpha1'),
        Integer(10, 32, name='maxIter1'),
        Real(10**0, 10**2, "log-uniform", name='alpha2'),
        Integer(10, 32, name='maxIter2')]},
  {'model':run_model, 'dataset':'Coil20', 'n_rand':10, 'epochs_pretrain':201, 'epochs':101, 'space':
       [Real(10**-4, 10**0, "log-uniform", name='lr_pretrain'),
        Real(10**-5, 10**-1, "log-uniform", name='lr'),
        Real(10**-1, 10**3, "log-uniform", name='alpha1'),
        Integer(10, 100, name='maxIter1'),
        Real(10**-1, 10**3, "log-uniform", name='alpha2'),
        Integer(10, 100, name='maxIter2')]},
  {'model':run_model, 'dataset':'Coil20', 'n_rand':10, 'epochs_pretrain':1001, 'epochs':251, 'space':
       [Real(10**-4, 10**0, "log-uniform", name='lr_pretrain'),
        Real(10**-5, 10**-1, "log-uniform", name='lr'),
        Real(10**-1, 10**3, "log-uniform", name='alpha1'),
        Integer(10, 200, name='maxIter1'),
        Real(10**-1, 10**3, "log-uniform", name='alpha2'),
        Integer(10, 200, name='maxIter2')]},
  {'model':run_model, 'dataset':'Coil20', 'n_rand':50, 'epochs_pretrain':1001, 'epochs':251, 'space':
       [Real(10**-4, 10**0, "log-uniform", name='lr_pretrain'),
        Real(10**-5, 10**-1, "log-uniform", name='lr'),
        Real(10**-1, 10**3, "log-uniform", name='alpha1'),
        Integer(10, 200, name='maxIter1'),
        Real(10**-1, 10**3, "log-uniform", name='alpha2'),
        Integer(10, 200, name='maxIter2')]},
  # 5
  {'model':run_ssc, 'dataset':'yaleB', 'n_rand':10, 'space':
       [Real(10**-1, 10**3, "log-uniform", name='alpha'),
        Integer(10, 200, name='maxIter')]},
  {'model':run_ssc, 'dataset':'Coil20', 'n_rand':10, 'space':
       [Real(10**-1, 10**3, "log-uniform", name='alpha'),
        Integer(10, 200, name='maxIter')]},
  {'model':run_ae, 'dataset':'yaleB', 'n_rand':10, 'epochs_pretrain':201, 'epochs':101, 'space':
       [Real(10**-2, 10**0, "log-uniform", name='lr_pretrain'),
        Real(10**-3, 10**-1, "log-uniform", name='lr'),
        Real(10**0, 10**2, "log-uniform", name='alpha2'),
        Integer(10, 32, name='maxIter2')]},
  {'model':run_ae, 'dataset':'Coil20', 'n_rand':10, 'epochs_pretrain':1001, 'epochs':251, 'space':
       [Real(10**-4, 10**0, "log-uniform", name='lr_pretrain'),
        Real(10**-5, 10**-1, "log-uniform", name='lr'),
        Real(10**-1, 10**3, "log-uniform", name='alpha2'),
        Integer(10, 200, name='maxIter2')]},
  {'model':run_ssc, 'dataset':'Coil20', 'n_rand':160, 'maxIter':63, 'space':
       [Real(10**0, 10**4, "log-uniform", name='alpha')]},
  # 10
  {'model':run_ae, 'dataset':'Coil20', 'n_rand':160, 'epochs_pretrain':1000, 'epochs':250,
   'maxIter2':63, 'space':
       [Real(10**-6, 10**-2, "log-uniform", name='lr_pretrain'),
        Real(10**-6, 10**-2, "log-uniform", name='lr'),
        Real(10**-3, 10**1, "log-uniform", name='lambda2'),
        Real(10**0, 10**4, "log-uniform", name='alpha2')]},
  {'model':run_model, 'dataset':'Coil20', 'n_rand':160, 'maxIter1':63, 'epochs_pretrain':1000,
   'epochs':250, 'maxIter2':63, 'trainC':False, 'giveC':False, 'space':
       [Real(10**-6, 10**-2, "log-uniform", name='lr_pretrain'),
        Real(10**0, 10**4, "log-uniform", name='alpha1'),
        Real(10**-6, 10**-2, "log-uniform", name='lr'),
        Real(10**-2, 10**2, "log-uniform", name='lambda1'),
        Real(10**-3, 10**1, "log-uniform", name='lambda2'),
        Real(10**0, 10**4, "log-uniform", name='alpha2')]},
  {'model':run_model, 'dataset':'Coil20', 'n_rand':160, 'maxIter1':63, 'epochs_pretrain':1000,
   'epochs':250, 'maxIter2':63, 'trainC':True, 'giveC':False, 'space':
       [Real(10**-6, 10**-2, "log-uniform", name='lr_pretrain'),
        Real(10**0, 10**4, "log-uniform", name='alpha1'),
        Real(10**-6, 10**-2, "log-uniform", name='lr'),
        Real(10**-2, 10**2, "log-uniform", name='lambda1'),
        Real(10**-3, 10**1, "log-uniform", name='lambda2'),
        Real(10**1, 10**5, "log-uniform", name='lambda3'),
        Real(10**0, 10**4, "log-uniform", name='alpha2')]},
  {'model':run_model, 'dataset':'Coil20', 'n_rand':160, 'maxIter1':63, 'epochs_pretrain':1000,
   'epochs':250, 'maxIter2':63, 'trainC':True, 'giveC':True, 'space':
       [Real(10**-6, 10**-2, "log-uniform", name='lr_pretrain'),
        Real(10**0, 10**4, "log-uniform", name='alpha1'),
        Real(10**-6, 10**-2, "log-uniform", name='lr'),
        Real(10**-2, 10**2, "log-uniform", name='lambda1'),
        Real(10**-3, 10**1, "log-uniform", name='lambda2'),
        Real(10**1, 10**5, "log-uniform", name='lambda3'),
        Real(10**0, 10**4, "log-uniform", name='alpha2')]},
  {'model':run_ssc, 'dataset':'Coil20', 'n_rand':40, 'maxIter':250, 'space':
       [Real(0.021193, 52.9834, "log-uniform", name='alpha')]},
  # 15
  {'model':run_ae, 'dataset':'Coil20', 'n_rand':40, 'epochs_pretrain':4000, 'epochs':1000,
   'maxIter2':250, 'space':
       [Real(10**-6, 10**-2, "log-uniform", name='lr_pretrain'),
        Real(10**-6, 10**-2, "log-uniform", name='lr'),
        Real(10**-3, 10**1, "log-uniform", name='lambda2'),
        Real(10**0, 10**4, "log-uniform", name='alpha2')]},
  {'model':run_model, 'dataset':'Coil20', 'n_rand':40, 'maxIter1':250, 'epochs_pretrain':4000,
   'epochs':1000, 'maxIter2':250, 'trainC':False, 'giveC':False, 'space':
       [Real(10**-6, 10**-2, "log-uniform", name='lr_pretrain'),
        Real(10**0, 10**4, "log-uniform", name='alpha1'),
        Real(10**-6, 10**-2, "log-uniform", name='lr'),
        Real(10**-2, 10**2, "log-uniform", name='lambda1'),
        Real(10**-3, 10**1, "log-uniform", name='lambda2'),
        Real(10**0, 10**4, "log-uniform", name='alpha2')]},
  {'model':run_model, 'dataset':'Coil20', 'n_rand':40, 'maxIter1':250, 'epochs_pretrain':4000,
   'epochs':1000, 'maxIter2':250, 'trainC':True, 'giveC':False, 'space':
       [Real(10**-6, 10**-2, "log-uniform", name='lr_pretrain'),
        Real(10**0, 10**4, "log-uniform", name='alpha1'),
        Real(10**-6, 10**-2, "log-uniform", name='lr'),
        Real(10**-2, 10**2, "log-uniform", name='lambda1'),
        Real(10**-3, 10**1, "log-uniform", name='lambda2'),
        Real(10**1, 10**5, "log-uniform", name='lambda3'),
        Real(10**0, 10**4, "log-uniform", name='alpha2')]},
  {'model':run_model, 'dataset':'Coil20', 'n_rand':40, 'maxIter1':250, 'epochs_pretrain':4000,
   'epochs':1000, 'maxIter2':250, 'trainC':True, 'giveC':True, 'space':
       [Real(10**-6, 10**-2, "log-uniform", name='lr_pretrain'),
        Real(10**0, 10**4, "log-uniform", name='alpha1'),
        Real(10**-6, 10**-2, "log-uniform", name='lr'),
        Real(10**-2, 10**2, "log-uniform", name='lambda1'),
        Real(10**-3, 10**1, "log-uniform", name='lambda2'),
        Real(10**1, 10**5, "log-uniform", name='lambda3'),
        Real(10**0, 10**4, "log-uniform", name='alpha2')]},
  {'model':run_ssc, 'dataset':'Coil20', 'n_rand':10, 'maxIter':1000, 'space':
       [Real(0.036796, 22.99753, "log-uniform", name='alpha')]},
  # 20
  {'model':run_ae, 'dataset':'Coil20', 'n_rand':10, 'epochs_pretrain':16000, 'epochs':1000,
   'maxIter2':1000, 'space':
       [Real(10**-6, 10**-2, "log-uniform", name='lr_pretrain'),
        Real(10**-6, 10**-2, "log-uniform", name='lr'),
        Real(10**-3, 10**1, "log-uniform", name='lambda2'),
        Real(10**0, 10**4, "log-uniform", name='alpha2')]},
  {'model':run_model, 'dataset':'Coil20', 'n_rand':10, 'maxIter1':1000, 'epochs_pretrain':16000,
   'epochs':4000, 'maxIter2':1000, 'trainC':False, 'giveC':False, 'space':
       [Real(10**-6, 10**-2, "log-uniform", name='lr_pretrain'),
        Real(10**0, 10**4, "log-uniform", name='alpha1'),
        Real(10**-6, 10**-2, "log-uniform", name='lr'),
        Real(10**-2, 10**2, "log-uniform", name='lambda1'),
        Real(10**-3, 10**1, "log-uniform", name='lambda2'),
        Real(10**0, 10**4, "log-uniform", name='alpha2')]},
  {'model':run_model, 'dataset':'Coil20', 'n_rand':10, 'maxIter1':1000, 'epochs_pretrain':16000,
   'epochs':4000, 'maxIter2':1000, 'trainC':True, 'giveC':False, 'space':
       [Real(10**-6, 10**-2, "log-uniform", name='lr_pretrain'),
        Real(10**0, 10**4, "log-uniform", name='alpha1'),
        Real(10**-6, 10**-2, "log-uniform", name='lr'),
        Real(10**-2, 10**2, "log-uniform", name='lambda1'),
        Real(10**-3, 10**1, "log-uniform", name='lambda2'),
        Real(10**1, 10**5, "log-uniform", name='lambda3'),
        Real(10**0, 10**4, "log-uniform", name='alpha2')]},
  {'model':run_model, 'dataset':'Coil20', 'n_rand':10, 'maxIter1':1000, 'epochs_pretrain':16000,
   'epochs':4000, 'maxIter2':1000, 'trainC':True, 'giveC':True, 'space':
       [Real(10**-6, 10**-2, "log-uniform", name='lr_pretrain'),
        Real(10**0, 10**4, "log-uniform", name='alpha1'),
        Real(10**-6, 10**-2, "log-uniform", name='lr'),
        Real(10**-2, 10**2, "log-uniform", name='lambda1'),
        Real(10**-3, 10**1, "log-uniform", name='lambda2'),
        Real(10**1, 10**5, "log-uniform", name='lambda3'),
        Real(10**0, 10**4, "log-uniform", name='alpha2')]}
]