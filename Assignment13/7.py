"""7) Using "Customizing Matplotlib Visualizations" discussed in Numpy session4 notes plot graph to compare your at least 2 semester result
    """

import matplotlib.pyplot as plt
import numpy as np

# Subjects
subjects = ['Maths', 'Physics', 'Chemistry', 'Python', 'English']

# Semester Marks
sem1 = [75, 68, 72, 80, 70]
sem2 = [82, 74, 78, 88, 76]

x = np.arange(len(subjects))
width = 0.35

plt.figure(figsize=(8, 5))

plt.bar(x-width/2, sem1, width, label='Semester 1')
plt.bar(x+width/2, sem2, width, label='Semester 2')

plt.title("Semester Result Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.xticks(x, subjects)
plt.legend()
plt.grid(axis='y', linestyle='--')

plt.show()
