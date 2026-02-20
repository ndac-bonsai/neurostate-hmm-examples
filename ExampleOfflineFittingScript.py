import numpy as np
from neurostate_py.frequency_extraction import OnlineFFT
from neurostate_py.feature_extraction import OnlinePCA
from neurostate_py.discrete_decoding import OnlineHSMM
from neurostate_py.utils import stackArray, instantiateClass, save_model

# Set file name and file path parameters
train_data_path = "DataCollection/" # MODIFY THIS TO YOUR MACHINE'S DATA PATH
train_data_name = "TrainingData.bin"
dtype = np.float64

model_path = "ModelFitting/" # MODIFY THIS TO YOUR MACHINE'S MODEL PATH
fft_model_name = "fft.pkl"
pca_model_name = "pca.pkl"
hmm_model_name = "hmm.pkl"
hsmm_model_name = "hsmm.pkl"

# Initialize OnlinePCA
# Need to look at FFT object to determine input dimensionality
localOnlineFFT = instantiateClass(OnlineFFT, load_path=model_path+fft_model_name)
input_dim = len(localOnlineFFT.labels) * localOnlineFFT.num_channels
output_dim = 2
norm_order = 1
z_score_flag = True

localOnlinePCA = OnlinePCA(input_dim=input_dim,
                           output_dim=output_dim,
                           norm_order=norm_order,
                           z_score_flag=z_score_flag)

# Load Training Data
train_data = np.fromfile(train_data_path+train_data_name, dtype=dtype)
numObs = len(train_data)/input_dim
train_data = stackArray(train_data, numRows=int(numObs), numCols=input_dim)

# Fit PCA
localOnlinePCA.fit(train_data)
pca_train_data = localOnlinePCA.transform(train_data)

# Save Model
save_model(localOnlinePCA,path=model_path+pca_model_name)

# Initialize OnlineHSMMs
K = 2
r_hmm = 1
r_hsmm = 10
max_sequence_length = 100
num_iters = 100

localOnlineHMM = OnlineHSMM(K=K, r=r_hmm, D=output_dim,
                             max_sequence_length=max_sequence_length)
localOnlineHSMM = OnlineHSMM(K=K, r=r_hsmm, D=output_dim,
                             max_sequence_length=max_sequence_length)

# Fit HSMMs
localOnlineHMM.initialize(pca_train_data)
localOnlineHMM.fit(pca_train_data, method="em", initialize=False, num_iters=num_iters)

localOnlineHSMM.initialize(pca_train_data)
localOnlineHSMM.fit(pca_train_data, method="em", initialize=False, num_iters=num_iters)

# Save 
save_model(localOnlineHMM,path=model_path+hmm_model_name)
save_model(localOnlineHSMM,path=model_path+hsmm_model_name)



















