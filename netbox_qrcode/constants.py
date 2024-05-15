from django.db.models import Q

CUSTOMURL_ASSIGNMENT_MODELS = Q(
    Q(app_label='dcim', model='cable') |
    Q(app_label='dcim', model='device') |
    Q(app_label='dcim', model='location') |
    Q(app_label='dcim', model='powerfeed') |
    Q(app_label='dcim', model='powerpanel') |
    Q(app_label='dcim', model='rack')
)