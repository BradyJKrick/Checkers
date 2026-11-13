from bakery import assert_equal
from drafter import *
from dataclasses import dataclass



hide_debug_information()
set_website_title("Your Drafter Website")
set_website_framed(False)

@dataclass
class Piece:
    col_let: str
    row_num: int
    is_king: bool
    color: str

empty = Piece(' ',0,False,' ')

@dataclass
class State:
    current_page: str
    color_turn: str
    material_score: int
    favored_color: str
    all_black_pieces: list[Piece]
    all_red_pieces: list[Piece]
    num_black: int
    num_black_kings: int
    num_red: int
    num_red_kings: int
    columns: str
    board = [[None,Piece('B',1,False,'Black'),None,Piece('D',1,False,'Black'),None,Piece('F',1,False,'Black'),None,Piece('H',1,False,'Black')],
        [Piece('A',2,False,'Black'),None,Piece('C',2,False,'Black'),None,Piece('E',2,False,'Black'),None,Piece('G',2,False,'Black'),None],
        [None,Piece('B',3,False,'Black'),None,Piece('D',3,False,'Black'),None,Piece('F',3,False,'Black'),None,Piece('H',3,False,'Black')],
        [empty,None,empty,None,empty,None,empty,None],
        [None,empty,None,empty,None,empty,None,empty],
        [Piece('A',6,False,'Red'),None,Piece('C',6,False,'Red'),None,Piece('E',6,False,'Red'),None,Piece('G',6,False,'Red'),None],
        [None,Piece('B',7,False,'Red'),None,Piece('D',7,False,'Red'),None,Piece('F',7,False,'Red'),None,Piece('H',7,False,'Red')],
        [Piece('A',8,False,'Red'),None,Piece('C',8,False,'Red'),None,Piece('E',8,False,'Red'),None,Piece('G',8,False,'Red'),None]]
    




for_str_board = [[None,Piece('B',1,False,'Black'),None,Piece('D',1,False,'Black'),None,Piece('F',1,False,'Black'),None,Piece('H',1,False,'Black')],
        [Piece('A',2,False,'Black'),None,Piece('C',2,False,'Black'),None,Piece('E',2,False,'Black'),None,Piece('G',2,False,'Black'),None],
        [None,Piece('B',3,False,'Black'),None,Piece('D',3,False,'Black'),None,Piece('F',3,False,'Black'),None,Piece('H',3,False,'Black')],
        [empty,None,empty,None,empty,None,empty,None],
        [None,empty,None,empty,None,empty,None,empty],
        [Piece('A',6,False,'Red'),None,Piece('C',6,False,'Red'),None,Piece('E',6,False,'Red'),None,Piece('G',6,False,'Red'),None],
        [None,Piece('B',7,False,'Red'),None,Piece('D',7,False,'Red'),None,Piece('F',7,False,'Red'),None,Piece('H',7,False,'Red')],
        [Piece('A',8,False,'Red'),None,Piece('C',8,False,'Red'),None,Piece('E',8,False,'Red'),None,Piece('G',8,False,'Red'),None]]

@route
def welcome_page(state: State) -> Page:
    state.current_page = 'game_page'
    welcome_section = Div([
        "Checkers is a game about moving your pieces to take your opponent's pieces.\n",
        "You take them by jumping over the opponent's pieces when able."
    ], text_align="left", font_weight="bold")
    picture_section = Div([
        "There will be a picture here."
    ], text_align='right')
    return Page(
        state,
        [
            Header("Welcome to Checkers!"),
            welcome_section,
            picture_section,
            Button("Start Game!", "index"),
            Button("How to Play", "scoring_page"),
        ],
    )

@route
def scoring_page(state: State) -> Page:
    rules_section = Div([
        "Checkers has a few rules to know: \nEvery piece can only move diagonally. \nRegular pieces can only move forward while kings can move any way they want.\n",
        "Players take turns moving their pieces. To capture a piece you have to be able to 'jump' it. This happens by having an additional open square",
        "two sqaures away from your current piece and an opponent's piece in between you and that square. This captures a piece and that piece is removed",
        "from the board. If you get a piece to the last rank on the opposing side of the board, that piece becomes a king. Kings are able to move in all four",
        "directions as opposed to just forwards. \nYou win the game by capturing every one of your opponent's pieces.\n",
        "Material scoring shows material advantage for whichever color has advantage. Each normal piece is worth 1 point while each king is worth two.",
        "The score is calculated by adding up all of the material points on red's side and subtracting the points on black's side. "
    ], text_align="left")
    return Page(
        state,
        [
            Header("How to Play: "),
            rules_section,
            Button("Start Game!", "index"),
            Button("Different Types of Checkers","american_checkers"),
        ],
    )

@route
def american_checkers(state: State) -> Page:
    history_part = Div([
        "American checkers is the most well known \nversion of checkers. It involves a 64 square \ngrid with 24 total pieces that go on them.",
        "\nEach piece is on the same color square and \ncaptures the opposing pieces via jumping them. \nGames similar to this form of checkers",
        "started \nbeing seen in history during the early age of the \nEgyptian pharohs in 1600BC. It was later \nmentioned by Homer and Plato in their",
        "writings \nfrom the Greek period.",
    ], text_align="left")
    picture_part = Div([
        "There will be a picture here."
    ], text_align="center")
    button_part = Div([
        Button("American Checkers","american_checkers"),
        '\n',
        Button("International Droughts","international"),
        '\n',
        Button("Russian Checkers","russian_checkers"),
        '\n',
        Button("Turkish Droughts","turkish_droughts"),
        '\n',
        Button("Spanish Droughts","spanish_droughts")
    ], text_align="right")
    other_buttons = Div([
        Button("How to Play", "scoring_page"),
        '\n',
        Button("Start Game!","index")
    ], text_align="left")
    return Page(
        state,
        [
            Header("American Checkers: "),
            history_part,
            picture_part,
            button_part,
            other_buttons,
        ],
    )

@route
def international(state: State) -> Page:
    history_part = Div([
        "American checkers is the most well known version of checkers. It involves a 64 square grid with 24 total pieces that go on them.",
        "Each piece is on the same color square and captures the opposing pieces via jumping them. Games similar to this form of checkers",
        "",
    ], text_align="left")
    picture_part = Div([
        "There will be a picture here."
    ], text_align="center")
    button_part = Div([
        Button("American Checkers","american_checkers"),
        '\n',
        Button("International Droughts","international"),
        '\n',
        Button("Russian Checkers","russian_checkers"),
        '\n',
        Button("Turkish Droughts","turkish_droughts"),
        '\n',
        Button("Spanish Droughts","spanish_droughts")
    ], text_align="right")
    other_buttons = Div([
        Button("How to Play", "scoring_page"),
        '\n',
        Button("Start Game!","index")
    ], text_align="left")
    return Page(
        state,
        [
            Header("International Droughts: "),
            history_part,
            picture_part,
            button_part,
            other_buttons,
        ],
    )

@route
def russian_checkers(state: State) -> Page:
    history_part = Div([
        "American checkers is the most well known version of checkers. It involves a 64 square grid with 24 total pieces that go on them.",
        "Each piece is on the same color square and captures the opposing pieces via jumping them. Games similar to this form of checkers",
        "",
    ], text_align="left")
    picture_part = Div([
        "There will be a picture here."
    ], text_align="center")
    button_part = Div([
        Button("American Checkers","american_checkers"),
        '\n',
        Button("International Droughts","international"),
        '\n',
        Button("Russian Checkers","russian_checkers"),
        '\n',
        Button("Turkish Droughts","turkish_droughts"),
        '\n',
        Button("Spanish Droughts","spanish_droughts")
    ], text_align="right")
    other_buttons = Div([
        Button("How to Play", "scoring_page"),
        '\n',
        Button("Start Game!","index")
    ], text_align="left")
    return Page(
        state,
        [
            Header("Russian Checkers: "),
            history_part,
            picture_part,
            button_part,
            other_buttons,
        ],
    )

@route
def turkish_droughts(state: State) -> Page:
    history_part = Div([
        "American checkers is the most well known version of checkers. It involves a 64 square grid with 24 total pieces that go on them.",
        "Each piece is on the same color square and captures the opposing pieces via jumping them. Games similar to this form of checkers",
        "",
    ], text_align="left")
    picture_part = Div([
        "There will be a picture here."
    ], text_align="center")
    button_part = Div([
        Button("American Checkers","american_checkers"),
        '\n',
        Button("International Droughts","international"),
        '\n',
        Button("Russian Checkers","russian_checkers"),
        '\n',
        Button("Turkish Droughts","turkish_droughts"),
        '\n',
        Button("Spanish Droughts","spanish_droughts")
    ], text_align="right")
    other_buttons = Div([
        Button("How to Play", "scoring_page"),
        '\n',
        Button("Start Game!","index")
    ], text_align="left")
    return Page(
        state,
        [
            Header("Turkish Droughts: "),
            history_part,
            picture_part,
            button_part,
            other_buttons,
        ],
    )

@route
def spanish_droughts(state: State) -> Page:
    history_part = Div([
        "American checkers is the most well known version of checkers. It involves a 64 square grid with 24 total pieces that go on them.",
        "Each piece is on the same color square and captures the opposing pieces via jumping them. Games similar to this form of checkers",
        "",
    ], text_align="left")
    picture_part = Div([
        "There will be a picture here."
    ], text_align="center")
    button_part = Div([
        Button("American Checkers","american_checkers"),
        '\n',
        Button("International Droughts","international"),
        '\n',
        Button("Russian Checkers","russian_checkers"),
        '\n',
        Button("Turkish Droughts","turkish_droughts"),
        '\n',
        Button("Spanish Droughts","spanish_droughts")
    ], text_align="right")
    other_buttons = Div([
        Button("How to Play", "scoring_page"),
        '\n',
        Button("Start Game!","index")
    ], text_align="left")
    return Page(
        state,
        [
            Header("Spanish Droughts: "),
            history_part,
            picture_part,
            button_part,
            other_buttons,
        ],
    )

def create_string_board(state: State) -> str:
    str_board = '  A  B  C  D  E  F  G  H\n'
    for i in range(len(state.board)):
        str_board += str(i+1)
        for j in range(len(state.board[i])):
            if state.board[i][j] == None:
                str_board += '   '
            else:
                str_board += ' ' + state.board[i][j].color[0] + ' '
        str_board += '\n'
    return str_board


def update_material_score(state: State) -> None:
    state.material_score = state.num_red + state.num_red_kings - state.num_black - state.num_black_kings
    if state.material_score >= 0:
        state.favored_color = 'Red'
    else:
        state.favored_color = 'Black'
    abs(state.material_score)

def update_piece_counts(state: State) -> None:
    state.num_black = 0
    state.num_black_kings = 0
    state.num_red = 0
    state.num_red_kings = 0
    for i in range(len(state.all_black_pieces)):
        if state.all_black_pieces[i].is_king:
            state.num_black += 1
            state.num_black_kings += 1
        else:
            state.num_black += 1
    for i in range(len(state.all_red_pieces)):
        if state.all_red_pieces[i].is_king:
            state.num_red += 1
            state.num_red_kings += 1
        else:
            state.num_red += 1
    
@route
def index(state: State) -> Page:
    if state.current_page == 'welcome_page':
        return welcome_page(state)
    elif state.current_page == 'game_page':
        state.all_black_pieces = []
        state.all_red_pieces = []
        
        str_board = create_string_board(state)
        for i in range(len(state.board)):
            for j in range(len(state.board[i])):
                if state.board[i][j] != None and state.board[i][j] != empty:
                    if state.board[i][j].color == 'Black':
                        state.all_black_pieces.append(state.board[i][j])
                    elif state.board[i][j].color == 'Red':
                        state.all_red_pieces.append(state.board[i][j])
        
        update_material_score(state)
        update_piece_counts(state)
        
        turn_section = Div([
            "Current Turn: " + state.color_turn
        ], text_align="left", font_weight="bold")
        
        board_section = Div([
            PreformattedText(str_board)
        ], margin="20px auto", text_align="center")

        controls_section = Div([
            "Which piece you are moving: ",
            TextBox("from_pos", ""),
            "\n Where you are moving it: \n",
            TextBox("to_pos", ""),
            Button("Make Move", "make_move")
        ], text_align="left")
        
        score_section = Div([
            "Black has " + str(state.num_black) + ' of pieces with ' + str(state.num_black_kings) + ' of them being kings.\n',
            'The material score is ' + str(state.material_score) + ' in favor of ' + state.favored_color + '.\n',
            "Red has " + str(state.num_red) + ' of pieces with ' + str(state.num_red_kings) + ' of them being kings.\n',
        ], text_align="right", margin_left="auto")
        
        bottom_row = Row([
            controls_section,
            score_section
        ], width="100%", justify_content="space-between", align_items="flex-end")
        
        main_box = Box([
            turn_section,
            board_section,
            bottom_row
        ], width="600px", padding="20px", border="2px solid black")
        
        return Page(
            state, [main_box]
        )

@route
def no_piece_found(state: State) -> Page:
    return Page(
        state,
        [
            Header("The position you inputed does not have your colored piece in it."),
            "Try a different position.",
            Button("Back", "index"),
        ],
    )


def get_current_piece(state: State, from_pos: str) -> Piece:
    for piece in state.all_red_pieces:
        if piece.col_let == from_pos[0] and piece.row_num == int(from_pos[1]):
            return piece
    for piece in state.all_black_pieces:
        if piece.col_let == from_pos[0] and piece.row_num == int(from_pos[1]):
            return piece

#def find_line_to_target(state: State, from_pos: str, to_pos: str) -> :
    

def get_possible_moves(state: State, current_piece: Piece) -> list[str]:
    possible_moves = []
    if current_piece.color == 'Red' and current_piece.is_king == False:
        if current_piece.col_let != 'A':
            up_left = state.board[state.columns.index(current_piece.col_let)-1][current_piece.row_num-1]
        if current_piece.col_let != 'H':
            up_right = state.board[state.columns.index(current_piece.col_let)+1][current_piece.row_num-1]
        if up_left == empty:
            possible_moves.append(state.columns[state.columns.index(current_place.col_let)-1] + str(current_place.row_num-1))
        elif up_left != empty and up_left.color == 'Black':
            if up_left.col_let != 'A':
                upper_left = state.board[state.columns.index(up_left.col_let)-1][up_left.row_num-1]
                #if upper_left == empty:
        if up_right == empty:
            possible_moves.append(state.columns[state.columns.index(current_place.col_let)+1] + str(current_place.row_num-1))
    elif current_piece.color == 'Black' and current_piece.is_king == False:
        if current_piece.col_let != 'A':
            down_left = state.board[state.columns.index(current_piece.col_let)-1][current_piece.row_num+1]
        if current_piece.col_let != 'H':
            down_right = state.board[state.columns.index(current_piece.col_let)+1][current_piece.row_num+1]
        if down_left == empty:
            possible_moves.append(state.columns[state.columns.index(current_place.col_let)-1] + str(current_place.row_num+1))
        if down_right == empty:
            possible_moves.append(state.columns[state.columns.index(current_place.col_let)+1] + str(current_place.row_num+1))
    return possible_moves
        


@route
def make_move(state: State, from_pos: str, to_pos: str) -> Page:
    if state.color_turn == 'Red':
        piece_found = False
        for piece in state.all_red_pieces:
            if piece.col_let == from_pos[0] and piece.row_num == int(from_pos[1]):
                piece_found = True
        if piece_found == False:
            return no_piece_found(state)
        piece = get_current_piece(state, from_pos)
        moves = get_possible_moves(state,piece)
        if to_pos in moves:
            state.board[int(to_pos[1])-1][state.columns.index(to_pos[0])] = piece
            state.board[int(from_pos[1])-1][state.columns.index(from_pos[0])] = empty
            piece.col_let = to_pos[0]
            piece.row_num = int(to_pos[1])
            state.color_turn = 'Black'
            return index(state)
    if state.color_turn == 'Black':
        piece_found = False
        for piece in state.all_black_pieces:
            if piece.col_let == from_pos[0] and piece.row_num == int(from_pos[1]):
                piece_found = True
        if piece_found == False:
            return no_piece_found(state)
        piece = get_current_piece(state, from_pos)
        moves = get_possible_moves(state,piece)
        if to_pos in moves:
            state.board[int(to_pos[1])-1][state.columns.index(to_pos[0])] = piece
            state.board[int(from_pos[1])-1][state.columns.index(from_pos[0])] = empty
            piece.col_let = to_pos[0]
            piece.row_num = int(to_pos[1])
            state.color_turn = 'Red'
            return index(state)
            

start_server(State('welcome_page','Red',0,'',[],[],12,0,12,0,'ABCDEFGH'))
