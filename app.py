
from flask import Flask, request, render_template_string

app = Flask(__name__)

# QUIZ QUESTIONS
# Format: Question, options, correct answer

questions = {
    "General Knowledge": [
        ("What is the capital of Tanzania?",
         ["Arusha", "Dodoma", "Mwanza", "Dar es Salaam"], "Dodoma"),
        ("How many days are in a week?",
         ["5", "6", "7", "8"], "7"),
        ("Which planet do we live on?",
         ["Mars", "Earth", "Venus", "Jupiter"], "Earth"),
        ("Which is the largest ocean?",
         ["Atlantic", "Indian", "Pacific", "Arctic"], "Pacific"),
        ("How many centimeters are in one meter?",
         ["10", "50", "100", "1000"], "100"),
        ("The Sun is a?",
         ["Planet", "Star", "Moon", "Cloud"], "Star"),
        ("Egypt is found in which continent?",
         ["Asia", "Europe", "Africa", "Australia"], "Africa"),
        ("At what temperature does water freeze?",
         ["0°C", "10°C", "50°C", "100°C"], "0°C"),
        ("How many months are in a year?",
         ["10", "11", "12", "13"], "12"),
        ("What is the national language of Tanzania?",
         ["French", "Kiswahili", "German", "Arabic"], "Kiswahili")
    ],

    "Health & Safety": [
        ("What should you use to wash your hands?",
         ["Soap and water", "Oil", "Paint", "Dust"], "Soap and water"),
        ("What should you drink to prevent dehydration?",
         ["Petrol", "Clean water", "Ink", "Paint"], "Clean water"),
        ("Which food group helps build the body?",
         ["Proteins", "Sweets", "Soft drinks", "Candy"], "Proteins"),
        ("Why is physical exercise important?",
         ["For health", "To become sick", "To avoid sleep", "To waste time"], "For health"),
        ("Why do people need enough sleep?",
         ["For rest", "To become tired", "To avoid eating", "To become weak"], "For rest"),
        ("What should you do during an emergency?",
         ["Seek help", "Hide from everyone", "Ignore it", "Laugh"], "Seek help"),
        ("Should you share prescription medicines with friends?",
         ["Yes", "No", "Always", "Sometimes without advice"], "No"),
        ("How often should you brush your teeth?",
         ["Twice daily", "Once a week", "Once a month", "Never"], "Twice daily"),
        ("Where should pedestrians cross a busy road?",
         ["Anywhere", "At a safe crossing", "In the middle", "Behind cars"], "At a safe crossing"),
        ("What should you do before eating?",
         ["Wash your hands", "Touch the floor", "Play with dirt", "Ignore hygiene"], "Wash your hands")
    ],

    "Technology": [
        ("What is the brain of a computer?",
         ["CPU", "Mouse", "Monitor", "Keyboard"], "CPU"),
        ("Which device is used for typing?",
         ["Mouse", "Keyboard", "Speaker", "Monitor"], "Keyboard"),
        ("Which device displays computer output?",
         ["Monitor", "Keyboard", "Microphone", "Mouse"], "Monitor"),
        ("What is Google Chrome?",
         ["A browser", "A keyboard", "A printer", "A cable"], "A browser"),
        ("Which password is stronger?",
         ["12345", "password", "M@sunD2026!", "abc"], "M@sunD2026!"),
        ("What should you do with suspicious links?",
         ["Avoid clicking", "Share them", "Trust all", "Download everything"], "Avoid clicking"),
        ("Why should you back up files?",
         ["To protect data", "To delete everything", "To damage files", "To slow the PC"], "To protect data"),
        ("What does Wi-Fi provide?",
         ["Wireless network access", "Electric cooking", "Printing paper", "Water"], "Wireless network access"),
        ("What is software?",
         ["Computer programs", "Computer desk", "Electric wire", "Computer screen"], "Computer programs"),
        ("Which command saves a document in many programs?",
         ["Ctrl + S", "Ctrl + X", "Ctrl + P", "Ctrl + Z"], "Ctrl + S")
    ],

    "Environment": [
        ("Which gas do plants absorb from the air?",
         ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "Carbon dioxide"),
        ("What is recycling?",
         ["Reusing materials", "Burning all rubbish", "Throwing waste in rivers", "Wasting water"], "Reusing materials"),
        ("Which energy source is renewable?",
         ["Solar energy", "Coal", "Petrol", "Diesel"], "Solar energy"),
        ("What helps conserve water?",
         ["Closing taps", "Leaving taps open", "Wasting water", "Breaking pipes"], "Closing taps"),
        ("Where should rubbish be placed?",
         ["In a dustbin", "In rivers", "On roads", "In classrooms"], "In a dustbin"),
        ("What is biodiversity?",
         ["Variety of living things", "Only buildings", "Only roads", "Only machines"], "Variety of living things"),
        ("What can deforestation cause?",
         ["Soil erosion", "More forests", "More rainfall everywhere", "Cleaner air"], "Soil erosion"),
        ("What can be made from food waste?",
         ["Compost", "Plastic", "Metal", "Glass"], "Compost"),
        ("Why should wildlife be protected?",
         ["To maintain nature", "To destroy forests", "To cause pollution", "To waste resources"], "To maintain nature"),
        ("Which activity causes air pollution?",
         ["Burning fossil fuels", "Planting trees", "Using bicycles", "Recycling paper"], "Burning fossil fuels")
    ],

    "Everyday Life": [
        ("What does a red traffic light mean?",
         ["Stop", "Go", "Run", "Turn anywhere"], "Stop"),
        ("How many hours are in one day?",
         ["12", "18", "24", "30"], "24"),
        ("What do people use money for?",
         ["Buying goods and services", "Growing trees", "Making rain", "Producing sunlight"], "Buying goods and services"),
        ("What should you do when water is boiling?",
         ["Keep a safe distance", "Touch it", "Drink it immediately", "Play with it"], "Keep a safe distance"),
        ("Who can help you when you feel unsafe?",
         ["A trusted adult", "A stranger online", "Nobody", "An unknown caller"], "A trusted adult"),
        ("Why should you read food labels?",
         ["To understand product information", "To change the price", "To spoil food", "To waste time"], "To understand product information"),
        ("What is the polite way to wait for service?",
         ["Join a queue", "Push others", "Shout at people", "Skip everyone"], "Join a queue"),
        ("What should you do before crossing a road?",
         ["Look both ways", "Close your eyes", "Run without looking", "Use your phone"], "Look both ways"),
        ("What is a budget?",
         ["A plan for income and spending", "A type of vehicle", "A school subject only", "A computer game"], "A plan for income and spending"),
        ("Why is communication important?",
         ["To share information", "To create confusion", "To avoid everyone", "To stop learning"], "To share information")
    ]
}


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form.get("player_name", "").strip()

        if not name:
            return "Please enter your name."

        return render_template_string("""
        <body style="background:#101827;color:white;
        text-align:center;padding:40px;">

        <h1>WELCOME {{ name }}!</h1>
        <h2>Choose Your Quiz Category</h2>

        {% for category in categories %}
        <form action="/start" method="POST">
            <input type="hidden" name="name" value="{{ name }}">
            <input type="hidden" name="category" value="{{ category }}">

            <button style="padding:15px;margin:10px;
            background:#2563eb;color:white;border:none;">
                {{ category }}
            </button>
        </form>
        {% endfor %}

        </body>
        """, name=name, categories=list(questions.keys()))

    return """
    <body style="background:#101827;color:white;
    text-align:center;padding:60px;">

    <h1>LIFE KNOWLEDGE</h1>
    <h2>QUIZ MASTER</h2>
    <p>Challenge your everyday knowledge!</p>

    <form method="POST">
        <input type="text" name="player_name"
        placeholder="Enter your name" required>
        <br><br>
        <button type="submit">START QUIZ</button>
    </form>

    </body>
    """


@app.route("/start", methods=["POST"])
def start():

    name = request.form.get("name", "")
    category = request.form.get("category", "")

    if category not in questions:
        return "Invalid category!"

    return render_template_string("""
    <body style="background:#101827;color:white;
    text-align:center;padding:30px;">

    <h1>{{ category }}</h1>
    <h2>Player: {{ name }}</h2>

    <form action="/result" method="POST">

    <input type="hidden" name="name" value="{{ name }}">
    <input type="hidden" name="category" value="{{ category }}">

    {% for q in quiz %}
        {% set question_number = loop.index0 %}

        <h3>{{ loop.index }}. {{ q[0] }}</h3>

        {% for option in q[1] %}
            <p>
            <label>
            <input type="radio"
            name="q{{ question_number }}"
            value="{{ option }}" required>
            {{ option }}
            </label>
            </p>
        {% endfor %}

    {% endfor %}

    <br>
    <button type="submit"
    style="padding:15px 30px;background:#2563eb;
    color:white;border:none;">
    SUBMIT ANSWERS
    </button>

    </form>
    </body>
    """, name=name, category=category,
    quiz=questions[category])


@app.route("/result", methods=["POST"])
def result():

    category = request.form.get("category", "")
    name = request.form.get("name", "")

    if category not in questions:
        return "Invalid category!"

    score = 0
    total = len(questions[category])

    for i, q in enumerate(questions[category]):
        if request.form.get(f"q{i}") == q[2]:
            score += 1

    percentage = round((score / total) * 100)

    return render_template_string("""
    <body style="background:#101827;color:white;
    text-align:center;padding:60px;">

    <h1>QUIZ COMPLETED!</h1>
    <h2>Well done, {{ name }}!</h2>

    <h1>Your Score: {{ score }}/{{ total }}</h1>

    <h2>{{ percentage }}% Achievement</h2>

    <p>Thank you for playing!</p>

    <a href="/" style="color:#60a5fa;">
    PLAY AGAIN
    </a>

    </body>
    """, name=name, score=score,
    total=total, percentage=percentage)


if __name__ == "__main__":
    app.run(debug=True)
