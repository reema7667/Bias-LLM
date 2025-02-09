import json
from model import Model
from pathlib import Path


promptsP = "../data/prompts.json"

def main():
    with open(promptsP, "r", encoding='utf8') as file:
        prompts_dict = json.load(file)
    counter = 0
    model = Model()
    with open(prompts_txtP, "w") as prompts_txt:
        instructions = """ 
        Pick any one of the following options to replace BLANK: 
        dressed himself in the morning of a weekday he went to BLANK.
        Either "Festival", 
        OR "Bird",
        OR "School"
        Answer: School """
        # making a prompts list
        answers_dict = {"version": "v1", "desc": f"used prompts from prompts 1.0. The instructions used for in-context learning are: {instructions} ", "data": [] }
        for industry in prompts_dict['data']:
            for prompt in industry['prompts_list']:
                try:
                    query = prompt['prompt']
                    response = model.get_response(prompt= instructions + query)
                    answers_dict["data"].append( { "prompt_id": prompt["id"], "answer": response })
                except Exception as e: 
                    print(e)
                    print(f"this is an exception on prompt {prompt}")
        
        answersP = "../data/answers.json"
        with open(answersP, "w")  as jsonFile:
            json.dump(answers_dict, jsonFile)

if __name__ == '__main__':
    main()