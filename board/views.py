from django.shortcuts import render
from .forms import BoardForm
from .utils import SudokuSolver

# Create your views here.
def index(request):
    board = {
      'board':  [
            [5,3,' ',' ',7,' ',' ',' ',' '],
            [6,' ',' ',1,9,5,' ',' ',' '],
            [' ',9,8,' ',' ',' ',' ',6,' '],
            [8,' ',' ',' ',6,' ',' ',' ',3],
            [4,' ',' ',8,' ',3,' ',' ',1],
            [7,' ',' ',' ',2,' ',' ',' ',6],
            [' ',6,' ',' ',' ',' ',2,8,' '],
            [' ',' ',' ',4,1,9,' ',' ',5],
            [' ',' ',' ',' ',8,' ',' ',7,9]
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


