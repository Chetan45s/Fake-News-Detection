from django.contrib import admin
from process.models import InputData,Contribution

@admin.register(InputData)
class InputDataAdmin(admin.ModelAdmin):
    pass

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    pass
