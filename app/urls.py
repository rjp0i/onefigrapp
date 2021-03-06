from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from . import views

app_name = 'app'
urlpatterns = [
	# Views with templates have names
	path('', views.index, name='index'),
	path('descriptions/', views.descriptions, name='descriptions'),
	path('tools/', views.tools, name='tools'),

	# Journals by Discipline
	path('journals-by-discipline/', views.journals_by_discipline, name='journalsByDiscipline'),
	path('journals-by-discipline/chart-data/<str:discipline>/', views.journals_by_discipline_chart_data),
	path('journals-by-discipline/journals-and-disciplines-map/', views.get_journals_and_disciplines_map),
	path('journals-by-discipline/disciplines-list/', views.disciplines_list), 

	# Journals By Discipline (Elsevier)
	path('journals-by-discipline-elsevier/', views.journals_by_discipline_elsevier, name='journalsByDisciplineElsevier'),
	path('journals-by-discipline/chart-data/<str:discipline>/', views.journals_by_discipline_chart_data_elsevier),
	path('journals-by-discipline/journals-and-disciplines-map/', views.get_journals_and_disciplines_map),
	path('journals-by-discipline/disciplines-list/', views.disciplines_list), 

	# Providers By Metric
	path('providers-by-metric/', views.providers_by_metric, name='providersByMetric'),	
	path('providers-by-metric/chart-data/', views.providers_by_metric_chart_data),
]