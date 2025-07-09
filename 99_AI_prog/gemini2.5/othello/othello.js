document.addEventListener('DOMContentLoaded', () => {
    // --- DOM Elements ---
    const titleContainer = document.getElementById('title-container');
    const setupContainer = document.getElementById('setup-container');
    const gameContainer = document.getElementById('game-container');

    const showSetupButton = document.getElementById('show-setup-button');
    const startGameButton = document.getElementById('start-game-button');
    const backToTitleButton = document.getElementById('back-to-title-button');
    const restartButton = document.getElementById('restart-button'); // This now means "back to setup"

    const modePvpRadio = document.getElementById('mode-pvp');
    const modePvcRadio = document.getElementById('mode-pvc');
    const cpuOptionsElement = document.getElementById('cpu-options');
    const cpuLevelSelect = document.getElementById('cpu-level');

    const boardElement = document.getElementById('board');
    const currentPlayerElement = document.getElementById('current-player');
    const blackScoreElement = document.getElementById('black-score');
    const whiteScoreElement = document.getElementById('white-score');
    const messageElement = document.getElementById('message');
    const progressContainerElement = document.getElementById('progress-container');
    const progressBarElement = document.getElementById('progress-bar');

    // --- Game State ---
    const boardSize = 8;
    let board = [];
    let currentPlayer = 'black';
    let gameMode = 'pvc'; // Default
    let cpuLevel = 5;
    let playerColor = 'black';
    let cpuColor = 'white';
    let isThinking = false;

    const boardWeights = [
        [120, -20, 20, 5, 5, 20, -20, 120],
        [-20, -40, -5, -5, -5, -5, -40, -20],
        [20, -5, 15, 3, 3, 15, -5, 20],
        [5, -5, 3, 3, 3, 3, -5, 5],
        [5, -5, 3, 3, 3, 3, -5, 5],
        [20, -5, 15, 3, 3, 15, -5, 20],
        [-20, -40, -5, -5, -5, -5, -40, -20],
        [120, -20, 20, 5, 5, 20, -20, 120]
    ];

    // --- Event Listeners for Screen Transitions ---
    showSetupButton.addEventListener('click', () => {
        titleContainer.classList.add('hidden');
        setupContainer.classList.remove('hidden');
    });

    backToTitleButton.addEventListener('click', () => {
        setupContainer.classList.add('hidden');
        titleContainer.classList.remove('hidden');
    });

    startGameButton.addEventListener('click', () => {
        // Get settings from the setup screen
        gameMode = document.querySelector('input[name="game-mode"]:checked').value;
        if (gameMode === 'pvc') {
            cpuLevel = parseInt(cpuLevelSelect.value);
            playerColor = document.querySelector('input[name="player-color"]:checked').value;
            cpuColor = playerColor === 'black' ? 'white' : 'black';
        }

        // Transition to the game screen and start the game
        setupContainer.classList.add('hidden');
        gameContainer.classList.remove('hidden');
        initGame();
    });

    restartButton.addEventListener('click', () => {
        // Go back to the setup screen from the game screen
        gameContainer.classList.add('hidden');
        setupContainer.classList.remove('hidden');
    });

    // --- Event Listeners for Setup Options ---
    modePvpRadio.addEventListener('change', () => {
        if (modePvpRadio.checked) {
            cpuOptionsElement.classList.add('hidden');
        }
    });

    modePvcRadio.addEventListener('change', () => {
        if (modePvcRadio.checked) {
            cpuOptionsElement.classList.remove('hidden');
        }
    });

    // --- Game Logic (The rest of the functions: initGame, renderBoard, etc.) ---
    function initGame() {
        board = Array(boardSize).fill(null).map(() => Array(boardSize).fill(null));
        board[3][3] = 'white';
        board[3][4] = 'black';
        board[4][3] = 'black';
        board[4][4] = 'white';
        currentPlayer = 'black';
        messageElement.textContent = '';
        isThinking = false;
        progressContainerElement.classList.add('hidden');

        updateTurnClasses();

        renderBoard();
        updateScores();
        highlightValidMoves();

        if (gameMode === 'pvc' && currentPlayer === cpuColor) {
            cpuMove();
        }
    }

    function renderBoard() {
        boardElement.innerHTML = '';
        for (let row = 0; row < boardSize; row++) {
            for (let col = 0; col < boardSize; col++) {
                const cell = document.createElement('div');
                cell.classList.add('cell');
                cell.dataset.row = row;
                cell.dataset.col = col;
                if (board[row][col]) {
                    const disc = document.createElement('div');
                    disc.classList.add('disc', board[row][col]);
                    cell.appendChild(disc);
                }
                boardElement.appendChild(cell);
            }
        }
        boardElement.querySelectorAll('.cell').forEach(cell => {
            cell.addEventListener('click', handleCellClick);
            // プレビュー機能のためにマウスイベントリスナーを追加
            cell.addEventListener('mouseenter', handleCellMouseEnter);
            cell.addEventListener('mouseleave', handleCellMouseLeave);
        });
    }

    function updateScores() {
        const scores = board.flat().reduce((acc, val) => {
            if (val) acc[val]++;
            return acc;
        }, { black: 0, white: 0 });

        blackScoreElement.textContent = scores.black;
        whiteScoreElement.textContent = scores.white;
        currentPlayerElement.textContent = `${currentPlayer === 'black' ? '黒' : '白'}`;
    }

    function handleCellClick(event) {
        if (isThinking) return;
        // For PVC, only allow clicks if it's the player's turn
        if (gameMode === 'pvc' && currentPlayer === cpuColor) return;

        const row = parseInt(event.currentTarget.dataset.row);
        const col = parseInt(event.currentTarget.dataset.col);

        if (isValidMove(row, col, currentPlayer, board)) {
            clearPreview(); // 石を置く直前にプレビューをクリア
            placeAndFlip(row, col, currentPlayer);
            switchPlayer();
        } else {
            messageElement.textContent = 'そこには置けません。';
        }
    }

    function placeAndFlip(row, col, player) {
        const flippedDiscs = getFlippedDiscs(row, col, player, board);
        board[row][col] = player;
        flippedDiscs.forEach(([r, c]) => { board[r][c] = player; });
    }

    function switchPlayer() {
        currentPlayer = currentPlayer === 'black' ? 'white' : 'black';

        updateTurnClasses();

        renderBoard();
        updateScores();
        highlightValidMoves();
        messageElement.textContent = '';

        if (isGameOver(board)) {
            endGame();
            return;
        }

        // Check for pass
        if (!hasValidMove(currentPlayer, board)) {
            messageElement.textContent = `${currentPlayer === 'black' ? '黒' : '白'}はパスします。`;
            // Wait a moment before the other player plays
            setTimeout(() => {
                currentPlayer = currentPlayer === 'black' ? 'white' : 'black';
                updateTurnClasses();
                updateScores();
                highlightValidMoves();
                if (isGameOver(board)) {
                    endGame();
                    return;
                }
                if (gameMode === 'pvc' && currentPlayer === cpuColor) {
                    cpuMove();
                }
            }, 1000);
            return;
        }

        // If it's CPU's turn, make a move
        if (gameMode === 'pvc' && currentPlayer === cpuColor) {
            cpuMove();
        }
    }

    function cloneBoard(currentBoard) {
        return currentBoard.map(row => [...row]);
    }

    function hasValidMove(player, currentBoard) {
        return getValidMoves(player, currentBoard).length > 0;
    }

    function highlightValidMoves() {
        // Remove previous highlights
        boardElement.querySelectorAll('.valid-move').forEach(cell => {
            cell.classList.remove('valid-move');
        });

        // Get and show valid moves for the current player
        const validMoves = getValidMoves(currentPlayer, board);
        validMoves.forEach(({ row, col }) => {
            const cell = boardElement.querySelector(`[data-row='${row}'][data-col='${col}']`);
            if (cell) { // Check if cell exists
                cell.classList.add('valid-move');
            }
        });
    }

    function isValidMove(row, col, player, currentBoard) {
        if (currentBoard[row]?.[col] !== null) {
            return false;
        }
        // getFlippedDiscsの結果が空配列でなければ、その手は有効
        return getFlippedDiscs(row, col, player, currentBoard).length > 0;
    }

    function getFlippedDiscs(row, col, player, currentBoard) {
        const flipped = [];
        const opponent = player === 'black' ? 'white' : 'black';
        const directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];

        for (const [dr, dc] of directions) {
            let r = row + dr;
            let c = col + dc;
            const potentialFlips = [];

            while (r >= 0 && r < boardSize && c >= 0 && c < boardSize && currentBoard[r][c] === opponent) {
                potentialFlips.push([r, c]);
                r += dr;
                c += dc;
            }

            if (r >= 0 && r < boardSize && c >= 0 && c < boardSize && currentBoard[r][c] === player) {
                flipped.push(...potentialFlips);
            }
        }
        return flipped;
    }

    function getValidMoves(player, currentBoard) {
        const validMoves = [];
        for (let row = 0; row < boardSize; row++) {
            for (let col = 0; col < boardSize; col++) {
                if (isValidMove(row, col, player, currentBoard)) {
                    validMoves.push({ row, col });
                }
            }
        }
        return validMoves;
    }

    function isGameOver(currentBoard) {
        return !hasValidMove('black', currentBoard) && !hasValidMove('white', currentBoard);
    }

    function endGame() {
        const scores = board.flat().reduce((acc, val) => {
            if (val) acc[val]++;
            return acc;
        }, { black: 0, white: 0 });

        let winnerMessage;
        if (scores.black > scores.white) {
            winnerMessage = '黒の勝ちです！';
        } else if (scores.white > scores.black) {
            winnerMessage = '白の勝ちです！';
        } else {
            winnerMessage = '引き分けです。';
        }
        messageElement.textContent = `ゲーム終了！ ${winnerMessage}`;
    }

    // --- CPU Logic ---
    async function cpuMove() {
        isThinking = true;
        clearPreview(); // 念のためプレビューをクリア
        messageElement.textContent = 'CPUが考慮中です...';
        progressContainerElement.classList.remove('hidden');
        progressBarElement.style.width = '0%';
        boardElement.style.pointerEvents = 'none';

        // 少し待って「考慮中」メッセージを表示させる
        await new Promise(resolve => setTimeout(resolve, 50));

        const depth = cpuLevel;
        const bestMove = await findBestMove(board, cpuColor, depth);

        // 最終的な手に確定したプレビューを少し見せる
        if (bestMove) {
            await new Promise(resolve => setTimeout(resolve, 500));
            clearPreview(); // 石を置く直前にプレビューを消す
            placeAndFlip(bestMove.row, bestMove.col, cpuColor);
        } else {
            // パスの場合など
            clearPreview();
        }

        isThinking = false;
        boardElement.style.pointerEvents = 'auto';
        progressContainerElement.classList.add('hidden');
        switchPlayer();
    }

    async function findBestMove(currentBoard, player, depth) {
        const validMoves = getValidMoves(player, currentBoard);
        if (validMoves.length === 0) return null;
        if (validMoves.length === 1) {
            showPreview(validMoves[0].row, validMoves[0].col);
            return validMoves[0];
        }

        let bestScore = -Infinity;
        let bestMove = validMoves[0];

        // 最初の候補をまずプレビュー
        showPreview(bestMove.row, bestMove.col);

        for (let i = 0; i < validMoves.length; i++) {
            const move = validMoves[i];
            const tempBoard = cloneBoard(currentBoard);
            applyMove(tempBoard, move, player);
            const score = alphaBeta(tempBoard, depth - 1, -Infinity, Infinity, false, player);

            if (score > bestScore) {
                bestScore = score;
                bestMove = move;
                // 最善手が変わるたびにプレビューを更新
                clearPreview();
                showPreview(bestMove.row, bestMove.col);
            }

            const progress = ((i + 1) / validMoves.length) * 100;
            progressBarElement.style.width = `${progress}%`;

            // UIが固まらないように、ループ内で少し待機する
            await new Promise(resolve => setTimeout(resolve, 10));
        }
        return bestMove;
    }

    function alphaBeta(currentBoard, depth, alpha, beta, isMaximizingPlayer, originalPlayer) {
        if (depth === 0 || isGameOver(currentBoard)) {
            return evaluateBoard(currentBoard, originalPlayer);
        }

        const opponent = originalPlayer === 'black' ? 'white' : 'black';
        const player = isMaximizingPlayer ? originalPlayer : opponent;
        const validMoves = getValidMoves(player, currentBoard);

        if (validMoves.length === 0) {
            return alphaBeta(currentBoard, depth - 1, alpha, beta, !isMaximizingPlayer, originalPlayer);
        }

        if (isMaximizingPlayer) {
            let maxEval = -Infinity;
            for (const move of validMoves) {
                const childBoard = cloneBoard(currentBoard);
                applyMove(childBoard, move, player);
                const evalScore = alphaBeta(childBoard, depth - 1, alpha, beta, false, originalPlayer);
                maxEval = Math.max(maxEval, evalScore);
                alpha = Math.max(alpha, evalScore);
                if (beta <= alpha) {
                    break;
                }
            }
            return maxEval;
        } else {
            let minEval = Infinity;
            for (const move of validMoves) {
                const childBoard = cloneBoard(currentBoard);
                applyMove(childBoard, move, player);
                const evalScore = alphaBeta(childBoard, depth - 1, alpha, beta, true, originalPlayer);
                minEval = Math.min(minEval, evalScore);
                beta = Math.min(beta, evalScore);
                if (beta <= alpha) {
                    break;
                }
            }
            return minEval;
        }
    }

    function applyMove(currentBoard, move, player) {
        const { row, col } = move;
        const flippedDiscs = getFlippedDiscs(row, col, player, currentBoard);
        currentBoard[row][col] = player;
        flippedDiscs.forEach(([r, c]) => { currentBoard[r][c] = player; });
    }

    function evaluateBoard(currentBoard, player) {
        const opponent = player === 'black' ? 'white' : 'black';
        let playerScore = 0;
        let opponentScore = 0;

        for (let row = 0; row < boardSize; row++) {
            for (let col = 0; col < boardSize; col++) {
                if (currentBoard[row][col] === player) {
                    playerScore += boardWeights[row][col];
                } else if (currentBoard[row][col] === opponent) {
                    opponentScore += boardWeights[row][col];
                }
            }
        }
        return playerScore - opponentScore;
    }

    /**
     * 現在のターンに応じてbodyタグのクラスを更新する
     */
    function updateTurnClasses() {
        document.body.classList.remove('turn-black', 'turn-white', 'cpu-turn');
        document.body.classList.add(`turn-${currentPlayer}`);
        if (gameMode === 'pvc' && currentPlayer === cpuColor) {
            document.body.classList.add('cpu-turn');
        }
    }

    // --- Preview Logic ---

    /**
     * マウスがセルに乗った時の処理
     * @param {MouseEvent} event - マウスイベント
     */
    function handleCellMouseEnter(event) {
        if (isThinking) return; // CPU思考中はプレビューしない
        const cell = event.currentTarget;

        // 有効な手を示すマーカーが付いているセルでのみプレビューを表示
        if (!cell.classList.contains('valid-move')) return;

        const row = parseInt(cell.dataset.row);
        const col = parseInt(cell.dataset.col);

        showPreview(row, col);
    }

    /**
     * マウスがセルから離れた時の処理
     */
    function handleCellMouseLeave() {
        if (isThinking) return;
        clearPreview();
    }

    /**
     * 指定された位置に石を置いた場合のプレビューを表示する
     * @param {number} row - 石を置く行
     * @param {number} col - 石を置く列
     */
    function showPreview(row, col) {
        // 1. これから置く石のプレビュー（半透明）
        const targetCell = boardElement.querySelector(`[data-row='${row}'][data-col='${col}']`);
        if (!targetCell) return;

        const previewDisc = document.createElement('div');
        // 'preview-disc'と現在のプレイヤーの色クラスを付与
        previewDisc.className = `preview-disc ${currentPlayer}`;
        targetCell.appendChild(previewDisc);

        // 2. ひっくり返る石のプレビュー（色が反転）
        const flippedDiscs = getFlippedDiscs(row, col, currentPlayer, board);
        flippedDiscs.forEach(([r, c]) => {
            const flippedCell = boardElement.querySelector(`[data-row='${r}'][data-col='${c}']`);
            const disc = flippedCell?.querySelector('.disc');
            if (disc) {
                // 'preview-flip'クラスを付与してCSSで見た目を変更
                disc.classList.add('preview-flip');
            }
        });
    }

    /**
     * すべてのプレビュー表示をクリアする
     */
    function clearPreview() {
        // 半透明のプレビュー石を全て削除
        const previewDiscs = boardElement.querySelectorAll('.preview-disc');
        previewDiscs.forEach(disc => disc.remove());

        // ひっくり返る石のハイライト（クラス）を全て削除
        const flippedPreviews = boardElement.querySelectorAll('.preview-flip');
        flippedPreviews.forEach(disc => disc.classList.remove('preview-flip'));
    }

    // --- Initial setup ---
    // Initially, show the title screen
    titleContainer.classList.remove('hidden');
    setupContainer.classList.add('hidden');
    gameContainer.classList.add('hidden');
    // Set default state for CPU options
    if (modePvcRadio.checked) {
        cpuOptionsElement.classList.remove('hidden');
    }
});
