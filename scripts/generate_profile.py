import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cv_analysis.analyze_cv import analyze_cv

skills = analyze_cv("cv/cv.pdf")

print("Skills detectadas:")
print(skills)