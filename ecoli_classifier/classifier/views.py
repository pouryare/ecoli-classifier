from django.shortcuts import render
from django.views.generic import FormView
from .forms import SequenceForm
from .ml_model import predict_sequence

class PredictionView(FormView):
    template_name = 'classifier/predict.html'
    form_class = SequenceForm
    success_url = '/'

    def form_valid(self, form):
        sequence = form.cleaned_data['sequence']
        prediction = predict_sequence(sequence)
        return render(self.request, self.template_name, {'form': form, 'prediction': prediction})