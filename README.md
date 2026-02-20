# neurostate-hmm-examples

This repository contains example Bonsai workflows using the [neurostate-hmm Bonsai package](https://github.com/ndac-bonsai/neurostate-hmm).

## Set-Up

To start, clone this repository to your local machine. Also, follow the installation instructions for [neurostate-hmm](https://github.com/ndac-bonsai/neurostate-hmm). Finally, use the Bonsai package manager to install the following workflow requirements:
1. **Bonsai.StarterPack** -> this contains basic Bonsai libraries required for useful nodes, visualization, etc.
2. **Bonsai.Shaders** -> this accesses a computer timer with high resolution, which we use as a clock to help simulate real-time neural data.
3. **Bonsai.Scripting.Python** -> this accesses Bonsai's Python scripting functionality.
4. **Bonsai.ML**

Now, you can open the Bonsai workflows from a Bonsai instance containing the [neurostate-hmm](https://github.com/ndac-bonsai/neurostate-hmm) nodes. In the 'CreateRuntime' Bonsai node, ensure that the 'PythonHome' field is set to the appropriate virtual environment and ensure that the 'ScriptPath' field is set to main.py in [neurostate-hmm](https://github.com/ndac-bonsai/neurostate-hmm). Similarly, ensure that the 'ScriptPath' field in the 'CreateModule' node (inside of 'LoadModule') is also set to main.py.

## Using the Example Workflows

### ExampleHSMMSimulationWorkflow

This workflow demonstrates HSMM decoding using observations created by an HSMM model. For convenience, the models are loaded from a supplied pickle file: `ModelFitting/sim1hsmm.pkl`.

### ExampleDataCollectionWorkflow

This workflow demonstrates how to collect data to fit a PCA and HSMM model. Using a provided example datafile to emulate incoming raw electrophysiology (30 kHz, 2 channels), the workflow streams in ephys data, filters it, applies an FFT to extract frequency information, then saves the data to a binary file. This data can then be used to fit PCA and HSMM models to the data with an offlin script.

### ExampleOfflineFittingScript

This Python script demonstrates how to fit PCA and HSMM models using the saved training data. Please note that local paths will have to be modified within the script. For convenience, pre-saved models have been provided as `.pkl` files in the ModelFitting subdirectory.

### ExampleDecodingWorkflow

This workflow demonstrates how streamed-in electrophysiology data can be used to find discrete state readouts. The workflow streams in ephys data, filters it, applies an FFT, applies a PCA feature extraction, then applies HSMM state decoding.