<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Prime Game - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        h1, h2, h3 {
            color: #4a90e2;
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
        }

        h2 {
            margin-top: 30px;
            margin-bottom: 10px;
        }

        p {
            line-height: 1.6;
        }

        ul, ol {
            margin-left: 20px;
        }

        pre {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }

        code {
            font-family: 'Courier New', Courier, monospace;
            background-color: #f9f9f9;
            padding: 2px 5px;
            border-radius: 3px;
        }

        a {
            color: #4a90e2;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        section {
            margin-bottom: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Prime Game - README</h1>

        <section>
            <h2>Project Overview</h2>
            <p>
                Maria and Ben are engaged in a game involving prime numbers. The game starts with a set of consecutive integers from 1 up to a given value <code>n</code>. On each player's turn, they select a prime number from the set and remove that prime number and all of its multiples from the set. The player who cannot make a valid move loses the game.
            </p>
        </section>

        <section>
            <h2>Game Rules</h2>
            <ul>
                <li>The game is played in rounds, where each round has a different set size <code>n</code>.</li>
                <li>Players alternate picking prime numbers from the set.</li>
                <li>When a player picks a prime number, they must remove that prime and all of its multiples from the set.</li>
                <li>The player who cannot make a move loses the game.</li>
            </ul>
        </section>

        <section>
            <h2>Function Prototype</h2>
            <pre><code>def isWinner(x, nums)</code></pre>
            <p><strong>x:</strong> The number of rounds.<br>
            <strong>nums:</strong> An array of integers where each value represents the set size <code>n</code> for that round.</p>
        </section>

        <section>
            <h2>Return Value</h2>
            <p>The function returns the name of the player (<em>Maria</em> or <em>Ben</em>) who won the most rounds. If the winner cannot be determined, the function returns <code>None</code>.</p>
        </section>

        <section>
            <h2>Constraints</h2>
            <ul>
                <li>x and each n in nums will not be larger than 10,000.</li>
                <li>You cannot import any external packages for this task.</li>
            </ul>
        </section>

        <section>
            <h2>Example</h2>
            <pre><code>x = 3
nums = [4, 5, 1]
</code></pre>

            <h3>Round 1: n = 4</h3>
            <p>Maria picks 2, removing 2 and 4. Remaining set: {1, 3}<br>
            Ben picks 3, removing 3. Remaining set: {1}<br>
            Ben wins because there are no prime numbers left for Maria to choose.</p>

            <h3>Round 2: n = 5</h3>
            <p>Maria picks 2, removing 2 and 4. Remaining set: {1, 3, 5}<br>
            Ben picks 3, removing 3. Remaining set: {1, 5}<br>
            Maria picks 5, removing 5. Remaining set: {1}<br>
            Maria wins because there are no prime numbers left for Ben to choose.</p>

            <h3>Round 3: n = 1</h3>
            <p>Ben wins because there are no prime numbers for Maria to choose from.</p>

            <h3>Result</h3>
            <p>Ben wins 2 rounds, Maria wins 1 round.<br>
            The function returns <code>"Ben"</code>.</p>
        </section>

        <section>
            <h2>Usage</h2>
            <ol>
                <li>Clone the repository:
                    <pre><code>git clone https://github.com/yourusername/alx-interview.git</code></pre>
                </li>
                <li>Navigate to the project directory:
                    <pre><code>cd alx-interview/0x0A-primegame</code></pre>
                </li>
                <li>Run the <code>0-prime_game.py</code> script with the required inputs.</li>
            </ol>
        </section>

        <section>
            <h2>Author</h2>
            <p>Endurance Ossai - <a href="https://github.com/yourusername" target="_blank">GitHub</a></p>
        </section>
    </div>
</body>
</html>
