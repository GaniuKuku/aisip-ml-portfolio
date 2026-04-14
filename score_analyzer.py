# Function returning multiple values (a tuple)
def analyze_scores(scores_list):
    if not scores_list:
        return 0, 0, 0
        
    average_score = sum(scores_list) / len(scores_list)
    highest_score = max(scores_list)
    lowest_score = min(scores_list)
    
    # Returns a tuple implicitly
    return average_score, highest_score, lowest_score

def main():
    print("--- AISIP Student Score Analyzer ---")
    bootcamp_scores = [88, 92, 76, 85, 98, 70, 89, 94]
    
    # Tuple unpacking in action
    avg, high, low = analyze_scores(bootcamp_scores)
    
    print(f"Scores processed: {bootcamp_scores}")
    print(f"Class Average: {avg:.2f}")
    print(f"Highest Score: {high}")
    print(f"Lowest Score: {low}")

if __name__ == "__main__":
    main()
