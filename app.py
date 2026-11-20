
from flask import Flask, request, render_template_string

app = Flask(__name__)

# =========================
# QUIZ QUESTIONS
# =========================

questions = {
    "General Knowledge": [
        ("What is the capital city of Tanzania?",
         ["Dodoma", "Dar es Salaam", "Arusha", "Mwanza"], "Dodoma"),

        ("How many days are in a leap year?",
         ["364", "365", "366", "367"], "366"),

        ("Which planet is known as the Red Planet?",
         ["Earth", "Mars", "Jupiter", "Venus"], "Mars"),

        ("How many continents are there?",
         ["5", "6", "7", "8"], "7"),

        ("Which is the largest ocean?",
         ["Atlantic", "Indian", "Pacific", "Arctic"], "Pacific"),

        ("Who invented the telephone?",
         ["Newton", "Alexander Graham Bell", "Einstein", "Edison"],
         "Alexander Graham Bell"),

        ("What is the fastest land animal?",
         ["Lion", "Horse", "Cheetah", "Leopard"], "Cheetah"),

        ("How many colours are in a rainbow?",
         ["5", "6", "7", "8"], "7"),

        ("Which country is famous for the Eiffel Tower?",
         ["Italy", "France", "Germany", "Spain"], "France"),

        ("What is the largest planet?",
         ["Earth", "Mars", "Jupiter", "Saturn"], "Jupiter")
    ],

    "Health & Safety": [
        ("How many times should you brush your teeth daily?",
         ["Once", "Twice", "Five times", "Never"], "Twice"),

        ("Which food helps build strong bones?",
         ["Sweets", "Milk", "Soda", "Chips"], "Milk"),

        ("What should you do before eating?",
         ["Wash hands", "Sleep", "Run", "Watch TV"], "Wash hands"),

        ("Which organ pumps blood?",
         ["Brain", "Heart", "Lungs", "Stomach"], "Heart"),

        ("What should you do during a fire?",
         ["Hide", "Raise alarm and move to safety", "Ignore it", "Play"],
         "Raise alarm and move to safety"),

        ("Which vitamin is commonly produced through sunlight exposure?",
         ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"],
         "Vitamin D"),

        ("What is a balanced diet?",
         ["Eating only meat", "Eating different nutritious foods",
          "Eating only sweets", "Skipping meals"],
         "Eating different nutritious foods"),

        ("Which organ helps us breathe?",
         ["Heart", "Lungs", "Kidneys", "Liver"], "Lungs"),

        ("What should you do with an electrical appliance near water?",
         ["Use it", "Keep it away from water",
          "Touch it with wet hands", "Pour water on it"],
         "Keep it away from water"),

        ("Why is physical activity important?",
         ["It supports good health", "It causes laziness",
          "It stops learning", "It wastes food"],
         "It supports good health")
    ],

    "Technology": [
        ("What does CPU stand for?",
         ["Central Processing Unit", "Computer Personal Unit",
          "Central Power Unit", "Control Program Unit"],
         "Central Processing Unit"),

        ("Which device is used to type?",
         ["Mouse", "Keyboard", "Monitor", "Speaker"], "Keyboard"),

        ("What is the brain of a computer?",
         ["Monitor", "CPU", "Mouse", "Printer"], "CPU"),

        ("What does WWW stand for?",
         ["World Wide Web", "World Web Window",
          "Wide World Wire", "Web World Work"],
         "World Wide Web"),

        ("Which language is used for web page styling?",
         ["Python", "CSS", "C", "Java"], "CSS"),

        ("What is an example of an operating system?",
         ["Windows", "Google", "Facebook", "YouTube"], "Windows"),

        ("Which device stores information?",
         ["Flash disk", "Speaker", "Microphone", "Mouse"], "Flash disk"),

        ("What does HTML stand for?",
         ["HyperText Markup Language", "HighText Machine Language",
          "Hyper Transfer Main Link", "Home Tool Markup Language"],
         "HyperText Markup Language"),

        ("Which device displays computer information?",
         ["Keyboard", "Monitor", "Mouse", "Scanner"], "Monitor"),

        ("What is software?",
         ["Physical computer parts", "Programs and applications",
          "Electricity", "Computer table"],
         "Programs and applications")
    ],

    "Environment": [
        ("Which gas do plants absorb from the air?",
         ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
         "Carbon dioxide"),

        ("What is recycling?",
         ["Reusing materials", "Burning rubbish",
          "Throwing waste in rivers", "Wasting water"],
         "Reusing materials"),

        ("Which energy source is renewable?",
         ["Coal", "Petrol", "Solar energy", "Diesel"],
         "Solar energy"),

        ("Which activity causes air pollution?",
         ["Planting trees", "Burning fuels", "Cleaning", "Recycling"],
         "Burning fuels"),

        ("What do trees release during photosynthesis?",
         ["Carbon dioxide", "Oxygen", "Nitrogen", "Smoke"],
         "Oxygen"),

        ("Which of these is biodegradable?",
         ["Plastic bottle", "Banana peel", "Glass", "Metal can"],
         "Banana peel"),

        ("What is deforestation?",
         ["Planting trees", "Cutting down forests",
          "Watering plants", "Protecting forests"],
         "Cutting down forests"),

        ("Which gas contributes to global warming?",
         ["Oxygen", "Carbon dioxide", "Helium", "Neon"],
         "Carbon dioxide"),

        ("What is the best way to conserve water?",
         ["Leave taps running", "Repair leaking taps",
          "Waste water", "Pollute rivers"],
         "Repair leaking taps"),

        ("Which natural resource is essential for life?",
         ["Plastic", "Water", "Petrol", "Iron"],
         "Water")
    ],

    "Everyday Life": [
        ("What should you do when meeting someone?",
         ["Ignore them", "Greet them politely",
          "Shout at them", "Walk away"],
         "Greet them politely"),

        ("Why is saving money important?",
         ["For future needs", "To waste it",
          "To lose it", "To avoid working"],
         "For future needs"),

        ("What is time management?",
         ["Wasting time", "Planning how to use time",
          "Sleeping all day", "Avoiding responsibilities"],
         "Planning how to use time"),

        ("What is teamwork?",
         ["Working together", "Working against others",
          "Avoiding people", "Refusing help"],
         "Working together"),

        ("What should you do when crossing a road?",
         ["Run without looking", "Look both ways",
          "Close your eyes", "Use your phone"],
         "Look both ways"),

        ("What is honesty?",
         ["Telling the truth", "Stealing", "Cheating", "Lying"],
         "Telling the truth"),

        ("Why is education important?",
         ["It develops knowledge", "It wastes time",
          "It prevents thinking", "It stops creativity"],
         "It develops knowledge"),

        ("What is communication?",
         ["Sharing information", "Hiding information",
          "Avoiding people", "Sleeping"],
         "Sharing information"),

        ("What should you do when you make a mistake?",
         ["Learn from it", "Blame everyone",
          "Ignore every lesson", "Repeat it intentionally"],
         "Learn from it"),

        ("What is responsibility?",
         ["Doing your duties", "Avoiding work",
          "Blaming others", "Breaking promises"],
         "Doing your duties")
    ]
}


# =========================
# WEBSITE DESIGN
# =========================

BASE_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }} - LIFE KNOWLEDGE QUIZ MASTER</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0b1020;
            color: white;
        }

        .navbar {
            padding: 20px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #10182b;
            border-bottom: 1px solid #303d59;
        }

        .brand {
            font-size: 19px;
            font-weight: bold;
            color: #fbbf24;
        }

        .brand span {
            color: white;
        }

        .container {
            max-width: 850px;
            margin: 45px auto;
            padding: 20px;
        }

        .hero {
            text-align: center;
            padding: 45px 25px;
            background: linear-gradient(135deg, #182747, #35205e);
            border: 1px solid #59418b;
            border-radius: 24px;
            box-shadow: 0 15px 45px #0005;
        }

        .tag {
            display: inline-block;
            padding: 9px 16px;
            background: #ffffff15;
            border: 1px solid #ffffff30;
            border-radius: 30px;
            color: #fbbf24;
            font-size: 13px;
        }

        h1 {
            font-size: clamp(28px, 6vw, 46px);
            margin: 25px 0 12px;
        }

        h1 span {
            color: #fbbf24;
        }

        .subtitle {
            color: #cbd5e1;
            line-height: 1.7;
        }

        .card {
            background: #151e33;
            border: 1px solid #303d59;
            padding: 25px;
            margin: 22px 0;
            border-radius: 18px;
        }

        input[type="text"] {
            width: 100%;
            padding: 16px;
            border-radius: 10px;
            border: 1px solid #52617d;
            background: #0b1020;
            color: white;
            font-size: 16px;
            margin: 15px 0;
        }

        .btn {
            display: inline-block;
            padding: 15px 25px;
            background: linear-gradient(90deg, #6554ee, #9b4de0);
            color: white;
            text-decoration: none;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 15px;
            font-weight: bold;
        }

        .btn:hover {
            opacity: .85;
        }

        .category {
            display: block;
            width: 100%;
            margin: 13px 0;
            text-align: left;
            padding: 20px;
            background: #151e33;
            color: white;
            border: 1px solid #354463;
            border-radius: 12px;
            cursor: pointer;
            font-size: 16px;
        }

        .category:hover {
            border-color: #a78bfa;
            background: #25264a;
        }

        .question {
            background: #151e33;
            padding: 22px;
            border-radius: 15px;
            border: 1px solid #354463;
            margin: 20px 0;
        }

        .question h3 {
            line-height: 1.5;
            color: #fbbf24;
        }

        .option {
            display: block;
            background: #202b43;
            padding: 13px;
            border-radius: 9px;
            margin: 10px 0;
            cursor: pointer;
        }

        .option:hover {
            background: #373363;
        }

        .option input {
            margin-right: 10px;
            accent-color: #a78bfa;
        }

        .score {
            font-size: 55px;
            font-weight: bold;
            color: #fbbf24;
            margin: 20px;
        }

        .footer {
            text-align: center;
            padding: 30px;
            color: #8491aa;
            border-top: 1px solid #27304a;
            font-size: 13px;
        }

        @media(max-width:600px) {
            .container {
                margin: 20px auto;
                padding: 14px;
            }

            .hero {
                padding: 30px 15px;
            }

            .navbar {
                padding: 16px;
                font-size: 13px;
            }
        }
    </style>
</head>

<body>

    <div class="navbar">
        <div class="brand">
            LIFE <span>KNOWLEDGE</span>
        </div>

        <div style="color:#fbbf24">
            QUIZ MASTER ✦
        </div>
    </div>

    <main class="container">
        {{ content|safe }}
    </main>

    <div class="footer">
        LIFE KNOWLEDGE QUIZ MASTER
        <br><br>
        Challenge Your Mind. Expand Your Knowledge.
    </div>

</body>
</html>
"""


def page(content, title="Quiz Master"):
    return render_template_string(
        BASE_HTML,
        content=content,
        title=title
    )


# =========================
# HOME PAGE
# =========================

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form.get("player_name", "").strip()

        if not name:
            return "Please enter your name."

        return page(render_template_string("""
            <div class="card">

                <div class="tag">WELCOME {{ name|e }}</div>

                <h1>Choose Your <span>Category</span></h1>

                <p class="subtitle">
                    Select your favourite category and test
                    your knowledge.
                </p>

                {% for category in categories %}

                    <form action="/start" method="POST">

                        <input type="hidden"
                               name="name"
                               value="{{ name }}">

                        <input type="hidden"
                               name="category"
                               value="{{ category }}">

                        <button class="category" type="submit">
                            ✦ {{ category }} →
                        </button>

                    </form>

                {% endfor %}

            </div>
        """, name=name, categories=list(questions.keys())),
        "Choose Category")

    return page("""
        <div class="hero">

            <div class="tag">
                ✦ THE ULTIMATE KNOWLEDGE CHALLENGE ✦
            </div>

            <h1>
                LIFE <span>KNOWLEDGE</span>
            </h1>

            <h2>QUIZ MASTER</h2>

            <p class="subtitle">
                Challenge your mind. Discover new knowledge.
                Become a champion!
            </p>

            <div class="card">

                <h3>Ready to test yourself?</h3>

                <form method="POST">

                    <input type="text"
                           name="player_name"
                           placeholder="Enter your name..."
                           required>

                    <button class="btn" type="submit">
                        START YOUR JOURNEY →
                    </button>

                </form>

            </div>

            <p style="color:#fbbf24">
                5 Categories | 50 Questions | Unlimited Learning
            </p>

        </div>
    """, "Welcome")


# =========================
# START QUIZ
# =========================

@app.route("/start", methods=["POST"])
def start():

    name = request.form.get("name", "").strip()
    category = request.form.get("category", "")

    if category not in questions or not name:
        return "Invalid request!", 400

    return page(render_template_string("""
        <div class="card">

            <div class="tag">{{ category }}</div>

            <h1>Let's <span>Play!</span></h1>

            <p class="subtitle">
                Player: {{ name|e }}
                | Answer all 10 questions.
            </p>

            <form action="/result" method="POST">

                <input type="hidden"
                       name="name"
                       value="{{ name }}">

                <input type="hidden"
                       name="category"
                       value="{{ category }}">

                {% for q in quiz %}

                    {% set n = loop.index0 %}

                    <div class="question">

                        <h3>{{ loop.index }}. {{ q[0] }}</h3>

                        {% for option in q[1] %}

                            <label class="option">

                                <input type="radio"
                                       name="q{{ n }}"
                                       value="{{ option }}"
                                       required>

                                {{ option }}

                            </label>

                        {% endfor %}

                    </div>

                {% endfor %}

                <button class="btn" type="submit">
                    SUBMIT MY ANSWERS →
                </button>

            </form>

        </div>
    """,
    name=name,
    category=category,
    quiz=questions[category]),
    "Play Quiz")


# =========================
# RESULTS PAGE
# =========================

@app.route("/result", methods=["POST"])
def result():

    category = request.form.get("category", "")
    name = request.form.get("name", "").strip()

    if category not in questions or not name:
        return "Invalid request!", 400

    score = 0
    total = len(questions[category])

    for i, q in enumerate(questions[category]):

        answer = request.form.get(f"q{i}")

        if answer == q[2]:
            score += 1

    percentage = round((score / total) * 100)

    if percentage >= 80:
        message = "Excellent! You are a knowledge champion!"

    elif percentage >= 50:
        message = "Good job! Keep learning and improving!"

    else:
        message = "Keep practising! You can do better!"

    return page(render_template_string("""
        <div class="hero">

            <div class="tag">
                QUIZ COMPLETED ✦
            </div>

            <h1>
                Well Done, <span>{{ name|e }}</span>!
            </h1>

            <p class="subtitle">
                {{ message }}
            </p>

            <div class="score">
                {{ percentage }}%
            </div>

            <h2>Your Score</h2>

            <h2 style="color:#fbbf24">
                {{ score }} / {{ total }}
            </h2>

            <p class="subtitle">
                Category: {{ category }}
            </p>

            <a href="/" class="btn">
                PLAY AGAIN →
            </a>

        </div>
    """,
    name=name,
    score=score,
    total=total,
    percentage=percentage,
    category=category,
    message=message),
    "Your Results")


# =========================
# RUN WEBSITE
# =========================

if __name__ == "__main__":
    app.run(debug=True)
