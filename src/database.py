import json
import os

class DataBase:
    def get_all_scores(self):
        """
            Get all the score
            Return
            -------
                Dictionnary with all the pseudo and score
        """
        if not os.path.exists("./scores.json"):
            return {}
        
        with open("./scores.json", 'r') as file:
            return json.loads(str(file.read()))

    def write_score(self, pseudo, score):
        """
            Write the current score to the database
            Parameters
            ----------
            pseudo : string
                The current user to save
            score : integer
                The current score to save
        """
        all_scores = self.get_all_scores()

        with open("./scores.json", 'w') as file:
            all_scores[pseudo] = score
            file.write(json.dumps(all_scores, indent=4, separators=(',', ': ')))

    def get_best_score(self): 
        """
            Get the best score
            Return
            -------
                Tuple with the best score with the pseudo (pseudo, score)
        """
        all_scores = self.get_all_scores()
        best_pseudo, best_score = "", 10

        for pseudo, score in all_scores.items():
            if score < best_score:
                best_pseudo = pseudo
                best_score = score
        
        print(f"The current best score is {best_score} by {best_pseudo}")
        return best_pseudo, best_score
        
if __name__ == "__main__":
    db = DataBase()
    print(f"All the score {db.get_all_scores()}")
    print("Write the score 9 with the pseudo alex210501")
    db.write_score("alex210501", 9)
    print(f"All the score {db.get_all_scores()}")
    print("Write the score 3 with the pseudo test_score32")
    db.write_score("test_score32", 3)
    print(f"All the score {db.get_all_scores()}")
    print(f"The best score is ({db.get_best_score()})")
