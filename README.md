# **Pattern Formation: Reaction-Diffusion Simulations**

This project simulates reaction-diffusion systems using the Grey-Scott model to demonstrate Turing instability. The system generates patterns, such as animal fur patterns, using numerical methods like the Explicit method and Crank-Nicolson method.

## **Installation**

### **Local Setup (Recommended)**

1. **Clone the Repository**
   
   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/niv-3/PatternFormation.git


Navigate to the Project Directory

Change to the project directory: 
cd PatternFormation


Set Up a Virtual Environment (Recommended)

To avoid dependency conflicts, it's recommended to create a virtual environment:

For Windows: python -m venv venv
venv\Scripts\activate

python -m venv venv
source venv/bin/activate

Install the Required Dependencies

Install the dependencies listed in requirements.txt: pip install -r requirements.txt


Google Colab Setup (For Running in Colab)
Clone the repository: !git clone https://github.com/niv-3/PatternFormation.git

Install the dependencies using requirements.txt:

!pip install -r PatternFormation/requirements.txt

Usage
Run the Reaction-Diffusion Simulation
To run the reaction-diffusion simulation, execute the pattern_simulation.py script:

python pattern_simulation.py


Project Structure
The project directory contains the following structure:

PatternFormation/
├── src/
│   ├── pattern_simulation.py      # Main simulation script
│   └── reaction_diffusion.py      # Code for reaction-diffusion calculations
├── requirements.txt               # List of dependencies
├── README.md                      # Project documentation
└── images/                        # Directory for saving generated images



Dependencies
The required dependencies for this project are listed in requirements.txt, which includes the following:

click==8.1.7
cloudpickle==3.1.0
colorama==0.4.6
contourpy==1.3.1
cycler==0.12.1
dask==2024.11.2
fonttools==4.55.1
fsspec==2024.10.0
kiwisolver==1.4.7
locket==1.0.0
matplotlib==3.9.3
numpy==2.1.3
packaging==24.2
partd==1.4.2
pattern_formation==0.1
pillow==11.0.0
pyparsing==3.2.0
python-dateutil==2.9.0.post0
PyYAML==6.0.2
scipy==1.14.1
six==1.16.0
tk==0.1.0
toolz==1.0.0





