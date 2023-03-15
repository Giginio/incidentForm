# incidentForm
incident declaration form

This is a prototype of a form to upload incidents, it only runs localy.
In this form it is possible to submit values which are saved in a local .csv file (dfCsv.csv).
it runs with the FLASK and FLASK_WFT framework to crate a website from python code. 

Following software and libraries are requierd:
- Python 3.8.13
- flask
- flask-wtf
- pandas

Recomendet changes to the prototype:
- After submitting the form the user should be redirected to another page to thank him or at least give a notification that the form was sent.
- A more sophisticated layout of the form could be created
- New input fields can be added by adding new variables under the module forms.py in the class DefectForm, and to be able to view the new fields in the website they have to be added under the file form.html
- The size of the individual fields can also be changed in the form.html file
