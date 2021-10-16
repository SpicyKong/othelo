# Othelo-Game for studying OOP.
# 1. 객체 종류


정리:

게임 시작.

내 턴 >
둘 수 있는 위치를 물어봄 >
둘 수 있는 위치 중 하나를 선택 함 >
그 위치에 돌을 둠 >
턴 종료 >
를 무한 반복.

## 1.1. 보드 판(Board)
> 보드 게임의 진행 상황을 관리 및 시각화 해주는 객체
### 1.1.1. 프로퍼티
| `타입` | `변수 명` | `설명` |
|-|-|-|
||||
### 1.1.2. 메소드
| `반환 타입` | `메소드 명` | `설명` |
|-|-|-|
|`void`|`__init__`|``|
|`void`|`put_a_piece(x, y, piece)`|`(x, y) 위치에 말을 둠`|
|`list`|`get_place(color)`|`(x, y) 위치에 말을 둠`|


## 1.2. 게임 말(Piece)
> 물리적으로 보드판 위에 위치할 수 있고 게임 진행에 있어 핵심이 되는 객체
### 1.2.1. 프로퍼티
| `타입` | `변수 명` | `설명` |
|-|-|-|
||||
### 1.2.2. 메소드
| `반환 타입` | `메소드 명` | `설명` |
|-|-|-|
|`void`|`__init__(x, y)`|`(x, y) 위치에 놓으라고 board에 요청`|
|`void`|`change_color()`|`나의 색을 바꿈`|
|`bool(int)`|`get_color()`|`나의 색을 반환함`|

## 1.3. 유저(User)
> 보드 게임을 플레이 하는 객체
### 1.3.1. 프로퍼티
| `타입` | `변수 명` | `설명` |
|-|-|-|
||||
### 1.3.2. 메소드
| `반환 타입` | `메소드 명` | `설명` |
|-|-|-|
|`void`|`__init__(username)`|`유저네임을 설정한다.`|
|`void`|`set_turn(turn)`|`턴을 설정한다.`|
|`void`|`put_a_piece(x, y)`|`(x, y) 위치에 게임 말을 둔다.`|


## 1.4. 게임(Game)
> 게임이 만들어지고 종료 될때까지 인게임 요소 외의 모든 것들을 관리하는 객체
### 1.4.1. 프로퍼티
| `타입` | `변수 명` | `설명` |
|-|-|-|
||||
### 1.4.2. 메소드
| `반환 타입` | `메소드 명` | `설명` |
|-|-|-|
|`void`|`__init__(user1, user2, board)`|`생성자이며 유저 둘과, 보드 판을 인자로 받고, 게임에서 사용되는 게임 말(Piece)을 관리할 변수를 만든다.`|

## 1.5. 규칙(Rule)
> 유저가 규칙에 정의된 행동만 할 수 있도록 물어보면 답해주는 객체
### 1.5.1. 프로퍼티
| `타입` | `변수 명` | `설명` |
|-|-|-|
||||
### 1.5.2. 메소드
| `반환 타입` | `메소드 명` | `설명` |
|-|-|-|
|`void`|`__init__`|``|