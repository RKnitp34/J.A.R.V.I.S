def Dict():
    speak('Dictionary Started!')
    speak('tell me the problem')
    problem1=takeCommand()
    if 'meaning' in problem1: 
        problem1=problem1.replce('what is the',"")
        problem1=problem1.replce('meaning',"")
        problem1=problem1.replce('syononame',"")
        problem1=problem1.replce('antoname',"")
        problem1=problem1.replce('of',"")
        problem1=problem1.replce('jarvis',"")
        result=Dict.meaning(problem1)
        print(result)
        speak("The meaning of {problem1} is {result}")
    if 'synoname' in problem1: 
        problem1=problem1.replce('what is the',"")
        problem1=problem1.replce('meaning',"")
        problem1=problem1.replce('syononame',"")
        problem1=problem1.replce('antoname',"")
        problem1=problem1.replce('of',"")
        problem1=problem1.replce('jarvis',"")
        result=Dict.synonym(problem1)
        print(result)
        speak("The meaning of {problem1} is {result}")
    if 'antoname' in problem1: 
        problem1=problem1.replce('what is the',"")
        problem1=problem1.replce('meaning',"")
        problem1=problem1.replce('syononame',"")
        problem1=problem1.replce('antoname',"")
        problem1=problem1.replce('of',"")
        problem1=problem1.replce('jarvis',"")
        result=Dict.antonym(problem1)
        print(result)
        speak("The meaning of {problem1} is {result}")