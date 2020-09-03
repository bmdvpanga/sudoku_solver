from django.shortcuts import render

# Create your views here.
def index(request):
    board = {
      'board':  [
            [0,0,0,0,0,1,0,0,0],
            [0,0,0,0,0,2,0,0,0],
            [0,0,0,0,0,3,0,0,0],
            [0,0,0,0,0,4,0,0,0],
            [0,0,0,0,0,5,0,0,0],
            [0,0,0,0,0,6,0,0,0],
            [0,0,0,0,0,7,0,0,0],
            [0,0,0,0,0,8,0,0,0],
            [0,0,0,0,0,9,0,0,0]
        ],
        'range': range(9)
    }

    return render(request, 'board/index.html', board)

