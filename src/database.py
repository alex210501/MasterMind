import json
import os

score_file = "./scores.json"

class DataBase:
    def get_all_scores(self):
        """
            Get all the score
            Return
            -------
                Dictionnary with all the pseudo and score
        """
        if not os.path.exists(score_file):
            return {}
        
        with open(score_file, 'r') as file:
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
        # Return if no pseudo entered
        if pseudo == '/':
            return
        
        all_scores = self.get_all_scores()

        # Save the score only if it's better tha the one saved
        if pseudo in all_scores.keys():
            if all_scores[pseudo] <= score:
                return
        
        with open(score_file, 'w') as file:
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
    print("Write the score 2 with the pseudo lisaRGT")
    db.write_score("lisaRGT", 2)
    print(f"All the score {db.get_all_scores()}")
    print(f"The best score is ({db.get_best_score()})")
