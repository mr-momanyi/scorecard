from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import TreeDataEntry
from .forms import TreePlantingForm  # Assuming you have a form defined for `TreePlanting`


# Homepage View
def home(request):
    return render(request, 'scoreapp/home.html')


# Scorecard View
def scorecard(request):
    return render(request, 'scoreapp/scorecard.html')


# Graphs View
def graphs(request):
    return render(request, 'scoreapp/graphs.html')


# About Us View
def about(request):
    return render(request, 'scoreapp/about.html')


# Contact Us View
def contact(request):
    return render(request, 'scoreapp/contact.html')



# Tree Planting Form View (Optional)

def treeplanting_form_view(request):
    if request.method == "POST":
        form = TreePlantingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('success_page')  # Replace with your success page URL or name
    else:
        form = TreePlantingForm()
    return render(request, 'scoreapp/treeplanting_form.html', {'form': form})


# def tree_planting_view(request):
#     if request.method == 'POST':
#         form = TreePlantingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Data submitted successfully!', content_type='text/plain')
#     else:
#         form = TreePlantingForm()

#     return render(request, 'scoreapp/tree_planting_form.html', {'form': form})
