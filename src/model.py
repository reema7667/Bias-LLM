# Author Ioannis Reklos
import openai
import ast
class Model:
    """
    The class the handles model queries and responses
    """
    
    def __init__(self, model_name=None, params_dict=None):
        """
        The constructor
        Args:
            model_name (): The openai model to use in string format
            params_dict (): The parameters of the model in dict format
        """
    openai.api_key = "ADD_YOUR_API_KEY_HERE" # not for deployment
        self.model_name = model_name if model_name is not None else "text-davinci-003"
        self.params = params_dict if params_dict is not None else {'temperature': 0,
                                                                   'max_tokens': 30,
                                                                   'top_p': 1,
                                                                   'frequency_penalty': 0,
                                                                   'presence_penalty': 0
                                                                   }

    def get_response(self, prompt):
        """
        A function that passes a prompt to the model and returns the response
        Args:
            prompt (): The prompt string

        Returns: The model response in string format

        """
        response = openai.Completion.create(
            model=self.model_name,
            prompt=prompt,
            **self.params
        )
        response = response["choices"][0]["text"]
        return response


