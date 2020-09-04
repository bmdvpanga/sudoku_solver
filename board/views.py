from django.shortcuts import render
from .forms import BoardForm
from .utils import SudokuSolver

# Create your views here.
def index(request):
    board = {
      'board':  [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ],
        'range': range(9)
    }

    if(request.method == 'GET'):
        return render(request, 'board/index.html', board)

    if(request.method == 'POST'):
        solver = SudokuSolver(request)
        
        print(solver.board)

        solver.solve_board( solver.board )

        return render(request, 'board/index.html', board)


