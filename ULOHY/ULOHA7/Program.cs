public class Die
{
    private static Random random = new Random();

    public int Roll()
    {
        return random.Next(1, 7);
    }
}

public class Player
{
    public string Name { get; private set; }
    public int Score { get; private set; }
    private Die die;

    public Player(string name)
    {
        Name = name;
        Score = 0;
        die = new Die();
    }

    public int RollDice(out bool lostAllPoints)
    {
        int roll1 = die.Roll();
        int roll2 = die.Roll();
        lostAllPoints = false;

        Console.WriteLine($"{Name} hodil: {roll1} a {roll2}");

        if (roll1 == 1 && roll2 == 1)
        {
            Score = 0;
            lostAllPoints = true;
            return 0;
        }
        else if (roll1 == 1 || roll2 == 1)
        {
            return 0;
        }
        else
        {
            return roll1 + roll2;
        }
    }

    public void AddToScore(int points)
    {
        Score += points;
    }
}

public class Game
{
    private List<Player> players;
    private int winningScore;

    public List<Player> Players => players;

    public Game(int winningScore)
    {
        this.winningScore = winningScore;
        players = new List<Player>();
    }

    public void AddPlayer(string name)
    {
        if (players.Exists(p => p.Name.Equals(name, StringComparison.OrdinalIgnoreCase)))
        {
            Console.WriteLine($"Hráč se jménem {name} už existuje.");
            Environment.Exit(0);
        }
        players.Add(new Player(name));
    }

    public void Play()
    {
        if (players.Count < 2 || players.Count > 5)
        {
            Console.WriteLine("Může hrát pouze 2 - 5 hráčů.");
            Environment.Exit(0);
        }

        bool gameWon = false;
        int currentPlayerIndex = 0;

        while (!gameWon)
        {
            Player currentPlayer = players[currentPlayerIndex];
            Console.WriteLine($"\nTah hráče {currentPlayer.Name}:");

            bool lostAllPoints;
            int rollScore = currentPlayer.RollDice(out lostAllPoints);

            if (!lostAllPoints)
            {
                currentPlayer.AddToScore(rollScore);
            }

            Console.WriteLine($"{currentPlayer.Name} má teď {currentPlayer.Score} bodů.");

            if (currentPlayer.Score >= winningScore)
            {
                gameWon = true;
                Console.WriteLine($"\n{currentPlayer.Name} vyhrál hru s {currentPlayer.Score} body!");
            }

            currentPlayerIndex = (currentPlayerIndex + 1) % players.Count;

            Console.ReadLine();
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Game game = new Game(100);
        Console.WriteLine(new string('-', 65));
        Console.WriteLine(@"
 ___   ___   ______   ______   _________  ___   ___   __  __    
/___/\/__/\ /_____/\ /_____/\ /________/\/___/\/__/\ /_/\/_/\   
\::.\ \\ \ \\:::_ \ \\::::_\/_\__.::.__\/\::.\ \\ \ \\ \ \ \ \  
 \:: \/_) \ \\:\ \ \ \\:\/___/\  \::\ \   \:: \/_) \ \\:\_\ \ \ 
  \:. __  ( ( \:\ \ \ \\_::._\:\  \::\ \   \:. __  ( ( \::::_\/ 
   \: \ )  \ \ \:\_\ \ \ /____\:\  \::\ \   \: \ )  \ \  \::\ \ 
    \__\/\__\/  \_____\/ \_____\/   \__\/    \__\/\__\/   \__\/  
        ");
        Console.WriteLine(new string('-', 65));
        Console.WriteLine("Jména hráčů (oddělte čárkami):");
        string[] playerNames = Console.ReadLine().Split(',');

        foreach (string name in playerNames)
        {
            string trimmedName = name.Trim();
            game.AddPlayer(trimmedName);
        }

        game.Play();
    }
}
