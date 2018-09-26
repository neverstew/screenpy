Forms
-----

Model Forms
~~~~~~~~~~~
Model forms are a large part of many django applications.  They also follow some fairly standard patterns.

To this end, you can find a number of functions dedicated to helping you construct locators for form elements quickly
in the `screenpy.django.page_objects` module::

   from screenpy.django.page_objects import model_form

   username_field = model_form.field("username")
   password_field_error = model_form.field_error("password")




Material Design Elements
~~~~~~~~~~~~~~~~~~~~~~~~
The material design plugin for django offers a lot of nice UI components.  These often break the standard template
pattern and can make it harder to locate the element you're looking for.

There are a number of methods designed to help with this including::

   from screenpy.django.page_objects import material_design_dropdown, material_design_dropdown_option

   dropdown = material_design_dropdown("options")
   dropdown_option_one = material_design_dropdown_option("options", "one")