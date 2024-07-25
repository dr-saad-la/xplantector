"""Summary
"""

from abc import ABC, abstractmethod

class BaseModel(ABC):

    """Summary
    """
    
    def __init__(self):
        """Initialize the model.
        """
        super().__init__()
    
    @abstractmethod
    def build_model(self):
        """Build the model architecture.
        """
        pass

    @abstractmethod
    def train(self, training_data, validation_data, epochs, batch_size):
        """Train the model with the given data.
        
        Parameters
        ----------
        training_data : TYPE
            Description
        validation_data : TYPE
            Description
        epochs : TYPE
            Description
        batch_size : TYPE
            Description
        """
        pass

    @abstractmethod
    def evaluate(self, test_data):
        """Evaluate the model performance on the test data.
        
        Parameters
        ----------
        test_data : TYPE
            Description
        """
        pass

    @abstractmethod
    def predict(self, new_data):
        """Make predictions on new data.
        
        Parameters
        ----------
        new_data : TYPE
            Description
        """
        pass

    def save_model(self, filepath):
        """Save the model to the specified file path.
        
        Parameters
        ----------
        filepath : TYPE
            Description
        """
        pass

    def load_model(self, filepath):
        """Load the model from the specified file path.
        
        Parameters
        ----------
        filepath : TYPE
            Description
        """
        pass
