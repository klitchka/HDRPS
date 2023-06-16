pragma solidity ^0.8.0;

contract RockPaperScissors {
    address public player;
    address public computer;
    uint256 public scorePlayer;
    uint256 public scoreComputer;
    
    enum Move {None, Rock, Paper, Scissors}
    
    mapping(Move => Move) private rules;
    
    event GameResult(address indexed player, address indexed computer, Move playerMove, Move computerMove, string result);
    
    constructor() {
        player = msg.sender;
        computer = address(0); // Computer's address is not known initially
        scorePlayer = 0;
        scoreComputer = 0;
        
        // Define the game rules
        rules[Move.None] = Move.None;
        rules[Move.Rock] = Move.Scissors;
        rules[Move.Paper] = Move.Rock;
        rules[Move.Scissors] = Move.Paper;
    }
    
    function joinGame() public {
        require(computer == address(0), "Game is already full.");
        computer = msg.sender;
    }
    
    function play(Move playerMove) public {
        require(msg.sender == player, "Only the player can make a move.");
        require(computer != address(0), "Game is not full yet.");
        
        Move computerMove = Move(uint256(blockhash(block.number - 1)) % 3 + 1);
        string memory result;
        
        if (playerMove == computerMove) {
            result = "It's a tie!";
        } else if (rules[playerMove] == computerMove) {
            result = "You win!";
            scorePlayer++;
        } else {
            result = "Computer wins!";
            scoreComputer++;
        }
        
        emit GameResult(player, computer, playerMove, computerMove, result);
    }
}
