```mermaid
flowchart TD
    A([Start]) --> B[温度を入力]
    B --> C{t > 30?}
    C -- はい --> D[クーラー]
    C -- いいえ --> E[off]
    D --> F([end])
    E --> F
```