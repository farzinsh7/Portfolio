from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView, ListView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import InformationForm, CounterFormSet, InterestedFormSet, SkillsForm, WebsiteForm
from django.utils.translation import gettext_lazy as _
from website.models import MyInformation, Skills, Website
from django.shortcuts import redirect


class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"


class AdminInformationView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/information/information.html"
    success_url = reverse_lazy("dashboard:information")
    success_message = "The information was updated successfully."
    form_class = InformationForm

    def get_object(self, queryset=None):
        return MyInformation.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ensure `object` is available in template
        context["object"] = self.get_object()

        # Get formsets for Counter and InterestedIn
        if self.request.POST:
            context["counter_formset"] = CounterFormSet(
                self.request.POST, instance=context["object"])
            context["interested_formset"] = InterestedFormSet(
                self.request.POST, instance=context["object"])
        else:
            context["counter_formset"] = CounterFormSet(
                instance=context["object"])
            context["interested_formset"] = InterestedFormSet(
                instance=context["object"])

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        counter_formset = context["counter_formset"]
        interested_formset = context["interested_formset"]

        if counter_formset.is_valid() and interested_formset.is_valid():
            self.object = form.save()  # Save the MyInformation form
            # Attach the instance for saving Counter
            counter_formset.instance = self.object
            # Attach the instance for saving InterestedIn
            interested_formset.instance = self.object
            counter_formset.save()  # Save the Counter formset
            interested_formset.save()  # Save the InterestedIn formset
            return super().form_valid(form)  # Proceed with the usual form_valid process
        else:
            return self.form_invalid(form)


# --------------- Start Skills ---------------
class AdminSkillCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "dashboard/skills/skill-create.html"
    form_class = SkillsForm
    success_message = "The skill was added successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:skill-update", kwargs={"pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:skill-list")


class AdminSkillListview(LoginRequiredMixin, ListView):
    template_name = "dashboard/skills/skill-list.html"
    success_url = reverse_lazy("dashboard:skills-list")
    queryset = Skills.objects.all()


class AdminSkillUpdateview(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/skills/skill-update.html"
    queryset = Skills.objects.all()
    form_class = SkillsForm
    success_message = "The skill was Updated successfully."

    def get_success_url(self):
        return reverse_lazy("dashboard:skill-update", kwargs={"pk": self.get_object().pk})


class AdminSkillDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    queryset = Skills.objects.all()
    http_method_names = ["post"]
    success_message = "The skill was Deleted successfully."
    success_url = reverse_lazy("dashboard:skill-list")

# --------------- End Skills ---------------


# --------------- Start Primary Information ---------------
class AdminWebsiteView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/website/website.html"
    success_url = reverse_lazy("dashboard:website")
    success_message = "The information was updated successfully."
    form_class = WebsiteForm

    def get_object(self, queryset=None):
        return Website.objects.first()
