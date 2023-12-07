import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox

from tkinter import filedialog

# You may import any submodules of tkinter here if you wish
# You may also import anything from the typing module
# All other additional imports will result in a deduction of up to 100% of your A3 mark
from tkinter.filedialog import asksaveasfile

from a3_support import *


# Write your classes here

class Model(object):
    def __init__(self) -> None:

        self._all_history = None
        self._no_undo = None
        self._score = None
        self._matrix = None
        self.new_game()
        self._all_history.append((self._score, self._matrix))

    def new_game(self) -> None:
        """
		Return :
		 Sets, or resets, the game state to an initial game state.
		"""
        self._matrix = [[None for i in range(NUM_COLS)] for i in range(NUM_ROWS)]
        self.add_tile()
        self.add_tile()
        self._score = 0  # clean score
        self._all_history = []  # clean history
        self._no_undo = MAX_UNDOS  # undo time

    def get_tiles(self) -> list[list[Optional[int]]]:
        """
		
		Returns:
			Return the current tiles matrix.
			Each internal list represents a row of the grid, ordered from
			top to bottom.

		"""
        return self._matrix

    def add_tile(self) -> None:
        """

		Returns:
			Randomly generate a new tile at an empty location and add it to the current tiles matrix.
		"""

        position, number = generate_tile(self._matrix)  # call from support
        row, column = position
        self._matrix[row][column] = number

    def move_left(self) -> None:
        """
		Moves all tiles to their LEFT extreme, merging where necessary
		"""
        left = stack_left(self._matrix)
        merge = combine_left(left)
        self._matrix = stack_left(merge[0])  # call stack_left and merge from support
        self._score += merge[1]

    def move_right(self) -> None:
        """
		Moves all tiles to their RIGHT extreme, merging where necessary
		"""
        self._matrix = reverse(self._matrix)
        self.move_left()
        self._matrix = reverse(self._matrix)

    def move_up(self) -> None:
        """
		Moves all tiles to their UP extreme, merging where necessary
		"""
        self._matrix = transpose(self._matrix)
        self.move_left()
        self._matrix = transpose(self._matrix)

    def move_down(self) -> None:
        """
		Moves all tiles to their down extreme, merging where necessary
		"""
        self._matrix = transpose(self._matrix)
        self.move_right()
        self._matrix = transpose(self._matrix)

    def attempt_move(self, move: str) -> bool:
        """
		Makes the appropriate move according to the move string provided.

		Args:
			move: string variable to identify move direction

		Returns: if key press that movement will implement,


		"""

        no_change_matrix = []

        for i in range(NUM_ROWS):
            row_list = []
            for j in range(NUM_ROWS):
                row_list.append(self._matrix[i][j])
            no_change_matrix.append(row_list)
        # identify the movement
        if move == LEFT:
            self.move_left()
        if move == RIGHT:
            self.move_right()
        if move == UP:
            self.move_up()
        if move == DOWN:
            self.move_down()

        after_matrix = self._matrix
        if no_change_matrix != after_matrix:
            self._all_history.append((self._score, self._matrix))  # add score and movement history
            return True
        return False

    def has_won(self) -> bool:
        """
		Returns:
			True if the game has been won, else False.
		"""

        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                if self._matrix[i][j] == 2048:
                    return True

        return False

    def has_lost(self) -> bool:
        """
		Returns True if the game has been lost, else False.

		"""
        # check None
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                if self._matrix[i][j] is None:
                    return False

        copy_matrix = []  # create new list to check

        for i in range(NUM_ROWS):
            row_list = []
            for j in range(NUM_COLS):
                row_list.append(self._matrix[i][j])
            copy_matrix.append(row_list)

        if self.attempt_move(UP):
            self._matrix = copy_matrix
            return False
        elif self.attempt_move(DOWN):
            self._matrix = copy_matrix
            return False
        elif self.attempt_move(LEFT):
            self._matrix = copy_matrix
            return False
        elif self.attempt_move(RIGHT):
            self._matrix = copy_matrix
            return False  # not lost
        return True  # lost

    def get_score(self) -> int:
        """

		Returns:
			the current score for the game.

		"""

        return self._score

    def get_undos_remaining(self) -> int:
        """
		Returns:
			Get the number of undos the player has remaining.

		"""

        return self._no_undo

    def use_undo(self) -> None:
        """
		Returns:
			Attempts to undo the previous move, returning the current tiles
			to the previous tiles state before the last move that made changes to the tiles matrix

		"""

        if self._no_undo > 0 and len(self._all_history) > 1:
            self._all_history.pop(-1)  # undo move will clear the last move history
            last_move = self._all_history[-1]  # get previous matrix,score
            self._score = last_move[0]
            self._matrix = last_move[1]
            self._no_undo = self.get_undos_remaining() - 1
    # when use undo move the remaining undo times will be reduced by 1
    @property
    def all_history(self):
        return self._all_history


def _get_bbox(position: tuple[int, int]) -> tuple[int, int, int, int]:
    """

	Args:
		position: tuple [integer ,interger]

	Returns:
		Return the bounding box for the (row, column) position, in the form (x_min, y_min, x_max, y_max).


	"""
    row, column = position
    min_x = column * (BOARD_WIDTH / NUM_ROWS) + BUFFER
    min_y = row * (BOARD_HEIGHT / NUM_COLS) + BUFFER

    max_x = min_x + ((BOARD_WIDTH / NUM_ROWS) - BUFFER)
    max_y = min_y + ((BOARD_WIDTH / NUM_ROWS) - BUFFER)
    return min_x, min_y, max_x, max_y


def _get_midpoint(position: tuple[int, int]) -> tuple[int, int]:
    """
	Args:
		position: tuple [integer,integer]

	Returns:
		Return the graphics coordinates for the center of the cell at the given (row, col) position.

	"""

    min_x, min_y, max_x, max_y = _get_bbox(position)
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    return int(center_x), int(center_y)


class GameGrid(tk.Canvas):
    def __init__(self, master: tk.Tk, **kwargs) -> None:
        """
		 A view class which inherits from tk.
		 Canvas and represents the 4x4 grid.
		Args:
			master: inherits from tk
			**kwargs: pass keyword variable length of arguments to all functions
		"""
        super().__init__(master, **kwargs)  # inherit

    def clear(self) -> None:
        """
		Return : Clears all items.
		"""
        self.delete(tk.ALL)

    def redraw(self, tiles: list[list[Optional[int]]]) -> None:
        """
		Return :
		Clears and redraws the entire grid based on the given tiles.
		"""
        self.clear()  # first need clean all history
        for i, row in enumerate(tiles):
            for j, each_tile in enumerate(row):

                self.create_rectangle(_get_bbox((i, j)),
                                      fill=COLOURS.get(each_tile),
                                      width=10,
                                      outline=BACKGROUND_COLOUR
                                      )
                if each_tile is not None:
                    self.create_text(_get_midpoint((i, j)),
                                     text=each_tile,
                                     font=TILE_FONT,
                                     fill=FG_COLOURS.get(each_tile))


class Game(object):
    def __init__(self, master: tk.Tk) -> None:
        """
		Implement a class for the controller
		Args:
			master:  instantiated in all main function to cause the game to be created and run.
		"""
        self._files = None
        self._master = master
        self._master.title('CSSE1001/7030 2022 Semester 2 A3')
        label = tk.Label(self._master, text='2048', bg=COLOURS.get(2048), fg=FG_COLOURS.get(2048), font=TITLE_FONT)
        label.pack(fill=tk.BOTH)
        self._model = Model()  # call model
        self._game_grid = GameGrid(master, bg=BACKGROUND_COLOUR, height=BOARD_HEIGHT, width=BOARD_WIDTH)
        self._game_grid.pack()
        self._master.bind("<KeyPress>", self.attempt_move)
        # call statusbar
        self._status_bar = StatusBar(master)
        self._status_bar.pack(side=tk.BOTTOM)
        self._status_bar.set_callbacks(self.start_new_game, self.undo_previous_move)  # callback
        # set menu
        menubar = tk.Menu(master)
        master.config(menu=menubar)
        self._filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="file", menu=self._filemenu)
        self._filemenu.add_command(label="Save game", command=self.menu_save_game)
        self._filemenu.add_command(label="Load game", command=self.menu_load_game)
        self._filemenu.add_command(label="New game", command=self.menu_start_game)
        self._filemenu.add_command(label="Quit", command=self.menu_quit_game)
        self.draw()  # order

    def draw(self) -> None:
        """
        Returns:
            Redraws any view classes based on the current model state
        """
        # show score and undo
        self._status_bar.redraw_infos(self._model.get_score(),
                                      self._model.get_undos_remaining())
        self._game_grid.redraw(self._model.get_tiles())  # model 's  get.tiles()

    def attempt_move(self, event: tk.Event) -> None:
        """
        Args:
            event: Attempt a move if the event represents a key press on character ‘a’, ‘w’, ‘s’, or ‘d’.
        Returns:
            Display the appropriate messagebox if the game has been won.
        """

        if event.char in ['a', 'w', 's', 'd']:  # set the keyboard with only those chars
            self._model.attempt_move(event.char)
            self.draw()
            if self._model.has_won():
                messagebox.showinfo(WIN_MESSAGE)  # ask win play again
            self._master.after(NEW_TILE_DELAY, self.new_tile)  # loss ask play again

    def new_tile(self) -> None:
        """
        Return :Adds a new tile to the model and redraws. If the game has been lost with the addition of the new tile,
        then the player should be prompted with the appropriate messagebox displaying the LOSS_MESSAGE.
        """
        self._model.add_tile()
        self.draw()
        if self._model.has_lost():  # when use loss game
            user_input = tkinter.messagebox.askyesno("Y or N", LOSS_MESSAGE)
            if user_input:  # when user click yes
                self._model.new_game()
            self._master.destroy()

    def undo_previous_move(self) -> None:
        """
        Returns:
            A handler for when the ‘Undo’ button is pressed in the status bar.
        """
        self._model.use_undo()
        self.draw()

    def start_new_game(self) -> None:
        """
        Returns:
            A handler for when the ‘New Game’ button is pressed in the status bar.
            """
        self._model.new_game()
        self.draw()

    def menu_start_game(self) -> None:
        """
        Return :
        New game start
        """
        self._model.new_game()
        self.draw()

    def menu_load_game(self) -> None:
        """
        Returns:
            Load a game from and load the game described in that file.
            """
        with filedialog.askopenfile(mode='r') as file:
            self.draw()


    def menu_quit_game(self) -> None:
        """
        Returns:
            Quit game and close window
        """
        if messagebox.askyesno(message="quit"):
            self._master.destroy()

    def menu_save_game(self) -> None:
        """
        return :
        Save all necessary information to replicate the current state of the game
        """
        files = filedialog.asksaveasfile(defaultextension=".txt")  # save file as "txt" version


class StatusBar(tk.Frame):

    def __init__(self, master: tk.Tk, **kwargs):
        """
        Args:
            master: inherits from tk.Frame
            **kwargs: pass keyword variable length of arguments to all functions (new game , undo move)
            return :
            inherits from tk.Frame and represents information about score and remaining undos,
            as well as a button to start a new game and a button to undo the previous move.
        """

        super().__init__(master, **kwargs)  # inherent
        # set score frame

        score_frame = tk.Frame(self, bg=BACKGROUND_COLOUR)
        score_frame.pack(side=tk.LEFT, padx=15, pady=10)
        # set undo frame

        undo_frame = tk.Frame(self, bg=BACKGROUND_COLOUR)
        undo_frame.pack(side=tk.LEFT, padx=15)
        # set buttons frame

        button = tk.Frame(self)
        button.pack(side=tk.LEFT, padx=15)
        # set score label

        score = tk.Label(score_frame, text="SCORE",
                         bg=BACKGROUND_COLOUR, font=20, fg=COLOURS.get(None))
        score.pack()
        # set score number  label
        self._score_num = tk.Label(score_frame,
                                   bg=BACKGROUND_COLOUR, font=20, fg=LIGHT)
        self._score_num.pack()
        # set undo label
        undos = tk.Label(undo_frame, text="UNDOS",
                         bg=BACKGROUND_COLOUR, font=20, fg=COLOURS.get(None))
        undos.pack()
        # set undo number label
        self._undos_num = tk.Label(undo_frame,
                                   bg=BACKGROUND_COLOUR, font=20, fg=LIGHT)
        self._undos_num.pack()
        # set new game button
        self._new_game = tk.Button(button, text="New Game")
        self._new_game.pack()
        # set undo button
        self._undo_move = tk.Button(button, text="Undo Move")
        self._undo_move.pack()

    def redraw_infos(self, score: int, undos: int) -> None:
        """
        Args:
            score: integer Updates the score
            undos: integer undo times
        Returns:  Updates the score and undos labels to reflect the information given.
        """
        self._score_num.configure(text=score)
        self._undos_num.configure(text=undos)

    def set_callbacks(self, new_game_command: callable, undo_command: callable) -> None:
        """
        Args:
            new_game_command: new game implement
            undo_command:  undo function implement
        def handler(event):
        Undo_Move.bind("<Button>",handler)
        Returns:
            None if user did not commend
        """
        self._new_game.config(command=new_game_command)
        self._undo_move.config(command=undo_command)


def play_game(root):
    """
    Args:
        root: user master instead
    Returns:
    None
    """
    game = Game(root)


if __name__ == '__main__':
    root = tk.Tk()
    play_game(root)
    root.mainloop()
