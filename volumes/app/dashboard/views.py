from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView, ListView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import (
    InformationForm,
    CounterFormSet,
    InterestedFormSet,
    SkillsForm,
    WebsiteForm,
    SocialFormSet,
    SummaryForm,
    ExperienceForm,
    EducationForm,
)
from django.utils.translation import gettext_lazy as _
from website.models import MyInformation, Skills, Website
from resume.models import Summary, Experience, Education
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_object()

        if self.request.POST:
            context["social_formset"] = SocialFormSet(
                self.request.POST, instance=context["object"])
        else:
            context["social_formset"] = SocialFormSet(
                instance=context["object"])

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        social_formset = context["social_formset"]

        if social_formset.is_valid():
            self.object = form.save()
            social_formset.instance = self.object
            social_formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

# --------------- End Primary Information ---------------


# --------------- Start Summary ---------------
class AdminSummaryView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/resume/summary.html"
    success_url = reverse_lazy("dashboard:summary")
    success_message = "The Summary was updated successfully."
    form_class = SummaryForm

    def get_object(self, queryset=None):
        return Summary.objects.first()

# --------------- End Summary ---------------


# --------------- Start Experience ---------------
class AdminExperienceListview(LoginRequiredMixin, ListView):
    template_name = "dashboard/resume/experience-list.html"
    success_url = reverse_lazy("dashboard:experiences-list")
    queryset = Experience.objects.all()


class AdminExperienceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "dashboard/resume/experience-create.html"
    form_class = ExperienceForm
    success_message = "The experience was added successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:experience-update", kwargs={"pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:experience-list")


class AdminExperienceUpdateview(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/resume/experience-update.html"
    queryset = Experience.objects.all()
    form_class = ExperienceForm
    success_message = "The experience was Updated successfully."

    def get_success_url(self):
        return reverse_lazy("dashboard:experience-update", kwargs={"pk": self.get_object().pk})


class AdminExperienceDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    queryset = Experience.objects.all()
    template_name = "dashboard/resume/experience-delete.html"
    success_message = "The experience was Deleted successfully."
    success_url = reverse_lazy("dashboard:experience-list")

# --------------- End Experience ---------------


# --------------- Start Education ---------------
class AdminEducationListview(LoginRequiredMixin, ListView):
    template_name = "dashboard/resume/education-list.html"
    success_url = reverse_lazy("dashboard:educations-list")
    queryset = Education.objects.all()


class AdminEducationCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "dashboard/resume/education-create.html"
    form_class = EducationForm
    success_message = "The education was added successfully."

    def form_valid(self, form):
        form.instance.user = self.request.user
        super().form_valid(form)
        return redirect(reverse_lazy("dashboard:education-update", kwargs={"pk": form.instance.pk}))

    def get_success_url(self):
        return reverse_lazy("dashboard:education-list")


class AdminEducationUpdateview(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/resume/education-update.html"
    queryset = Education.objects.all()
    form_class = EducationForm
    success_message = "The education was Updated successfully."

    def get_success_url(self):
        return reverse_lazy("dashboard:education-update", kwargs={"pk": self.get_object().pk})


class AdminEducationDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    queryset = Education.objects.all()
    template_name = "dashboard/resume/education-delete.html"
    success_message = "The education was Deleted successfully."
    success_url = reverse_lazy("dashboard:education-list")
