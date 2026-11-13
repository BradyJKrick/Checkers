from bakery import assert_equal
from drafter import *
from dataclasses import dataclass
from typing import Optional

set_website_title("Checkers")
hide_debug_information()
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
    jump_again: str
    board = [[None,Piece('B',1,False,'Black'),None,Piece('D',1,False,'Black'),None,Piece('F',1,False,'Black'),None,Piece('H',1,False,'Black')],
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
        "Players take turns moving their pieces. To capture a piece you have to be able to 'jump' it. \nThis happens by having an additional open square",
        "two sqaures away from your current piece \nand an opponent's piece in between you and that square. This captures a piece and that piece is removed",
        "from the board. \nYou are not forced to make a jump if it is able, but it is recommended. After you make a jump, you can either jump again or end your turn.",
        "\nIf you get a piece to the last rank on the opposing side of the board, that piece becomes a king. Kings are able to move in all four",
        "directions as opposed to just forwards. \nYou win the game by capturing every one of your opponent's pieces.\n",
        "Material scoring shows material advantage for whichever color has advantage. Each normal piece is worth 1 point while each king is worth two.",
        "\nThe score is calculated by adding up all of the material points on red's side and subtracting the points on black's side. "
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
        Button("Turkish Droughts","turkish_droughts")
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
        "International droughts is the seconde most popular form of the game. \nIt features a 100 square board on a 10x10 grid. Unlike American \nCheckers,",
        "The normal piece can move in all four directions. This \nallows for a different strategy and helps shorten the long game.",
        "\nThe starting color for international droughts is the light pieces.",
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
        Button("Turkish Droughts","turkish_droughts")
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
        "Russian checkers is very similar to american checkers. Russian \ncheckers is played on a 64 square board on an 8x8 grid. Russian \ncheckers plays",
        "almost exactly like american checkers. The one major \ndifference is how the king works. In american checkers, the king can \nmove one square in any",
        "direction while in russian checkers, it can \nmove any number of squares in any direction similar to a bishop in \nchess. Russian checkers also has a",
        "mid-capture promotion system \nwhere is a piece reaches the back rank on a jump, it can promote \nand take the rest of its moves as a king.",
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
        Button("Turkish Droughts","turkish_droughts")
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
        "Turkish droughts is played on a 64 square board in an 8x8 grid. This \nversion of checkers has 16 pieces per side. The pieces are setup in \nthe",
        "second two rows, leaving the back row open. Normal pieces move \nforwards and side-to-side while kings move like rooks. There is no \ndiagonal",
        "movement in this version of checkers. Turkish droughts is \nalso known as turkish dama as they call the king in this game the \ndama. The word",
        "dama originates from Spanish or Italian meaning \nqueen.",
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
        Button("Turkish Droughts","turkish_droughts")
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

def create_string_board(state: State) -> str:
    str_board = '  A  B  C  D  E  F  G  H\n'
    for i in range(len(state.board)):
        str_board += str(i+1)
        for j in range(len(state.board[i])):
            piece = state.board[i][j]
            if piece != None:
                letter = piece.color[0].lower()
                if piece.is_king == True:
                    letter = letter.upper()
                str_board += ' ' + letter + ' '
            else:
                str_board += ' ⬛ '
        str_board += '\n'
    return str_board


def update_material_score(state: State) -> None:
    state.material_score = state.num_red + state.num_red_kings - state.num_black - state.num_black_kings
    if state.material_score >= 0:
        state.favored_color = 'Red'
    else:
        state.favored_color = 'Black'
    state.material_score = abs(state.material_score)

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
        
        turn_section = Div([
            "Current Turn: " + state.color_turn
        ], text_align="left", font_weight="bold")
        
        board_section = Div([
            PreformattedText(create_string_board(state))
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

@route
def must_jump_again(state: State) -> Page:
    return Page(
        state,
        [
            "You have to either jump again with the piece on " + state.jump_again + ' or end turn.',
            Button("Back", "index"),
        ],
    )

@route
def not_legal_move(state: State, from_pos: str, choices: str) -> Page:
    return Page(
        state,
        [
            'That is not a legal move.',
            'The moves for the piece on ' + from_pos + ' are ' + choices,
            Button('Back','index'),
        ],
    )


def get_current_piece(state: State, from_pos: str) -> Piece:
    for piece in state.all_red_pieces:
        if piece.col_let == from_pos[0] and piece.row_num == int(from_pos[1]):
            return piece
    for piece in state.all_black_pieces:
        if piece.col_let == from_pos[0] and piece.row_num == int(from_pos[1]):
            return piece

def get_directions(piece: Piece) -> list[tuple[int, int]]:
    if piece.is_king:
        return [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    if piece.color == 'Red':
        return [(-1, -1), (-1, 1)]
    else:
        return [(1, -1), (1, 1)]


def get_possible_moves(state: State, piece: Piece, must_jump: bool) -> list[str]:
    possible_moves = []
    row = piece.row_num - 1
    col = state.columns.index(piece.col_let)
    for dr, dc in get_directions(piece):
        print(get_directions(piece))
        new_r = dr + row
        new_c = dc + col
        if ((0 <= new_r and new_r < 8) and (0 <= new_c and new_c < 8)) == False:
            continue
        possible_move = state.board[new_r][new_c]
        if possible_move == empty:
            if must_jump == False:
                possible_moves.append(state.columns[new_c] + str(new_r + 1))
        
        elif possible_move.color != piece.color:
            jump_row = row + 2 * dr
            jump_col = col + 2 * dc
            if ((0 <= jump_row and jump_row < 8) and (0 <= jump_col and jump_col < 8)) and state.board[jump_row][jump_col] == empty:
                possible_moves.append(state.columns[jump_col] + str(jump_row + 1))
    print(possible_moves)
    return possible_moves

def parse_pos(state: State, pos: str) -> Optional[tuple[int,int]]:
    pos = pos.strip().upper()
    if len(pos) != 2 or pos[0] not in state.columns or pos[1] not in '12345678':
        return None
    return int(pos[1]) - 1, state.columns.index(pos[0])

def refresh_pieces(state: State) -> None:
    state.all_black_pieces = []
    state.all_red_pieces = []
    for i in range(len(state.board)):
        for j in range(len(state.board[i])):
            if state.board[i][j] != None and state.board[i][j] != empty:
                if state.board[i][j].color == 'Black':
                    state.all_black_pieces.append(state.board[i][j])
                elif state.board[i][j].color == 'Red':
                    state.all_red_pieces.append(state.board[i][j])
    
    update_piece_counts(state)
    update_material_score(state)

@route
def make_move(state: State, from_pos: str, to_pos: str) -> Page:
    from_pos = from_pos.strip().upper()
    to_pos = to_pos.strip().upper()
    from_pars = parse_pos(state, from_pos)
    to_pars = parse_pos(state, to_pos)
    if from_pars == None or to_pars == None:
        return no_piece_found(state)
    
    piece = state.board[from_pars[0]][from_pars[1]]
    if piece.color != state.color_turn:
        return no_piece_found(state)
    
    if state.jump_again != '' and from_pos != state.jump_again:
        return must_jump_again(state)
    
    if state.jump_again != '':
        must_jump = True
    else:
        must_jump = False
        
    moves = get_possible_moves(state, piece, must_jump)
    if to_pos not in moves:
        if len(moves) != 0:
            choices = ', '.join(moves)
            return not_legal_move(state, from_pos, choices)
    
    from_row = from_pars[0]
    from_col = from_pars[1]
    to_row = to_pars[0]
    to_col = to_pars[1]
    piece.row_num += to_row - from_row
    piece.col_let = state.columns[state.columns.index(piece.col_let) + (to_col - from_col)]
    state.board[from_row][from_col] = empty
    state.board[to_row][to_col] = piece
    
    
    jump_happened = False
    if to_row - from_row == 2 or to_row - from_row == -2:
        jump_happened = True
        state.board[(from_row + to_row) // 2][(from_col + to_col) // 2] = empty
        
    promotion_happened = False
    if piece.is_king == False:
        if piece.color == 'Red' and to_row == 0 or piece.color == 'Black' and to_row == 7:
            promotion_happened = True
            piece.is_king = True
    
    refresh_pieces(state)
    
    if state.color_turn == 'Red':
        if len(state.all_black_pieces) == 0:
            return game_over_page(state, 'Red')
    else:
        if (len(state.all_red_pieces)) == 0:
            return game_over_page(state, 'Black')
    
    if jump_happened == True and promotion_happened == False and get_possible_moves(state, piece, must_jump = True):
        state.jump_again = to_pos
    else:
        state.jump_again = ''
        if state.color_turn == 'Red':
            state.color_turn = 'Black'
        else:
            state.color_turn = 'Red'
    return index(state)
            
@route
def game_over_page(state: State,winner: str) -> Page:
    return Page (
        state,
        [
            Header(winner + ' wins!'),
            'Thank you for playing!',
        ],
    )


start_server(State('welcome_page','Red',0,'',[],[],12,0,12,0,'ABCDEFGH',''))
