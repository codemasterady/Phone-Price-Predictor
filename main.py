# Importing the libraries
from Screens.main_gui import MainGUI
from models.training_model import NeuralEngine

#! Defining the objects
ENGINE = NeuralEngine()
GUI = MainGUI()

#! Calling the executable
# ENGINE.train()
# ENGINE.performanceTester()
GUI.buildGUI()
GUI.showGUI()
