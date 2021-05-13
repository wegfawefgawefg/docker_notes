import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

function Square(props) {
    return (
        <button
            className="square"
            onClick={() => props.onClick()}
        >
            {props.value}
        </button>
    );
}

function getWinner(grid) {
    let winner = null;
    // check rows
    for (let y = 0; y < 3; y++) {
        if (grid[y][0] === grid[y][1] && grid[y][1] === grid[y][2]) {
            winner = grid[y][0];
            if (winner) {
                return winner;
            }
        }
    }
    //  check colums
    for (let x = 0; x < 3; x++) {
        if (grid[0][x] === grid[1][x] && grid[1][x] === grid[2][x]) {
            winner = grid[0][x];
            if (winner) {
                return winner;
            }
        }
    }
    //  check diagonals
    if (grid[0][0] === grid[1][1] && grid[1][1] === grid[2][2]) {
        winner = grid[0][0];
        if (winner) {
            return winner;
        }
    }
    if (grid[0][2] === grid[1][1] && grid[1][1] === grid[2][0]) {
        winner = grid[0][2];
        if (winner) {
            return winner;
        }
    }
    return winner;
}


class Board extends React.Component {
    renderSquare(x, y) {
        return (
            <Square
                value={this.props.grid[y][x]}
                onClick={() => this.props.onClick(x, y)}
            />
        )
    }

    renderRow(length, y) {
        let squares = [];
        for (let x = 0; x < length; x++) {
            squares.push(
                this.renderSquare(x, y)
            );
        }
        return (
            <div className="board-row">
                {squares}
            </div>
        )
    }

    render() {
        let rows = []
        for (let y = 0; y < 3; y++) {
            rows.push(this.renderRow(3, y));
        }
        return (<div>{rows}</div>);
    }
}

class Game extends React.Component {
    constructor(props) {
        super(props);
        let grid = [];
        for (let y = 0; y < 3; y++) {
            let row = [];
            for (let x = 0; x < 3; x++) {
                row.push(null);
            }
            grid.push(row);
        }
        this.state = {
            history: [{
                grid: grid,
            }],
            turnNum: 0,
            player: 'X',
        }
    }

    jumpTo(turn) {
        let player = ((turn % 2 === 0) ? 'O' : 'X');
        this.setState({
            turnNum: turn,
            player: player
        })
    }

    handleClick(x, y) {
        const history = this.state.history.slice(0, this.state.turnNum + 1);
        const nowTimeFrame = history[this.state.turnNum];
        if (getWinner(nowTimeFrame.grid)) {
            return;
        }
        const grid = nowTimeFrame.grid.slice();
        let nextPlayer = this.state.player;
        if (grid[y][x] === null) {
            grid[y][x] = this.state.player;
            nextPlayer = ((this.state.player === 'X') ? 'O' : 'X');
        }
        else{
            return;
        }

        this.setState({
            history: history.concat([{
                grid: grid,
            }]),
            player: nextPlayer,
            turnNum: this.state.history.length,
        });
    }

    render() {
        const history = this.state.history;
        const nowTimeFrame = history[this.state.turnNum];
        const winner = getWinner(nowTimeFrame.grid);

        const moves = history.map((grid, turnNum) => {
            const desc = turnNum ?
                'Go go move #' + turnNum :
                'Go to game start';
            return (
                <li key={turnNum}>
                    <button onClick={() => this.jumpTo(turnNum)}>
                        {desc}
                    </button>
                </li>
            )
        })

        let status = null;
        if (winner) {
            status = 'Winner: ' + winner;
        } else {
            status = 'Next player: ' + this.state.player;
        }

        return (
            <div className="game">
                <div className="game-board">
                    <Board
                        grid={nowTimeFrame.grid}
                        onClick={(x, y) => this.handleClick(x, y)}
                    />
                </div>
                <div className="game-info">
                    <div>{status}</div>
                    <ol>{moves}</ol>
                </div>
            </div>
        );
    }
}

// ========================================

ReactDOM.render(
    <Game />,
    document.getElementById('root')
);
