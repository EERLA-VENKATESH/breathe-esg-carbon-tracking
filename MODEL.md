\# Data Model Design - Carbon Emissions Tracking System



\## Core Tables



\### Organization (Multi-tenant)

```python

class Organization(models.Model):

&#x20;   name = models.CharField(max\_length=255)

&#x20;   created\_at = models.DateTimeField(auto\_now\_add=True)

&#x20;   # Scope 1/2/3 categorization rules per org

