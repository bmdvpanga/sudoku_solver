from django.shortcuts import render
from .forms import BoardForm
from .utils import SudokuSolver

# Create your views here.
def index(request):
    board = {
      'board':  [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
        ],
        'range': range(9)
    }

    if(request.method == 'GET'):
        return render(request, 'board/index.html', board)

    if(request.method == 'POST'):
        solver = SudokuSolver(request)

        solved = solver.solve_board( solver.board )
        board["board"] = solved[1].tolist()

        return render(request, 'board/index.html', board)


