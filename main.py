def scrabble_score(word: str) -> int:
    
    letter_to_score: dict[str, int] = {
        "A":1, "B":3, "C":3, "D":2, "E":1, "F":4, "G":2, "H":4, 
        "I":1, "J":8, "K":5, "L":1, "M":3, "N":1, "O":1, "P":3, 
        "Q":10, "R":1, "S":1, "T":1, "U":1, "V":4, "W":4, "X":8, 
        "Y":4, "Z":10
    }
   
    total_score:int = sum([letter_to_score.get(char, 0) for char in word.upper()])
    
    return total_score

def main():
    
    input_word=input("Enter a word: ")
    total_score=scrabble_score(input_word)
    
    print(f"Scrabble score for '{input_word}' = {total_score}.")
    

if __name__=="__main__":
    main()