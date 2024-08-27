function initDiv(div_id) {
    const div = document.getElementById(div_id);
    // Discard previous board
    while (div.firstChild) {
        div.removeChild(div.firstChild);
    }
    side = 7;
    html_board = [];

    for (let i = 0; i < side; i++) {
        html_board.push([]);
        for (let j = 0; j < side; j++) {
            let cell = document.createElement('div');
            cell.classList.add('cell');
            if (i == 0 || i == side - 1 || j == 0 || j == side - 1) {
                cell.classList.add('wall');
            } else {
                cell.classList.add('empty');
            }
            div.appendChild(cell);
            html_board[i].push(cell);
        }
    }
    return html_board;
}

function colorBoard(html_board, body, head, food) {
    for (let i = 0; i < html_board.length; i++) {
        for (let j = 0; j < html_board[0].length; j++) {
            html_board[i][j].classList.remove('wall', 'empty', 'snake', 'food', 'head');
            for (let k = 0; k < body.length; k++) {
                if (body[k][0] == i && body[k][1] == j) {
                    html_board[i][j].classList.add('snake');
                }
            }
            if (head[0] == i && head[1] == j) {
                html_board[i][j].classList.add('head');
            } else if (food[0] == i && food[1] == j) {
                html_board[i][j].classList.add('food');
            } else if (i == 0 || i == html_board.length - 1 || j == 0 || j == html_board[0].length - 1) {
                html_board[i][j].classList.add('wall');
            } else {
                html_board[i][j].classList.add('empty');
            }
        }
    }
}

const simulateButton = document.getElementById('simulate-button');
const numActionsInput = document.getElementById('num-actions');

simulateButton.addEventListener('click', async () => {
    const numActions = parseInt(numActionsInput.value);
    if (numActions < 1 || numActions > 100) {
        alert('Number of actions must be between 1 and 100');
        return;
    }

    try {
        const response = await fetch(`/api/simulate-snake-game?num_actions=${numActions}`);
        const data = await response.json();
        const html_board = initDiv('snake-board');
        bodies = data['bodies'];
        heads = data['heads'];
        foods = data['fruits'];

        for (let i = 0; i < bodies.length; i++) {
            colorBoard(html_board, bodies[i], heads[i], foods[i]);
            await new Promise(r => setTimeout(r, 200));
        }
    } catch (error) {
        console.error('Error:', error);
    }
});