from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request,'session_words/index.html')

def process(request):
	if request.method=="POST":
		request.session['word'] = request.POST['word']
		request.session['color'] = request.POST['color']
		request.session['size'] = request.POST['size']
	return redirect('/')	


def clear(request):
	return redirect('/')