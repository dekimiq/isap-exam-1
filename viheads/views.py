from django.shortcuts import render, redirect, get_object_or_404
from .models import Idea
from .forms import IdeaForm

def index(request):
  ideas = Idea.objects.all()

  return render(request, 'index.html', {'ideas': ideas})

def create_idea(request):
  if request.method == 'POST':
    form = IdeaForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = IdeaForm()
    return render(request, 'create_idea.html', {'form': form})

def get_idea(request, pk):
  idea = get_object_or_404(Idea, pk=pk)
  return render(request, 'detail.html', {'idea': idea})

def update_idea(request, pk):
  idea = get_object_or_404(Idea, pk=pk)
  if request.method == 'POST':
    form = IdeaForm(request.POST, instance=idea)
    if form.is_valid():
      form.save()
      return redirect('detail_idea', pk=pk)
  else:
    form = IdeaForm(instance=idea)
    return render(request, 'update_idea.html', {'form': form, 'idea': idea})

def delete_idea(request, pk):
  idea = get_object_or_404(Idea, pk=pk)
  if request.method == 'POST':
    idea.delete()
    return redirect('index')
  else:
    return render(request, 'delete_idea.html', {'idea': idea})

