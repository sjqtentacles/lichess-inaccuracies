# tricky-knights: a Python3 chess puzzle web application

Still under development.

### Introduction

tricky-knights is a Python3 chess puzzle web application with support for inaccuracy puzzles thanks to the Lichess API.


### Documentation

Still nothing here.

### Features

* Inaccuracy puzzles

### HTTP API

You can use the tricky-knights api for whatever you want.

### API Limits

Users of the tricky-knights API are restricted to 60 calls per minute, or 1 per second.

### `GET /api/puzzles/` fetch list of puzzles

```
> curl https://trickyknights.org/api/puzzles/
```

name | type | default | description
--- | ---- | ---- | ----
**page** | int | - | page number
**page_size** | int | 5 | max number of records per page, capped at 50

```javascript

{
   "results" : [
      {
         "best_move_uci" : "e1-g1",
         "move_played" : "Bd3",
         "init_fen" : "r1bqkbnr/pppp1ppp/8/1B6/3pP3/8/PPPP1PPP/RNBQK2R w KQkq - 0 5",
         "best_move_san" : "O-O",
         "game_url" : "https://lichess.org/5wE2mlQh/white",
         "uuid" : "2fd8156b-33fa-459f-b347-4eab4e10308f"
      },
      {
         "best_move_san" : "d5",
         "game_url" : "https://lichess.org/5wE2mlQh/white",
         "uuid" : "dae4bcd0-eb2a-4a71-8fa5-6ea2bdff370c",
         "best_move_uci" : "d7-d5",
         "move_played" : "Qg5",
         "init_fen" : "r1bqkbnr/pppp1ppp/8/8/3pP3/3B4/PPPP1PPP/RNBQK2R b KQkq - 1 5"
      },
      ... // other puzzles
   ],
   "previous" : null,
   "count" : 69,
   "next" : "http://trickyknights.org/api/puzzles/?page=2"
}


```


### `GET /api/puzzles/{uuid}` fetch single puzzle by UUID

```
> curl https://trickyknights.org/api/puzzles/2fd8156b-33fa-459f-b347-4eab4e10308f
```

A single puzzle is returned.

```javascript
{
   "move_played" : "Bd3",
   "game_url" : "https://lichess.org/5wE2mlQh/white",
   "uuid" : "2fd8156b-33fa-459f-b347-4eab4e10308f",
   "best_move_uci" : "e1-g1",
   "init_fen" : "r1bqkbnr/pppp1ppp/8/1B6/3pP3/8/PPPP1PPP/RNBQK2R w KQkq - 0 5",
   "best_move_san" : "O-O"
}
```

### Requirements

* Python 3
* python-chess
* Django 2.0+
