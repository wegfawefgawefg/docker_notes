const WIDTH = 3;
const HEIGHT = 3;

const allEqual = arr => arr.every(v => v === arr[0]);
const transpose = arrog => {
    let arr = JSON.parse(JSON.stringify(arrog));
    for (let i = 0; i < arr.length; i++) {
       for (let j = 0; j < i; j++) {
          const tmp = arr[i][j];
          arr[i][j] = arr[j][i];
          arr[j][i] = tmp;
       };
    }
    return arr;
 }

function makeGrid(width, height) {
    var grid = [];
    for (var y = 0; y < HEIGHT; y++) {
        var row = [];
        for (var x = 0; x < WIDTH; x++) {
            row.push(null);
        }
        grid.push(row);
    }
    return grid;
}

function getWinner(grid){
    let winner = null;
    // check rows
    for (let y = 0; y < HEIGHT; y++) {
        if (allEqual(grid[y])) {
            winner = grid[y][0];
            if(winner){
                return winner;
            }
        }
    }
    //  check colums
    let tgrid = transpose(grid);
    for (let y = 0; y < WIDTH; y++) {
        if (allEqual(tgrid[y])) {
            winner = tgrid[y][0]
            if(winner){
                return winner;
            }
        }
    }
    //  check diagonals
    console.log(grid);
    if( grid[0][0] === grid[1][1] && grid[1][1] === grid[2][2]){
        winner = grid[0][0];
        if(winner){
            return winner;
        }
    }
    if( grid[0][2] === grid[1][1] && grid[1][1] ===grid[2][0]){
        winner = grid[0][2];
        if(winner){
            return winner;
        }
    }
    return winner;
}

let grid = makeGrid();
// grid[0][0] = 'X';
// grid[0][1] = 'X';
// grid[0][2] = 'X';
grid[0][2] = 'X';
grid[1][2] = 'X';
grid[2][2] = 'X';
// grid[0][2] = 'X';
// grid[1][1] = 'X';
// grid[2][0] = 'X';
console.log(grid);
console.log(getWinner(grid))