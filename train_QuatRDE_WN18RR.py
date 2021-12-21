import config
from  models import *
import json
import os 
import numpy as np

con = config.Config()
con.set_in_path("./benchmarks/WN18RR/")
con.set_logger('wn18rr', 'logs')
con.set_work_threads(8)
con.set_train_times(3000)
con.set_nbatches(100)
con.set_alpha(0.1)
con.set_bern(1)
# Test ở các chiều: 100, 200, 300, 400
con.set_dimension(100)
# L2 regularization: 0.05, 0.1
con.set_lmbda(0.1)
con.set_lmbda_two(0.01)
con.set_margin(1.0)
# Number of negative triples for each triple: 1, 5, 10
con.set_ent_neg_rate(10)
con.set_rel_neg_rate(0)
con.set_opt_method("adagrad")
con.set_save_steps(1)
con.set_valid_steps(1)
con.set_early_stopping_patience(10)
con.set_checkpoint_dir("./checkpoint_WN18RR")
con.set_result_dir("./result_WN18RR")
con.set_test_link(True)
con.set_test_triple(True)
con.init()
con.set_train_model(QuatRDE)
con.train()

'''
Best config
- dimension:
- lambda:
- lambda_2:
- ent_neg_rate:
- optimizer:
'''