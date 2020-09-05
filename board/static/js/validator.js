function validateForm() {
    let inputs = document.getElementsByClassName("square");
    grid = to2DGrid(inputs)
    let valid = isValidSudoku(grid);
    console.log(grid);
    console.log(typeof grid);
    if (!valid) {
        alert("Not a valid Sudoku puzzle! Please enter a valid puzzle and click \'Solve.\'");
        return false;
    }else{
        alert("Valid.");
    }
   
    return true;
}

/**
 * Changes from a list of HTML elements to a 2D array of Sudoku number strings.
 * @param {HTMLCollectionOf<Element>} inputs contains the list of inputs which correspond to Sudoku squares.
 */
function to2DGrid(inputs) {
    // todo: set the grid size based off the the number of inputs on the front end.
    const GRID_SIZE = 9;
    // todo: figure out how to dynamically add cols based off of the grid size.
    let grid = [[], [], [], [], [], [], [], [], []];
    let j = 0;
    for (let i = 0; i < inputs.length; i++) {
        if (i % (GRID_SIZE) == 0 && i != 0) {
            j++;
        }
        square_value = inputs[i].value;
        grid[j].push(square_value);
    }
    return grid;
}

function isValidSudoku(grid) {

    for (i = 0; i < grid.length; i++) {
        if (!hasNoDuplicates(grid[i]) /*|| !hasNoDuplicates(getCol(grid, i))*/) {
            console.log("failing, here")
            return false;
        }
    }

    // (0,0) (0,3) (0,6) 
    // (3,0) (3,3) (3,6)
    // (6,0) (6,3) (6,6)
    for (offi = 0; offi <= grid.length - 3; offi += 3) {
        for (offj = 0; offj <= grid.length - 3; offj += 3) {

            if (!hasNoDuplicates(getSubGrid(grid, offi, offj))) {
                console.log("failing, here too")
                return false;
            }
        }
    }
    return true;
};

function hasNoDuplicates(grid) {
    let set = new Set();
    console.log(typeof grid[0]);
    for (let i = 0; i < grid.length; i++) {
        //" ", "", "      " all should not be processed
        if (grid[i] !== undefined && grid[i].trim() !== "") {
            if (set.has(grid[i]) || !isValidSudokuClue(grid[i])) {
                return false;
            }
            set.add(grid[i]);
        }
    }
    return true;
};

function getCol(matrix, col) {
    let column = [];

    for (let i = 0; i < matrix.length; i++) {
        column.push(matrix[i][col]);
    }
    return column;
}

function getSubGrid(grid, offi, offj) {
    let grid = [];
    for (let i = offi; i < (offi + 3); i++) {
        for (j = offj; j < (offj + 3); j++) {
            grid.push(grid[i][j]);
        }
    }
    return grid;
}

/**
 * If between 1-9 it is a valid clue.
 * @param {String} clue a valid or invalid sudoku clue. 
 */
function isValidSudokuClue(clue){
    return Number(clue) >= 0 && Number(clue) <=9;
}