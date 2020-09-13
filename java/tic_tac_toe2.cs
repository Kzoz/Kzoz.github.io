//////////////MODEL//////////////
var currentPlayer = 1;
var gameBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0];
var message = "";
var winner = 0; //0 means no winner yet

//////////////VIEW//////////////
function printGameBoard() {
    for (var i = 0; i < 9; i++) {
        if (gameBoard[i] == 1)
            setText("pos" + i, "X");
        else if (gameBoard[i] == 2) 
            setText("pos" + i, "O");
        else if (gameBoard[i] == 0) 
            setText("pos" + i, "");
        else 
            console.log("ERROR: INVALID GAMEBOARD");
    }
    setText("textArea", message);
}

//////////////CONTROLLER//////////////
function clicked(position) {
  message = "";
  if (winner != 0)
    return;
  if (gameBoard[position] != 0) {
    message = "ERROR: THIS POSITION IS ALREADY TAKEN";
    printGameBoard();
    return;
  }
  gameBoard[position] = currentPlayer;
  var result = checkGame(gameBoard);
  if (result != 0) {
    winner = result;
    if (winner == 3)
        message = "Game has ended in a tie";
    else
        message = "Player " + winner + " has won!";
  }
  currentPlayer = currentPlayer % 2 + 1;
  printGameBoard();
}

function reset(){
  currentPlayer = 1;
  gameBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0];
  message = "";
  winner = 0; //0 means no winner yet
  printGameBoard();
}

/////////////////////////////////////////////
//////////////CHECK FOR WINNERS//////////////
//1-X wins,  2-O wins, 3-Tie, 0-Not over
function checkGame(gameBoard) {
    var tieGame = checkTie(gameBoard);
    if (tieGame)
        return 3;
    var rowWinner = checkRows(gameBoard);
    if (rowWinner != 0)
        return rowWinner;
    var colWinner = checkColumns(gameBoard);
    if (colWinner != 0)
        return colWinner;
    var diagWinner = checkDiagonals(gameBoard);
    if (diagWinner != 0)
        return diagWinner;
        
    return 0;
}

//Return true if game has ended in a tie otherwise return false
function checkTie(gameBoard) {
    for (var i = 0; i < 9; i++) {
        if (gameBoard[i] == 0)
            return false;
    }
    return true;
}

//1- X wins, 2-O wins, 0-No one won any row
function checkRows(gameBoard) {
    var piece;
    piece = gameBoard[0];
    if (piece != 0 && piece == gameBoard[1] && piece == gameBoard[2])
        return piece;
    piece = gameBoard[3];
    if (piece != 0 && piece == gameBoard[4] && piece == gameBoard[5])
        return piece;
    piece = gameBoard[6];
    if (piece != 0 && piece == gameBoard[7] && piece == gameBoard[8])
        return piece;
    return 0;
}

//1- X wins, 2-O wins, 0-No one won any row
function checkColumns(gameBoard) {
    var piece;
    piece = gameBoard[0];
    if (piece != 0 && piece == gameBoard[3] && piece == gameBoard[6])
        return piece;
    piece = gameBoard[1];
    if (piece != 0 && piece == gameBoard[4] && piece == gameBoard[7])
        return piece;
    piece = gameBoard[2];
    if (piece != 0 && piece == gameBoard[5] && piece == gameBoard[8])
        return piece;
    return 0;
}

//1- X wins, 2-O wins, 0-No one won any row
function checkDiagonals(gameBoard) {
    var piece;
    piece = gameBoard[0];
    if (piece != 0 && piece == gameBoard[4] && piece == gameBoard[8])
        return piece;
    piece = gameBoard[2];
    if (piece != 0 && piece == gameBoard[4] && piece == gameBoard[6])
        return piece;
    return 0;
}
//////////////END CHECK FOR WINNERS//////////////
/////////////////////////////////////////////////

onEvent("pos0", "click", function(event) {clicked(0)});
onEvent("pos1", "click", function(event) {clicked(1)});
onEvent("pos2", "click", function(event) {clicked(2)});
onEvent("pos3", "click", function(event) {clicked(3)});
onEvent("pos4", "click", function(event) {clicked(4)});
onEvent("pos5", "click", function(event) {clicked(5)});
onEvent("pos6", "click", function(event) {clicked(6)});
onEvent("pos7", "click", function(event) {clicked(7)});
onEvent("pos8", "click", function(event) {clicked(8)});
onEvent("reset", "click", function(event) {reset();});