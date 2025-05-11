from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import ProtectedError

from task_manager.statuses.forms import StatusForm
from .models import Status
from task_manager.users.mixins import CustomLoginRequiredMixin


STATUSES='statuses:statuses'


class ShowStatuses(CustomLoginRequiredMixin, ListView):

    model = Status
    template_name = 'statuses/statuses_index.html'
    context_object_name = 'statuses'
    allow_empty = True


class CreateStatus(CustomLoginRequiredMixin,
                   SuccessMessageMixin,
                   CreateView):

    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = reverse_lazy(STATUSES)
    success_message = _('Status successfully created')
    extra_context = {
        'title': _('Create status'),
        'button_value': _('Create')
    }


class UpdateStatus(CustomLoginRequiredMixin,
                   SuccessMessageMixin,
                   UpdateView):

    model = Status
    template_name = 'form.html'
    form_class = StatusForm
    success_url = reverse_lazy(STATUSES)
    success_message = _('Status successfully updated')
    extra_context = {
        'title': _('Edit status'),
        'button_value': _('Update')
    }


class DeleteStatus(CustomLoginRequiredMixin,
                   SuccessMessageMixin,
                   DeleteView):

    model = Status
    template_name = 'delete_confirmation_form.html'
    success_url = reverse_lazy(STATUSES)
    success_message = _('Status successfully deleted')
    extra_context = {
        'title': _('Delete status'),
    }

    deletion_denied_message = _('Cannot delete status because it is in use')

    # Can't delete status because it's in use
    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except ProtectedError:
            messages.add_message(
                self.request,
                messages.ERROR,
                self.deletion_denied_message
            )
        else:
            messages.add_message(
                self.request,
                messages.SUCCESS,
                self.success_message
            )
        return HttpResponseRedirect(success_url)