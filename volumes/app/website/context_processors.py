from website.models import Website


def static_website_processor(request):

    website = Website.objects.first()

    return {'website': website}
