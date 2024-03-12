standard_prompt = '''
Prüfe die Anwendbarkeit des deutschen Gesetzes "{input_law}" für die folgende Rechtsfrage: "{input_question}". Der letzte Satz muss enden mit "1", wenn das Gesetz anwendbar ist oder "0", wenn das Gesetz nicht anwendbar ist.  
'''

cot_prompt = '''
Prüfe die Anwendbarkeit des Gesetzes "{input_law}" für die folgende Rechtsfrage: "{input_question}".  

Die Prüfung umfasst die gründliche Analyse des Sachverhalts, die Identifikation relevanter Rechtsnormen, deren Auslegung, die Subsumtion des Sachverhalts unter diese Normen, die rechtliche Bewertung und die klare Dokumentation und Kommunikation der Schlussfolgerungen. 
Erstelle einen Plan und schreibe danach. Der Output muss folgendermaßen strukturiert sein:

Plan:
Dein Plan hier.

Prüfung:
Deine Prüfung hier.

Der letzte Satz muss enden mit "1", wenn das Gesetz anwendbar ist oder "0", wenn das Gesetz nicht anwendbar ist.
'''


vote_prompt = '''Gegeben eine Prüfung und mehrere Optionen, entscheide, welche Option am vielversprechendsten ist. Analysiere jede Option im Detail und schließe im letzten Satz mit "Die beste Wahl ist {s}", wobei s die Ganzzahl-ID der Wahl ist'''

# compare_prompt = '''Briefly analyze the coherency of the following two passages. Conclude in the last line "The more coherent passage is 1", "The more coherent passage is 2", or "The two passages are similarly coherent".
# '''

# score_prompt = '''Analyze the following passage, then at the last line conclude "Thus the coherency score is {s}", where s is an integer from 1 to 10.
# '''






"""

 Prüfe die Anwendbarkeit des Gesetzes {input_law} für die folgende Rechtsfrage: {input_question}.  
 
 
 umfasst die gründliche Analyse des Sachverhalts, die Identifikation relevanter Rechtsnormen, deren Auslegung, die Subsumtion des Sachverhalts unter diese Normen, die rechtliche Bewertung und die klare Dokumentation und Kommunikation der Schlussfolgerungen. Dies erfordert umfassendes Rechtswissen, analytische Fähigkeiten und methodische Kompetenz, um zu argumentieren, welche Gesetze anwendbar sind und welche rechtlichen Folgen sich daraus ergeben.

"""