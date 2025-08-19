# neurostate-hmm-examples
Bonsai workflows demonstrating the usage of the real-time neural state decoding tools in the neurostate-hmm repository.

## Set-Up

To start, clone this repository to your local machine. But, before using these example Bonsai workflows, we will need to 1) download Bonsai and the relevant Bonsai packages and 2) install a Python virtual environment.

### Bonsai

First, install Bonsai on your system, if not already present (https://bonsai-rx.org/). After Bonsai is installed, use the built-in Bonsai package manager to install a couple of libraries that are needed for the example workflows: 
1. **Bonsai.StarterPack** -> this contains basic Bonsai libraries required for useful nodes, visualization, etc.
2. **Bonsai.Shaders** -> this access a computer timer with high resolution, which we use as a clock to help simulate real-time neural data.
3. **neurostate_hmm** -> this is the package we are testing.

Check the 'prerelease' and 'show advanced' options on the search bar to find the prereleased **neurostate_hmm** NuGet package. These libraries should install all of the Bonsai dependencies and tools needed to run the example workflows.

### Virtual Environment

Next, we need to set-up a Python virtual environment to be able to run Python code from Bonsai scripting nodes in the **neurostate_hmm** package. To make this easy, we recommend installing Microsoft Visual Studio Code (https://code.visualstudio.com/). Next, download Python 3.10.11 (https://www.python.org/downloads/release/python-31011/). 
