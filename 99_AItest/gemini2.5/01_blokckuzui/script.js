const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const startButton = document.getElementById('startButton');
const resetButton = document.getElementById('resetButton');
const scoreDisplay = document.getElementById('score');
const livesDisplay = document.getElementById('lives');

let ballRadius = 10;
let x = canvas.width / 2;
let y = canvas.height - 30;
let dx = 2;
let dy = -2;

let paddleHeight = 10;
let paddleWidth = 75;
let paddleX = (canvas.width - paddleWidth) / 2;

let rightPressed = false;
let leftPressed = false;

let brickOffsetTop = 30; // グローバルスコープに移動
let brickOffsetLeft = 30; // グローバルスコープに移動
let brickPadding = 10; // グローバルスコープに移動

let brickRowCount = 8; // ブロックの行数を増やす
let brickColumnCount = 10; // ブロックの列数を増やす
let brickWidth = (canvas.width - brickOffsetLeft * 2 - brickPadding * (brickColumnCount - 1)) / brickColumnCount; // canvasのサイズに合わせて調整
let brickHeight = 25; // ブロックの高さを少し大きく

let score = 0;
let lives = 3;
let gameStarted = false;
let animationFrameId;

const bricks = [];

function initBricks() {
    for (let c = 0; c < brickColumnCount; c++) {
        bricks[c] = [];
        for (let r = 0; r < brickRowCount; r++) {
            bricks[c][r] = { x: 0, y: 0, status: 1 };
        }
    }
}
initBricks();

document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);
document.addEventListener("mousemove", mouseMoveHandler, false);
startButton.addEventListener("click", startGame);
resetButton.addEventListener("click", resetGame);

function keyDownHandler(e) {
    if (e.key == "Right" || e.key == "ArrowRight") {
        rightPressed = true;
    } else if (e.key == "Left" || e.key == "ArrowLeft") {
        leftPressed = true;
    }
}

function keyUpHandler(e) {
    if (e.key == "Right" || e.key == "ArrowRight") {
        rightPressed = false;
    } else if (e.key == "Left" || e.key == "ArrowLeft") {
        leftPressed = false;
    }
}

function mouseMoveHandler(e) {
    const relativeX = e.clientX - canvas.offsetLeft;
    if (relativeX > 0 && relativeX < canvas.width) {
        paddleX = relativeX - paddleWidth / 2;
        if (paddleX < 0) paddleX = 0;
        if (paddleX + paddleWidth > canvas.width) paddleX = canvas.width - paddleWidth;
    }
}

function collisionDetection() {
    for (let c = 0; c < brickColumnCount; c++) {
        for (let r = 0; r < brickRowCount; r++) {
            const b = bricks[c][r];
            if (b.status == 1) {
                // ボールの中心がブロックの範囲内にあるか
                if (x > b.x && x < b.x + brickWidth && y > b.y && y < b.y + brickHeight) {
                    dy = -dy;
                    b.status = 0;
                    score++;
                    scoreDisplay.textContent = score;

                    // ボールがブロックの側面に当たった場合の反射処理を追加
                    // ブロックの左右の辺との衝突判定
                    let ballPrevX = x - dx;
                    if ((ballPrevX < b.x && x >= b.x) || (ballPrevX > b.x + brickWidth && x <= b.x + brickWidth)) {
                        if (!(y > b.y && y < b.y + brickHeight)) { // 上下には既に当たっていない場合
                            dx = -dx;
                        }
                    }

                    if (score == brickRowCount * brickColumnCount) {
                        alert("クリア！おめでとう！");
                        resetGame(true);
                    }
                }
            }
        }
    }
}

function drawBall() {
    ctx.beginPath();
    ctx.arc(x, y, ballRadius, 0, Math.PI * 2);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}

function drawPaddle() {
    ctx.beginPath();
    ctx.rect(paddleX, canvas.height - paddleHeight, paddleWidth, paddleHeight);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}

function drawBricks() {
    for (let c = 0; c < brickColumnCount; c++) {
        for (let r = 0; r < brickRowCount; r++) {
            if (bricks[c][r].status == 1) {
                const brickX = (c * (brickWidth + brickPadding)) + brickOffsetLeft;
                const brickY = (r * (brickHeight + brickPadding)) + brickOffsetTop;
                bricks[c][r].x = brickX;
                bricks[c][r].y = brickY;
                ctx.beginPath();
                ctx.rect(brickX, brickY, brickWidth, brickHeight);
                ctx.fillStyle = "#DD0095";
                ctx.fill();
                ctx.closePath();
            }
        }
    }
}

function drawInitialMessage() {
    ctx.font = "24px Arial";
    ctx.fillStyle = "#333";
    ctx.textAlign = "center";
    ctx.fillText("「スタート」ボタンを押してね！", canvas.width / 2, canvas.height / 2);
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBricks();
    drawBall();
    drawPaddle();
    collisionDetection();

    if (x + dx > canvas.width - ballRadius || x + dx < ballRadius) {
        dx = -dx;
    }
    if (y + dy < ballRadius) {
        dy = -dy;
    } else if (y + dy > canvas.height - ballRadius - paddleHeight) { // パドルの厚さを考慮
        if (x > paddleX && x < paddleX + paddleWidth) {
            // パドルに当たった位置によって反射角度を変える
            let collidePoint = x - (paddleX + paddleWidth / 2);
            // collidePoint は -paddleWidth/2 から paddleWidth/2 の範囲
            // 正規化して -1 から 1 の範囲にする
            collidePoint = collidePoint / (paddleWidth / 2);
            let angle = collidePoint * (Math.PI / 3); // 最大60度で反射
            dx = Math.sin(angle) * Math.sqrt(dx * dx + dy * dy); // 速度の大きさを維持
            dy = -Math.cos(angle) * Math.sqrt(dx * dx + dy * dy);
            if (dy > -1 && dy <= 0) dy = -1; // 最小 y 속도 보장
            if (dy < 0 && dy > -Math.abs(dx) * 0.5) dy = -Math.abs(dx) * 0.5; // y方向の速度が小さすぎないように調整

        } else {
            lives--;
            livesDisplay.textContent = lives;
            if (!lives) {
                alert("ゲームオーバー");
                resetGame(false);
                return;
            } else {
                x = canvas.width / 2;
                y = canvas.height - 30;
                dx = Math.random() < 0.5 ? 2 : -2; // ランダムな方向にボールを再開
                dy = -2;
                paddleX = (canvas.width - paddleWidth) / 2;
            }
        }
    }

    if (rightPressed && paddleX < canvas.width - paddleWidth) {
        paddleX += 7;
    } else if (leftPressed && paddleX > 0) {
        paddleX -= 7;
    }

    x += dx;
    y += dy;
    animationFrameId = requestAnimationFrame(draw);
}

function startGame() {
    if (!gameStarted) {
        gameStarted = true;
        startButton.style.display = 'none';
        resetButton.style.display = 'inline-block';
        score = 0;
        lives = 3;
        scoreDisplay.textContent = score;
        livesDisplay.textContent = lives;
        initBricks(); // ゲーム開始時にブロックを再初期化
        x = canvas.width / 2;
        y = canvas.height - 30;
        dx = 2;
        dy = -2;
        paddleX = (canvas.width - paddleWidth) / 2;
        if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
        }
        draw();
    }
}

function resetGame(isWin = false) {
    gameStarted = false;
    if (animationFrameId) {
        cancelAnimationFrame(animationFrameId);
    }
    startButton.style.display = 'inline-block';
    resetButton.style.display = 'none';

    x = canvas.width / 2;
    y = canvas.height - 30;
    paddleX = (canvas.width - paddleWidth) / 2;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    initBricks(); // リセット時にブロックを再描画
    drawBricks();
    drawPaddle();
    drawBall();

    if (!isWin && lives === 0) {
        ctx.font = "24px Arial";
        ctx.fillStyle = "#333";
        ctx.textAlign = "center";
        ctx.fillText("ゲームオーバー！「スタート」で再挑戦", canvas.width / 2, canvas.height / 2);
    } else if (isWin) {
        ctx.font = "24px Arial";
        ctx.fillStyle = "green";
        ctx.textAlign = "center";
        ctx.fillText("クリア！「スタート」で再挑戦", canvas.width / 2, canvas.height / 2);
    }
    else {
        drawInitialMessage();
    }

    scoreDisplay.textContent = 0;
    livesDisplay.textContent = 3;
}

function initialDraw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    // canvasのサイズ変更に伴い、ブロックの再計算と描画を行う
    brickWidth = (canvas.width - brickOffsetLeft * 2 - brickPadding * (brickColumnCount - 1)) / brickColumnCount;
    initBricks();
    drawBricks();
    drawPaddle();
    drawBall();
    drawInitialMessage();
}

initialDraw();
