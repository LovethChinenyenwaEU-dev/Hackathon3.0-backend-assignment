# my_admin.py
from user_admin import Admin

# Create Admin instance and show privileges
admin_profile = Admin("loveth", "edeugwu", 21, "female")
admin_profile.privileges.show_privileges()
