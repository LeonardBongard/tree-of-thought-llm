# minimal test if library is working (at least with chatgpt)
import argparse
from tot.methods.bfs import solve
from tot.tasks.game24 import Game24Task
from tot.tasks.text import TextTask
from tot.tasks.law_applicable import LawApplicableTask

#args = argparse.Namespace(backend='gpt-4', temperature=0.7, task="law_applicable", naive_run=False, prompt_sample="standard", method_generate='sample', method_evaluate='vote', method_select='greedy', n_generate_sample=3, n_evaluate_sample=3, n_select_sample=5)
args = argparse.Namespace(backend='gpt-4', temperature=0.7, task="law_applicable", naive_run=False, prompt_sample="standard", method_generate='sample', method_evaluate='vote', method_select='greedy', n_generate_sample=3, n_evaluate_sample=3, n_select_sample=5)

task = LawApplicableTask()
ys, infos = solve(args, task, 0)
print(ys[0])