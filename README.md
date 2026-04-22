# 🎓 Student Grade Calculator

A simple Python program that takes a student's name and marks as input, validates the input, and assigns a grade along with a performance message.

---

## 📌 Features

- Accepts student name and marks (0–100)
- Validates input to ensure marks are within range
- Assigns grades based on score
- Displays a personalized result summary
- Beginner-friendly and easy to understand

---

## 🧮 Grading Criteria

| Marks Range | Grade | Message                     |
|------------|-------|-----------------------------|
| 90 - 100   | A     | Very Good! Keep it up! 👍   |
| 80 - 89    | B     | Well Done!                  |
| 70 - 79    | C     | Average performance         |
| 60 - 69    | D     | You can do better           |
| Below 60   | F     | You failed. Try again       |

---

## ▶️ How to Run

1. Make sure you have Python installed (Python 3.x recommended)
2. Save the script as `grade_calculator.py`
3. Open a terminal or command prompt
4. Run the program:

```bash
python grade_calculator.py
📝 Example Output
Enter student name: John
Enter marks (0-100): 85

Result for John:
Marks: 85
Grade: B
Comments: Well Done!
```
⚠️ Input Validation

If the entered marks are outside the range of 0–100, the program will prompt the user to re-enter valid marks:
```bash
❌ Out of range. Try again.
Enter marks between 0 and 100:
```

👤 Author

Prathamesh

📄 License

This project is open-source and free to use for learning purposes.
