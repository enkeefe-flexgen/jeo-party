# Jeo-Party
A software replication of the classic Jeopardy! TV show

## Functionality Goals
- Allows creation of boards for a typical Jeopardy game
- Stores old boards from created games
- Has an option to randomly assign Daily Doubles
- Keeps accurate scores for each player
- Has an optional question selection verification option
- Has a "Verbal/In-Person" mode
    - the "Host" will confirm whether or not a Player answered correctly out loud
- Has separate screen for each player with a buzzer (reach)
- Has a "Textual/Virtual" mode (reach)
     - the Player will type his/her respone (and be allowed more time to answer) and the "Host" will have the option to override the system's designation of correct or incorrect
- Creates a game by selecting a random set of boards from J! archives (reach)
- Has multiple game modes (reach)
- Is downloadable and playable online (reach)

## User Stories
__Players__
- Can see an accurate score and player name
- Can select the desired question themself (reach)
- Can see which questions have an have not been answered on the board
- Can select a custom amount to wager on Daily Doubles
- Can vote as to whether a person answered correctly in "Textual/Virtual" mode (reach)

__Creators__
- Can create, edit, or delete games
- Can custom name category titles
- Can rearrange questions in a category to change points values
- Can randomly assign or pick specific questions to be Daily Doubles
- Can create a first round, second round, and final jeopardy round all in one go
- Can start creating a game, and save it to work on it later (reach)

__Hosts__
- Has complete control of the board/main screen
- Can select whether a player answered a question correctly or not
- Can add time and point handicaps to players at the beginning of the game

## Milestones
#### 1. Diagrams - all planning and data flow is documented
    - use cases created
    - class structure finalized
    - downloadable game file structure finalized
    - backend logic diagramed
    - UI wireframes designed
    - frontend-backend communication diagramed

### __Creation__
#### 2. Backend - fully functioning creation logic encoded
    - backend logic is coded/finished
    - backend logic is tested
#### 3. Frontend - the creation portion of the web app is fully traversable 
    - UI pages are coded
    - UI pages are tested
#### 4. Communication - a full game can be created and downloaded
    - UI connects with the backend
    - integration testing completed

### __Gameplay__
#### 5. Backend - fully functioning gameplay logic coded
    - round logic is coded/finished
    - round logic is tested
    - final jeopardy logic is coded/finished
    - final jeopardy logic is tested
    - full game functionality tests passing
#### 6. Frontend - the gameplay portion of the web app is fully traversable
    - board UI pages coded
    - board UI pages tested
    - final jeopardy page(s) coded
    - final jeopardy page(s) tested
#### 7. Communication - a full game can be played
    - UIs and backend connect
    - integration testing completed
  
#### 8. End-to-End Testing - a full game can be created, downloaded, uploaded, and played
