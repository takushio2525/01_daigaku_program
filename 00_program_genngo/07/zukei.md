```mermaid
flowchart TD
    A([Start]) --> B[ i = 0 ]
    B --> C{ i < 9? }
    C -- Yes --> D[#をi+1回出力]
    D --> E[ i++ ]
    E --> C
    C -- No --> F([End])
  
```