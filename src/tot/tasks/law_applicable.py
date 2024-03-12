import os
import re
from tot.tasks.base import Task, DATA_PATH
from tot.prompts.law_applicable import *
from tot.models import gpt
import json

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(f) for f in file.readlines()]
    return data


class LawApplicableTask(Task):
    """
    Input (x)   : a legal question
    Output (y)  : a legal answer
    Reward (r)  : # TODO
    Input Example:
    Output Example:
    """

    def __init__(self, file='bgb_dev_rearranged.json'):
        """
        file: a text file, each line is a legal question with a law passage that could be applicable
        """
        super().__init__()
        path = os.path.join(DATA_PATH, 'law_applicable', file)
        self.data = read_data(path)  #open(path).readlines() # {"question": "<text>", "paragraph": "\u00a7 969", "content": "Herausgabe an den Verlierer. Der Finder wird durch die Herausgabe der Sache an den Verlierer auch den sonstigen Empfangsberechtigten gegen\u00fcber befreit.", "applicable": 0}

        self.steps = 2
        self.stops = [None] * 4  #['\nPassage:\n', None] TODO think about a better stop condition to avoid long input thoughts

    def __len__(self) -> int:
        return len(self.data)

    def get_input(self, idx: int) -> str:
        return self.data[idx]["question"] + '\n' + self.data[idx]["paragraph"] + ": " + self.data[idx]["content"]
        #return self.data[idx]
    
    def test_output(self, idx: int, output: str): # evaluate the output if applicable or not
        # Missing line if we ever split the output TODO
        gold_solution = self.data[idx]["applicable"]

        output_solution = None # TODO extract the solution from the output and compare it with the gold solution

        if gold_solution == output_solution:
            return {'r': 1}


        # prompt = score_prompt + output
        # score_outputs = gpt(prompt, n=5, model='gpt-4')
        # scores = []
        # for score_output in score_outputs:
        #     # print(score_output)
        #     pattern = r".*coherency score is (\d+).*"  # TODO change through more legal terms
        #     match = re.match(pattern, score_output, re.DOTALL)
        #     if match:
        #         score = int(match.groups()[0])
        #         scores.append(score)
        #     else:
        #         print(f'------------------score no match: {[score_output]}')
        # print(scores)
        # # print('------------')
        # info = {'rs': scores, 'r': sum(scores) / len(scores) if scores else 0}
        info = {'r': 0}
        return info
    

    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        parts = x.split("\n")
        #print("Parts: ", parts)
        #print(standard_prompt.format(input=(parts[1],parts[0])) + y)
        return standard_prompt.format(input_law=parts[1], input_question=parts[0]) + y
        #return standard_prompt.format(input=x) + y
    

    @staticmethod
    def cot_prompt_wrap(x: str, y:str='') -> str:
        parts = x.split("\n")
        return cot_prompt.format(input_law=parts[1], input_question=parts[0]) + y


    @staticmethod
    def vote_prompt_wrap(x: str, ys: list) -> str:  
        prompt = vote_prompt
        for i, y in enumerate(ys, 1):
            # y = y.replace('Plan:\n', '')
            # TODO: truncate the plan part?
            prompt += f'Choice {i}:\n{y}\n'
        return prompt
    
    @staticmethod
    def vote_outputs_unwrap(vote_outputs: list, n_candidates: int) -> list:
        vote_results = [0] * n_candidates
        for vote_output in vote_outputs:
            pattern = r".*Die beste Wahl ist .*(\d+).*" 
            match = re.match(pattern, vote_output, re.DOTALL)
            if match:
                vote = int(match.groups()[0]) - 1
                if vote in range(n_candidates):
                    vote_results[vote] += 1
            else:
                print(f'vote no match: {[vote_output]}')
        return vote_results

    # @staticmethod  # Not needed apparently?
    # def compare_prompt_wrap(x: str, ys: list) -> str:
    #     assert len(ys) == 2, 'compare prompt only supports 2 candidates'
    #     #ys = [y.split('Passage:\n')[-1] for y in ys]
    #     prompt = compare_prompt + f'Passage 1:\n{ys[0]}\n\nPassage 2:\n{ys[1]}\n'
    #     return prompt
    
    # @staticmethod
    # def compare_output_unwrap(compare_output: str):
    #     if 'more coherent passage is 1' in compare_output:
    #         return 0
    #     elif 'more coherent passage is 2' in compare_output:
    #         return 1
    #     elif 'two passages are similarly coherent' in compare_output:
    #         return 0.5
    #     else:
    #         print(f'-----------------compare no match: {[compare_output]}')
    #         return -1