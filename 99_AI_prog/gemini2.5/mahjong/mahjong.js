// 牌の種類
const TILES = [
    // 萬子
    'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9',
    // 筒子
    'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9',
    // 索子
    's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9',
    // 字牌
    'ew', 'sw', 'ww', 'nw', 'wd', 'gd', 'rd' // 東南西北白発中
];

// 牌の画像パスを生成するためのプレフィックス
const TILE_IMAGE_PATH = 'img/';

// ゲームの状態
let gameState = {
    deck: [],
    playerHand: [],
    opponentHand: [],
    // 他のプレイヤーの手牌も同様
    river: [],
};

// ゲームの初期化
function initGame() {
    // 山を作成
    createDeck();
    // 牌を配る
    dealTiles();
    // UIを更新
    updateUI();
}

// 山を作成する関数
function createDeck() {
    gameState.deck = [];
    // 各牌を4枚ずつ山に入れる
    for (const tile of TILES) {
        for (let i = 0; i < 4; i++) {
            gameState.deck.push(tile);
        }
    }
    // 山をシャッフル
    shuffleDeck();
}

// 山をシャッフルする関数
function shuffleDeck() {
    for (let i = gameState.deck.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [gameState.deck[i], gameState.deck[j]] = [gameState.deck[j], gameState.deck[i]];
    }
}

// 牌を配る関数
function dealTiles() {
    // プレイヤーに13枚配る
    for (let i = 0; i < 13; i++) {
        gameState.playerHand.push(gameState.deck.pop());
        // 他のプレイヤーにも配る処理をここに追加
    }
}

// UIを更新する関数
function updateUI() {
    const playerHandDiv = document.getElementById('player-hand');
    playerHandDiv.innerHTML = '';
    for (const tile of gameState.playerHand) {
        const tileDiv = document.createElement('div');
        tileDiv.className = 'tile';

        // 牌の画像要素を作成
        const tileImage = document.createElement('img');
        // 画像のパスを設定 (例: img/m1.png)
        tileImage.src = `${TILE_IMAGE_PATH}${tile}.png`;
        tileImage.alt = tile; // 代替テキストとして牌のIDを設定

        tileDiv.appendChild(tileImage);

        // 赤ドラのスタイルはCSSで制御するように変更も可能
        // if (tile === 'm5' || tile === 'p5' || tile === 's5') {
        //     tileDiv.classList.add('red-dragon');
        // }

        playerHandDiv.appendChild(tileDiv);
    }
    // 他のUI要素の更新もここに追加
}

// ゲーム開始
initGame();
