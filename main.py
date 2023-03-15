from get_submissions import *
import matplotlib.pyplot as plt

problem_id = 1038
user_ids = ["snowgot", "aass0900"]

submissions = get_submissions(problem_id, user_ids)

print(submissions)


plt.hist(submissions["correct"], bins=[0, 0.5, 1], align="mid", color="purple")
plt.xticks([0.25, 0.75], ["Incorrect", "Correct"])
plt.xlabel("Result")
plt.ylabel("Number of Correct People")
plt.title("Binary Histogram of Problem Submissions")
plt.show()