import numpy as np

with open('input.txt') as file:

    bingo_boards = list()
    for ll, line in enumerate(file):
        if ll == 0:
            drawn_nums = np.asarray([int(n) for n in line.split(',')])

        elif line == '\n':
            if ll == 1:
                this_board = list()
            else:
                bingo_boards.append(this_board)
                this_board = list()
        else:
            vctr = [int(n) for n in line.split()]
            this_board.append(vctr)

    else:
        bingo_boards.append(this_board)

bingo_boards = np.asarray(bingo_boards)
mask_board = np.full_like(bingo_boards, fill_value=False, dtype=bool)



winning_boards = list()
winning_mask = list()
winning_num = list()

for num in drawn_nums:
    # set true in boolean playing boards where the bingo board equals the called number
    match_idx = np.where(bingo_boards == num)
    mask_board[match_idx] = True

    # does the magic of checking for full rows or columns
    vertical = np.any(np.all(mask_board,axis=1), axis=1)
    horizontal = np.any(np.all(mask_board,axis=2), axis=1)
    bingo = vertical | horizontal

    if np.any(bingo):
        # find the board, add it to the winning list
        winning_boards.append(bingo_boards[bingo])
        winning_mask.append(mask_board[bingo].copy())
        winning_num.append(num)
        # then remove it from the working pool
        bingo_boards = bingo_boards[~bingo]
        mask_board = mask_board[~bingo].copy()



for ii in [0, -1]:
    board = winning_boards[ii]
    mask = winning_mask[ii]
    num = winning_num[ii]
    unmarked = board[~mask]

    if ii == 0:
        cocky_msg = 'bingo grandma!'
    else:
        cocky_msg = 'bite the dust squid!'

    print(f'{cocky_msg}: {num * np.sum(unmarked)}')