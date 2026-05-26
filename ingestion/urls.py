from .normalization_views import NormalizeRecordsView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .upload_views import FileUploadView
from .review_views import ApproveRecordView, FlagRecordView, ReviewDashboardView


router = DefaultRouter()
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'datasources', views.DataSourceViewSet)
router.register(r'raw-records', views.RawEmissionRecordViewSet)
router.register(r'normalized-records', views.NormalizedEmissionRecordViewSet)
router.register(r'review-statuses', views.ReviewStatusViewSet)
router.register(r'audit-logs', views.AuditLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/<int:organization_id>/<str:source_type>/', FileUploadView.as_view(), name='file-upload'),
    path('normalize/<int:organization_id>/', NormalizeRecordsView.as_view(), name='normalize'),
    path('approve/<int:record_id>/', ApproveRecordView.as_view(), name='approve'),
    path('flag/<int:record_id>/', FlagRecordView.as_view(), name='flag'),
    path('dashboard/<int:organization_id>/', ReviewDashboardView.as_view(), name='dashboard'),
]