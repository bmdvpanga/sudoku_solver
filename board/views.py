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
        print(request.POST)
        print(request.POST.get('11',''))

        ###TODO: Look up QueryDict https://stackoverflow.com/questions/10023213/extracting-items-out-of-a-querydict"
        # solved_board = utils.solve_board(request)
        return render(request, 'board/index.html', board)


