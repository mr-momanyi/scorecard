from django.contrib import admin
from .models import TreeDataEntry
    


@admin.register(TreeDataEntry)
class TestPlantingAdmin(admin.ModelAdmin):
    list_display = (
        'Region', 
        'County', 
        'Subcounty', 
        'Field_id', 
        'Entry_number', 
        'Date_collected', 
        'Location', 
        'Tree_species', 
        'Field_size', 
        'Trees_planted'
    )
    search_fields = ('Region', 'County', 'Subcounty', 'Tree_species', 'Location')
    list_filter = ('Region', 'County', 'Subcounty', 'Date_collected')
    fieldsets = (
        ('General Information', {
            'fields': ('Region', 'County', 'Subcounty', 'Field_id', 'Location')
        }),
        ('Tree Planting Details', {
            'fields': ('Tree_species', 'Field_size', 'Trees_planted', 'Date_collected', 'Entry_number')
        }),
    )