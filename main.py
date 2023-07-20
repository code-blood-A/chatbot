import json
from difflib import get_close_matches

def load_queries(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_queries(file_path: str,data: dict):
    with open(file_path,'w') as file:
        json.dump(data,file,indent=2)

def find_best_match(user_question: str, questions: list) -> str or None:
    matches: list = get_close_matches(user_question,questions,n=1,cutoff=0.6)
    return matches[0] if matches else None

def get_answer(question: str, queries: dict) -> str or None:
    for q in queries["questions"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    queries: dict = load_queries('queries.json')
    
    while True:
        user_input: str = input("You: ")
        
        if user_input.lower() == "quit":
            break
        
        best_response: str or None = find_best_match(user_input, [q["question"] for q in queries["questions"]])
        
        if best_response:
            ans: str = get_answer(best_response,queries)
            print(f"Bot: {ans}")
        else:
            print("Bot: Feed the answer")
            new_ans: str = input("Type the answer: ")
            
            queries["questions"].append({"question": user_input,"answer": new_ans})
            save_queries("queries.json", queries)
            print("New response saved!")

if __name__ == '__main__':
    chat_bot()
